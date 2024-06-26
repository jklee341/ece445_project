import cv2
from picamera2 import Picamera2
import numpy as np
from led_test import *
# thres = 0.45 # Threshold to detect object


classNames = []
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

picam2 = None

def getObjects(img, thres, nms, draw=True, objects=['person']):
    classIds, confs, bbox = net.detect(img, confThreshold=thres, nmsThreshold=nms)
    # print(classIds,bbox)

    objectInfo = []

    if len(classIds) != 0:
        flash_led()
        for classId, confidence, box in zip(classIds.flatten(), confs.flatten(), bbox):
            className = classNames[classId - 1]
            if className in objects:
                objectInfo.append([box, className])

                if draw:
                    cv2.rectangle(img, box, color=(0, 255, 0), thickness=2)
                    cv2.putText(img, classNames[classId - 1].upper(), (box[0] + 10, box[1] + 30),
                                cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                    cv2.putText(img, str(round(confidence * 100, 2)), (box[0] + 200, box[1] + 30),
                                cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

    else:
        turn_off_led()
    return img, objectInfo

def cameraOn():
    # Initialize PiCamera2
    global picam2
    picam2 = Picamera2()
    picam2.configure(picam2.create_preview_configuration())  # Lower resolution
    picam2.start()

    while True:
        # Capture frame from PiCamera2
        frame = picam2.capture_array()

        # Convert the frame to OpenCV format
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Resize frame
        img = cv2.resize(frame, (640, 480))

        # Run object detection
        result, objectInfo = getObjects(img, 0.45, 0.2)
        # print(objectInfo)

        cv2.imshow("Output", result)
        if cv2.waitKey(1) == ord('q'):
            break

def stop_camera():
    global picam2
    if picam2 is not None:
        picam2.stop()
        picam2 = None
    cv2.destroyAllWindows()
