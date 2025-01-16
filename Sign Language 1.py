import cv2
import mediapipe as mp
mphands=mp.solutions.hands
hands=mphands.Hands()
mpDraw=mp.solutions.drawing_utils
import math

cap=cv2.VideoCapture(0)

while True:
    success, img=cap.read()
    if not success:
        print('ignoring camera')
        continue
    imgRGB=cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    result=hands.process(imgRGB)
    cv2.imshow('camera feed', img)
    if (result.multi_hand_landmarks):
        for i in result.multi_hand_landmarks:

            for id, lm in enumerate (i.landmark):
                h,w,c=img.shape
                cx,cy=int(lm.x*w), int(lm.y*h)

                if (id==17):
                    point_17=cx,cy
                if(id==1):
                    point_1=cx,cy
                if(id==0):
                    point_0=cx,cy

                if(id==8):
                    point_8=cx,cy
                if(id==5):
                    point_5=cx,cy
                if(id==12):
                    point_12=cx,cy
                
            if(point_8  and point_5  and  point_12):
                angle_v=math.degrees(math.atan2(point_8[1]-point_5[1], point_8[0]-point_5[0]) - math.atan2(point_12[1]-point_5[1],point_12[0]-point_5[0]))
                      
            if(point_17 and point_1 and point_0):
                angle_c=math.degrees(math.atan2(point_1[1]-point_0[1], point_1[0]-point_0[0]) - math.atan2(point_17[1]-point_0[1], point_17[0]-point_0[0]))
                
                
                if (i.landmark[8].y*img.shape[0] > i.landmark[6].y*img.shape[0]  and  i.landmark[12].y*img.shape[0] > i.landmark[10].y*img.shape[0]  and  i.landmark[16].y*img.shape[0] > i.landmark[14].y*img.shape[0]  and  i.landmark[20].y*img.shape[0] > i.landmark[18].y*img.shape[0]  and  i.landmark[2].y*img.shape[0]>i.landmark[3].y*img.shape[0]>i.landmark[4].y*img.shape[0]  and  i.landmark[4].x*img.shape[1]> i.landmark[6].x*img.shape[1]):
                    #corpus=[]
                    #corpus.append('A')
                    print('A')
                    #here all tips need to be below 6,10,14,18, and thumb should be standing and beside knuckle of index
                if (i.landmark[8].y*img.shape[0] < i.landmark[7].y*img.shape[0]  and  i.landmark[12].y*img.shape[0] < i.landmark[11].y*img.shape[0]  and  i.landmark[16].y*img.shape[0] < i.landmark[15].y*img.shape[0]  and  i.landmark[20].y*img.shape[0] < i.landmark[19].y*img.shape[0]  and i.landmark[4].x*img.shape[1] < i.landmark[6].x*img.shape[1] and i.landmark[4].y*img.shape[0]>i.landmark[6].y*img.shape[0] ):
                    print('B')
                    #all tips need to be above 6,10,14,18 and thumb should be less than/ within 6 x coordinate
                 #(abs(i.landmark[8].y - i.landmark[4].y) < 0.20 or abs(i.landmark[12].y - i.landmark[4].y) < 0.20 or abs(i.landmark[16].y - i.landmark[4].y) < 0.20 or abs(i.landmark[20].y - i.landmark[4].y) < 0.20 ):#or i.landmark[4].x > i.landmark[8].x > i.landmark[12].x > i.landmark[16].x > i.landmark[20].x):
                
                #if (((i.landmark[8].y - i.landmark[4].y) and (i.landmark[8].x - i.landmark[4].x)) > 0.001 or ((i.landmark[12].y - i.landmark[4].y) and (i.landmark[12].x - i.landmark[4].x)) > 0.001 or ((i.landmark[16].y - i.landmark[4].y) and (i.landmark[16].x - i.landmark[4].x))> 0.001 or ((i.landmark[20].y - i.landmark[4].y) and (i.landmark[20].x - i.landmark[4].x)) > 0.001 ):#or i.landmark[4].x > i.landmark[8].x > i.landmark[12].x > i.landmark[16].x > i.landmark[20].x):
                if (55<angle_c<75):
                    print('C')
                    #angle between 1,0,17 should be between 55 and 75. during normal uphold angle=85

                if(i.landmark[12].y*img.shape[0] > i.landmark[10].y*img.shape[0] and i.landmark[16].y*img.shape[0] > i.landmark[14].y*img.shape[0] and i.landmark[20].y*img.shape[0] > i.landmark[18].y*img.shape[0] and i.landmark[8].y*img.shape[0]< i.landmark[6].y*img.shape[0]          and i.landmark[4].x*img.shape[0]< i.landmark[10].x*img.shape[0]):
                    print('D')
                    #all tips except index should be below 10,14,18. index should be above 6. no Fucks for thumb 

                if (i.landmark[2].y*img.shape[0]> i.landmark[8].y*img.shape[0] and i.landmark[3].y*img.shape[0]> i.landmark[12].y*img.shape[0] and i.landmark[2].y*img.shape[0]>i.landmark[12].y*img.shape[0] and i.landmark[4].y*img.shape[0]> i.landmark[20].y*img.shape[0] and i.landmark[2].x*img.shape[1]>i.landmark[3].x*img.shape[1]>i.landmark[4].x*img.shape[1] and i.landmark[8].y*img.shape[0]>i.landmark[6].y*img.shape[0] and i.landmark[12].y*img.shape[0]> i.landmark[10].y*img.shape[0]):
                    #thumb points should be below rest 4 tips, thumb should be horizontal, rest 4 fingers's tips should be below mid knucles
                    print('E')

                if (i.landmark[10].y*img.shape[0]> i.landmark[12].y*img.shape[0] and i.landmark[14].y*img.shape[0]> i.landmark[16].y*img.shape[0] and i.landmark[18].y*img.shape[0]> i.landmark[20].y*img.shape[0]  and  i.landmark[3].y*img.shape[0]>i.landmark[4].y*img.shape[0]> i.landmark[8].y*img.shape[0]> i.landmark[6].y*img.shape[0]):
                    print('F')
                    #middle,ring,pinky should be above its respective knuckles and index knuckle above index tip, above thumb tip, above thumb knuckle

                if (i.landmark[8].x*img.shape[1]> i.landmark[6].x*img.shape[1]  and  i.landmark[4].x*img.shape[1]>i.landmark[2].x*img.shape[1]  and  i.landmark[7].y*img.shape[0]> i.landmark[6].y*img.shape[0]  and  i.landmark[11].y*img.shape[0]> i.landmark[10].y*img.shape[0]  and  i.landmark[15].y*img.shape[0]> i.landmark[14].y*img.shape[0]  and i.landmark[19].y*img.shape[0]> i.landmark[18].y*img.shape[0]):
                    #joint below tip should be below knuckle of middle,ring, pinky finger,    index and thumb finger should be horizontal 
                    print('G')

                if (i.landmark[18].y*img.shape[0]>i.landmark[14].y*img.shape[0]> i.landmark[10].y*img.shape[0]> i.landmark[6].y*img.shape[0]  and  i.landmark[12].x*img.shape[1]> i.landmark[10].x*img.shape[1]  and  i.landmark[8].x*img.shape[1]>i.landmark[6].x*img.shape[1]):
                    print('H')
                    #all knuckle joints should be below one on the other, index and middle should be horizontal with respect to its knuckle

                if (i.landmark[18].y*img.shape[0]> i.landmark[20].y*img.shape[0]  and  i.landmark[16].y*img.shape[0]>i.landmark[18].y*img.shape[0]  and i.landmark[6].x*img.shape[1]> i.landmark[4].x*img.shape[1]):
                    print('I')
                    #pinky finger should be vertical WRT its knuckle, joint below ring should be below knuckle of ring, thumb should be inside joint of index WRT x axis

                #NO "J" AS OF NOW AS IT REQUIRES MOVEMENT

                if (i.landmark[6].x*img.shape[1]>i.landmark[4].x*img.shape[1]> i.landmark[10].x*img.shape[1]  and  i.landmark[15].y*img.shape[0]< i.landmark[16].y*img.shape[0] and i.landmark[10].y*img.shape[0]>i.landmark[12].y*img.shape[0]):
                    print('K')
                    #thumb should be between knuckle of middle finger and index finger, joint below ring and pinky should be below knuckle of ring and pinky, while index is vertical

                if (i.landmark[11].y*img.shape[0]>i.landmark[10].y*img.shape[0]  and  i.landmark[15].y*img.shape[0]>i.landmark[14].y*img.shape[0]  and  i.landmark[19].y*img.shape[0]>i.landmark[18].y*img.shape[0]  and  i.landmark[6].y*img.shape[0]> i.landmark[8].y*img.shape[0]  and i.landmark[4].x*img.shape[1]>i.landmark[2].x*img.shape[1]):
                    print('L')
                    #joints should be below knuckle of middle,ring,pinky and index should be vertical WRT its knuckle and thumb should be horizontal WRT its knuckle
                
                if (i.landmark[6].x*img.shape[1]> i.landmark[10].x*img.shape[1]> i.landmark[14].x*img.shape[1]> i.landmark[4].x*img.shape[1]> i.landmark[18].x*img.shape[1]  and  i.landmark[8].y*img.shape[0]> i.landmark[6].y*img.shape[0]):
                    print('M')
                    #thumb should be between pinky and ring finger WRT x-axis, index finger should be bent. we could have included index,middle,ring but it would make it long
                if (i.landmark[6].x*img.shape[1]> i.landmark[10].x*img.shape[1]> i.landmark[4].x*img.shape[1]> i.landmark[14].x*img.shape[1]> i.landmark[18].x*img.shape[1]  and  i.landmark[15].y*img.shape[0]>i.landmark[4].y*img.shape[0]):
                    print('N')
                    #thumb should be between middle and ring finger WRT x-axis, inorder for it to not confuse with 'S' thumb should be above joint of ring

                #NO "O" AS OF NOW AS IT IS SIMILAR TO C

                #if ((i.landmark[12].y*img.shape[0]> i.landmark[10].y*img.shape[0] or i.landmark[16].y*img.shape[0]> i.landmark[14].y*img.shape[0] or i.landmark[20].y*img.shape[0]> i.landmark[18].y*img.shape[0] ) and  i.landmark[8].y*img.shape[0]> i.landmark[6].y*img.shape[0]  and  i.landmark[8].x*img.shape[1]<i.landmark[6].x*img.shape[1]):
                 #   print('P')
                    #not working accurately
                    #middle and thumb should be down, index should be horizontal. ('or' was done for all fingers because it wasnt distinguishing middle and other fingers)

                if (i.landmark[8].y*img.shape[0]>i.landmark[6].y*img.shape[0]  and  i.landmark[4].y*img.shape[0]>i.landmark[2].y*img.shape[0]):
                    print('Q')
                    #index and ring should be down
                    #confusing between P and Q
                
                if(i.landmark[12].x*img.shape[1]>i.landmark[8].x*img.shape[1]):
                    print('R')
                    #index tip should be after middle tip but inorder for it not confuse with 'N' dont give use thumb 

                #if (i.landmark[11].y*img.shape[0]>i.landmark[4].y*img.shape[0]>i.landmark[10].y*img.shape[0]):
                 #   print('S')
                    #if thumb is between joint and knuckle of middle finger

                if (i.landmark[6].x*img.shape[1]> i.landmark[4].x*img.shape[1]> i.landmark[10].x*img.shape[1]> i.landmark[14].x*img.shape[1]> i.landmark[18].x*img.shape[1]):
                    print('T')
                    #if thumb is between middle and index finger
                    #confusing between S and P

                if (i.landmark[15].y*img.shape[0]> i.landmark[14].y*img.shape[0]  and  i.landmark[19].y*img.shape[0]> i.landmark[18].y*img.shape[0]  and  i.landmark[6].y*img.shape[0]> i.landmark[8].y*img.shape[0]  and  i.landmark[10].y*img.shape[0]>i.landmark[12].y*img.shape[0]  and  angle_v<15):
                    print('U')
                    #if index and middle finger are standing, ring is bent, and angle_v is less than 15 degree
                
                #if ((i.landmark[5].x*img.shape[1]-i.landmark[9].x*img.shape[1])  <  (i.landmark[8].x*img.shape[1]-i.landmark[12].x*img.shape[1])):
                if (20<angle_v<50  and  i.landmark[16].y*img.shape[0]>i.landmark[14].y*img.shape[0]):
                    print('V')
                    #if angle between index tip, index base, middle tip is between 20-50. usual standing angle is around 10-15 which is used for 'U

                if (i.landmark[6].y*img.shape[0]>i.landmark[8].y*img.shape[0]  and  i.landmark[10].y*img.shape[0]>i.landmark[12].y*img.shape[0]  and i.landmark[14].y*img.shape[0]>i.landmark[16].y*img.shape[0]  and  i.landmark[20].y*img.shape[0]>i.landmark[18].y*img.shape[0]):
                    print('W')
                    #if index,middle,ring are vertical
                
                #if (i.landmark[5].y*img.shape[0]> i.landmark[6].y*img.shape[0]  and  i.landmark[8].x*img.shape[1]> i.landmark[6].x*img.shape[1]  and  i.landmark[11].y*img.shape[0]<i.landmark[12].y*img.shape[0]  and  i.landmark[15].y*img.shape[0]<i.landmark[16].y*img.shape[0]  and  i.landmark[19].y*img.shape[0]<i.landmark[20].y*img.shape[0]):
                 #   print('X')
                    #not working properly
                    #knuckle of index should be above base, and tip of index should be left side of knuckle of index

                if (i.landmark[17].y*img.shape[0]>i.landmark[20].y*img.shape[0]  and  i.landmark[2].y*img.shape[0]>i.landmark[4].y*img.shape[0]  and  i.landmark[7].y*img.shape[0]>i.landmark[6].y*img.shape[0]  and  i.landmark[11].y*img.shape[0]>i.landmark[10].y*img.shape[0]  and  i.landmark[15].y*img.shape[0]>i.landmark[14].y*img.shape[0]):
                    print('Y')








            mpDraw.draw_landmarks(img,i,mphands.HAND_CONNECTIONS)
            cv2.imshow('camera feed', img)
    if (cv2.waitKey(1) & 0xFF == ord('q')):
        break
cap.release()
cv2.destroyAllWindows()