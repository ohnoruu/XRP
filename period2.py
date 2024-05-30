# APCSP Period 2
from XRPLib.motor import Motor
from XRPLib.timeout import Timeout

# left motor on 6 and 7 is flipped
motorL = Motor(6,7,True)
motorR = Motor(14,15)

def turnRight():
    timer = Timeout(1) 
    while not timer.is_done():
        motorL.set_effort(0.50)
    motorL.set_effort(0)
    
def turnLeft():
    timer = Timeout(1) 
    while not timer.is_done():
        motorR.set_effort(0.50)
    motorR.set_effort(0)
    
def moveForward():
    timer = Timeout(1) # 1 second timer
    while not timer.is_done():
        motorL.set_effort(0.50)
        motorR.set_effort(0.50)

    # timer finishes
    motorL.set_effort(0)
    motorR.set_effort(0)
    
def moveSquare():
    for i in range (4):
        moveForward()
        turnRight()
    
#moveForward()
#turnRight()

moveSquare()
