import math
from turtle import *


##Law of Cosine

def myTriangle():
    firstSide = int(input("Please give me the first side length: "))
    secondSide = int(input("Please give me the second side length: "))
    firstAngle = int(input("Please give me an angle: "))

    thirdSide = (pow(firstSide,2) + pow(secondSide,2)) - ((2)*(firstSide)*(secondSide)*(math.cos(math.radians(firstAngle))))
    thirdSide1 = pow(thirdSide,0.5)


    secondAngle = math.acos(((pow(secondSide,2)) - (pow(firstSide,2)) - (pow(thirdSide1,2)))/ ((-2)*(firstSide)*(thirdSide1)))
    secondAngle1 = math.degrees(secondAngle)

    thirdAngle = (180 - firstAngle - secondAngle1)

    ## TURTLE DRAWING ##
    jaslyn = Turtle ()
    jaslyn.goto (0,0)
    jaslyn.down ()
    jaslyn.forward(firstSide)
    jaslyn.left (180 - thirdAngle)
    jaslyn.forward(secondSide)
    jaslyn.left (180 - firstAngle1)
    jaslyn.forward (thirdSide1)



    print("First Angle: ")
    print(firstAngle)
    print("Second Angle: ")
    print(secondAngle1)
    print("Third Angle: ")
    print(thirdAngle)
    ###print(thirdSide1)

if __name__ == "__main__":

        myTriangle()
