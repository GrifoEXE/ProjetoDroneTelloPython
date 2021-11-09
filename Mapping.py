import KeyPressModule as kp
from djitellopy import Tello, tello
import numpy as np
from time import sleep
import time
import cv2
import math

####### PARAMETERS #######
fSpeed = 117/10 # Forward Speed in cm/s (15cm/s)
aSpeed = 360/10 # Angular Speed in degrees/s
interval = 0.25

dInterval = fSpeed * interval
aInterval = aSpeed * interval
##########################
x, y = 500, 500
a = 0
yaw = 0


kp.init()
me = tello.Tello()
me.connect()
print(me.get_battery())
me.streamon()

points = []

me.takeoff()
sleep(3)


def getKeyInput():
    lr, fb, ud, yv, tk = 0, 0, 0, 0, 0
    speed = 50
    d = 0
    global x, y, yaw, a

    if kp.getKey("a"): #LEFT
        lr = -speed
        d = dInterval
        a = -180

    elif kp.getKey("d"): #RIGHT
        lr = speed
        d = -dInterval
        a = 180

    # Forward/backwards
    if kp.getKey("w"): #FORWARDS
        fb = speed
        d = dInterval
        a = 270


    elif kp.getKey("s"): #BACKWARDS
        fb = -speed
        d = -dInterval
        a = -90


    if kp.getKey("UP"): #UP
        ud = speed


    elif kp.getKey("DOWN"): #DOWN
        ud = -speed


    # Rotation
    if kp.getKey("LEFT"): #ROTATION LEFT
        yv = speed
        yaw -= aInterval


    elif kp.getKey("RIGHT"): #ROTATION RIGHT
        yv = -speed
        yaw += aInterval



    if kp.getKey("q"): tk = me.takeoff() #TAKEOFF
    if kp.getKey("e"): tk = me.land() #LANDING

    #if kp.getKey("z"): #TAKE PICTURE
        #cv2.imwrite(f'Resources/Images/{time.time()}.png',img)
       # time.sleep (0.5)


    sleep(interval)
    a += yaw
    x += int(d * math.cos(math.radians(a)))
    y += int(d * math.sin(math.radians(a)))

    return [lr, fb, ud, yv, x, y, tk]

while True:
    #vals = getKeyInput()

    vals = [0, 50, 0, 0]
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    sleep(2)

    vals = [0, 0, 0, 0]
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    sleep(1.5)

    vals = [0, 0, 0, 50]
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    sleep(11)

    vals = [0, 0, 0, 0]
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    sleep(1.5)

    me.land()
