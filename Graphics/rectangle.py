# Daniel & Michael
# Rectangle 
# 2 April 2019

from graphics import *

# Create blank canvas at 720p
win = GraphWin("Rectangle Lesson", 1280, 720)

# Set corner points for rectangle
p1 = Point(100, 200)
p2 = Point(300, 600)

# Assigns variable "rectangle" to a rectangle from points (100, 200) to (300, 400) with a black 1p border and transparent
# This example is from top-left to bottom-right, but any two corners will work
rectangle = Rectangle(p1, p2)
rectangle.setFill('gold') # Just some colours
rectangle.draw(win)

# Shows the two corners of rectangle at top-left and bottom-right
# In this case they are equal to p1 and p2
print(rectangle.getP1())
print(rectangle.getP2())

# Get centre point of rectangle
middlerectangle = rectangle.getCenter()
print(middlerectangle)

# Shrinking rectangles!
list = ['green', 'red', 'pink', 'blue', 'orange', 'white', 'blueviolet']
for x in range(7):
    temporaryrectangle = Rectangle(middlerectangle, rectangle.getP2())
    temporaryrectangle.setFill(list[x])
    temporaryrectangle.setOutline(list[x])
    middlerectangle = temporaryrectangle.getCenter()
    temporaryrectangle.draw(win)