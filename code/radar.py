import RPi.GPIO as GPIO
import pygame
import math
import time
import colors
import sys
from target import *
from display import draw
from ultrasonicsensor import ultrasonicRead
from servo import SetAngle
def radar_loop():
    print('Radar Start')

    # initialize the program
    pygame.init()
    pygame.font.init()
    defaultFont = pygame.font.get_default_font()
    fontRenderer = pygame.font.Font(defaultFont, 20)
    radarDisplay = pygame.display.set_mode((1400, 800))
    pygame.display.set_caption('Radar Screen')

    # setup the servo and ultrasonic
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    servoPin = 12
    GPIO.setup(servoPin, GPIO.OUT)
    servo = GPIO.PWM(servoPin, 50)
    servo.start(7)
    TRIG = 16
    ECHO = 18
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)

    # targets list
    targets = {}

    try:
        # rotate from 0 to 180
        for angle in range(0, 180):
            print(len(targets))
            distance = ultrasonicRead(GPIO, TRIG, ECHO)
            # change the condition if the range is changed
            if distance != -1 and distance <= 50:
                targets[angle] = Target(angle, distance)
            draw(radarDisplay, targets, angle, distance, fontRenderer)
            angle = 180 - angle
            dc = 1.0 / 18.0 * angle + 2
            servo.ChangeDutyCycle(dc)
            time.sleep(0.001)

        # rotate from 180 to 0
        for angle in range(180, 0, -1):
            distance = ultrasonicRead(GPIO, TRIG, ECHO)
            # change the condition if the range is changed
            if distance != -1 and distance <= 50:
                targets[angle] = Target(angle, distance)
            draw(radarDisplay, targets, angle, distance, fontRenderer)
            angle = 180 - angle
            dc = 1.0 / 18.0 * angle + 2
            servo.ChangeDutyCycle(dc)
            time.sleep(0.001)

    except KeyboardInterrupt:
        print('Radar Exit')
    except Exception as e:
        print(e)
        print('Radar Exit')
    finally:
        SetAngle(0)
        servo.stop()
        #SetAngle(0)
        GPIO.cleanup()
        pygame.quit()

if __name__ == "__main__":
    radar_loop()
