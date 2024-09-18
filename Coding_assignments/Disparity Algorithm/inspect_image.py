import argparse
import cv2 as cv # Import Opencv Library and alias as cv

image = None

def mouse_display(event,x,y,flags,param):
    if event==cv.EVENT_LBUTTONDOWN:  #Works only if the event is left mouse double click
        print("Disparity:",image[y, x]) 

def main():
    parser = argparse.ArgumentParser(description='Tool to inspect images')      
    parser.add_argument('--image', type=str, help='Input image', required=True)  
    args = parser.parse_args()

    image_path=args.image
    global image
    image=cv.imread(image_path, 0)
    cv.imshow("Original",image)
    cv.setMouseCallback("Original",mouse_display)
    cv.waitKey(0)

if __name__ == '__main__':
    main()
