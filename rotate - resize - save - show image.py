import cv2 
#to make the image has color, add -1 value, 0 is for gray scale, 1 for 
#imread returns the image array values (number of rows, number of columns, number of channels)
img=cv2.imread('./image.PNG',-1)
img=cv2.resize(img,(0,0), fx=7, fy=8)
img=cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
#save the image into storage device 
cv2.imwrite('new_img.png',img)
#showing the image 
cv2.imshow("img",img)
#delay value 
cv2.waitKey(0)
#closing all widows after ending the script 
cv2.destroyAllWindows() 
