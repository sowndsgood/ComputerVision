import cv2 as cv
import numpy as np
image_path_1=r"D:\Journey\CV\Puzzles\Greenery\up.jpg"
image_path_2=r"D:\Journey\CV\Puzzles\Greenery\down.jpg"
image=cv.imread(image_path_2)
hsv=cv.cvtColor(image,cv.COLOR_BGR2HSV)
'''For Up image'''
brown_lower = np.array([0, 0, 30],dtype=np.uint8)
brown_upper = np.array([255, 255, 200],dtype=np.uint8)
'''
brown_lower = np.array([ 0 , 0 ,81],dtype=np.uint8)
brown_upper = np.array([136,37,103],dtype=np.uint8)
'''
mask=cv.inRange(hsv,brown_lower,brown_upper)
hsv[mask>0,1]=np.clip(hsv[mask>0,1]*2.1,0,255)
hsv[mask>0,2]=np.clip(hsv[mask>0,2]*1.7,0,255)
enhanced=cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
combined=np.hstack([image,enhanced])
cv.imwrite("Combined_Image_Trunk_HSV.jpg",combined)