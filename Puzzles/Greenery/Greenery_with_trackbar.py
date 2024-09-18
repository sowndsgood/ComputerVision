import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def nothing(x):
    pass

cv.namedWindow("Image",cv.WINDOW_NORMAL)
cv.resizeWindow("Image",600,600)

cv.createTrackbar("Saturation","Image",20,100,nothing)
cv.createTrackbar("Brightness","Image",1,5,nothing)

image=cv.imread(r"D:\Journey\CV\Puzzles\Greenery\up.jpg")
original_hsv=cv.cvtColor(image,cv.COLOR_BGR2HSV)

lower=np.array([30, 40, 40],dtype=np.uint8)
upper=np.array([90, 255, 255],dtype=np.uint8)

mask=cv.inRange(original_hsv,lower,upper)

#cv.imshow("Original Image",image)

while(True):
    hsv=original_hsv.copy()

    s=cv.getTrackbarPos("Saturation","Image")
    v=cv.getTrackbarPos("Brightness","Image")

    s=s/10

    hsv[mask>0,1]=np.clip(hsv[mask>0,1]*s,0,255)
    hsv[mask>0,2]=np.clip(hsv[mask>0,2]*v,0,255)

    enhanced_img=cv.cvtColor(hsv,cv.COLOR_HSV2BGR)

    combined_img=np.hstack((image,enhanced_img))
    cv.imshow("Image",combined_img)

    if cv.waitKey(1) & 0xFF==ord('q'):
        break

cv.destroyAllWindows()
