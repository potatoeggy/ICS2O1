# Daniel Chen
# 7 April 2019
# Draw a filled rectangle in the middle of your screen and put your name in the centre.

from graphics import *

x = 640
y = 480

win = GraphWin('Name + rectangle', x, y)

name = Text(Point(x / 2, y / 2), 'Daniel')
rectangle = Rectangle(Point(x / 3, y / 3), Point(x * 2 / 3, y * 2 / 3))
rectangle.setFill('pink')
rectangle.setOutline('pink')

rectangle.draw(win)
name.draw(win)