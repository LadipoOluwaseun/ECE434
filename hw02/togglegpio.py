import Adafruit_BBIO.GPIO as GPIO
import time

out = "P9_12"
 
GPIO.setup(out, GPIO.OUT)
 
delay = float(input("delay " ))

while True:
    GPIO.output(out, GPIO.HIGH)
    time.sleep(delay)
    GPIO.output(out, GPIO.LOW)
    time.sleep(delay)

