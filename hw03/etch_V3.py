import curses
import time
from PIL import Image
from PIL import ImageDraw
from Adafruit_LED_Backpack import Matrix8x8
from Adafruit_I2C import Adafruit_I2C
from Adafruit_BBIO.Encoder import RotaryEncoder, eQEP2, eQEP1
import Adafruit_BBIO.GPIO as GPIO

##############################
# Author: Seun Ladipo
# ECE 434 HW #3
# Dr. Yoder
##############################

#instantiane variables
height = 8
width = 8
x = 1
y = 1

#set up display matrix
display = Matrix8x8.Matrix8x8(address=0x70, busnum=2)
display.begin()

#setup gpio for erase screen
erase = "P9_30"
GPIO.setup(erase, GPIO.IN)

#setup encoders
xenc = RotaryEncoder(eQEP1)
yenc = RotaryEncoder(eQEP2)
xenc.setAbsolute()
yenc.setAbsolute()
xenc.enable()
yenc.enable()

x_cur = 0
y_cur = 0

#main program
while True:
    x_last = x_cur
    y_last = y_cur
    x_cur = xenc.position
    y_cur = yenc.position
    
    if GPIO.input(right_key): 
        display.clear()
        break
    elif x_cur < x_last: 
        if x <  width:
            x+=1
    elif x_cur > x_last: 
        if x > 1:
            x-=1
    elif y_cur < y_last: 
        if y > 1:
            y-=1 
    elif y_cur < y_last: 
        if y < height:
            y+=1
    else: True
    
    display.set_pixel(x, y - 1, 5)
    display.write_display()
    time.sleep(0.1)

display.clear()    