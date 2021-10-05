# File: Breakout.py

"""
This program (once you have finished it) implements the Breakout game
"""

from tkinter.constants import TRUE
from pgl import GWindow, GOval, GRect, GState
import random

# Constants
GWINDOW_WIDTH = 360                     # Width of the graphics window
GWINDOW_HEIGHT = 600                    # Height of the graphics window
N_ROWS = 10                             # Number of brick rows
N_COLS = 10                             # Number of brick columns
BRICK_ASPECT_RATIO = 4 / 1              # Width to height ratio of a brick
BRICK_TO_BALL_RATIO = 3 / 1             # Ratio of brick width to ball size
BRICK_TO_PADDLE_RATIO = 2 / 3           # Ratio of brick to paddle width
BRICK_SEP = 2                           # Separation between bricks (in pixels)
TOP_FRACTION = 0.1                      # Fraction of window above bricks
BOTTOM_FRACTION = 0.05                  # Fraction of window below paddle
N_BALLS = 3                             # Number of balls (lives) in a game
TIME_STEP = 10                          # Time step in milliseconds
INITIAL_Y_VELOCITY = 3.0                # Starting y velocity downwards
MIN_X_VELOCITY = 1.0                    # Minimum random x velocity
MAX_X_VELOCITY = 3.0                    # Maximum random x velocity

# Derived Constants
BRICK_WIDTH = (GWINDOW_WIDTH - (N_COLS + 1) * BRICK_SEP) / N_COLS
BRICK_HEIGHT = BRICK_WIDTH / BRICK_ASPECT_RATIO
PADDLE_WIDTH = BRICK_WIDTH / BRICK_TO_PADDLE_RATIO
PADDLE_HEIGHT = BRICK_HEIGHT / BRICK_TO_PADDLE_RATIO
PADDLE_Y = (1 - BOTTOM_FRACTION) * GWINDOW_HEIGHT - PADDLE_HEIGHT
BALL_SIZE = BRICK_WIDTH / BRICK_TO_BALL_RATIO


# Function: breakout
def breakout():
    """The main program for the Breakout game."""

    gw = GWindow(GWINDOW_WIDTH, GWINDOW_HEIGHT)
    gs = GState()
    Grey_Paddle(gw,160)
    gw.add_event_listener("mousemove", mousemove_event)
    populateBricks(gw)
    setBallLocation(gw,.1,.1,80,PADDLE_Y-50)
    # You fill in the rest of this function along with any additional
    # helper and callback functions you need

def Grey_Paddle(gw,xpos):
    rect = GRect(xpos,PADDLE_Y,PADDLE_WIDTH,PADDLE_HEIGHT)
    rect.set_color("Grey")
    rect.set_filled(True)
    gw.add(rect)
    # You fill in the rest of this function along with any additional
    # helper and callback functions you need

def mousemove_event(e):
        x = e.get_x()
        y = e.get_y()
        #Grey_Paddle(gw,x)
        print(x)
def drag_action(e):
        gs.line.set_end_point(e.get_x(), e.get_y())

gw = GWindow(360, 600)
gs = GState()
gs.line = None
gw.add_event_listener("mousemove", mousemove_event)
    
    
def setBallLocation(gw,vx,vy,initialX,initialY):
    #step function updates the ball location in the timer function 
    def step():
        oval.move(dx, dy)
        if oval.get_x() <0 or oval.get_x()>GWINDOW_WIDTH-40:
            oval.move(-dx,dy)
            timer.stop()
        elif oval.get_y() <0 or oval.get_y()>GWINDOW_HEIGHT-40:
            timer.stop()
    #initialize deltas and set the ball into canvas
    dx = 1
    dy = .4
    oval=GOval(initialX,initialY,BALL_SIZE,BALL_SIZE)
    oval.set_color('black')
    oval.set_filled(True)
    gw.add(oval)
    timer = gw.set_interval(step, 20)

def populateBricks(gw):
    
    #initalizing values for the bricks
    columnCount=0
    totalBlocks=0
    color=['red','orange','green','#1F85DE','blue']
    colorRowCount=0
    colorIndex=0
    brickXLoc=5
    brickYLoc=20
    brickColor=color[0]
    while(totalBlocks<N_ROWS*N_COLS):
        if(columnCount==N_COLS):
            #separate the rows and start at the beginning of a new row
            columnCount=0
            colorRowCount+=1
            brickYLoc+=35
            brickXLoc=5
            #every other row the color changes
            #also makes sure index is not out of bounds
        if(colorRowCount==2):
            colorRowCount=0
            colorIndex+=1
            if(len(color)>colorIndex):
                brickColor=color[colorIndex]

        #initalizing the brick to be added to the canvas
        rect=GRect(brickXLoc,brickYLoc,BRICK_WIDTH-5,BRICK_HEIGHT)
        rect.set_color(brickColor)
        rect.set_filled(True)

        #update for next brick and push current brick to canvas
        brickXLoc+=35
        totalBlocks+=1
        columnCount+=1
        gw.add(rect)




# Startup code
if __name__ == "__main__":
    breakout()
