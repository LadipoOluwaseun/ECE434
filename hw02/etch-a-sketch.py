import curses
import time
import Adafruit_BBIO.GPIO as GPIO

##############################
# Author: Seun Ladipo
# ECE 434 HW #2
# Dr. Yoder
##############################
height = int(input("What is the height of the board? "))
width = int(input("What is the width of the board? "))

up_key = "P9_30"
down_key = "P9_27"
left_key = "P9_23"
right_key = "P9_41"

up_led = "P8_15"
down_led ="P8_7"
left_led = "P8_11"
right_led = "P8_9"

GPIO.setup(up_key, GPIO.IN)
GPIO.setup(down_key, GPIO.IN)
GPIO.setup(left_key, GPIO.IN)
GPIO.setup(right_key, GPIO.IN)

GPIO.setup(up_led, GPIO.OUT)
GPIO.setup(down_led, GPIO.OUT)
GPIO.setup(left_led, GPIO.OUT)
GPIO.setup(right_led, GPIO.OUT)

def main(window):
  
    for w in range(width):
      window.addstr(0, w * 2, str(w))
      window.refresh()
      
    for h in range(height - 1):
      window.addstr(h + 1, 0, str(h + 1))
      window.refresh()
    
    x = 1
    y = 1
    window.nodelay(1)
    while True:
      GPIO.output(up_led, GPIO.LOW)
      GPIO.output(down_led, GPIO.LOW)
      GPIO.output(left_led, GPIO.LOW)
      GPIO.output(right_led, GPIO.LOW)
      
      char = window.getch()
      if char == 27: 
        break
    
      elif GPIO.input(right_key): 
        if x <  width - 1:
          x+=1
          GPIO.output(right_led, GPIO.HIGH)
      elif GPIO.input(left_key):
        if x > 1:
          x-=1
          GPIO.output(left_led, GPIO.HIGH)
      elif GPIO.input(up_key): 
        if y > 1:
          y-=1
          GPIO.output(up_led, GPIO.HIGH) 
      elif GPIO.input(down_key): 
        if y < height - 1:
          y+=1
          GPIO.output(down_led, GPIO.HIGH)
      else: True
      window.addstr(y, x * 2, "X")
      window.refresh()
      time.sleep(0.1)  
GPIO.cleanup()      
curses.wrapper(main)