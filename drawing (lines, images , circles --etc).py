import numpy as np
import cv2

cap=cv2.VideoCapture(0)

while True:
    ret, frame=cap.read()
    width=int(cap.get(3))
    height=int(cap.get(4))
    #drawing cross lines
    img=cv2.line(frame, (0,0),(width,height), (255,0,0),10)
    img=cv2.line(frame, (0,height),(width,0), (255,0,0),10)
    #drawing rectangle, if you want to fill its area by color, write -1 as las argument 
    img=cv2.rectangle(frame, (100,100),(200,200), (255,0,0),5)
    #drawing circle with radius 50 
    img=cv2.circle(frame, (0,0),50, (255,0,0),5)
    #writing a word and specify the target color and style of the font
    font=cv2.FONT_HERSHEY_COMPLEX
    img=cv2.putText(img,'Arwa',(10, height-10),font,4,(0,255,0),5,cv2.LINE_AA)
    cv2.imshow('frame',img)
    if cv2.waitKey(1)==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()