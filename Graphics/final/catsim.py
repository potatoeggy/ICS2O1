# Daniel Chen + Mehra Shariati
# 30 May 2019
# Journey of Cat - An animated storybook about a cat's journey for acceptance

# import all external libraries
from graphics import *
from math import sin
from random import randint
from playsound import playsound # must install via pip or some other way first
import time
from threading import Thread

# setup canvas
x = 640
y = 480
win = GraphWin('Journey of Cat', x, y, autoflush = False)

radius = 10
miniradius = radius
# Initial defining of everything
# Cat
# Pop Tart
# Background

def setcat():
    global catlist
    global rainbowlist
    global starlist
    global taillist2, taillist
    global squintlist, eyelist
    global ptbgcircle1, ptbgcircle3, ptbgcircle4, tailtip
    global externalmovelist
    global mouthsmilecover, mouth, mouthtip, nose
    # Rounded edges
    ptbgcircle1 = Circle(Point(x / 2 - radius * 8, y / 2), radius)
    ptbgcircle1.setWidth(6)
    ptbgcircle1.setFill(color_rgb(234,209,134))

    ptbgcircle2 = ptbgcircle1.clone()
    ptbgcircle2.move(radius * 15, 0)

    ptbgcircle3 = ptbgcircle1.clone()
    ptbgcircle3.move(0, radius * 11)

    ptbgcircle4 = ptbgcircle2.clone()
    ptbgcircle4.move(0, radius * 11)

    # Cover up ugly circle holes
    ptbgcover1 = Point(ptbgcircle1.getCenter().getX(), ptbgcircle1.getCenter().getY() - radius)
    ptbgcover2 = Point(ptbgcircle2.getCenter().getX(), ptbgcircle2.getCenter().getY() - radius)
    ptbgcover3 = Point(ptbgcircle1.getCenter().getX() - radius, ptbgcircle1.getCenter().getY())
    ptbgcover4 = Point(ptbgcircle2.getCenter().getX() + radius, ptbgcircle2.getCenter().getY())
    ptbgcover5 = Point(ptbgcircle3.getCenter().getX() - radius, ptbgcircle3.getCenter().getY())
    ptbgcover6 = Point(ptbgcircle4.getCenter().getX() + radius, ptbgcircle4.getCenter().getY())
    ptbgcover7 = Point(ptbgcircle3.getCenter().getX(), ptbgcircle3.getCenter().getY() + radius)
    ptbgcover8 = Point(ptbgcircle4.getCenter().getX(), ptbgcircle4.getCenter().getY() + radius)

    # Cover up gap in circle
    ptbgcover = Polygon(ptbgcover1, ptbgcover2, ptbgcover4, ptbgcover6, ptbgcover8, ptbgcover7, ptbgcover5, ptbgcover3)
    ptbgcover.setWidth(6)
    ptbgcover.setFill(color_rgb(234, 209, 134))

    # Cover up ugly octogon lines
    ptbgcovercircle1 = Circle(ptbgcircle1.getCenter(), radius - 3)
    ptbgcovercircle1.setWidth(0)
    ptbgcovercircle1.setFill(color_rgb(234, 209, 134))

    ptbgcovercircle2 = ptbgcovercircle1.clone()
    ptbgcovercircle2.move(radius * 15, 0)

    ptbgcovercircle3 = ptbgcovercircle1.clone()
    ptbgcovercircle3.move(0, radius * 11)

    ptbgcovercircle4 = ptbgcovercircle1.clone()
    ptbgcovercircle4.move(radius * 15, radius * 11)

    ptbglist = [ptbgcircle1, ptbgcircle2, ptbgcircle3, ptbgcircle4, ptbgcover, ptbgcovercircle1, ptbgcovercircle2, ptbgcovercircle3, ptbgcovercircle4]

    # Rounded interior edges
    ptcircle1 = Circle(Point(ptbgcovercircle1.getCenter().getX() + radius, ptbgcovercircle1.getCenter().getY() + radius), miniradius)
    ptcircle1.setWidth(0)
    ptcircle1.setFill(color_rgb(254,119,255))

    # found by (total_width) - (radius_of_ptcircle * 2)
    ptcircle2 = ptcircle1.clone()
    ptcircle2.move(radius * (15 - 2), 0)

    ptcircle3 = ptcircle1.clone()
    ptcircle3.move(0, radius * (11 - 2))

    ptcircle4 = ptcircle2.clone()
    ptcircle4.move(0, radius * (11 - 2))

    # Cover up gap in circle
    ptcover1 = Point(ptcircle1.getCenter().getX(), ptcircle1.getCenter().getY() - miniradius)
    ptcover2 = Point(ptcircle2.getCenter().getX(), ptcircle2.getCenter().getY() - miniradius)
    ptcover3 = Point(ptcircle1.getCenter().getX() - miniradius, ptcircle1.getCenter().getY())
    ptcover4 = Point(ptcircle2.getCenter().getX() + miniradius, ptcircle2.getCenter().getY())
    ptcover5 = Point(ptcircle3.getCenter().getX() - miniradius, ptcircle3.getCenter().getY())
    ptcover6 = Point(ptcircle4.getCenter().getX() + miniradius, ptcircle4.getCenter().getY())
    ptcover7 = Point(ptcircle3.getCenter().getX(), ptcircle3.getCenter().getY() + miniradius)
    ptcover8 = Point(ptcircle4.getCenter().getX(), ptcircle4.getCenter().getY() + miniradius)

    ptcover = Polygon(ptcover1, ptcover2, ptcover4, ptcover6, ptcover8, ptcover7, ptcover5, ptcover3)
    ptcover.setOutline(color_rgb(254, 119, 255))
    ptcover.setFill(color_rgb(254, 119, 255))

    ptlist = [ptcircle1, ptcircle2, ptcircle3, ptcircle4, ptcover]

    # Sprinkles
    ptsprinkle1 = Circle(Point(ptcircle1.getCenter().getX() + radius * 3 / 2, ptcircle1.getCenter().getY() + radius), miniradius / 2)
    ptsprinkle1.setOutline(color_rgb(255, 23, 192))
    ptsprinkle1.setFill(color_rgb(255, 23, 192))

    ptsprinkle2 = ptsprinkle1.clone()
    ptsprinkle2.move(radius * 4.2, -radius * 2 / 3)

    ptsprinkle3 = ptsprinkle2.clone()
    ptsprinkle3.move(radius * 3, 0)

    ptsprinkle4 = ptsprinkle3.clone()
    ptsprinkle4.move(radius * 3, radius * 2)

    ptsprinkle5 = ptsprinkle1.clone()
    ptsprinkle5.move(radius * 3.5, radius * 2.5)

    ptsprinkle6 = ptsprinkle1.clone()
    ptsprinkle6.move(radius, radius * 4)

    ptsprinkle7 = ptsprinkle6.clone()
    ptsprinkle7.move(radius * 4, radius * 3 / 4)

    ptsprinkle8 = ptsprinkle6.clone()
    ptsprinkle8.move(-radius * 2, radius * 2)

    ptsprinkle9 = ptsprinkle8.clone()
    ptsprinkle9.move(radius * 2, radius * 2)

    ptsprinkle10 = ptsprinkle9.clone()
    ptsprinkle10.move(radius * 2, -radius)

    ptsprinklelist = [ptsprinkle1, ptsprinkle2, ptsprinkle3, ptsprinkle4, ptsprinkle5, ptsprinkle6, ptsprinkle7, ptsprinkle8, ptsprinkle9, ptsprinkle10]

    # Ears
    # Ear tip
    ears1 = Point(ptsprinkle4.getCenter().getX() - radius * 2, ptsprinkle4.getCenter().getY())
    # Other ear tip
    ears3 = Point(ptsprinkle4.getCenter().getX() + radius * 4, ptsprinkle4.getCenter().getY())
    # Under and to the right of first ear tip
    ears2 = Point(ears1.getX() + (ears3.getX() - ears1.getX()) * 1 / 3, ptsprinkle5.getCenter().getY() + radius)
    # Under and to the left of second ear tip
    ears4 = Point(ears1.getX() + (ears3.getX() - ears1.getX()) * 2 / 3, ptsprinkle5.getCenter().getY() + radius)
    # Under second ear tip
    ears5 = Point(ears3.getX() + radius, ears2.getY() + radius / 2)
    # Under first ear tip
    ears6 = Point(ears1.getX() - radius, ears2.getY() + radius / 2)
    # Bonus second ear tip
    ears7 = Point(ears3.getX() + miniradius, ears3.getY())
    # Bonus first ear tip
    ears8 = Point(ears1.getX() - miniradius, ears1.getY())
    ears = Polygon(ears8, ears1, ears2, ears4, ears3, ears7, ears5, ears6)
    ears.setFill(color_rgb(166, 166, 166))
    ears.setWidth(6)

    # Face
    #   _____   x1 rectangle, x1 rectangle cover, x2 circle/oval
    # (|)___(|)
    leftface1 = Point(ears6.getX() - (ears1.getX() - ears8.getX()) - 6, ears6.getY() - 3)
    leftface2 = Point((ears6.getX() + ears5.getX()) / 2, ptbgcover8.getY() - 3)
    leftface = Oval(leftface1, leftface2)
    leftface.setWidth(6)
    leftface.setFill(color_rgb(166, 166, 166))

    rightface = leftface.clone()
    rightface.move(leftface2.getX() - leftface1.getX() + 3, 0)

    facecover1 = Point((leftface1.getX() + leftface2.getX()) / 2, leftface1.getY() + 3)
    facecover2 = Point((rightface.getP1().getX() + rightface.getP2().getX()) / 2, leftface2.getY())
    facecover = Rectangle(facecover1, facecover2)
    facecover.setFill(color_rgb(166, 166, 166))
    facecover.setWidth(6)

    facecovercover1 = Point(ears6.getX() + 3, ears6.getY() - 5)
    facecovercover2 = Point(ears7.getX() - 3, facecover2.getY() - 3)
    facecovercover = Rectangle(facecovercover1, facecovercover2)
    facecovercover.setFill(color_rgb(166, 166, 166))
    facecovercover.setWidth(0)

    headlist = [ears, leftface, rightface, facecover, facecovercover]

    # Features
    eye1 = Circle(Point(ears2.getX() - radius, leftface.getCenter().getY() - radius), radius * 9 / 10)
    eye1.setFill('black')
    eye1dot = Circle(Point(eye1.getCenter().getX() - radius / 2, eye1.getCenter().getY() - radius / 2), radius / 2 * (7 / 10))
    eye1dot.setFill('white')
    eye1dot.setOutline('white')

    eye2 = Circle(Point(ears4.getX() + radius * 2, leftface.getCenter().getY() - radius), radius * 9 / 10)
    eye2.setFill('black')
    eye2dot = Circle(Point(eye2.getCenter().getX() - radius / 2, eye2.getCenter().getY() - radius / 2), radius / 2 * (7 / 10))
    eye2dot.setFill('white')
    eye2dot.setOutline('white')

    eyelist = [eye1, eye1dot, eye2, eye2dot]

    squintleft1 = Line(Point(eye1.getCenter().getX() + radius * 9 / 10, eye1.getCenter().getY()), eye1.getP1())
    squintleft1.setWidth(4)

    squintleft2 = Line(squintleft1.getP1(), Point(squintleft1.getP2().getX(), squintleft1.getP2().getY() + radius * 18 / 10))
    squintleft2.setWidth(4)

    squintright1 = Line(Point(eye2.getCenter().getX() - radius * 9 / 10, eye2.getCenter().getY()), Point(eye2.getP2().getX(), eye2.getP1().getY()))
    squintright1.setWidth(4)

    squintright2 = Line(squintright1.getP1(), Point(squintright1.getP2().getX(), squintleft1.getP2().getY() + radius * 18 / 10))
    squintright2.setWidth(4)

    squintlist = [squintleft1, squintleft2, squintright1, squintright2]

    nose = Circle(Point((eye1.getCenter().getX() + eye2.getCenter().getX()) / 2 - 3 + radius / 2, eye2.getCenter().getY() + radius), 4)
    nose.setFill('black')

    cheek1 = eye1.clone()
    cheek1.setFill('pink')
    cheek1.setWidth(0)
    cheek1.move(-radius * 2, radius * 1.8)

    cheek2 = eye2.clone()
    cheek2.setFill('pink')
    cheek2.setWidth(0)
    cheek2.move(radius * 1, radius * 2)

    mouth1 = Point((ears6.getX() + ears5.getX()) / 2, nose.getCenter().getY() + radius)
    mouth2 = Point(mouth1.getX(), mouth1.getY() + radius)
    mouth = Line(mouth1, mouth2)
    mouth.setWidth(6)

    mouthtip = Circle(mouth1, 2)
    mouthtip.setFill('black')
    mouthtip.setWidth(2)

    mouthsmile1 = Point(cheek1.getCenter().getX() + radius * 1.75, cheek1.getCenter().getY() - radius)
    mouthsmile2 = Point(cheek2.getCenter().getX() - radius * 1.75, mouth2.getY())
    mouthsmile = Oval(mouthsmile1, mouthsmile2)
    mouthsmile.setWidth(6)

    mouthsmilecover1 = Point(mouthsmile.getP1().getX() - 2, mouthsmile.getP1().getY())
    mouthsmilecover2 = Point(mouthsmile.getP2().getX() + 2, (mouthsmile.getP1().getY() + mouthsmile.getP2().getY()) / 2)
    mouthsmilecover = Rectangle(mouthsmilecover1, mouthsmilecover2)
    mouthsmilecover.setWidth(4)
    mouthsmilecover.setOutline(color_rgb(166, 166, 166))
    mouthsmilecover.setFill(color_rgb(166, 166, 166))

    mouthlist = [mouthsmile, mouthsmilecover, mouth, mouthtip]
    eyelist = [eye1, eye1dot, eye2, eye2dot]
    otherfeatureslist = [nose, cheek1, cheek2]

    # Legs
    leg1 = Circle(Point(ptbgcircle3.getCenter().getX() - radius * 1.5, ptbgcircle3.getCenter().getY() + radius * 1.8), radius * 1.2)
    leg1.move(20, 0)
    leg1.setFill(color_rgb(166, 166, 166))
    leg1.setWidth(6)

    leg2 = leg1.clone()
    leg2.move(40, 0)

    leg3 = leg2.clone()
    leg3.move(60, 0)

    leg4 = leg3.clone()
    leg4.move(40, 0)

    leglist = [leg1, leg2, leg3, leg4]

    # Tail, must recalculate for every flick usually
    tailtip = (Circle(Point(ptbgcircle1.getCenter().getX() - 50, (ptbgcircle1.getCenter().getY() + ptbgcircle3.getCenter().getY()) / 2 + radius * 3), radius))
    tailtip.setWidth(6)
    tailtip.setFill(color_rgb(166, 166, 166))
    tailback3 = Point(ptbgcircle1.getCenter().getX(), tailtip.getCenter().getY() + radius)
    tailback4 = Point(ptbgcircle1.getCenter().getX(), tailtip.getCenter().getY() - radius)
    tailback1 = Point(tailtip.getCenter().getX(), tailtip.getCenter().getY() + radius)
    tailback2 = Point(tailtip.getCenter().getX(), tailtip.getCenter().getY() - radius)
    tailback = Polygon(tailback1, tailback2, tailback4, tailback3)
    tailback.setFill(color_rgb(166, 166, 166))
    tailback.setWidth(6)
    tailbackcover = Line(Point(tailback1.getX(), tailback1.getY() - 3), Point(tailback2.getX(), tailback2.getY() + 3))
    tailbackcover.setOutline(color_rgb(166, 166, 166))
    tailbackcover.setWidth(6)
    taillist = [tailtip, tailback, tailbackcover]

    tailtip2 = tailtip.clone()
    tailtip2.move(0, -20)
    tailbackcover2 = tailbackcover.clone()
    tailbackcover2.move(0, -20)
    tailback_3 = Point(ptbgcircle1.getCenter().getX(), tailtip.getCenter().getY() + radius)
    tailback_4 = Point(ptbgcircle1.getCenter().getX(), tailtip.getCenter().getY() - radius)
    tailback_1 = Point(tailtip2.getCenter().getX(), tailtip2.getCenter().getY() + radius)
    tailback_2 = Point(tailtip2.getCenter().getX(), tailtip2.getCenter().getY() - radius)
    tailback_second = Polygon(tailback_1, tailback_2, tailback_4, tailback_3)
    tailback_second.setFill(color_rgb(166, 166, 166))
    tailback_second.setWidth(6)
    taillist2 = [tailtip2, tailback_second, tailbackcover2]

    # Rainbow
    amp = 3 # lower is less of a wave
    freq = 15 # higher is less waves
    offsetx = -10 # moves it left or right the canvas
    offsety = -10 # moves it up or down the canvas

    temp = []
    lowertemp = []

    for a in range(640): # range is the x value you want it to go to
        equation = y / 2 + (amp * sin((a - offsetx) / freq) + offsety) # Equation retrieved from Stack Overflow
        temp.append(Point(a - 400, equation))
        lowertemp.append(Point(a - 400, equation + 20))
    redwave = Polygon(temp + list(reversed(lowertemp)))
    redwave.setFill('red')
    redwave.setOutline('red')

    orangewave = redwave.clone()
    orangewave.move(0, 20)
    orangewave.setOutline('orange')
    orangewave.setFill('orange')

    yellowwave = orangewave.clone()
    yellowwave.move(0, 20)
    yellowwave.setOutline('yellow')
    yellowwave.setFill('yellow')

    greenwave = yellowwave.clone()
    greenwave.move(0, 20)
    greenwave.setOutline('lime')
    greenwave.setFill('lime')

    bluewave = greenwave.clone()
    bluewave.move(0, 20)
    bluewave.setOutline('royal blue')
    bluewave.setFill('royal blue')

    purplewave = bluewave.clone()
    purplewave.move(0, 20)
    purplewave.setOutline('blueviolet')
    purplewave.setFill('blueviolet')

    rainbowlist = [redwave, orangewave, yellowwave, greenwave, bluewave, purplewave]

    star1 = starcreator(Point(x / 5, y * 7 / 8), radius * 2)
    star2 = starcreator(Point(x * 6 / 7, y * 9 / 10), radius * 3)
    star3 = starcreator(Point(x * 9 / 10, y / 4), radius * 2.5)
    star4 = starcreator(Point(x * 1 / 16, y / 8), radius * 2)
    star5 = starcreator(Point(x * 2 / 3, y / 5), radius * 2.5)
    starlist = [star1, star2, star3, star4, star5]

    catlist = taillist + leglist + ptbglist + ptlist + ptsprinklelist + headlist + mouthlist + eyelist + otherfeatureslist
    externalmovelist = leglist + headlist + mouthlist + eyelist + otherfeatureslist

# Press any key to continue
paktc = Text(Point(x * 25 / 32, y * 31 / 32), 'Press any key to continue...')
paktc.setFill('white')
paktc.setSize(12)
paktc.setStyle('italic')
paktc.setFace('courier')

# Esc to pause
esctp = Text(Point(x / 2, y * 31 / 32), 'Press Escape at any time to pause')
esctp.setFill('white')
esctp.setSize(12)
esctp.setStyle('bold')
esctp.setFace('courier')

# Exploration reward
expget = Text(Point(x / 7, y * 31 / 32), 'Exploration +1!')
expget.setStyle('bold')
expget.setFill('white')
expget.setFace('courier')
expget.setSize(14)

# Stars
def starcreator(centre, size): # centre should be a point, size is basically radius
    p1 = Point(centre.getX(), centre.getY() - size)
    p2 = Point(centre.getX() + size / 3, centre.getY() - size / 3)
    p3 = Point(centre.getX() + size, centre.getY())
    p4 = Point(centre.getX() + size / 2, centre.getY() + size / 3)
    p5 = Point(centre.getX() + size * 2 / 3, centre.getY() + size)
    p6 = Point(centre.getX(), centre.getY() + size * 2 / 3)
    p7 = Point(centre.getX() - size * 2 / 3, centre.getY() + size)
    p8 = Point(centre.getX() - size / 2, centre.getY() + size / 3)
    p9 = Point(centre.getX() - size, centre.getY())
    p10 = Point(centre.getX() - size / 3, centre.getY() - size / 3)
    star = Polygon(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10)
    star.setWidth(6)
    star.setFill('yellow')
    return star

def catflip(centre): # flips cat along vertical axis
    temp = 0
    # Because of the large variety of shapes in the cat (Rectangle, Circle, Oval, various Polygons) we cycle through all of them
    for i in catlist:
        try:
            temp = centre - i.getCenter().getX()
        except:
            try:
                temp = centre - (i.getP1().getX() + i.getP2().getX()) / 2
            except:
                try:
                    if abs(centre - i.getPoints()[0].getX()) == 22 or abs(centre - i.getPoints()[0].getX()) == 102:
                        temp = centre - (i.getPoints()[0].getX() + i.getPoints()[5].getX()) / 2
                    else:
                        temp = centre - (i.getPoints()[0].getX() + i.getPoints()[4].getX()) / 2
                except:
                    try:
                        temp = centre - (i.getPoints()[0].getX() + i.getPoints()[3].getX()) / 2
                    except:
                        pass
        temp *= 2
        i.move(temp, 0)
    return catlist

def pause(): # pause menu
    # pause overlay to hide everything
    pauser = Rectangle(Point(0, 0), Point(x, y))
    pauser.setFill('gray')
    pauser.setOutline('gray')

    # "Paused"
    pausetext = Text(Point(x / 2, y / 4), 'Paused')
    pausetext.setFill('white')
    pausetext.setStyle('bold')
    pausetext.setSize(32)

    # "Continue", "Restart", "Exit" buttons and text
    continuebutton = Rectangle(Point(x / 3, y * 7 / 16), Point(x * 2 / 3, y * 9 / 16))
    continuebutton.setFill('green')
    continuebutton.setOutline('green')

    continuetext = Text(Point(x / 2, (continuebutton.getP1().getY() + continuebutton.getP2().getY()) / 2), 'Continue')
    continuetext.setFill('white')
    continuetext.setSize(14)
    continuetext.setStyle('bold')

    restartbutton = Rectangle(Point(x / 3, y * 10 / 16), Point(x * 2 / 3, y * 12 / 16))
    restartbutton.setFill('orange')
    restartbutton.setOutline('orange')

    restartscenebutton = Rectangle(Point(x * 1 / 12, y * 10 / 16), Point(x * 5 / 12, y * 12 / 16))
    restartscenebutton.setFill('orange')
    restartscenebutton.setOutline('orange')

    restarttext = Text(Point(x / 2, (restartbutton.getP1().getY() + restartbutton.getP2().getY()) / 2), 'Restart')
    restarttext.setFill('white')
    restarttext.setSize(14)
    restarttext.setStyle('bold')

    restartscenetext = Text(Point(x / 4, (restartscenebutton.getP1().getY() + restartbutton.getP2().getY()) / 2), 'Restart Scene')
    restartscenetext.setFill('white')
    restartscenetext.setSize(14)
    restartscenetext.setStyle('bold')

    exitbutton = Rectangle(Point(x / 3, y * 13 / 16), Point(x * 2 / 3, y * 15 / 16))
    exitbutton.setFill('red')
    exitbutton.setOutline('red')

    exittext = Text(Point(x / 2, (exitbutton.getP1().getY() + exitbutton.getP2().getY()) / 2), 'Exit')
    exittext.setFill('white')
    exittext.setSize(14)
    exittext.setStyle('bold')

    # Displays Exploration Points *after* they have finished the scene
    explabel = Text(Point(x / 32, y * 15 / 16), 'EXP')
    explabel.setSize(14)
    exptext = Text(Point(x / 64, y * 63 / 64), str(exp))
    exptext.setSize(12)
    for i in explabel, exptext:
        i.setStyle('bold')
        i.setFill('white')

    # easier draw
    everything = [pauser, pausetext, continuebutton, continuetext, restartbutton, restarttext, exitbutton, exittext, explabel, exptext]
    for i in everything:
        i.draw(win)
    update()

    restart = 0

    # loop until user does something
    while True:
        mouse = win.getMouse()
        # used to increase performance if user dumb and click randomly
        if mouse is not None:
            # if mouse click is in bounding box
            if continuebutton.getP1().getX() <= mouse.getX() <= continuebutton.getP2().getX() and continuebutton.getP1().getY() <= mouse.getY() <= continuebutton.getP2().getY():
                # undraw pause elements and exit pause function, telling other function to continue
                for i in everything:
                    i.undraw()
                if restart == 2:
                        for i in restartscenebutton, restartscenetext:
                            i.undraw()
                update()
                return 0
            elif restartbutton.getP1().getY() <= mouse.getY() <= restartbutton.getP2().getY():
                if restartbutton.getP1().getX() <= mouse.getX() <= restartbutton.getP2().getX():
                    # undraw pause elements and exit pause function, telling other function to restart
                    if restarttext.getText() == 'Restart':
                        restarttext.setText('Restart from beginning')
                        restartbutton.move(x * 3 / 12, 0)
                        restarttext.move(x * 3 / 12, 0)
                        for i in [restartscenebutton, restartscenetext]:
                            i.draw(win)
                        restart = 2
                        update()
                    else:
                        try:
                            for i in everything + [restartscenebutton, restartscenetext]:
                                i.undraw()
                        except:
                            pass
                        update()
                        return 1
                elif restart == 2:
                    if restartscenebutton.getP1().getX() <= mouse.getX() <= restartscenebutton.getP2().getX() and restartscenebutton.getP1().getY() <= mouse.getY() <= restartscenebutton.getP2().getY():
                        for i in everything + [restartscenebutton, restartscenetext]:
                            i.undraw()
                        update()
                        return 3
                    # if first time clicked verify with user, otherwise kill thing
            elif exitbutton.getP1().getX() <= mouse.getX() <= exitbutton.getP2().getX() and exitbutton.getP1().getY() <= mouse.getY() <= exitbutton.getP2().getY():
                if exittext.getText() == 'Exit':
                    exittext.setText('Click again to exit')
                else:
                    exit()


def cover(): # function for scene 0 (cover)
    # workaround for Mehra's incompatible code *even* though this should work because Python dumb and stupid global variables no global
    x = 640
    y = 480
    # title
    title = Text(Point(x / 2, y / 4), 'Journey of Cat')
    title.setFace('helvetica')
    title.setStyle('bold')
    title.setSize(32)
    title.setFill('white')

    # button to start
    startbutton1 = Point(x / 3, y * 7 / 8)
    startbutton2 = Point(x * 2 / 3, y)
    startbutton = Rectangle(startbutton1, startbutton2)
    startbutton.setFill('green')
    startbutton.setWidth(10)

    starttext = Text(Point(x / 2, (startbutton1.getY() + startbutton2.getY()) / 2), 'START')
    starttext.setFill('white')
    starttext.setSize(18)
    starttext.setStyle('bold')

    #The right side:
    #moon
    x = 640
    y = 0
    r = 150

    moon_base = Circle (Point(x, y), r)
    moon_base.setFill('lightgrey')
    moon_base.setOutline('lightgrey')

    moon_spot1 = Circle (Point(x-40, y+50), r/7.5)
    moon_spot1.setFill('grey')
    moon_spot1.setOutline('grey')

    moon_spot2 = Circle (Point(x-100, y+10), r/10)
    moon_spot2.setFill('grey')
    moon_spot2.setOutline('grey')

    moon_spot3 = Circle (Point(x-80, y+110), r/17)
    moon_spot3.setFill('grey')
    moon_spot3.setOutline('grey')

    moon_spot4 = Circle (Point(x, y+120), r/6)
    moon_spot4.setFill('grey')
    moon_spot4.setOutline('grey')

    moon = [moon_base, moon_spot1, moon_spot2, moon_spot3, moon_spot4]

    #rainbow
    p1_x = 714
    p1_y = 0
    p2_x = 156
    p2_y = 480
    w = 25

    red_stripe = Line (Point(p1_x, p1_y),Point(p2_x, p2_y))
    red_stripe.setWidth(w)
    red_stripe.setOutline('red')

    orange_stripe = Line (Point(p1_x +25, p1_y),Point(p2_x+25, p2_y))
    orange_stripe.setWidth(w)
    orange_stripe.setOutline('orange')

    yellow_stripe = Line (Point(p1_x +50, p1_y),Point(p2_x+50, p2_y))
    yellow_stripe.setWidth(w)
    yellow_stripe.setOutline('yellow')

    green_stripe = Line (Point(p1_x +75, p1_y),Point(p2_x+75, p2_y))
    green_stripe.setWidth(w)
    green_stripe.setOutline('lightgreen')

    blue_stripe = Line (Point(p1_x +100, p1_y),Point(p2_x+100, p2_y))
    blue_stripe.setWidth(w)
    blue_stripe.setOutline('blue')

    indigo_stripe = Line (Point(p1_x +125, p1_y),Point(p2_x+125, p2_y))
    indigo_stripe.setWidth(w)
    indigo_stripe.setOutline('darkblue')

    violet_stripe = Line (Point(p1_x +150, p1_y),Point(p2_x+150, p2_y))
    violet_stripe.setWidth(w)
    violet_stripe.setOutline('purple')


    rainbow = [red_stripe, orange_stripe, yellow_stripe, green_stripe,
                        blue_stripe, indigo_stripe, violet_stripe]

    # the cloud
    x = 554
    y = 342
    r = 60

    cloud2_part1 = Circle(Point(x, y), r)
    cloud2_part1.setOutline("white")
    cloud2_part1.setFill("white")

    cloud2_part2 = Circle(Point(x / 1.17, y / 0.93), r / 1.25)
    cloud2_part2.setOutline("white")
    cloud2_part2.setFill("white")

    cloud2_part3 = Oval (Point(x / 1.43, y / 0.92),Point(x / 0.89, y / 0.81))
    cloud2_part3.setOutline("white")
    cloud2_part3.setFill("white")

    cloud2 = [cloud2_part1, cloud2_part2, cloud2_part3]

    # workaround to fix Mehra's code 2
    x = 640
    y = 480

    #The left side:
    #cave
    cavewall = color_rgb(68, 67, 66)
    cavefloor = color_rgb(38, 37, 37)
    caverock = color_rgb(25, 23, 22)

    cave_wall = Rectangle (Point (0,0), Point(320, 480))
    cave_wall.setFill(cavewall)
    cave_wall.setOutline(cavewall)

    cave_floor = Rectangle (Point (0,360), Point(320, 480))
    cave_floor.setFill(cavefloor)
    cave_floor.setOutline(cavefloor)

    #--------------------
    #Rock1
    x1 = 260
    y1 = 400

    cave_rock1 = Polygon(Point(x1, y1), Point(x1 / 1.1, y1 / 1.05),
                            Point(x1 / 1.1, y1 / 1.11), Point(x1 / 1.23, y1 / 1.17),
                            Point(x1 / 1.61, y1 / 1.11), Point(x1 / 1.9, y1))
    cave_rock1.setFill(caverock)
    cave_rock1.setOutline(caverock)

    #--------------------
    #Cave roof
    #roof1

    roof_rock1 = Polygon(Point(0, 168.0), Point(32.0, 129.0),
                            Point(91.0, 126.0), Point(136.0, 60.0),
                            Point(206.0, 0), Point(0, 0))
    roof_rock1.setFill(caverock)
    roof_rock1.setOutline(caverock)

    cave = [cave_wall, cave_floor, cave_rock1, roof_rock1]

    # less typing
    win.setBackground('darkblue')
    everything = moon + rainbow + cloud2 + cave + catlist + [startbutton, title, starttext]
    for i in everything:
        i.draw(win)
    update()

    # wait for user loop
    while True:
        mouse = win.getMouse()
        if mouse is not None:
            if startbutton.getP1().getX() <= mouse.getX() <= startbutton.getP2().getX() and startbutton.getP1().getY() <= mouse.getY() <= startbutton.getP2().getY():
                break
    for i in everything:
        i.undraw()
    # tell main loop to run backstory
    return 1

def backstory(): # scene 1 ish
    win.setBackground('black')
    backstorytext1 = 'Once upon a time, there lived a cat in a'
    backstorytext2 = '\ndark cave. The cat was very upset with his'
    backstorytext3 = '\ncave. It was so dark and boring!'
    backstorytext4 = ' \n\nOne morning, he was so bored that he'
    backstorytext5 = '\ndecided to go outside and find a new home...'
    backstorytemp = ['','','','','']
    backstory = [Text(Point(x / 2, y / 6), ''), Text(Point(x / 2 - 6, y / 6 + 14), ''), Text(Point(x / 2 - 6, y / 6 + 42), ''), Text(Point(x / 2 - 18, y / 6 + 70), ''), Text(Point(x / 2, y / 6 + 112), '')]

    for i in backstory:
        i.setFill('white')
        i.setSize(18)
        i.setFace('courier')
        i.setStyle('bold')
    paktc.setText('Press right arrow to skip')
    esctp.draw(win)
    update()

    # Skip text for testing purposes/lazy
    tick = 0
    while tick != 180:
        key = win.checkKey()
        if key == 'Right':
            break
        time.sleep(1/60)
        tick += 1
    esctp.undraw()
    for i in catlist + backstory + [paktc]:
        i.draw(win)

    # initialise
    counter = 0
    skip = False
    for i in [backstorytext1, backstorytext2, backstorytext3, backstorytext4, backstorytext5]:
        # creates nice typing effect with pauses after periods
        for a in i:
            backstorytemp[counter] += a
            backstorytemptemp = backstorytemp[counter].ljust(43)
            backstory[counter].setText(backstorytemptemp)
            update()
            if not skip:
                time.sleep(1/20)
                if a == '.' or a == '!':
                    time.sleep(1/4)
            key = win.checkKey()
            if key != '':
                if key == 'Escape':
                    paused = pause()
                    if paused == 1:
                        for i in catlist + backstory + [paktc]:
                            i.undraw()
                        return 0
                    elif paused == 3:
                        for i in catlist + backstory + [paktc]:
                            i.undraw()
                        return 1
                elif key == 'Right':
                    skip = True
        counter += 1
    paktc.setText('Press any key to continue...')
    update()

    while True: # loop for user to do something, either pausing or not pausing
        key = win.getKey()
        if key != '': # used for performance
            if key != 'Escape': # continue to scene 2 if any other key is pressed
                for i in catlist + backstory + [paktc]:
                    i.undraw()
                return 2
            else:
                paused = pause() # find out what user clicks after pausing
                if paused == 1: # 1 is to restart, anything else is either to continue (do nothing) or exit (handled by pause function)
                    for i in catlist + backstory + [paktc]:
                        i.undraw()
                    return 0
                elif paused == 3:
                    for i in catlist + backstory + [paktc]:
                        i.undraw()
                    update()
                    return 1

def desert():
    global exp
    tempexp = 0
    #------------------------------------------------------------
    #The Sun

    sun = Circle(Point(150,160),130)
    sun.setOutline('yellow')
    sun.setFill('yellow')

    #------------------------------------------------------------
    #The Mountains

    mountain1 = Polygon (Point(80,100), Point(100,80), Point(120,100))
    mountain1.setFill(color_rgb(109, 36, 5))
    mountain1.setOutline(color_rgb(109, 36, 5))

    mountain2 = Polygon (Point(120,100), Point(140,90), Point(160,100))
    mountain2.setFill(color_rgb(109, 36, 5))
    mountain2.setOutline(color_rgb(109, 36, 5))

    mountain3 = Polygon (Point(300,100), Point(320,80), Point(340,100))
    mountain3.setFill(color_rgb(109, 36, 5))
    mountain3.setOutline(color_rgb(109, 36, 5))

    mountain4 = Polygon (Point(340,100), Point(390,50), Point(440,100))
    mountain4.setFill(color_rgb(109, 36, 5))
    mountain4.setOutline(color_rgb(109, 36, 5))

    mountain5 = Polygon (Point(440,100), Point(470,60), Point(500,100))
    mountain5.setFill(color_rgb(109, 36, 5))
    mountain5.setOutline(color_rgb(109, 36, 5))
    #------------------------------------------------------------
    #The Ground

    ground = Rectangle(Point(0,100), Point(640,480))
    ground.setFill(color_rgb(209, 100, 54))
    ground.setOutline(color_rgb(209, 100, 54))

    #------------------------------------------------------------
    #The Rocks

    rock1 = Polygon(Point(650,190), Point(630,160), Point(620,170), Point(610,170), Point(600,190), Point(590,180), Point(570,190))
    rock1.setFill(color_rgb(249, 172, 64))
    rock1.setOutline(color_rgb(249, 172, 64))

    rock2 = Polygon(Point(130,300), Point(100,270), Point(70,300), Point(130,300))
    rock2.setFill(color_rgb(249, 172, 64))
    rock2.setOutline(color_rgb(249, 172, 64))

    rock3 = Polygon(Point(210,300), Point(190,280), Point(190,260), Point(170,240), Point(130,260), Point(110,300))
    rock3.setFill(color_rgb(249, 172, 64))
    rock3.setOutline(color_rgb(249, 172, 64))

    #------------------------------------------------------------
    #Cactus

    cactus2_part1 = Oval (Point(240,120), Point(200,200))
    cactus2_part1.setFill('darkgreen')
    cactus2_part1.setOutline('darkgreen')

    cactus2_part2 = Oval (Point(180,170), Point(210,160))
    cactus2_part2.setFill('darkgreen')
    cactus2_part2.setOutline('darkgreen')

    cactus2_part3 = Oval (Point(230,160), Point(270,145))
    cactus2_part3.setFill('darkgreen')
    cactus2_part3.setOutline('darkgreen')

    cactus2_base = Rectangle (Point(200,200),Point(240,180))
    cactus2_base.setFill(color_rgb(209, 100, 54))
    cactus2_base.setOutline(color_rgb(209, 100, 54))


    cactus4_part1 = Oval (Point(570,280), Point(590,200))
    cactus4_part1.setFill('darkgreen')
    cactus4_part1.setOutline('darkgreen')

    cactus4_part2 = Oval (Point(545,235), Point(585,220))
    cactus4_part2.setFill('darkgreen')
    cactus4_part2.setOutline('darkgreen')

    cactus4_base = Rectangle (Point(570,260),Point(590,280))
    cactus4_base.setFill(color_rgb(209, 100, 54))
    cactus4_base.setOutline(color_rgb(209, 100, 54))

    #------------------------------------------------------------
    #Foreground

    foregroundbrown = color_rgb(226, 135, 38)
    foreground = Rectangle (Point (0,360), Point(640, 480))
    foreground.setFill(foregroundbrown)
    foreground.setOutline(foregroundbrown)

    lightcactusgreen = color_rgb(22, 124, 8)
    x = 380
    y = 290

    cactus1_part1 = Oval (Point(x,y), Point(x / 0.86, y / 0.64))
    cactus1_part1.setFill(lightcactusgreen)
    cactus1_part1.setOutline(lightcactusgreen)

    cactus1_part2 = Oval (Point(x / 0.76, y / 0.80), Point(x / 0.97, y / 0.74))
    cactus1_part2.setFill(lightcactusgreen)
    cactus1_part2.setOutline(lightcactusgreen)

    cactus1_part3 = Oval (Point(x / 1.11, y / 0.85), Point(x / 0.90, y / 0.80))
    cactus1_part3.setFill(lightcactusgreen)
    cactus1_part3.setOutline(lightcactusgreen)

    cactus1_base = Rectangle (Point(x / 0.87, y / 0.69),Point(x, y / 0.60))
    cactus1_base.setFill(foregroundbrown)
    cactus1_base.setOutline(foregroundbrown)

    # Fixing x and y to make sense
    x = 640
    y = 480
    text1 = Text(Point(x / 2, y * 1 / 4), 'The cat arrived in a desert, and looked around. It was far too dry.')
    text1.setFill('white')
    text1.setStyle('bold')
    text1.setSize(14)
    text2 =  'So he moved on...'
    addtext = 'and on...'

    desertlist = [sun, mountain1, mountain2, mountain3, mountain4, mountain5, ground, rock1, rock2, rock3, foreground, cactus1_part1, cactus1_part2, cactus1_part3, cactus1_base, cactus2_part1, cactus2_part2, cactus2_part3, cactus2_base, cactus4_part1, cactus4_part2, cactus4_base, text1]

    win.setBackground('lightblue')
    for i in desertlist:
        i.draw(win)
    update()

    # Cat is reset after every scene
    for i in catlist:
        i.move(-x + 200, 40)

    # Bounce in
    tick = 0
    minitick = 1
    while tick != 60:
        key = win.checkKey()
        mouse = win.checkMouse()
        if mouse != None and tempexp == 0:
            # checking if sun is clicked, probably could be better optimised
            if sun.getP1().getX() <= mouse.getX() <= sun.getP2().getX() and sun.getP1().getY() <= mouse.getY() <= sun.getP2().getY():
                tempexp += 1
                expget.draw(win)
                update()
                time.sleep(1)
                expget.undraw()
                update()
        if key == 'Escape':
            paused = pause()
            if paused == 1:
                for i in catlist + desertlist:
                    i.undraw()
                update()
                return 0
            elif paused == 3:
                for i in catlist + desertlist:
                    i.undraw()
                update()
                return 2
        if tick % 5 == 0:
            minitick *= -1
        if minitick == 1:
            for i in catlist:
                i.move(0, 3)
        else:
            for i in catlist:
                i.move(0, -3)
        for i in catlist:
            i.undraw()
            i.move(5, 0)
            i.draw(win)
        time.sleep(1/60)
        update()
        tick += 1

    # Look around
    tick = 0
    while tick != 60:
        centre = (ptbgcircle1.getCenter().getX() + ptbgcircle4.getCenter().getX()) / 2
        key = win.checkKey()
        mouse = win.checkMouse()
        if mouse != None and tempexp == 0:
            if sun.getP1().getX() <= mouse.getX() <= sun.getP2().getX() and sun.getP1().getY() <= mouse.getY() <= sun.getP2().getY():
                tempexp += 1
                expget.draw(win)
                update()
                time.sleep(1)
                expget.undraw()
                update()
        if key == 'Escape':
            paused = pause()
            if paused == 1:
                for i in catlist + desertlist:
                    i.undraw()
                update()
                return 0
            elif paused == 3:
                for i in catlist + desertlist:
                    i.undraw()
                update()
                return 2
        if tick % 15 == 0:
            catflip(centre)
            for i in catlist:
                i.undraw()
                i.draw(win)
            update()
        time.sleep(1/60)
        tick += 1

    paktc.setText('Press right arrow to move')
    paktc.draw(win)

    potato2 = 0
    for potato in range(-2, 3):
# hop, copied from a previous deleted function
        flip = 0
        potato2 += 1
        wrap_movement = True
        while True:
            mx = 0
            my = 0
            centre = (ptbgcircle1.getCenter().getX() + ptbgcircle4.getCenter().getX()) / 2
            key = win.checkKey()
            mouse = win.checkMouse()
            if mouse != None and tempexp == 0:
                if sun.getP1().getX() <= mouse.getX() <= sun.getP2().getX() and sun.getP1().getY() <= mouse.getY() <= sun.getP2().getY() and exp == 0:
                    tempexp += 1
                    expget.draw(win)
                    update()
                    time.sleep(1)
                    expget.undraw()
                    update()
            if key != '':
                if key == 'Right':
                    if flip == 1:
                        catflip(centre)
                        flip = 0
                    mx = 10
                    my = 0
                elif key == 'Escape':
                    paused = pause() # find out what user clicks after pausing
                    if paused == 1: # 1 is to restart, anything else is either to continue (do nothing) or exit (handled by pause function)
                        for i in catlist + desertlist + [paktc]:
                            i.undraw()
                        update()
                        return 0
                    elif paused == 3:
                        for i in catlist + desertlist + [paktc]:
                            i.undraw()
                        update()
                        return 2
                # Current way to break
            if ptbgcircle4.getCenter().getX() >= cactus1_base.getP1().getX() - 120:# configurable value
                break
            for i in catlist:
                i.undraw()
                i.move(mx, my)
                i.draw(win)
            update()
            time.sleep(1/60)
        if potato2 == 1:
            text1.setText(text2)
            text1.undraw()
            text1.draw(win)
        # jump over thing
        for i in range(-30, 31, 2):
            if flip == 0:
                mx = 10
            elif flip == 1:
                mx = -10
            key = win.checkKey()
            mouse = win.checkMouse()
            if mouse != None and tempexp == 0: # again handling pausing and clicking of sun
                if sun.getP1().getX() <= mouse.getX() <= sun.getP2().getX() and sun.getP1().getY() <= mouse.getY() <= sun.getP2().getY() and exp == 0:
                    tempexp += 1
                    expget.draw(win)
                    update()
                    time.sleep(1)
                    expget.undraw()
                    update()
            if key == 'Escape':
                paused = pause()
                if paused == 1:
                    for i in catlist + desertlist + [paktc]:
                        i.undraw()
                    update()
                    return 0
                elif paused == 3:
                    for i in catlist + desertlist + [paktc]:
                        i.undraw()
                    update()
                    return 2
            for a in catlist:
                a.move(mx, i)
                a.undraw()
                a.draw(win)
            update()
            time.sleep(1/60)
        for i in range(40):
            for i in catlist:
                i.move(5, 0)
                i.undraw()
                i.draw(win)
            time.sleep(1/120)
            update()
        if potato != 2:
            for i in catlist:
                i.move(-x - 200, 0)
            sun.move(75, potato * 20) # shows progression of time
            if potato != 1:
                text1.setText(text2 + addtext * potato2)
            else:
                text1.setText('And on, until he finally reached the end.')
                update()

    paktc.setText('Press any key to continue...')
    paktc.undraw()
    paktc.draw(win)
    while True: # loop for user to do something, either pausing or not pausing
        key = win.getKey()
        mouse = win.checkMouse()
        if mouse != None:
            if sun.getP1().getX() <= mouse.getX() <= sun.getP2().getX() and sun.getP1().getY() <= mouse.getY() <= sun.getP2().getY() and exp == 0:
                tempexp += 1
                expget.draw(win)
                update()
                time.sleep(1)
                expget.undraw()
                update()
        if key != '': # used for performance
            if key != 'Escape': # continue to scene 3 if any other key is pressed
                for i in catlist + desertlist + [paktc]:
                    i.undraw()
                exp += tempexp
                return 3
            else:
                paused = pause() # find out what user clicks after pausing
                if paused == 1: # 1 is to restart, anything else is either to continue (do nothing) or exit (handled by pause function)
                    for i in desertlist + catlist + [paktc]:
                        i.undraw()
                    return 0
                elif paused == 3:
                    for i in desertlist + catlist + [paktc]:
                        i.undraw()
                    return 2

def forest():
    global exp
    barkbrown = color_rgb(170, 76, 8)
    leafgreen = color_rgb(44, 160, 50)
    darkbark = color_rgb(114, 54, 14)

    #background
    win.setBackground(color_rgb(49, 66, 47))

    #tree1
    tree1 = Rectangle (Point(470.0, 376.0),Point(600.0, 0))
    tree1.setFill(darkbark)
    tree1.setOutline(darkbark)

    #tree2
    tree2 = Rectangle (Point(63.0, 392.0), Point(0, 0))
    tree2.setFill(barkbrown)
    tree2.setOutline(barkbrown)

    #tree3
    tree3 = Polygon (Point(215.0, 380.0), Point(255.0, 380.0),
                      Point(255.0, 0), Point(215.0, 0),
                      Point(215.0, 182.0), Point(165.0, 178.0),
                      Point(164.0, 186.0), Point(215.0, 202.0))
    tree3.setFill(darkbark)
    tree3.setOutline(darkbark)

    #tree4
    trunk4 = Polygon (Point(544, 360), Point(544, 278), Point(506, 246), Point(485, 245), Point(504, 239), Point(546, 250),
                      Point(546, 158), Point(633, 134), Point(633, 360), Point(546, 360))
    trunk4.setFill(barkbrown)
    trunk4.setOutline(barkbrown)

    tree4_part1 = Circle (Point(563, 77), 70)
    tree4_part1.setFill(leafgreen)
    tree4_part1.setOutline(leafgreen)

    tree4_part2 = Circle (Point(508, 58), 50)
    tree4_part2.setFill(leafgreen)
    tree4_part2.setOutline(leafgreen)

    tree4_part3 = Circle (Point(496, 135), 50)
    tree4_part3.setFill(leafgreen)
    tree4_part3.setOutline(leafgreen)

    tree4_part4 = Circle (Point(627, 105), 60)
    tree4_part4.setFill(leafgreen)
    tree4_part4.setOutline(leafgreen)

    tree4_part5 = Circle (Point(556, 151), 60)
    tree4_part5.setFill(leafgreen)
    tree4_part5.setOutline(leafgreen)

    tree4 = [trunk4, tree4_part1, tree4_part2, tree4_part3, tree4_part4, tree4_part5]

    #tree5
    trunk5 = Polygon (Point(113, 375), Point(117, 166), Point(67, 140),
                      Point(122, 150), Point(123, 74), Point(177, 67),
                      Point(193, 242), Point(239, 229), Point(194, 258),
                      Point(197, 382))
    trunk5.setFill(barkbrown)
    trunk5.setOutline(barkbrown)

    tree5_part1 = Circle (Point(163, 52), 50)
    tree5_part1.setFill(leafgreen)
    tree5_part1.setOutline(leafgreen)

    tree5_part2 = Circle (Point(108, 35), 50)
    tree5_part2.setFill(leafgreen)
    tree5_part2.setOutline(leafgreen)

    tree5_part3 = Circle (Point(96, 110), 50)
    tree5_part3.setFill(leafgreen)
    tree5_part3.setOutline(leafgreen)

    tree5_part4 = Circle (Point(227, 80), 50)
    tree5_part4.setFill(leafgreen)
    tree5_part4.setOutline(leafgreen)

    tree5_part5 = Circle (Point(156, 126), 60)
    tree5_part5.setFill(leafgreen)
    tree5_part5.setOutline(leafgreen)

    tree5 = [trunk5, tree5_part1, tree5_part2, tree5_part3, tree5_part4, tree5_part5]

    #tree6
    tree6 = Polygon (Point(270, 374), Point(385, 377),
                      Point(385, 120), Point(530, 82),
                      Point(448, 87), Point(454, 63),
                      Point(429, 91), Point(385, 83),
                      Point(385, 0), Point(270, 0))
    tree6.setFill(barkbrown)
    tree6.setOutline(barkbrown)

    #tree7
    trunk7 = Polygon (Point(370, 380), Point(370, 240),
                      Point(435, 239), Point(435, 288),
                      Point(444, 287), Point(445, 301),
                      Point(435, 305), Point(443, 377))
    trunk7.setFill(darkbark)
    trunk7.setOutline(darkbark)

    tree7_part1 = Circle (Point(376, 242), 50)
    tree7_part1.setFill(leafgreen)
    tree7_part1.setOutline(leafgreen)

    tree7_part2 = Circle (Point(418, 176), 50)
    tree7_part2.setFill(leafgreen)
    tree7_part2.setOutline(leafgreen)

    tree7_part3 = Circle (Point(438, 230), 50)
    tree7_part3.setFill(leafgreen)
    tree7_part3.setOutline(leafgreen)

    tree7_part4 = Circle (Point(352, 186), 40)
    tree7_part4.setFill(leafgreen)
    tree7_part4.setOutline(leafgreen)

    tree7 = [trunk7, tree7_part1, tree7_part2, tree7_part3, tree7_part4]

    trees = [tree1, tree2, tree3] + tree4 + tree5 + [tree6] + tree7

    #grass
    grassgreen = color_rgb(118, 229, 103)
    grass_foreground = Rectangle (Point (0,360), Point(640, 480))
    grass_foreground.setFill(grassgreen)
    grass_foreground.setOutline(grassgreen)

    grassblades = Polygon (Point(249, 368), Point(256, 332), Point(264, 363), Point(275, 327),
                      Point(304, 366), Point(326, 320), Point(323, 365), Point(433, 365), Point(439, 316), Point(448, 375),
                      Point(480, 371), Point(487, 332), Point(492, 371), Point(539, 369), Point(540, 332),
                      Point(552, 368), Point(565, 332), Point(562, 368), Point(581, 367), Point(582, 343), Point(599, 371))
    grassblades.setFill(grassgreen)
    grassblades.setOutline(grassgreen)

    grass = [grass_foreground, grassblades]

    #flowers
    flower1 = Oval (Point (547, 436), Point (562, 446))
    flower1.setFill('orange')
    flower1.setWidth(4)
    flower1.setOutline('white')

    flower2 = Oval (Point (405, 392), Point (420, 402))
    flower2.setFill('orange')
    flower2.setWidth(4)
    flower2.setOutline('white')

    flower3 = Oval (Point (233, 433), Point (248, 443))
    flower3.setFill('orange')
    flower3.setWidth(4)
    flower3.setOutline('white')

    flower4 = Oval (Point (42, 428), Point (57, 438))
    flower4.setFill('orange')
    flower4.setWidth(4)
    flower4.setOutline('white')

    flowers = [flower1, flower2, flower3, flower4]

    #bush
    bush_part1 = Circle (Point(23, 228), 50)
    bush_part1.setFill('darkgreen')
    bush_part1.setOutline('darkgreen')

    bush_part2 = Circle (Point(190, 355), 50)
    bush_part2.setFill('darkgreen')
    bush_part2.setOutline('darkgreen')

    bush_part3 = Circle (Point(120, 272), 40)
    bush_part3.setFill('darkgreen')
    bush_part3.setOutline('darkgreen')

    bush_part4 = Circle (Point(125, 337), 60)
    bush_part4.setFill('darkgreen')
    bush_part4.setOutline('darkgreen')

    bush_part5 = Circle (Point(73, 239), 40)
    bush_part5.setFill('darkgreen')
    bush_part5.setOutline('darkgreen')

    bush_part6 = Circle (Point(38, 328), 70)
    bush_part6.setFill('darkgreen')
    bush_part6.setOutline('darkgreen')

    bush = [bush_part1, bush_part2, bush_part3, bush_part4, bush_part5, bush_part6]

    #Obstacle(Tree Stump)
    p1_X = 370
    p1_Y = 350
    p2_X = 480
    p2_Y = 390

    top = Oval (Point(p1_X, p1_Y), Point(p2_X, p2_Y))
    top.setFill('orange2')
    top.setOutline('orange2')

    n = (top.getCenter().getY() - p1_Y)

    base = Polygon (Point (p1_X, p1_Y + n), Point(p2_X, p2_Y - n),
                    Point(p2_X + n*1.5, p2_Y + n*1.5), Point(p1_X - n*1.5, p2_Y + n*1.5))
    base.setFill(barkbrown)
    base.setOutline(barkbrown)

    stump = [base, top]

    storytext = Text(Point(x / 2, y * 3 / 10), 'The cat entered a forest and looked around. There were far too\n many trees for him to see anything here, let alone fly.')
    storytext.setSize(14)
    storytext.setStyle('bold')
    storytext.setFill('white')
    storytext2 = 'Cursing as he left, he bumped into tree after tree before making it out.'

    forestlist = trees + grass + flowers + bush
    for i in forestlist:
        i.draw(win)

    for i in catlist:
        i.move(-x + 200, 0)

    # Bounce in
    tick = 0
    tempexp = 0
    flower1exp = 0
    flower2exp = 0
    minitick = 1
    while tick != 80:
        key = win.checkKey()
        mouse = win.checkMouse()
        if mouse != None: # checking where clicks happen and for pausing
            if flower1.getP1().getX() <= mouse.getX() <= flower1.getP2().getX() and flower1.getP1().getY() <= mouse.getY() <= flower1.getP2().getY() and flower1exp == 0:
                tempexp += 1
                flower1exp += 1
                expget.draw(win)
                update()
                time.sleep(1)
                expget.undraw()
                update()
            elif flower2.getP1().getX() <= mouse.getX() <= flower2.getP2().getX() and flower2.getP1().getY() <= mouse.getY() <= flower2.getP2().getY() and flower2exp == 0:
                tempexp += 1
                flower2exp += 1
                expget.draw(win)
                update()
                time.sleep(1)
                expget.undraw()
                update()
        if key == 'Escape':
            paused = pause()
            if paused == 1:
                for i in catlist + forestlist + [storytext]:
                    i.undraw()
                update()
                return 0
            elif paused == 3:
                for i in catlist + forestlist + [storytext]:
                    i.undraw()
                update()
                return 3
        if tick % 5 == 0: # handles bouncing in
            minitick *= -1
        if minitick == 1:
            for i in catlist:
                i.move(0, 3)
        else:
            for i in catlist:
                i.move(0, -3)
        for i in catlist:
            i.undraw()
            i.move(5, 0)
            i.draw(win)
        for i in bush + [storytext]:
            i.undraw()
            i.draw(win)
        time.sleep(1/60)
        update()
        tick += 1

    paktc.draw(win)
    update()
    while True: # press any key to continue before moving on to next story line
        key = win.checkKey()
        mouse = win.checkMouse()
        if key != '':
            if key == 'Escape':
                paused = pause()
                if paused == 1:
                    for i in forestlist + catlist + [storytext, paktc]:
                        i.undraw()
                    return 0
                elif paused == 3:
                    for i in forestlist + catlist + [storytext, paktc]:
                        i.undraw()
                    return 3
            else:
                break
        if mouse != None:
            if flower1.getP1().getX() <= mouse.getX() <= flower1.getP2().getX() and flower1.getP1().getY() <= mouse.getY() <= flower1.getP2().getY() and flower1exp == 0:
                tempexp += 1
                flower1exp += 1
                expget.draw(win)
                update()
                time.sleep(1)
                expget.undraw()
                update()
            elif flower2.getP1().getX() <= mouse.getX() <= flower2.getP2().getX() and flower2.getP1().getY() <= mouse.getY() <= flower2.getP2().getY() and flower2exp == 0:
                tempexp += 1
                flower2exp += 1
                expget.draw(win)
                update()
                time.sleep(1)
                expget.undraw()
                update()

    storytext.setText(storytext2)
    paktc.undraw()

    tick = 0
    wrap_times = 0
    while wrap_times <= 8: # bump into things over and over again
        key = win.checkKey()
        mouse = win.checkMouse()
        if mouse != None:
            if flower1.getP1().getX() <= mouse.getX() <= flower1.getP2().getX() and flower1.getP1().getY() <= mouse.getY() <= flower1.getP2().getY() and flower1exp == 0:
                tempexp += 1
                flower1exp += 1
                expget.draw(win)
                update()
                time.sleep(1)
                expget.undraw()
                update()
            elif flower2.getP1().getX() <= mouse.getX() <= flower2.getP2().getX() and flower2.getP1().getY() <= mouse.getY() <= flower2.getP2().getY() and flower2exp == 0:
                tempexp += 1
                flower2exp += 1
                expget.draw(win)
                update()
                time.sleep(1)
                expget.undraw()
                update()
        if key == 'Escape':
            paused = pause()
            if paused == 1:
                for i in catlist + forestlist + [storytext]:
                    i.undraw()
                update()
                return 0
            elif paused == 3:
                for i in catlist + forestlist + [storytext]:
                    i.undraw()
                update()
                return 3
        if tick % 5 == 0:
            minitick *= -1
        if minitick == 1:
            for i in catlist:
                i.move(0, 3)
        else:
            for i in catlist:
                i.move(0, -3)
        for i in catlist:
            i.undraw()
            i.move(5, 0)
            i.draw(win)
        for i in bush + [storytext]:
            i.undraw()
            i.draw(win)
        if tick % 20 == 0:
            time.sleep(0.5)
            wrap_times += 1
        elif tick % 45 == 0:
            time.sleep(0.25)
            wrap_times += 1
        time.sleep(1/60)
        update()
        tick += 1
    paktc.draw(win)

    while True: # loop for user to do something, either pausing or not pausing
        key = win.getKey()
        if key != '': # used for performance
            if key != 'Escape': # continue to scene 4 if any other key is pressed
                for i in forestlist + catlist + [storytext, paktc]:
                    i.undraw()
                exp += tempexp
                return 4
            else:
                paused = pause() # find out what user clicks after pausing
                if paused == 1: # 1 is to restart, anything else is either to continue (do nothing) or exit (handled by pause function)
                    for i in forestlist + [storytext, paktc]:
                        i.undraw()
                    return 0
                elif paused == 3:
                    for i in forestlist:
                        i.undraw()
                    return 3

def ocean():
    global exp
    kelpgreen = color_rgb(29, 79, 33)
    sandyellow = color_rgb(255, 212, 119)
    tempexp = 0
    def kelp(x, y, s):
        leaf1 = Rectangle(Point(x-(s/12),y-(s/2)), Point (x+(s/12), y-(s/6)))
        leaf1.setFill(kelpgreen)
        leaf1.setOutline(kelpgreen)
        leaf2 = Rectangle(Point(x-(s/24),y-(s/6)), Point (x+(s/8), y+(s/6)))
        leaf2.setFill(kelpgreen)
        leaf2.setOutline(kelpgreen)
        leaf3 = Rectangle(Point(x-(s/12),y+(s/6)), Point (x+(s/12), y+(s/2)))
        leaf3.setFill(kelpgreen)
        leaf3.setOutline(kelpgreen)
        return [leaf1, leaf2, leaf3]

    #fish
    class fish():
        def __init__(self, x, y, s):
            fishgrey = color_rgb(108, 143, 199)
            self.body = Oval (Point (x, y), Point (x + s, y + (s/2)))
            self.body.setFill(fishgrey)
            self.body.setOutline(fishgrey)
            self.tail = Polygon (Point (x + (s/4), y + (s/4)), Point (x - (s/4), y),
                        Point (x - (s/4), y + (s/2)))
            self.tail.setFill(fishgrey)
            self.tail.setOutline(fishgrey)

        def draw(self, win):
            self.body.draw(win)
            self.tail.draw(win)

        def undraw(self):
            self.body.undraw()
            self.tail.undraw()

        def getP1(self): return self.tail.getPoints()[1]

        def getP2(self): return self.body.getP2()

        def move(self, dx, dy):
            for i in [self.body, self.tail]:
                i.move(dx, dy)


    fish1 = fish(100, 200, 25)
    fish2 = fish(150, 100, 10)
    fish3 = fish(260, 160, 15)
    fish4 = fish(200, 220, 30)
    fish5 = fish(300, 60, 32)

    fish = [fish1, fish2, fish3, fish4, fish5]


    #back kelp
    kelp1 = kelp(200, 330, 100)
    kelp2 = kelp(550, 300, 150)

    #sand
    sand = Rectangle (Point (0,360), Point(640, 480))
    sand.setFill(sandyellow)
    sand.setOutline(sandyellow)

    #front kelp
    kelp3 = kelp(70, 370, 130)
    kelp4 = kelp(400, 425, 100)

    #rocks

    ocean_rock1 = Polygon(Point(105, 462), Point(193, 462),
                         Point(189, 425), Point(145, 411),
                         Point(112, 430))
    ocean_rock1.setFill('grey')
    ocean_rock1.setOutline('grey')


    ocean_rock2 = Polygon(Point(455, 390), Point(605, 390),
                          Point(569, 341), Point(550, 284),
                          Point(475, 321))
    ocean_rock2.setFill('grey')
    ocean_rock2.setOutline('grey')

    ocean_rocks = [ocean_rock1, ocean_rock2]
    # rainbow
    p1_x = 940
    p1_y = 735
    r = 655
    w = 25

    red_ring = Circle (Point(p1_x, p1_y), r)
    red_ring.setWidth(w)
    red_ring.setOutline('purple')

    orange_ring = Circle (Point(p1_x, p1_y), r+25)
    orange_ring.setWidth(w)
    orange_ring.setOutline('darkblue')

    yellow_ring = Circle (Point(p1_x, p1_y), r+50)
    yellow_ring.setWidth(w)
    yellow_ring.setOutline('blue')

    green_ring = Circle (Point(p1_x, p1_y), r+75)
    green_ring.setWidth(w)
    green_ring.setOutline('lightgreen')

    blue_ring = Circle (Point(p1_x, p1_y), r+100)
    blue_ring.setWidth(w)
    blue_ring.setOutline('yellow')

    indigo_ring = Circle (Point(p1_x, p1_y), r+125)
    indigo_ring.setWidth(w)
    indigo_ring.setOutline('orange')

    violet_ring = Circle (Point(p1_x, p1_y), r+150)
    violet_ring.setWidth(w)
    violet_ring.setOutline('red')

    rainbow = [red_ring, orange_ring, yellow_ring, green_ring,
                        blue_ring, indigo_ring, violet_ring]

    # move rainbow to better location since it's too far
    for i in rainbow:
        i.move(200, 0)

    kelplist = kelp1 + kelp2 + kelp3 + kelp4
    movingkelplist = [kelp1[1], kelp2[1], kelp3[1], kelp4[1]]
    topmovingkelplist = [kelp1[0], kelp2[0], kelp3[0], kelp4[0]]

    # Shark
    shark = Image(Point(x / 2 - radius * 5, y / 4), 'baby shark.gif')

    storytext = Text(Point(x / 2, y * 1 / 16), 'Leaving the forest, the cat entered the ocean.')
    storytext.setSize(14)
    storytext.setFill('white')
    storytext.setStyle('bold')
    storytext2 = 'The ocean was nice, but the cat\'s fur was soaked. It was as\n boring as the cave, until...'
    storytext3 = 'A shark appeared! The cat swam as fast as it could!'
    storytext4 = 'Deciding that there were far too many predators in this area,\n the cat left on a rainbow.'
    oceanlist = fish + [sand] + kelplist + ocean_rocks

    win.setBackground('royalblue')
    for i in oceanlist + [storytext]:
        i.draw(win)

    for i in catlist:
        i.move(-x + 200, -40)

    # Swim in
    tick = 0
    tempexp = 0
    kelptick = 1
    kelp1exp = 0
    kelp2exp = 0
    kelp3exp = 0
    fish1exp = 0
    fish2exp = 0
    fish3exp = 0
    fish4exp = 0
    fish5exp = 0
    swimspeed = 8
    while tick <= 180:
        key = win.checkKey()
        mouse = win.checkMouse()
        if mouse != None: # probably could be better optimised
            experience_collected = False
            if kelp1[1].getP1().getX() <= mouse.getX() <= kelp1[1].getP2().getX() and kelp1[1].getP1().getY() <= mouse.getY() <= kelp1[1].getP2().getY() and kelp1exp == 0:
                kelp1exp += 1
                experience_collected = True
            if kelp2[1].getP1().getX() <= mouse.getX() <= kelp2[1].getP2().getX() and kelp2[1].getP1().getY() <= mouse.getY() <= kelp2[1].getP2().getY() and kelp2exp == 0:
                kelp2exp += 1
                experience_collected = True
            if kelp3[1].getP1().getX() <= mouse.getX() <= kelp3[1].getP2().getX() and kelp3[1].getP1().getY() <= mouse.getY() <= kelp3[1].getP2().getY() and kelp3exp == 0:
                kelp3exp += 1
                experience_collected = True
            elif fish1.getP1().getX() <= mouse.getX() <= fish1.getP2().getX() and fish1.getP1().getY() <= mouse.getY() <= fish1.getP2().getY() and fish1exp == 0:
                fish1exp += 1
                experience_collected = True
            elif fish2.getP1().getX() <= mouse.getX() <= fish2.getP2().getX() and fish2.getP1().getY() <= mouse.getY() <= fish2.getP2().getY() and fish2exp == 0:
                fish2exp += 1
            elif fish3.getP1().getX() <= mouse.getX() <= fish3.getP2().getX() and fish3.getP1().getY() <= mouse.getY() <= fish3.getP2().getY() and fish3exp == 0:
                fish3exp += 1
            elif fish4.getP1().getX() <= mouse.getX() <= fish4.getP2().getX() and fish4.getP1().getY() <= mouse.getY() <= fish4.getP2().getY() and fish4exp == 0:
                fish4exp += 1
            elif fish5.getP1().getX() <= mouse.getX() <= fish5.getP2().getX() and fish5.getP1().getY() <= mouse.getY() <= fish5.getP2().getY() and fish5exp == 0:
                fish5exp += 1
                experience_collected = True
            if experience_collected == True:
                tempexp += 1
                expget.draw(win)
                update()
                time.sleep(1)
                expget.undraw()
                update()
        if key == 'Escape':
            paused = pause()
            if paused == 1:
                for i in catlist + oceanlist + [storytext, shark]:
                    i.undraw()
                update()
                return 0
            elif paused == 3:
                for i in catlist + oceanlist + [storytext, shark]:
                    i.undraw()
                update()
                return 4

        if tick % 40 == 0:
            kelptick *= -1
        for i in movingkelplist:
            i.move(0.25 * kelptick, 0)
        for i in topmovingkelplist:
            i.move(0.1 * kelptick, 0)
        for i in fish:
            i.move(2, 0)
            if i.getP1().getX() >= x:
                i.move(-x - 40, 0)

        if swimspeed == 0:
            swimspeed = 8
        # handles swimming speed and paws
        for i in catlist:
            i.undraw()
            i.move(swimspeed / 2, 0)
            i.draw(win)
        if tick % 4 == 0:
            if swimspeed == 8:
                for i in externalmovelist[:4]:
                    i.move(0, -1)
            elif 5 <= swimspeed <= 7:
                for i in externalmovelist[:4]:
                    i.move(2, 0)
            elif swimspeed == 4:
                for i in externalmovelist[:4]:
                    i.move(0, 1)
            elif 1 <= swimspeed <= 3:
                for i in externalmovelist[:4]:
                    i.move(-2, 0)

        if tick % 8 == 0:
            swimspeed -= 1
        time.sleep(1/60)
        update()
        tick += 1

    # float there and do nothing, waiting for user to finish reading two stories
    paktc.draw(win)
    while True:
        key = win.checkKey()
        if key != 'Escape' and key != '':
            if storytext.getText() == storytext2:
                break
            else:
                storytext.setText(storytext2)
        mouse = win.checkMouse()
        if mouse != None:
            experience_collected = False
            if kelp1[1].getP1().getX() <= mouse.getX() <= kelp1[1].getP2().getX() and kelp1[1].getP1().getY() <= mouse.getY() <= kelp1[1].getP2().getY() and kelp1exp == 0:
                kelp1exp += 1
                experience_collected = True
            if kelp2[1].getP1().getX() <= mouse.getX() <= kelp2[1].getP2().getX() and kelp2[1].getP1().getY() <= mouse.getY() <= kelp2[1].getP2().getY() and kelp2exp == 0:
                kelp2exp += 1
                experience_collected = True
            if kelp3[1].getP1().getX() <= mouse.getX() <= kelp3[1].getP2().getX() and kelp3[1].getP1().getY() <= mouse.getY() <= kelp3[1].getP2().getY() and kelp3exp == 0:
                kelp3exp += 1
                experience_collected = True
            elif fish1.getP1().getX() <= mouse.getX() <= fish1.getP2().getX() and fish1.getP1().getY() <= mouse.getY() <= fish1.getP2().getY() and fish1exp == 0:
                fish1exp += 1
                experience_collected = True
            elif fish2.getP1().getX() <= mouse.getX() <= fish2.getP2().getX() and fish2.getP1().getY() <= mouse.getY() <= fish2.getP2().getY() and fish2exp == 0:
                fish2exp += 1
            elif fish3.getP1().getX() <= mouse.getX() <= fish3.getP2().getX() and fish3.getP1().getY() <= mouse.getY() <= fish3.getP2().getY() and fish3exp == 0:
                fish3exp += 1
            elif fish4.getP1().getX() <= mouse.getX() <= fish4.getP2().getX() and fish4.getP1().getY() <= mouse.getY() <= fish4.getP2().getY() and fish4exp == 0:
                fish4exp += 1
            elif fish5.getP1().getX() <= mouse.getX() <= fish5.getP2().getX() and fish5.getP1().getY() <= mouse.getY() <= fish5.getP2().getY() and fish5exp == 0:
                fish5exp += 1
                experience_collected = True
            if experience_collected == True:
                tempexp += 1
                expget.draw(win)
                update()
                time.sleep(1)
                expget.undraw()
                update()

        if key == 'Escape':
            paused = pause()
            if paused == 1:
                for i in catlist + oceanlist + [storytext, shark, paktc]:
                    i.undraw()
                update()
                return 0
            elif paused == 3:
                for i in catlist + oceanlist + [storytext, shark, paktc]:
                    i.undraw()
                update()
                return 4

        if tick % 40 == 0:
            kelptick *= -1
        for i in movingkelplist:
            i.move(0.25 * kelptick, 0)
        for i in topmovingkelplist:
            i.move(0.1 * kelptick, 0)
        for i in catlist:
            i.undraw()
            i.move(0, 0.25 * kelptick)
            i.draw(win)
        update()
        for i in fish:
            i.move(2, 0)
            if i.getP1().getX() >= x:
                i.move(-x - 40, 0)
        time.sleep(1/60)
        update()
        tick += 1

    storytext.setText(storytext3)
    update()

    shark.move(-550, 0)

    # Shark attack
    paktc.undraw()
    tick = 0
    while tick != 120:
        key = win.checkKey()
        mouse = win.checkMouse()
        if mouse != None:
            experience_collected = False
            if kelp1[1].getP1().getX() <= mouse.getX() <= kelp1[1].getP2().getX() and kelp1[1].getP1().getY() <= mouse.getY() <= kelp1[1].getP2().getY() and kelp1exp == 0:
                kelp1exp += 1
                experience_collected = True
            if kelp2[1].getP1().getX() <= mouse.getX() <= kelp2[1].getP2().getX() and kelp2[1].getP1().getY() <= mouse.getY() <= kelp2[1].getP2().getY() and kelp2exp == 0:
                kelp2exp += 1
                experience_collected = True
            if kelp3[1].getP1().getX() <= mouse.getX() <= kelp3[1].getP2().getX() and kelp3[1].getP1().getY() <= mouse.getY() <= kelp3[1].getP2().getY() and kelp3exp == 0:
                kelp3exp += 1
                experience_collected = True
            elif fish1.getP1().getX() <= mouse.getX() <= fish1.getP2().getX() and fish1.getP1().getY() <= mouse.getY() <= fish1.getP2().getY() and fish1exp == 0:
                fish1exp += 1
                experience_collected = True
            elif fish2.getP1().getX() <= mouse.getX() <= fish2.getP2().getX() and fish2.getP1().getY() <= mouse.getY() <= fish2.getP2().getY() and fish2exp == 0:
                fish2exp += 1
            elif fish3.getP1().getX() <= mouse.getX() <= fish3.getP2().getX() and fish3.getP1().getY() <= mouse.getY() <= fish3.getP2().getY() and fish3exp == 0:
                fish3exp += 1
            elif fish4.getP1().getX() <= mouse.getX() <= fish4.getP2().getX() and fish4.getP1().getY() <= mouse.getY() <= fish4.getP2().getY() and fish4exp == 0:
                fish4exp += 1
            elif fish5.getP1().getX() <= mouse.getX() <= fish5.getP2().getX() and fish5.getP1().getY() <= mouse.getY() <= fish5.getP2().getY() and fish5exp == 0:
                fish5exp += 1
                experience_collected = True
            if experience_collected == True:
                tempexp += 1
                expget.draw(win)
                update()
                time.sleep(1)
                expget.undraw()
                update()

        if key == 'Escape':
            paused = pause()
            if paused == 1:
                for i in catlist + oceanlist + [storytext, shark, paktc]:
                    i.undraw()
                update()
                return 0
            elif paused == 3:
                for i in catlist + oceanlist + [storytext, shark, paktc]:
                    i.undraw()
                update()
                return 4

        if tick % 40 == 0:
            kelptick *= -1
        for i in movingkelplist:
            i.move(0.25 * kelptick, 0)
        for i in topmovingkelplist:
            i.move(0.1 * kelptick, 0)
        for i in catlist:
            i.undraw()
            i.move(0, 0.25 * kelptick)
            i.draw(win)
        update()
        for i in fish:
            i.move(2, 0)
            if i.getP1().getX() >= x:
                i.move(-x - 40, 0)

        shark.undraw()
        shark.move(2, 0)
        shark.draw(win)
        storytext.undraw()
        storytext.draw(win)
        time.sleep(1/60)
        update()
        tick += 1

    for i in catlist:
        i.move(20, 0)

    # shark escape, no checking for stuff here because things are moving quickly
    tick = 0
    swimtick = 0
    shark.undraw()
    for i in oceanlist:
        i.undraw()
    sand.draw(win)
    while tick != 120:
        key = win.checkKey()
        if key == 'Escape':
            paused = pause()
            if paused == 1:
                for i in catlist + oceanlist + [storytext, paktc]:
                    i.undraw()
                update()
                return 0
            elif paused == 3:
                for i in catlist + oceanlist + [storytext, paktc]:
                    i.undraw()
                update()
                return 4

        for i in kelplist:
            i.move(-40, 0)
            if i.getP2().getX() <= 0:
                i.move(x + 20, 0)
            i.undraw()
            i.draw(win)

        for i in catlist:
            i.undraw()
            i.draw(win)
        if swimtick == 3:
            for i in externalmovelist[:4]:
                i.move(0, -5)
        elif swimtick == 2:
            for i in externalmovelist[:4]:
                i.move(5, 0)
        elif swimtick == 1:
            for i in externalmovelist[:4]:
                i.move(0, 5)
        elif swimtick == 0:
            for i in externalmovelist[:4]:
                i.move(-5, 0)

        if swimtick == 3:
            swimtick = 0
        else:
            swimtick += 1
        storytext.undraw()
        storytext.draw(win)
        time.sleep(1/60)
        update()
        tick += 1

    # floatingly continue to next scene
    paktc.draw(win)
    storytext.setText(storytext4)
    for i in rainbow:
        i.draw(win)
    sand.undraw()
    sand.draw(win)
    for i in kelplist:
        i.undraw()
        i.draw(win)
    tick = 0
    while True:
        key = win.checkKey()
        if key != '' and key != 'Escape':
            for a in range(-30, 30, 1):
                for i in catlist:
                    i.move(20, a)
                    i.undraw()
                    i.draw(win)
                update()
                time.sleep(1/60)
            break
        mouse = win.checkMouse()
        if mouse != None:
            experience_collected = False
            if kelp1[1].getP1().getX() <= mouse.getX() <= kelp1[1].getP2().getX() and kelp1[1].getP1().getY() <= mouse.getY() <= kelp1[1].getP2().getY() and kelp1exp == 0:
                kelp1exp += 1
                experience_collected = True
            if kelp2[1].getP1().getX() <= mouse.getX() <= kelp2[1].getP2().getX() and kelp2[1].getP1().getY() <= mouse.getY() <= kelp2[1].getP2().getY() and kelp2exp == 0:
                kelp2exp += 1
                experience_collected = True
            if kelp3[1].getP1().getX() <= mouse.getX() <= kelp3[1].getP2().getX() and kelp3[1].getP1().getY() <= mouse.getY() <= kelp3[1].getP2().getY() and kelp3exp == 0:
                kelp3exp += 1
                experience_collected = True
            if experience_collected == True:
                tempexp += 1
                expget.draw(win)
                update()
                time.sleep(1)
                expget.undraw()
                update()

        if key == 'Escape':
            paused = pause()
            if paused == 1:
                for i in catlist + oceanlist + rainbow + [storytext, paktc]:
                    i.undraw()
                update()
                return 0
            elif paused == 3:
                for i in catlist + oceanlist + rainbow + [storytext, paktc]:
                    i.undraw()
                update()
                return 4

        if tick % 40 == 0:
            kelptick *= -1
        for i in movingkelplist:
            i.move(0.25 * kelptick, 0)
        for i in topmovingkelplist:
            i.move(0.1 * kelptick, 0)
        for i in catlist:
            i.undraw()
            i.move(0, 0.25 * kelptick)
            i.draw(win)
        update()
        time.sleep(1/60)
        update()
        tick += 1

    # move on to next scene
    for i in catlist + oceanlist + rainbow + [paktc, storytext]:
        i.undraw()
    update()
    exp += tempexp
    return 5

def sky():
    global exp

    #the clouds
    cloud1_part1 = Circle(Point(188, 111),50)
    cloud1_part1.setOutline("white")
    cloud1_part1.setFill("white")

    cloud1_part2 = Circle(Point(249, 133),35)
    cloud1_part2.setOutline("white")
    cloud1_part2.setFill("white")

    cloud1_part3 = Oval (Point(88, 131),Point(306, 174))
    cloud1_part3.setOutline("white")
    cloud1_part3.setFill("white")

    cloud1 = [cloud1_part1, cloud1_part2, cloud1_part3]

    cloud2_part1 = Circle(Point(554, 342),60)
    cloud2_part1.setOutline("white")
    cloud2_part1.setFill("white")

    cloud2_part2 = Circle(Point(473, 367),48)
    cloud2_part2.setOutline("white")
    cloud2_part2.setFill("white")

    cloud2_part3 = Oval (Point(385, 369),Point(621, 422))
    cloud2_part3.setOutline("white")
    cloud2_part3.setFill("white")

    cloud2 = [cloud2_part1, cloud2_part2, cloud2_part3]

    clouds = cloud1 + cloud2

    p1_x = 650
    p1_y = 50
    p2_x = 0
    p2_y = 500
    w = 25

    red_stripe = Line (Point(p1_x, p1_y),Point(p2_x, p2_y))
    red_stripe.setWidth(w)
    red_stripe.setOutline('red')

    orange_stripe = Line (Point(p1_x +25, p1_y),Point(p2_x+25, p2_y))
    orange_stripe.setWidth(w)
    orange_stripe.setOutline('orange')

    yellow_stripe = Line (Point(p1_x +50, p1_y),Point(p2_x+50, p2_y))
    yellow_stripe.setWidth(w)
    yellow_stripe.setOutline('yellow')

    green_stripe = Line (Point(p1_x +75, p1_y),Point(p2_x+75, p2_y))
    green_stripe.setWidth(w)
    green_stripe.setOutline('lightgreen')

    blue_stripe = Line (Point(p1_x +100, p1_y),Point(p2_x+100, p2_y))
    blue_stripe.setWidth(w)
    blue_stripe.setOutline('blue')

    indigo_stripe = Line (Point(p1_x +125, p1_y),Point(p2_x+125, p2_y))
    indigo_stripe.setWidth(w)
    indigo_stripe.setOutline('darkblue')

    violet_stripe = Line (Point(p1_x +150, p1_y),Point(p2_x+150, p2_y))
    violet_stripe.setWidth(w)
    violet_stripe.setOutline('purple')

    rainbow = [red_stripe, orange_stripe, yellow_stripe, green_stripe, blue_stripe, indigo_stripe, violet_stripe]

    storytext = Text(Point(x / 2, y * 1 / 5), 'Climbing up the rainbow, the cat reached the sky and looked around.')
    storytext.setFill('black')
    storytext.setStyle('bold')
    storytext.setSize(14)

    storytext2 = 'It was very comfortable up there, with the clouds moving, \nplenty of space, and lots of wind.'
    storytext3 = 'At least, until the cat looked down. It was so high up! \n The rainbow began to fade away.'
    storytextgood = 'Having seen the wonders of the world, the cat was determined to \nexplore and jumped upward, fueled by the power of the rainbow.'
    storytextbad = 'Scared about what would happen, the cat quickly jumped off the rainbow.'

    skylist = clouds + rainbow

    win.setBackground('lightblue')
    for i in skylist:
        i.draw(win)

    storytext.draw(win)
    for i in catlist:
        i.move(-x / 2 + 50, y / 8)

    # Move cat in
    for b in range(3):
        for a in range(-10, 5, 1):
            for i in clouds:
                i.move(-1, 0)
                if i.getP2().getX() <= 0:
                    i.move(x, 0)
            key = win.checkKey()
            if key == 'Escape':
                paused = pause()
                if paused == 1:
                    for i in catlist + skylist + [storytext]:
                        i.undraw()
                    update()
                    return 0
                elif paused == 3:
                    for i in catlist + skylist + [storytext]:
                        i.undraw()
                    update()
                    return 5
            for i in catlist:
                i.move(5, a)
                i.undraw()
                i.draw(win)
            time.sleep(1/60)
            update()

    # Look around
    tick = 0
    centre = (ptbgcircle1.getCenter().getX() + ptbgcircle4.getCenter().getX()) / 2
    for p in range(60):
        key = win.checkKey()
        if tick % 15 == 0:
            catflip(centre)
        for i in clouds:
            i.move(-1, 0)
            if i.getP2().getX() <= 0:
                i.move(x, 0)
        if key == 'Escape':
            paused = pause()
            if paused == 1:
                for i in catlist + skylist + [storytext]:
                    i.undraw()
                update()
                return 0
            elif paused == 3:
                for i in catlist + skylist + [storytext]:
                    i.undraw()
                update()
                return 5
        time.sleep(1/60)
        tick += 1
        update()
    paktc.draw(win)
    update()

    # Story
    while True:
        for i in clouds:
            i.move(-1, 0)
            if i.getP2().getX() <= 0:
                i.move(x, 0)
        key = win.checkKey()
        if key == 'Escape':
            paused = pause()
            if paused == 1:
                for i in catlist + skylist + [storytext, paktc]:
                    i.undraw()
                update()
                return 0
            elif paused == 3:
                for i in catlist + skylist + [storytext, paktc]:
                    i.undraw()
                update()
                return 5
        elif key != '':
            if storytext.getText() == storytext2:
                storytext.setText(storytext3)
                for i in [mouthsmilecover, mouth, mouthtip, nose]:
                    i.undraw()
                for i in eyelist[1], eyelist[3]:
                    i.move(6, 10)
            elif storytext.getText() == storytext3:
                paktc.undraw()
                update()
                if exp <= 4:
                    storytext.setText(storytextbad)
                    for p in range(-10, 50, 1):
                        for i in clouds:
                            i.move(-1, 0)
                            if i.getP2().getX() <= 0:
                                i.move(x, 0)
                        for i in catlist:
                            i.move(5, p)
                        update()
                        time.sleep(1/60)
                    break
                else:
                    storytext.setText(storytextgood)
                    for p in range(-30, 0, 1):
                        for i in clouds:
                            i.move(-1, 0)
                            if i.getP2().getX() <= 0:
                                i.move(x, 0)
                        for i in catlist:
                            i.move(1, p)
                        update()
                        time.sleep(1/60)
                    break
            else:
                storytext.setText(storytext2)
        time.sleep(1/60)

    # Move on
    paktc.draw(win)
    update()
    while True:
        for i in clouds:
            i.move(-1, 0)
            if i.getP2().getX() <= 0:
                i.move(x, 0)
        key = win.checkKey()
        if key != '':
            if key != 'Escape':
                for i in skylist + catlist + [paktc, storytext]:
                    i.undraw()
                    update()
                return 6
            else:
                paused = pause()
                if paused == 1:
                    for i in skylist + catlist + [paktc, storytext]:
                        i.undraw()
                    update()
                    return 0
                elif paused == 3:
                    for i in skylist + catlist + [paktc, storytext]:
                        i.undraw()
                    update()
                    return 5
        time.sleep(1/60)

def endcave():
    cavewall = color_rgb(68, 67, 66)
    cavefloor = color_rgb(38, 37, 37)
    caverock = color_rgb(25, 23, 22)

    win.setBackground(cavewall)

    #floor
    cave_floor = Rectangle (Point (0,360), Point(640, 480))
    cave_floor.setFill(cavefloor)
    cave_floor.setOutline(cavefloor)

    #--------------------
    #Rock1
    x1 = 260
    y1 = 400

    cave_rock1 = Polygon(Point(x1, y1), Point(x1 / 1.1, y1 / 1.05),
                         Point(x1 / 1.1, y1 / 1.11), Point(x1 / 1.23, y1 / 1.17),
                         Point(x1 / 1.61, y1 / 1.11), Point(x1 / 1.9, y1))
    cave_rock1.setFill(caverock)
    cave_rock1.setOutline(caverock)


    #rock 2
    x2 = 619
    y2 = 375

    cave_rock2 = Polygon(Point(x2, y2), Point(x2 / 1.3, y2),
                         Point(x2 / 1.23, y2 / 1.2), Point(x2 / 1.12, y2 / 1.24),
                         Point(x2 / 1.05, y2 / 1.37), Point(x2 / 1.008, y2 / 1.15))
    cave_rock2.setFill(caverock)
    cave_rock2.setOutline(caverock)



    #--------------------
    #Cave roof
    #roof1
    x = 13
    y = 168

    roof_rock1 = Polygon(Point(0, 168.0), Point(32.0, 129.0),
                         Point(91.0, 126.0), Point(136.0, 60.0),
                         Point(206.0, 0), Point(0, 0))
    roof_rock1.setFill(caverock)
    roof_rock1.setOutline(caverock)


    #roof2
    roof_rock2 = Polygon(Point(513.0, 0), Point(542.0, 27.0),
                         Point(572.0, 56.0), Point(611.0, 63.0),
                         Point(640.0, 130.0), Point(640.0, 0))
    roof_rock2.setFill(caverock)
    roof_rock2.setOutline(caverock)

    cave = [cave_floor, cave_rock1, cave_rock2, roof_rock1, roof_rock2]

    # Workaround Mehra's code
    x = 640
    y = 480

    # Story bad ending
    storytext = Text(Point(x / 2, y * 2 / 5), 'The cat fell to the ground, and landed in his cave. Uninterested \n in the world around him, the cat stayed in his cave, forever.')
    storytext.setStyle('bold')
    storytext.setSize(14)
    storytext.setFill('white')

    # button to exit
    exitbutton = Rectangle(Point(x * 1 / 12, y * 7 / 8), Point(x * 5 / 12, y))
    exitbutton.setFill('red')
    exitbutton.setWidth(0)

    exittext = Text(Point(x / 4, (exitbutton.getP1().getY() + exitbutton.getP2().getY()) / 2), 'Exit')
    exittext.setFill('white')
    exittext.setSize(18)
    exittext.setStyle('bold')

    # button to play again
    restartbutton = Rectangle(Point(x * 7 / 12, y * 7 / 8), Point(x * 11 / 12, y))
    restartbutton.setFill('orange')
    restartbutton.setWidth(0)

    restarttext = Text(Point(x * 3 / 4, (restartbutton.getP1().getY() + restartbutton.getP2().getY()) / 2), 'Try again')
    restarttext.setFill('white')
    restarttext.setSize(18)
    restarttext.setStyle('bold')

    theend = Text(Point(x / 2, y * 3 / 10), 'The End')
    theend.setSize(32)
    theend.setFill('white')
    theend.setStyle('bold')

    helptext = Text(Point(x / 2, y * 4 / 10), 'Interact with the environment to gain Exploration Points!')
    helptext.setFill('white')
    helptext.setStyle('bold')
    helptext.setSize(14)

    endlist = [exitbutton, exittext, restartbutton, restarttext, theend, helptext]

    for i in cave:
        i.draw(win)
    update()

    # falling from sky
    for i in catlist + squintlist:
        i.move(0, -400)
        i.draw(win)
    storytext.draw(win)

    for i in range(0, 30):
        key = win.checkKey()
        if key == 'Escape':
            paused = pause()
            if paused == 1:
                for a in catlist + squintlist + cave + [storytext]:
                    a.undraw()
                update()
                return 0
            elif paused == 3:
                for a in catlist + squintlist + cave + [storytext]:
                    a.undraw()
                update()
                return 6
        for a in catlist + squintlist:
            a.move(0, i)
            a.undraw()
            a.draw(win)
        storytext.undraw()
        storytext.draw(win)
        for i in eyelist:
            i.undraw()
        time.sleep(1/60)
        update()

    # cat closes eyes after bouncing twice
    for i in range(-10, 11):
        if key == 'Escape':
            paused = pause()
            if paused == 1:
                for a in catlist + squintlist + cave + [storytext]:
                    a.undraw()
                update()
                return 0
            elif paused == 3:
                for a in catlist + squintlist + cave + [storytext]:
                    a.undraw()
                update()
                return 6
        for a in catlist + squintlist:
            a.move(1, i)
            a.undraw()
            a.draw(win)
        for i in eyelist:
            i.undraw()
        time.sleep(1/60)
        update()

    for i in squintlist:
        i.undraw()
    # bounce again
    for i in range(-5, 6):
        if key == 'Escape':
            paused = pause()
            if paused == 1:
                for a in catlist + squintlist + cave + [storytext]:
                    a.undraw()
                update()
                return 0
            elif paused == 3:
                for a in catlist + squintlist + cave + [storytext]:
                    a.undraw()
                update()
                return 6
        for a in catlist:
            a.move(1, i)
            a.undraw()
            a.draw(win)
        time.sleep(1/60)
        update()

    # press any key to continue
    paktc.draw(win)
    key = win.getKey()
    if key == 'Escape':
        paused = pause()
        if paused == 1:
            for a in catlist + cave + [storytext, paktc]:
                a.undraw()
            update()
            return 0
        elif paused == 3:
            for a in catlist + cave + [storytext, paktc]:
                a.undraw()
            update()
            return 6

    for i in [paktc, storytext]:
        i.undraw()

    for i in endlist:
        i.draw(win)
    update()

    # exit or try again
    while True:
        mouse = win.getMouse()
        if mouse != None:
            if exitbutton.getP1().getX() <= mouse.getX() <= exitbutton.getP2().getX() and exitbutton.getP1().getY() <= mouse.getY() <= exitbutton.getP2().getY():
                exit()
            elif restartbutton.getP1().getX() <= mouse.getX() <= restartbutton.getP2().getX() and restartbutton.getP1().getY() <= mouse.getY() <= restartbutton.getP2().getY():
                for i in starlist + rainbowlist + catlist + endlist + taillist2 + cave:
                    i.undraw()
                update()
                return 0

def space():
    # setup scene
    win.setBackground(color_rgb(41, 42, 121))

    # Final text
    storytext = Text(Point(x / 2, y * 2 / 5), 'The cat arrived in space, where it lived happily ever after.')
    storytext.setFill('white')
    storytext.setSize(14)
    storytext.setStyle('bold')

    # button to exit
    exitbutton = Rectangle(Point(x * 1 / 12, y * 7 / 8), Point(x * 5 / 12, y))
    exitbutton.setFill('red')
    exitbutton.setWidth(0)

    exittext = Text(Point(x / 4, (exitbutton.getP1().getY() + exitbutton.getP2().getY()) / 2), 'Exit')
    exittext.setFill('white')
    exittext.setSize(18)
    exittext.setStyle('bold')

    # button to play again
    restartbutton = Rectangle(Point(x * 7 / 12, y * 7 / 8), Point(x * 11 / 12, y))
    restartbutton.setFill('green')
    restartbutton.setWidth(0)

    restarttext = Text(Point(x * 3 / 4, (restartbutton.getP1().getY() + restartbutton.getP2().getY()) / 2), 'Restart')
    restarttext.setFill('white')
    restarttext.setSize(18)
    restarttext.setStyle('bold')

    theend = Text(Point(x / 2, y * 3 / 10), 'The End')
    theend.setSize(32)
    theend.setFill('white')
    theend.setStyle('bold')

    endlist = [exitbutton, exittext, restartbutton, restarttext, theend]

    for i in catlist + rainbowlist + taillist2:
        i.move(-650, 0)

    # porting code from picture project to work properly since I don't want to have five functions to move a cat
    tick = 0
    cattick = 0
    for i in rainbowlist:
        i.draw(win)
    storytext.draw(win)

    while tick != 130:
        # pausing
        key = win.checkKey()
        if key == 'Escape':
            paused = pause()
            if paused == 1:
                for i in starlist + rainbowlist + catlist + taillist2 + [storytext]:
                    i.undraw()
                return 0
            elif paused == 3:
                for i in starlist + rainbowlist + catlist + taillist2 + [storytext]:
                    i.undraw()
                return 6
        # move in from left
        for i in taillist2 + catlist + rainbowlist:
            i.move(5, 0)
        # wiggle rainbow
        if cattick == 6:
            for i in rainbowlist:
                i.move(50, 0)
            for i in taillist2:
                i.undraw()
                i.draw(win)
        elif cattick == 12:
            for i in rainbowlist:
                i.move(-50, 0)
            for i in taillist2:
                i.undraw()

        # move legs/head
        if 1 <= cattick <= 3:
            for i in externalmovelist:
                i.move(0, -2)
        elif 4 <= cattick <= 6:
            for i in externalmovelist:
                i.move(2, 0)
        elif 7 <= cattick <= 9:
            for i in externalmovelist:
                i.move(0, 2)
        elif 10 <= cattick <= 12:
            for i in externalmovelist:
                i.move(-2, 0)

        # move stars
        for i in starlist:
            i.move(-15, 0)
            if i.getPoints()[2].getX() <= 0 or i.getPoints()[1].getX() <= 0:
                i.move(x, 0)

        # refresh
        for i in catlist + starlist:
            i.undraw()
            i.draw(win)

        # use second tail instead of recalculating each time
        if 6 <= cattick <= 11:
            for i in taillist:
                i.undraw()
        update()
        time.sleep(1/60)
        if cattick == 12:
            cattick = 0
        else:
            cattick += 1
        tick += 1

    tick = 0
    cattick = 0
    endprompt = 0
    paktc.draw(win)
    # the end (good ending)
    while True: # bulk of this is to handle moving cat while allowing user to click things
        key = win.checkKey()
        mouse = win.checkMouse()
        if key != '':
            if key == 'Escape':
                paused = pause()
                if paused == 1:
                    for i in starlist + rainbowlist + catlist + taillist2 + [paktc]:
                        i.undraw()
                    return 0
                elif paused == 3:
                    for i in starlist + rainbowlist + catlist + taillist2 + [paktc]:
                        i.undraw()
                    return 6
            elif endprompt == 0:
                storytext.undraw()
                for i in endlist:
                    i.draw(win)
                paktc.undraw()
                endprompt = 1
        if cattick == 6:
            for i in rainbowlist:
                i.move(50, 0)
            for i in taillist2:
                i.undraw()
                i.draw(win)
        elif cattick == 12:
            for i in rainbowlist:
                i.move(-50, 0)
            for i in taillist2:
                i.undraw()
        # check for exit/restart
        if mouse != None and endprompt == 1:
            if exitbutton.getP1().getX() <= mouse.getX() <= exitbutton.getP2().getX() and exitbutton.getP1().getY() <= mouse.getY() <= exitbutton.getP2().getY():
                exit()
            elif restartbutton.getP1().getX() <= mouse.getX() <= restartbutton.getP2().getX() and restartbutton.getP1().getY() <= mouse.getY() <= restartbutton.getP2().getY():
                for i in starlist + rainbowlist + catlist + endlist + taillist2:
                    i.undraw()
                update()
                return 0

        if 1 <= cattick <= 3:
            for i in externalmovelist:
                i.move(0, -2)
        elif 4 <= cattick <= 6:
            for i in externalmovelist:
                i.move(2, 0)
        elif 7 <= cattick <= 9:
            for i in externalmovelist:
                i.move(0, 2)
        elif 10 <= cattick <= 12:
            for i in externalmovelist:
                i.move(-2, 0)

        for i in starlist:
            i.move(-15, 0)
            if i.getPoints()[2].getX() <= 0 or i.getPoints()[1].getX() <= 0:
                i.move(x, 0)

        if endprompt == 0:
            for i in catlist + starlist + [paktc]:
                i.undraw()
                i.draw(win)
        else:
            for i in catlist + starlist + endlist:
                i.undraw()
                i.draw(win)

        if 6 <= cattick <= 11:
            for i in taillist:
                i.undraw()
        update()
        time.sleep(1/60)
        if cattick == 12:
            cattick = 0
        else:
            cattick += 1
        tick += 1

# initialise for main loop
transition = 0
exp = 0

# main loop
while True:
    # reset elements
    setcat()
    update()
    # select scenes based on things
    if transition == 0:
        exploration = 0
        transition = cover()
    elif transition == 1:
        transition = backstory()
    elif transition == 2:
        transition = desert()
    elif transition == 3:
        transition = forest()
    elif transition == 4:
        transition = ocean()
    elif transition == 5:
        transition = sky()
    elif transition == 6:
        if exp <= 4:
            transition = endcave()
        else:
            transition = space()