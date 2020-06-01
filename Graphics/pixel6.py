# Daniel Chen
# 7 April 2019
# Draw house thing

from graphics import *

x = 640
y = 480
win = GraphWin('triangle', x, y)

triangle = Polygon(Point(x / 2, y / 8), Point(x / 5, y / 3), Point(x * 4 / 5, y / 3))
rectangle = Rectangle(Point(x / 5, y * 9 / 24), Point(x * 4 / 5, y * 3 / 5))
triangle.draw(win)
rectangle.draw(win)