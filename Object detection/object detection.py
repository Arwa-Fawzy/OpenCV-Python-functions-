import numpy as np
import cv2

img=cv2.imread('Desktop/img.jpg',0)
template=cv2.imread('Desktop/img - Copy.jpg',0)
img2=img.copy()
#get the height and width of the template img
h, w=template.shape

#methods
methods=[cv2.TM_CCOEFF,cv2.TM_CCOEFF_NORMED,cv2.TM_CCORR,cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

for method in methods:
    img2=img.copy()
    #convlution in every single region in the base img to detect the match, **see the last lines
    result=cv2.matchTemplate(img2, template, method)
    min_val, max_val, min_loc, max_loc=cv2.minMaxLoc(result)
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF]:
        loc=min_loc
    else:
        loc=max_loc
    bottom_right=(loc[0]+w, loc[1]+h)
    cv2.rectangle(img2, loc,bottom_right, 255,5)
    cv2.imshow('match',img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()







# the matrix of the original image
# [[255,255,5],
#  [255,255,5],
#  [5,5,500],
#  [5,5,500]]

#the matrix of the template( object)
#[[255,255],
# [255,255]]

#template matching test is perfect at the highest values which is equal to 1
# so the result =
# [[1,1,0],
#  [1,1,0],
#  [0,0,0]] 