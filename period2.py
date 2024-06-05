# APCSP Period 2
import math
from XRPLib.motor import Motor
from XRPLib.timeout import Timeout
from XRPLib.servo import Servo # arm
from XRPLib.encoder import Encoder # sensors
from XRPLib.imu import IMU
from XRPLib.imu_defs import *

# DEFINING PINS
motorL = Motor(6,7,True) # left motor on 6 and 7 is flipped
encoderL = Encoder(0,4,5) # encoder 0 on pins 4 and 5
motorR = Motor(14,15)
encoderR = Encoder(1,12,13) # encoder 1 on pins 12 and 13
imu = IMU(19, 18, LSM_ADDR_PRIMARY) # IMU (clock_pin, data_pin, mem_address)
arm = Servo(16)

wheelDiameter = 6 # cm

def turnRight():
    imu.reset_yaw()
    while imu.get_yaw() > (-90):
        motorL.set_effort(0.5)
        motorR.set_effort(-0.5)
    imu.reset_yaw()
    stop()
    
def turnLeft():
    imu.reset_yaw()
    while imu.get_yaw() < 90:
        motorL.set_effort(-0.5)
        motorR.set_effort(0.5)
    imu.reset_yaw()
    stop()
    
def moveForward(distancecm):
    while abs(encoderL.get_position())*math.pi*wheelDiameter < distancecm: 
        motorL.set_effort(0.5)
        motorR.set_effort(0.5)
    resetEncoders()
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
#moveSquare(10)

# 1 tile = 30cm
moveForward(60) # 2 tiles 
turnRight()
moveForward(60) # 2 tiles
turnLeft()
moveForward(90) # 3 tiles 
turnLeft()
moveForward(60) # 2 tiles 
turnRight()
moveForward(30) # 1 tile
