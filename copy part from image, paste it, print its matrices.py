from random import random
import cv2 
import random 

img=cv2.imread('./img.jpg',-1)

#print(img) >> matrcis 
#print (type(img)) >> numpy array
#print(img.shape) >> (height, width, channels"color space" like RGB which is 3)
tag=img[500:700,600:900] #copy part from the image
img[100:300, 650:950]=tag  #paste it


cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()