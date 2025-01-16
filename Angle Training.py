import cv2
import mediapipe as mp
import time
import math

mppose=mp.solutions.pose
pose=mppose.Pose()
mpDraw=mp.solutions.drawing_utils

cap=cv2.VideoCapture(0)
count=0

while True:
    success,img=cap.read()
    if not success:
        print('ignoring camera')
        continue
    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    result=pose.process(imgRGB)

    if (result.pose_landmarks):
       for id,lm in enumerate(result.pose_landmarks.landmark):
           h,w,c=img.shape
           cx,cy=int(lm.x*w), int(lm.y*h)
           if (id==11):           #id 11,13,15 represent left arm
               point_11=cx,cy
               cv2.circle(img,(cx,cy),10,(200,0,0), cv2.FILLED)
               #print(id,cx,cy)
           if (id==13):
               point_13=cx,cy
               cv2.circle(img,(cx,cy),10,(200,0,0), cv2.FILLED)
               #print(id,cx,cy)
           if (id==15):
               point_15=cx,cy
               cv2.circle(img,(cx,cy), 10, (200,0,0), cv2.FILLED)


           if (id==12):            #id 12,14,16 represent right arm
               point_12=cx,cy
               cv2.circle(img,(cx,cy),10,(200,0,0), cv2.FILLED)
               #print(id,cx,cy)
           if (id==14):
               point_14=cx,cy
               cv2.circle(img,(cx,cy),10,(200,0,0), cv2.FILLED)
               #print(id,cx,cy)
           if (id==16):
               point_16=cx,cy
               cv2.circle(img,(cx,cy), 10, (200,0,0), cv2.FILLED)

               if (point_11 and point_13 and point_15):   #prints angle of left inner elbow
                 angle1=math.degrees(math.atan2(point_15[1]-point_13[1], point_15[0]-point_13[0]) - math.atan2(point_11[1]-point_13[1], point_11[0]- point_13[0]))
                 print ('Angle 1= ',angle1)
               if (point_12 and point_14 and point_16):   #prints angle of right inner elbow
                 angle2=math.degrees(math.atan2(point_12[1]-point_14[1], point_12[0]-point_14[0]) - math.atan2(point_16[1]-point_14[1], point_16[0]- point_14[0]))
                 print('Angle 2= ', angle2)


               
                 
                   
            


       mpDraw.draw_landmarks(img,result.pose_landmarks,mppose.POSE_CONNECTIONS)
       cv2.imshow('camera feed',img)
    if (cv2.waitKey(1) & 0xFF == ord('q')):
        break
cap.release()
cv2.destroyAllWindows()
