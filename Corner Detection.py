import numpy as np 
import cv2

img=cv2.imread('Desktop/chess.jpg')
img=cv2.resize(img, (0,0),fx=0.75,fy=0.75)
gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#0-1 quality, 1 means perfect
#detect 100 corners in the image  
#the last argument means the minimum euclidean(straight distance between two points) distance between corners
corners=cv2.goodFeaturesToTrack(gray, 100,0.01, 10)
#print(corners) is float values 
corners=np.int0(corners)

#loop through the corners 
for corner in corners:
    #make the array flatten [[1,2],[2,1]]>>[1,2,2,1]
    x,y=corner.ravel()
    #to draw the corner 
    cv2.circle(img, (x,y),5,(255,0,0),-1)
# to draw lines between corners 
for i in range(len(corners)):
    for j in range(i+1,len(corners)):
        corner1=tuple(corners[i][0])
        corner2=tuple(corners[j][0])
        #random return 64 bits as list of integers and numpy converts it ro regular integers 
        #lambda converts every number into integer and save it in a map, finally, convert it to a tuple 
        color=tuple(map(lambda x: int(x), np.random.randint(0,255,size=3)))
        cv2.line(img,corner1,corner2,color,1)




cv2.imshow('frame',img)
cv2.waitKey(0)
cv2.destroyAllWindows()