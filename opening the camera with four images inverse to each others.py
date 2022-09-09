import numpy as np
import cv2

#open web camera 
cap=cv2.VideoCapture(0)
while True:
    # cap.read() returns a bool (True/False). If frame is read correctly, it will be True.
    ret, frame= cap.read()
    #assign the width and height value 
    width=int(cap.get(3))
    height=int(cap.get(4))
    img=np.zeros(frame.shape,np.uint8)
    smaller_frame=cv2.resize(frame,(0,0),fx=0.5,fy=0.5)
    #opening the camera with four images which are inverse to each others
    img[:height//2, :width//2]=cv2.rotate(smaller_frame, cv2.ROTATE_180)
    img[height//2:, :width//2]=smaller_frame
    img[:height//2, width//2:]=cv2.rotate(smaller_frame, cv2.ROTATE_180)
    img[height//2:, width//2:]=smaller_frame
    cv2.imshow('frame',img)

    #if the delay time which passed is 1 and the user pressed q, break the loop and close the window
    if cv2.waitKey(1)==ord('q'):
        break
# video capture destructor and called automatically, Closes video file or capturing device
cap.release()
cv2.destroyAllWindows()