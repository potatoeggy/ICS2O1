# Daniel Chen
# 7 April 2019
# Draw face in centre

from graphics import *

win = GraphWin('Face', 640, 480)

p1 = Point(270, 190)
p2 = Point(370, 190)

line = Line(Point(280, 290), Point(360, 290))
rectangle = Rectangle(Point(220, 140), Point(420, 340))

p1.draw(win)
p2.draw(win)
line.draw(win)
rectangle.draw(win)