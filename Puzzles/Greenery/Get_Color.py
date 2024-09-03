import cv2 as cv # Import Opencv Library and alias as cv
def mouse_display(event,x,y,flags,param):
    if event==cv.EVENT_LBUTTONDBLCLK:  #Works only if the event is left mouse double click
        print("The BGR Values are:",image[x,y]) 
        print("The HSV Values are:",hsv[x,y])
image_path=r"D:\Journey\CV\Puzzles\Greenery\up.jpg" 
image=cv.imread(image_path)
hsv=cv.cvtColor(image,cv.COLOR_BGR2HSV)
cv.imshow("Original",image)
#cv.imshow("HSV",hsv)  #Use if we need to get color value when the image is represented in HSV Format
cv.setMouseCallback("Original",mouse_display)
#cv.setMouseCallback("HSV",mouse_display)   #Use if need to get color value for HSV Format
cv.waitKey(0)