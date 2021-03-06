import KeyPressModule as kp
from djitellopy import Tello, tello
import numpy as np
from time import sleep
import time
import cv2
import math
import Communication_Serial

test = Communication_Serial.classSerial()

me = tello.Tello()
me.connect() #Drone
print(me.get_battery())
global img


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


print("Startando Communication_Serial")
test.Start()

vals = []

if(test.Process()):
    me.takeoff()
    sleep(7.0)


    vals = [0, 50, 0, 0]  # ir para frente
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    sleep(2.2)

    vals = [0, 0, 0, 0]  # PARADA
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    sleep(2.0)

    vals = [0, 0, 0, 25]  # girar
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    sleep(1.50)

    vals = [0, 0, 0, 0]  # PARADA COM FOTO
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    sleep(2.0)

    vals = [0, 0, 0, -25]  # girar
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    sleep(3.7)

    vals = [0, 0, 0, 0]  # PARADA COM FOTO
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    sleep(2.0)

    vals = [0, 0, 0, 25]  # girar de volta
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    sleep(1.7)

    vals = [0, 0, 0, 0]  # PARADA COM FOTO
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    sleep(2.0)

    vals = [0, -50, 0, 0]  # VOLTA
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    sleep(2.2)

    vals = [0, 0, 0, 0]  # PARADA
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    sleep(1.5)

    me.land()
    sleep(1.5)

while True:
    img = me.get_frame_read().frame
    img = cv2.resize(img,(1000, 800))
    cv2.imshow("Image", img)
    cv2.waitKey(0.5)
