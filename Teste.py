import KeyPressModule as kp
from djitellopy import Tello, tello
import numpy as np
from time import sleep
import time
import cv2
import math

kp.init()
me = tello.Tello()
me.connect()
print(me.get_battery())
me.streamon()
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


vals = []

me.takeoff()
sleep(3.0)

vals = [0, 50, 0, 0]  # ir para frente
me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
sleep(3)

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
sleep(3.0)

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
sleep(2.5)

vals = [0, 0, 0, 0]  # PARADA
me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
sleep(1.5)

me.land()
sleep(1.5)
me.streamoff()


