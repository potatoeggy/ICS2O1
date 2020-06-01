# Daniel Chen
# 7 April 2019
# Draw a heart

from graphics import *

x = 640
y = 480

win = GraphWin('Heart', x, y)

width = 100

circle = Circle(Point(x / 2 - width, y / 3), width + 15)
circle.setOutline('red')
circle.setFill('red')

circle2 = circle.clone()
circle2.move(circle.getCenter().getX(), 0)

rectangle = Rectangle(Point(x / 2 - 50, y / 2 - 50), Point(x / 2 + 50, y / 2 + 50))
rectangle.setOutline('red')
rectangle.setFill('red')

triangle = Polygon(Point(circle.getCenter().getX() - circle.getRadius() + 30, y / 2), Point(circle2.getCenter().getX() + circle2.getRadius() - 30, y / 2), Point(circle.getP2().getX(), y * 3 / 4))
triangle.setOutline('red')
triangle.setFill('red')

circle.draw(win)
circle2.draw(win)
triangle.draw(win)
rectangle.draw(win)