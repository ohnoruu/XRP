# APCSP Period 2
import math
from XRPLib.motor import Motor
from XRPLib.timeout import Timeout
from XRPLib.servo import Servo # arm
from XRPLib.encoder import Encoder # sensors

# left motor on 6 and 7 is flipped
motorL = Motor(6,7,True)
encoderL = Encoder(0,4,5) # encoder 0 on pins 4 and 5

motorR = Motor(14,15)
encoderR = Encoder(1,12,13)

arm = Servo(16)

wheelDiameter = 6 # cm

def turnRight():
    trackwidth = 15.5 # cm
    quarterTurn = 0.25*math.pi*trackwidth
    while abs(encoderR.get_position())*math.pi*wheelDiameter < quarterTurn: 
        motorL.set_effort(0.5)
        motorR.set_effort(-0.5)
    stop()
    
def turnLeft():
    trackwidth = 15.5 # cm
    quarterTurn = 0.25*math.pi*trackwidth
    while abs(encoderL.get_position())*math.pi*wheelDiameter < quarterTurn: 
        motorL.set_effort(-0.5)
        motorR.set_effort(0.5)
    stop()
    
def moveForward(distancecm):
    while abs(encoderL.get_position())*math.pi*wheelDiameter < distancecm: 
        motorL.set_effort(0.5)
        motorR.set_effort(0.5)
    stop()
    
def stop():
    motorR.set_effort(0)
    motorL.set_effort(0)
    
def resetEncoders():
    encoderL.reset_encoder_position()
    encoderR.reset_encoder_position()
    
def waveArm():
    arm.set_angle(0)
    for i in range (5):
        timer = Timeout(0.25)
        while not timer.is_done():
            arm.set_angle(100)
        
        timer = Timeout(0.25)
        while not timer.is_done():
            arm.set_angle(0)
    
def moveSquare(sidelength):
    for i in range (4):
        resetEncoders()
        moveForward(sidelength)
        resetEncoders()
        turnLeft()

#stop()
moveSquare(10)
#waveArm()
