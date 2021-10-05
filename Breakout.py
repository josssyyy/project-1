# File: Breakout.py

"""
This program (once you have finished it) implements the Breakout game
"""

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
    populateBricks(gw)
    setBallLocation(gw,.2,.3,80,PADDLE_Y-50)
    # You fill in the rest of this function along with any additional
    # helper and callback functions you need

def setBallLocation(gw,vx,vy,initialX,initialY):
    boundLeft=0
    boundTop=0
    boundRight=GWINDOW_WIDTH
    boundBottom=GWINDOW_HEIGHT
    
    vx=vx
    vy=vy

    oval=GOval(initialX,initialY,BALL_SIZE,BALL_SIZE)
    oval.set_color('black')
    oval.set_filled(True)
    gw.add(oval)
    if(initialX<boundLeft or initialX>boundRight or initialY<boundTop or initialY>boundBottom):
        print("out of bounds")
    else:
        setBallLocation(gw,vx,vy,initialX+vx,initialY+vy)

def populateBricks(gw):
    i=0
    totalBlocks=0
    color=['red','orange','green','#1F85DE','blue']
    colorRowCount=0
    colorIndex=0
    brickXLoc=5
    brickYLoc=20
    brickColor=color[0]
    while(totalBlocks<N_ROWS*N_COLS):
        if(i==N_COLS):
            i=0
            colorRowCount+=1
            brickYLoc+=35
            brickXLoc=5
        if(colorRowCount==2):
            colorRowCount=0
            colorIndex+=1
            if(len(color)>colorIndex):
                brickColor=color[colorIndex]
        rect=GRect(brickXLoc,brickYLoc,BRICK_WIDTH-5,BRICK_HEIGHT)
        rect.set_color(brickColor)
        rect.set_filled(True)
        brickXLoc+=35
        totalBlocks+=1
        i+=1
        gw.add(rect)




# Startup code
if __name__ == "__main__":
    breakout()
