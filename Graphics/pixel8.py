# Daniel Chen
# 7 April 2019
# Draw a filled circle inside an outline of a rectangle.

from graphics import *

x = 640
y = 480

win = GraphWin('Circle + rectangle', x, y)
win.setBackground('white')
rectangle = Rectangle(Point(x / 3, y / 3), Point(x * 2 / 3, y * 2 / 3))
circle = Circle(Point(x / 2, y / 2), (y * 2 / 3 - y / 3) / 2 - 2)
circle.setFill('pink')
circle.setOutline('pink')

circle.draw(win)
rectangle.draw(win)