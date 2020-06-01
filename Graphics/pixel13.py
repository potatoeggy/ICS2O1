# Daniel Chen
# 7 April 2019
# Draw a cylinder and decorate the label with words (e.g. ICS2O Cola).

from graphics import *

x = 640
y = 480

# Scalable except text
win = GraphWin('Cylinder', x, y)
win.setBackground('white')

# Top
oval = Oval(Point(x / 3, y / 7), Point(x * 2 / 3, y / 4))
oval.setWidth('10')
oval.setOutline('gray')
oval.setFill('silver')

# Body
rectangle = Rectangle(Point(x / 3, (y / 7 + y / 4) / 2), Point(x * 2 / 3, y * 7 / 8))
rectangle.setWidth('9')
rectangle.setOutline('silver')
rectangle.setFill('red2')

# Bottom
oval2 = oval.clone()
oval2.setWidth('10')
oval2.setOutline('silver')
oval2.setFill('red2')
oval2.move(0, y * 7 / 8 - (y / 7 + y / 4) / 2 + 5)

# Get rid of ugly line at oval2
line = Line(Point(x / 3 + 5, y * 7 / 8), Point(x * 2 / 3 - 4, y * 7 / 8))
line.setWidth('9')
line.setFill('red2')

# Text
text = Text(Point(x / 2, y / 2), 'Not Cola')
text.setSize(24)
text.setTextColor('white')
text.setStyle('bold italic')
text.setFace('helvetica')

# Draw
oval2.draw(win)
rectangle.draw(win)
oval.draw(win)
line.draw(win)
text.draw(win)