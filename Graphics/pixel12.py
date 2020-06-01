# Daniel Chen
# 7 April 2019
# Draw a heart with input

from graphics import *

x = 640
y = 480

# Total width of heart is input; width here is a misnomer it's really radius but I didn't want to correct it
width = int(input('Width: ')) / 4
win = GraphWin('Heart', x, y)
win.setBackground('white')

circle = Circle(Point(x / 2 - width, y / 3), width)
circle.setFill('red')
circle.setOutline('red')

circle2 = circle.clone()
circle2.move(width * 2, 0)

# a little ugly but it'll do
tp1 = Point(circle.getCenter().getX() - width * 22 / 25 + 0.5, circle.getCenter().getY() + width / 2)
tp2 = Point(circle2.getCenter().getX() + width * 22 / 25 - 1, circle2.getCenter().getY() + width / 2)
tp3 = Point(x / 2, y / 3 + width * 3 + width / 16)
 
triangle = Polygon(tp1, tp2, tp3)
triangle.setOutline('red')
triangle.setFill('red')

rectangle = Rectangle(circle.getCenter(), Point(circle2.getCenter().getX(), circle2.getCenter().getY() + width))
rectangle.setOutline('red')
rectangle.setFill('red')

circle.draw(win)
circle2.draw(win)
triangle.draw(win)
rectangle.draw(win)