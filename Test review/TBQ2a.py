# Daniel Chen
# 21 May 2019
# Landscape with kite

# import everything
from graphics import *

# create canvas
x = 500
y = 400
win = GraphWin('Landscape', x, y)
win.setBackground('sky blue')

# hill
hill = Oval(Point(0, y + y / 3), Point(x, y * 2 / 3))
hill.setOutline('green')
hill.setFill('green')

# clouds
def cloudcreator(bigcentrex, bigcentrey):
    bigcentre = Point(bigcentrex, bigcentrey)
    bigcloud = Oval(Point(bigcentrex - 30, bigcentrey - 20), Point(bigcentrex + 20, bigcentrey + 20))
    smallcloud = Oval(Point(bigcentrex - 42, bigcentrey - 12), Point(bigcentrex, bigcentrey + 12))
    cloudlist = [bigcloud, smallcloud]
    for i in cloudlist:
        i.setFill('white')
        i.setOutline('white')
    return cloudlist

cloud1 = cloudcreator(x * 3 / 8, y * 1 / 7)
cloud2 = cloudcreator(x * 1 / 5, y * 1 / 8)
cloud3 = cloudcreator(x * 1 / 7, y * 1 / 3)

cloudlist = cloud1 + cloud2 + cloud3

# kite
kitecentre = Point(x * 3 / 4, y * 6 / 7)

kitestring = Line(kitecentre, Point(x, y))
kitestring.setOutline('red')
kitestring.setWidth(2)

kite1 = Point(kitecentre.getX() - 60, kitecentre.getY())
kite2 = Point(kitecentre.getX() + 60, kitecentre.getY())
kite3 = Point(kitecentre.getX(), kitecentre.getY() - 30)
kite4 = Point(kitecentre.getX(), kitecentre.getY() + 30)
kite = Polygon(kite1, kite2, kite3, kite4)
kite.setFill('orange')
kite.setOutline('orange')

kitelist = [kitestring, kite]

for i in [hill] + cloudlist + kitelist:
    i.draw(win)