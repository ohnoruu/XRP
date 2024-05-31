# APCSP Period 2
from XRPLib.motor import Motor
from XRPLib.timeout import Timeout
from XRPLib.servo import Servo

# left motor on 6 and 7 is flipped
motorL = Motor(6,7,True)
motorR = Motor(14,15)
arm = Servo(16)

def turnRight():
    timer = Timeout(0.5)
    while not timer.is_done():
        motorL.set_effort(0.50)
    motorL.set_effort(0)
    
def turnLeft():
    timer = Timeout(0.5)
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
    
def waveArm():
    for i in range (5):
        timer = Timeout(0.25)
        while not timer.is_done():
            arm.set_angle(100)
        
        timer = Timeout(0.25)
        while not timer.is_done():
            arm.set_angle(0)
    
def moveSquare():
    for i in range (4):
        moveForward()
        turnRight()

#motorR.set_effort(0)
#motorL.set_effort(0)
moveSquare()
waveArm()
