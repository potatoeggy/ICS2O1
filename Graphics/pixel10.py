# Daniel Chen
# 7 April 2019
# Draw a picture of a multicolour lollipop.

from graphics import *

x = 640
y = 480

win = GraphWin('Lollipop', x, y)

width = 20

stick = Rectangle(Point(x / 2 - width / 2, y / 2), Point(x / 2 + width / 2, y * 47 / 48))
stick.setFill('white')
stick.setWidth(2)
stick.draw(win)

for num in range(5):
    suckypart = Circle(Point(x / 2, y * 7 / 24), 125 - 25 * (num + 1))
    if num % 2 == 0:
        if num != 0:
            suckypart.setOutline('pink')
        else:
            suckypart.setWidth(2)
        suckypart.setFill('pink')
    else:
        suckypart.setOutline('white')
        suckypart.setFill('white')
    suckypart.draw(win)
    