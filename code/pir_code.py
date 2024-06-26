import RPi.GPIO as GPIO
import time
#sensor_num=7

def pir(sensor_num):

    sensor = sensor_num 

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(sensor,GPIO.IN)

    print("Initialzing PIR Sensor......")
    time.sleep(3)
    print("PIR Ready...")

    try: 
       while True:
          if GPIO.input(sensor):
              print("Motion Detected")
              while GPIO.input(sensor):
                  time.sleep(0.2)
          else:
              print("no motion detected")
              time.sleep(0.2)


    except KeyboardInterrupt:
        GPIO.cleanup()
