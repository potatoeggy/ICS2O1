# Daniel Chen
# 7 April 2019
# Modify the above program that draws a vertical line that is 50 pixels long

from graphics import *

win = GraphWin('Line', 1280, 720)

line = Line(Point(15, 10), Point(15, 60))
line.setOutline('blue')
line.draw(win)