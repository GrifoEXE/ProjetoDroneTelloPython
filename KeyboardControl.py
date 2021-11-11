import KeyPressModule as kp
from djitellopy import Tello, tello
from time import sleep

kp.init()
me = tello.Tello()
me.connect()
print(me.get_battery())


def getKeyInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 20

    if kp.getKey("a"):
        lr = -speed
    elif kp.getKey("d"):
        lr = speed

    if kp.getKey("UP"):
        ud = speed
    elif kp.getKey("DOWN"):
        ud = -speed

    # Forward/backwards
    if kp.getKey("w"):
        fb = speed
    elif kp.getKey("s"):
        fb = -speed

    # Rotation
    if kp.getKey("LEFT"):
        yv = speed
    elif kp.getKey("RIGHT"):
        yv = -speed

    if kp.getKey("q"): yv = me.takeoff()
    if kp.getKey("e"): yv = me.land()



    return [lr, fb, ud, yv]


while True:
    vals = getKeyInput()
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    sleep(0.1)
