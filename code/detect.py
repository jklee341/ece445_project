import cv2
from picamera2 import Picamera2
import numpy as np
from led_test import *
import RPi.GPIO as GPIO
import time


classNames = []
net = None
picam2 = None
lock = False
servo = None

def set_servo_angle(angle):
    global servo
    duty_cycle = 1.0 / 18.0 * angle + 2
    servo.ChangeDutyCycle(duty_cycle)
    time.sleep(0.001)


def getObjects(img, thres, nms, draw=True, objects=['person']):
    classIds, confs, bbox = net.detect(img, confThreshold=thres, nmsThreshold=nms)
    objectInfo = []
    if len(classIds) != 0:
        for classId, confidence, box in zip(classIds.flatten(), confs.flatten(), bbox):
            className = classNames[classId - 1]
            if className in objects:
                flash_led()
                objectInfo.append([box, classNames[classId - 1], confidence])
                if draw:
                    cv2.rectangle(img, box, color=(0, 255, 0), thickness=2)
                    cv2.putText(img, classNames[classId - 1].upper(), (box[0] + 10, box[1] + 30),
                                cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                    cv2.putText(img, str(round(confidence * 100, 2)), (box[0] + 200, box[1] + 30),
                                cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
    else:
        turn_off_led()

    if len(objectInfo) > 0:
        box, _, _ = objectInfo[0]
        center_x = (box[0] + box[2]) // 2
        center_y = (box[1] + box[3]) // 2
        return img, objectInfo, (center_x, center_y)
    else:
        return img, objectInfo, None

def cameraOn():
    global picam2, classNames, net, servo
    picam2 = Picamera2()
    picam2.configure(picam2.create_preview_configuration())
    picam2.start()

    classFile = "/home/a123/Desktop/Object_Detection_Files/coco.names"
    with open(classFile, "rt") as f:
        classNames = f.read().rstrip("\n").split("\n")

    configPath = "/home/a123/Desktop/Object_Detection_Files/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt"
    weightsPath = "/home/a123/Desktop/Object_Detection_Files/frozen_inference_graph.pb"

    net = cv2.dnn_DetectionModel(weightsPath, configPath)
    net.setInputSize(320, 320)
    net.setInputScale(1.0 / 127.5)
    net.setInputMean((127.5, 127.5, 127.5))
    net.setInputSwapRB(True)
    
    
    # Servo setup
    servoPin = 12 # adjust value
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(servoPin, GPIO.OUT)
    servo = GPIO.PWM(servoPin, 50)
    servo.start(7) # adjust servo values

    rotation_and_tracking()

def rotation_and_tracking():
    global lock
    angle = 0
    while True:
        # Rotate from 0 to 180 degrees
        for angle in range(0, 181, 10):
            set_servo_angle(angle)
            frame = picam2.capture_array()
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = cv2.resize(frame, (640, 480))
            result, objectInfo, center = getObjects(img, 0.45, 0.2)

            if len(objectInfo) > 0:
                lock = True
                break

            cv2.imshow("Output", result)
            if cv2.waitKey(1) == ord('q'):
                break

        if lock:
            # Track the person
            while lock:
                frame = picam2.capture_array()
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = cv2.resize(frame, (640, 480))
                result, objectInfo, center = getObjects(img, 0.45, 0.2)

                if center is not None:
                    center_x, center_y = center
                    img_width = img.shape[1]
                    img_height = img.shape[0]

                    if center_x < img_width // 4:
                        angle -= 10
                    elif center_x > img_width * 3 // 4:
                        angle += 10

                    set_servo_angle(angle)

                cv2.imshow("Output", result)
                if cv2.waitKey(1) == ord('q'):
                    break

                if len(objectInfo) == 0:
                    lock = False

        else:
            # Rotate from 180 to 0 degrees
            for angle in range(180, -1, -10):
                set_servo_angle(angle)
                frame = picam2.capture_array()
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = cv2.resize(frame, (640, 480))
                result, objectInfo, center = getObjects(img, 0.45, 0.2)

                if len(objectInfo) > 0:
                    lock = True
                    break

                cv2.imshow("Output", result)
                if cv2.waitKey(1) == ord('q'):
                    break

        if not lock:
            break

    stop_camera()

def stop_camera():
    global picam2
    if picam2 is not None:
        picam2.stop()
        picam2 = None
    cv2.destroyAllWindows()
    servo.stop()
    GPIO.cleanup()
