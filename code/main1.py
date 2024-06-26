import RPi.GPIO as GPIO
import time
import cv2
from picamera2 import Picamera2
import numpy as np
import math
import sys
import threading
from radar import *
from detect import *

# change all these numbers to their respective GPIO pins
pir_1_in = 1
pir_2_in = 2
pir_3_in = 3

led_out = 4
buzzer_out = 5

# radar code sets up servo for pir/UR tower so we dont worry about this



def main():
    
    #Initialize all sensors/servos
        
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False) # Ignore warning for now
    
    #Inputs
    GPIO.setup(pir_1_in,GPIO.IN)
    GPIO.setup(pir_2_in,GPIO.IN)
    GPIO.setup(pir_3_in,GPIO.IN)
    
    #Outputs
    GPIO.setup(led_out, GPIO.OUT)
    GPIO.setup(buzzer_out, GPIO.OUT)
    

    
    while True:
        
        #Check if PIR detects anything
        
        while True:
            
            if GPIO.input(pir_1_in) or GPIO.input(pir_2_in) or GPIO.input(pir_3_in):
                print("Motion detected")
                break
    
        #If does start radar
        radar_loop()
    
        #Once radar stops start camera
        cameraOn()
        
        
        #Camera will make loop see if it detects anyhting, if does detect, lock on (this will be hard part)
            #Turn on LEDs and buzzer if detect 
        #If stop detecting restart loop
        
