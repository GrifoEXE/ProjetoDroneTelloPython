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
me.takeoff()
me.land()
#def getKeyInput():

while True:
    # vals = getKeyInput()
    #vals = [0, 50, 0, 0] #Andar pra frente 1
    #me.send_rc_control(vals[0], vals[1], vals[2], vals[3])


    #vals = [0, 0, 0, 0] #parada
    #me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    #sleep(1.5)

    #vals = [0, 0, 0, 50] #RODADA 360
    #me.send_rc_control(vals[0], vals[1], vals[2], vals[3])


    #cv2.imwrite(f'Resources/Images/{time.time()}.png', img)
    #time.sleep(1)

    #sleep(10.2)

    #vals = [0, 0, 0, 0] #PARADA DPS DE RODADA 360
   # me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    #sleep(1.5)

    #vals = [0, -50, 0, 0] #VOLTAR DE RÉ
    #me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    #sleep(2)

    #vals = [0, 0, 0, 0] # PARAR DEPOIS DE VOLTAR
    #me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
   # sleep(1.5)

     #ATERRISSAR

    img = me.get_frame_read().frame
    img = cv2.resize(img,(360,240))
    cv2.imshow("Image", img)
    cv2.waitKey(1)
