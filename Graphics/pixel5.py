# Daniel Chen
# 7 April 2019
# Modify the above program so that the rectangle is filled in with a different colour than the border.

from graphics import *

rectangle = Rectangle(Point(100, 200), Point(200, 340))
rectangle.setFill('red')
rectangle.draw(GraphWin('Rectangle', 640, 480))