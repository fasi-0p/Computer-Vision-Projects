import cv2
import numpy as np

cap=cv2.VideoCapture(0)
for i in range(60):
    success,background=cap.read()

while True:
    success,frame=cap.read()
    if not success:
        print('Ignoring Camera')
        continue

    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    #lower_color=np.array([0,0,0]) # <--black  |  yellow-->([20, 100, 100]) #lower bound of yellow 
    #higher_color=np.array([180, 255, 50]) #<-- black |  yellow-->([30, 255, 255])  # Upper bound of yellow
    lower_color=np.array([140, 100, 100]) #for Pink
    higher_color=np.array([170,255,255]) 

    mask=cv2.inRange(hsv,lower_color,higher_color)

    colored_area=cv2.bitwise_and(frame,background, mask=mask)  #comparing pixels of current frame and capatured background. if same=1, else pixel=0. if 0 and in range of mask then replace it with backgorund image pixel. (not sure though)
    noncolored_area=cv2.bitwise_and(frame, frame, mask=cv2.bitwise_not(mask))
    #final_output=cv2.addWeighted(colored_area, 1, noncolored_area, 1, 0)
    final_output=cv2.add(colored_area, noncolored_area)

    cv2.imshow('Invisible Cloak',final_output)

    if cv2.waitKey(1)==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()