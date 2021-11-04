import KeyPressModule as kp
from djitellopy import Tello, tello
from time import sleep
import time
import cv2

kp.init()
me = tello.Tello()
me.connect()
print(me.get_battery())
global img
me.streamon()


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

    if kp.getKey("z"): cv2.imwrite(f'Resources/Images/{time.time()}.png',img)


    return [lr, fb, ud, yv]


while True:
    vals = getKeyInput()
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    sleep(0.1)
    img = me.get_frame_read().frame
    img = cv2.resize(img,(360,240))
    cv2.imshow("Image", img)
    cv2.waitKey(1)