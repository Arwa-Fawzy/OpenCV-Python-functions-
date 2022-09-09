import numpy as np
import cv2

cap=cv2.VideoCapture(0)

while True:
    ret, frame=cap.read()
    width=int(cap.get(3))
    height=int(cap.get(4))
    #converting from BGR sccale to HSV 
    hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #determining the upper and lower boundries 
    lower_blue=np.array([110,50,50])
    upper_blue=np.array([130,255,255])
    #mask is a specific portion of the image which is blue objects  
    mask=cv2.inRange(hsv, lower_blue,upper_blue)
    result=cv2.bitwise_and(frame,frame,mask=mask)
    
    cv2.imshow('frame',result)
    cv2.imshow('mask',mask)
    if cv2.waitKey(1)==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
bgr_color=np.array([[[255,0,0]]])
x=cv2.cvtColor(bgr_color, cv2.COLOR_BGR2HSV)
x[0][0]
