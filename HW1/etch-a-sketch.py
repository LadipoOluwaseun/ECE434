import curses
import time
##############################
# Author: Seun Ladipo
# ECE 434 HW #1
# Dr. Yoder
##############################
height = int(input("What is the height of the board? "))
width = int(input("What is the width of the board? "))
    
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
      char = window.getch()
      if char == 27: break
      elif char == curses.KEY_RIGHT: 
        if x <  width - 1:
          x+=1
      elif char == curses.KEY_LEFT:
        if x > 1:
          x-=1
      elif char == curses.KEY_UP: 
        if y > 1:
          y-=1 
      elif char == curses.KEY_DOWN: 
        if y < height - 1:
          y+=1
      else: True
      window.addstr(y, x * 2, "X")
      window.refresh()
      time.sleep(0.1)  
curses.wrapper(main)