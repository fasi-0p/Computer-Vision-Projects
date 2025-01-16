import cv2
import time
import mediapipe as mp
import math
import numpy as np
hands=mp.solutions.hands
mphands=hands.Hands()
mpDraw=mp.solutions.drawing_utils

from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)
volumerange=volume.GetVolumeRange()
minvol=volumerange[0]
maxvol=volumerange[1]
volume.SetMasterVolumeLevel(-20.0, None)
cap=cv2.VideoCapture(0)

while True:
    success, img=cap.read()
    if not success:
        print('ignoring camera')
        continue
    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    result=mphands.process(imgRGB)
    cv2.imshow('camera feed',img)

    if (result.multi_hand_landmarks):
        for i in result.multi_hand_landmarks:
            for id,lm in enumerate(i.landmark):  #real shit for controlling volume
                h,w,c=img.shape
                cx,cy=int(lm.x*w),int(lm.y*h)
                if (id==4):
                    cv2.circle(img,(cx,cy),15,(100,255,100),cv2.FILLED) #plots cordinates of thumb
                    point_4=cx,cy
                if (id==8):
                    cv2.circle(img,(cx,cy),15,(100,255,100),cv2.FILLED) #plots cordinates of index
                    point_8=cx,cy
            if (point_4 and point_8):  #this shouldnt be in id,lm for loop
                cv2.line(img, point_4,point_8,color= (0,255,0), thickness=2) #creates a line between 2 cordinates 
                
                length=math.hypot(point_4[0]-point_8[0], point_4[1]-point_8[1]) #calculates distance between thumb and index
                #print(length)
                vol_controller=np.interp(length,[30,200],[minvol,maxvol]) #interpretes the distance which will be between 30,200 for minvol,maxvol
                volume.SetMasterVolumeLevel(vol_controller, None) #sets the volume as vol_controller transmits
                
            mpDraw.draw_landmarks(img,i,hands.HAND_CONNECTIONS) #tracks and draws line on hand
            cv2.imshow('camera feed',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
