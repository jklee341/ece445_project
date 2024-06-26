import RPi.GPIO as GPIO
import time
import threading

# This code will handle the functions for all the sensors


# Set the GPIO mode to BCM (Broadcom SOC channel numbering)
GPIO.setmode(GPIO.BCM)

# Set the GPIO pin for the servo signal (you can change this to any available GPIO pin)
servo_pin = 18
# Set the GPIO pin for the LED (you can change this to any available GPIO pin)
led_pin = 23

GPIO.setup(servo_pin, GPIO.OUT)
GPIO.setup(led_pin, GPIO.OUT)

# Define a function to turn the servo left or right by 10 degrees
def turn_servo(direction):
    # Set the initial duty cycle to 0
    servo = GPIO.PWM(servo_pin, 50)  # 50 Hz frequency
    servo.start(0)

    # Move the servo to the initial position (90 degrees)
    servo.ChangeDutyCycle(7.5)  # 7.5% duty cycle corresponds to 90 degrees
    time.sleep(1)  # Sleep for 1 second

    # Move the servo left or right by 10 degrees
    if direction == 1:
        servo.ChangeDutyCycle(5)  # 5% duty cycle corresponds to 0 degrees
    elif direction == 0:
        servo.ChangeDutyCycle(10)  # 10% duty cycle corresponds to 180 degrees
    time.sleep(1)  # Sleep for 1 second

    # Clean up the GPIO pins
    servo.stop()
    GPIO.cleanup()

# Define a function to flash the LED indefinitely
led_thread = None
led_flashing = False

def flash_led(frequency):
    global led_flashing
    period = 1 / frequency  # Calculate the period of the square wave
    led_flashing = True

    while led_flashing:
        GPIO.output(led_pin, GPIO.HIGH)
        time.sleep(period / 2)  # On for half the period
        GPIO.output(led_pin, GPIO.LOW)
        time.sleep(period / 2)  # Off for half the period

# Define a function to turn off the LED
def turn_off_led():
    global led_flashing
    led_flashing = False
