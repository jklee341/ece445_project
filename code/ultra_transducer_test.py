import RPi.GPIO as GPIO
import time

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False) # Ignore warning for now

# Set the GPIO pin for the ultrasonic transducer
TRIG_PIN = 32

# Set the PWM frequency and duty cycle
PWM_FREQ = 10000  # 12 kHz
DUTY_CYCLE = 50   # 50% duty cycle

# Set up the GPIO pin as an output
GPIO.setup(TRIG_PIN, GPIO.OUT)

# Create a PWM object
pwm = GPIO.PWM(TRIG_PIN, PWM_FREQ)

# Start the PWM signal
pwm.start(DUTY_CYCLE)

# Set the total duration for the loop
TOTAL_DURATION = 5  # 5 seconds

# Get the start time
start_time = time.time()

# Generate bursts of pulses until the total duration is reached
while time.time() - start_time < TOTAL_DURATION:
    # Generate a burst of pulses for a specific duration
    BURST_DURATION = 0.0025  # 250 microseconds
    pwm.ChangeFrequency(PWM_FREQ)
    time.sleep(BURST_DURATION)

# Stop the PWM signal
pwm.stop()

# Clean up the GPIO pins
GPIO.cleanup()
