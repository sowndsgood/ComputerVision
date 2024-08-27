from graphics import *
import math
import time

def main():
    win=GraphWin("Wagon Effect",500,500)
    circle=Circle(Point(250,250),200)
    circle.draw(win)

    no_of_times=2/3

    angle=no_of_times*360
    print(angle)
    dot=Circle(Point(250,50),5)
    
    dot.draw(win)
    text="The Wagon Wheel Effect for "+str(no_of_times)+"frames per second."
    display=Text(Point(250,25),text)
    display.draw(win)
    present_angle=0
    for i in range(100):
        present_angle+=angle
        dot.undraw()
        x=250+200*math.cos(math.radians(present_angle))
        y=250+200*math.sin(math.radians(present_angle))
        dot=Circle(Point(x,y),5)
        dot.setFill("green")
        dot.draw(win)
        time.sleep(1/3)
        
    win.getMouse()
    win.close()

main()

