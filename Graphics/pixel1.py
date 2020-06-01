# Daniel Chen
# 7 April 2019
# Draw a horizontal line that is 100 pixels long starting at the point     (15, 10).  Use colour blue

from graphics import *

win = GraphWin('Line', 1280, 720)

line = Line(Point(15, 10), Point(115, 10))
line.setOutline('blue')
line.draw(win)