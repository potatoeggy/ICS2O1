# Daniel Chen

import graphics # requires graphics.*

# use from graphics import * to ignore using graphics.*

win = graphics.GraphWin("Graphics Test", 640, 480)

# make dot
pt = graphics.Point(100, 50)
pt.draw(win)

# make line
pt1 = graphics.Point(220, 240)
pt2 = graphics.Point(420, 240)

# actually make line
line1 = graphics.Line(pt1, pt2)
line1.setOutline('red')
line1.setWidth(2)
line1.draw(win)

# make circle with centre at point 50, 50 with a radius of 50
circle1 = graphics.Circle(graphics.Point(50, 50), 50)
circle1.setFill('yellow')
circle1.setOutline('yellow')
circle1.draw(win)

circle2 = graphics.Circle(graphics.Point(500, 400), 25)
circle2.setOutline('white')
circle2.setFill('white')
circle2.draw(win)