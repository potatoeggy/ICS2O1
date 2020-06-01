# Daniel Chen
# 12 April 2019
# Project Pop-Tart-Cat-Pooping-Rainbows

# import external graphics library
from graphics import *
from math import sin
from random import randint
from playsound import playsound # must install via pip or some other way first
import time

from threading import Thread

# setup canvas
x = 640
y = 480
win = GraphWin('Cat Simulator', x, y, autoflush = False)
win.setBackground(color_rgb(41, 42, 121))

radius = 10
miniradius = radius

def menu():
    global mode
    global title
    global tick
    global cattick
    global mainhelptext
    global mainbuttonlist
    global configbutton
    begin = 0
    title = Text(Point(x / 2, y / 4), 'Cat Simulator')
    title.setFace('helvetica')
    title.setStyle('bold')
    title.setSize(32)
    title.setFill('white')
    
    # Menu buttons
    defaultbutton = Rectangle(Point(0, y * 7 / 8), Point(x / 3, y))
    configbutton = Rectangle(Point(x / 3, y * 7 / 8), Point(x * 2 / 3, y))
    configcodebutton = Rectangle(Point(x * 2 / 3, y * 7 / 8), Point(x, y))
    mainbuttonlist = [defaultbutton, configbutton, configcodebutton]
    for i in mainbuttonlist:
        i.setFill('gray')
        i.setWidth(10)
    
    # Menu text
    defaulttext = Text(defaultbutton.getCenter(), 'Use default cat')
    configtext = Text(configbutton.getCenter(), 'Configure your cat')
    configcodetext = Text(configcodebutton.getCenter(), 'Use config code')
    mainhelptext = Text(Point(configbutton.getCenter().getX(), configbutton.getCenter().getY() - radius * 5), 'Please select an option')
    mainhelptext.setFill('white')
    mainhelptext.setSize(14)
    
    maintextlist = [defaulttext, configtext, configcodetext]
    for i in maintextlist:
        i.setFill('grey5')
    
    # Try to have an idle animation and using checkMouse
    movetail()
    for i in catlist:
        i.draw(win)
    for i in mainbuttonlist + maintextlist + [mainhelptext, title]:
        i.draw(win)
    update()
    
    # Main menu button handling
    mode = 0
    cattick = 0
    tick = 0
    while mode == 0:
        mouse = win.checkMouse()
        if mouse != None:
            if defaultbutton.getP1().getX() <= mouse.getX() <= defaultbutton.getP2().getX() and defaultbutton.getP1().getY() <= mouse.getY() <= defaultbutton.getP2().getY():
                mode = 'default'
            elif configbutton.getP1().getX() <= mouse.getX() <= configbutton.getP2().getX() and configbutton.getP1().getY() <= mouse.getY() <= configbutton.getP2().getY():
                mode = 'config'
            elif configcodebutton.getP1().getX() <= mouse.getX() <= configcodebutton.getP2().getX() and configcodebutton.getP1().getY() <= mouse.getY() <= configcodebutton.getP2().getY():
                mode = 'configcode'
                for i in mainbuttonlist + maintextlist:
                    i.undraw()
        # Begin basic cat code (after initialising cattick and tick)
        for i in catlist:
            i.undraw()
        # add whatever relies on ticks here
        movecat()
        movetail()
        for i in catlist:
            i.draw(win)
        update(120)
        time.sleep(1 / 120)
        tick += 1
        # End basic cat code
    if mode == 'default':
        for i in mainbuttonlist + maintextlist + [mainhelptext, title] + rainbowlist + taillist + leglist + ptbglist + ptlist + ptsprinklelist + headlist + mouthlist + eyelist + otherfeatureslist:
            i.undraw()
        init(mode)
    elif mode == 'config':
        for i in mainbuttonlist + maintextlist:
            i.undraw()
        config(0)
    elif mode == 'configcode':
        configcode()

def config(confirm):
    global cattick
    global tick
    global options
    global mode
    global tailback
    global tailbackcover
    global epilepsy
    ynbutton1 = Rectangle(Point(x * 1 / 5, y * 7 / 8), Point(x * 2 / 5, y))
    ynbutton2 = Rectangle(Point(x * 3 / 5, y * 7 / 8), Point(x * 4 / 5, y))
    yes = Text(ynbutton1.getCenter(), 'Enabled')
    no = Text(ynbutton2.getCenter(), 'Disabled')
    ynbuttonlist = [ynbutton1, ynbutton2]
    ynbutton1.setFill('green')
    ynbutton2.setFill('red')
    for i in ynbuttonlist:
        i.setWidth(6)
        i.draw(win)
    for i in [yes, no]:
        i.draw(win)
    options = ['Stars', 'Rainbow', 'Epilepsy', 'Planets', 'Rocket', 'Kelp', 'Bubbles', 'Ground', 'Starfish']
    # bouncing mode/game mode (avoid obstacles) (only accessible via up up down down left right left right b a enter)
    for option in options:
        mainhelptext.setText(option)
        chosen = 0
        while chosen == 0:
            mouse = win.checkMouse()
            if mouse != None:
                if ynbutton1.getP1().getX() <= mouse.getX() <= ynbutton1.getP2().getX() and ynbutton1.getP1().getY() <= mouse.getY() <= ynbutton1.getP2().getY():
                    confirm = True
                    chosen = 1
                elif ynbutton2.getP1().getX() <= mouse.getX() <= ynbutton2.getP2().getX() and ynbutton2.getP1().getY() <= mouse.getY() <= ynbutton2.getP2().getY():
                    confirm = False
                    chosen = 1
            for i in catlist:
                i.undraw()
            # add whatever relies on ticks here
            movecat()
            movetail()
            for i in catlist:
                i.draw(win)
            update(120)
            time.sleep(1 / 120)
            tick += 1
            # End basic cat code
        options[options.index(option)] = confirm
        if option == 'Starfish':
            for i in catlist:
                i.undraw()
    movecat()
    movetail()
    for i in [title, mainhelptext, yes, no] + ynbuttonlist:
        i.undraw()
    init('config')

def configcode():
    global tick
    global mode
    global cattick
    code = 0
    secret = 0
    secretlist = ['Up', 'Up', 'Down', 'Down', 'Left' ,'Right', 'Left', 'Right', 'b', 'a', 'Return']
    mainhelptext.setText('Please enter your configuration code')
    codebox = Entry(configbutton.getCenter(), 12)
    codebox.setFill(color_rgb(41, 42, 121))
    codebox.setTextColor('white')
    codebox.setSize(24)
    codebox.draw(win)
    while code == 0:
        codecheck = win.checkKey()
        codecheck2 = win.checkMouse()
        if secret != 11:
            if codecheck == secretlist[secret] and codecheck2 == None:
                secret += 1
            elif codecheck == '' and codecheck2 == None:
                pass
            else:
                secret = 0
        elif secret == 11:
            mode = 'baby shark'
            code = 1
        if codecheck == 'Return':
            code = codebox.getText()
            if code == 'default':
                mode = 'default'
            elif code == 'full':
                mode = 'full'
            elif code == 'epilepsy':
                mode = 'epilepsy'
            elif code == 'marine':
                mode = 'marine'
            elif code == 'empty':
                mode = 'empty'
            elif code == 'original':
                mode = 'original'
            elif code == 'truemarine':
                mode = 'truemarine'
            else:
                mainhelptext.setText('Invalid code')
                code = 0
        for i in catlist:
            i.undraw()
        # add whatever relies on ticks here
        movecat()
        movetail()
        for i in catlist:
            i.draw(win)
        update(120)
        time.sleep(1 / 120)
        tick += 1
    for i in [mainhelptext, title, codebox] + catlist:
        i.undraw()
    init(mode)

# Configurable
speed = 5

# Initial defining of everything
# Cat
# Pop Tart
# Background

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

mouthsmilecover1 = mouthsmile.getP1()
mouthsmilecover2 = Point(mouthsmile.getP2().getX( ) + 2, (mouthsmile.getP1().getY() + mouthsmile.getP2().getY()) / 2)
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

tailtip = (Circle(Point(ptbgcircle1.getCenter().getX() - 50, (ptbgcircle1.getCenter().getY() + ptbgcircle3.getCenter().getY()) / 2 + radius * 3), radius))
tailtip.setWidth(6)
tailtip.setFill(color_rgb(166, 166, 166))

tailback3 = Point(ptbgcircle1.getCenter().getX(), tailtip.getCenter().getY() + radius)
tailback4 = Point(ptbgcircle1.getCenter().getX(), tailtip.getCenter().getY() - radius)

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

# Accessories
# Planets
# Jupiter
jupiterbody = Circle(Point(x / 5, y / 3), radius * 5)
jupiterbody.setFill(color_rgb(201, 144, 57))
jupiterbody.setWidth(6)

jupitereye = Oval(Point(jupiterbody.getCenter().getX() + radius, jupiterbody.getCenter().getY() + radius), Point(jupiterbody.getCenter().getX() + radius * 3, jupiterbody.getCenter().getY() + radius * 2))
jupitereye.setFill(color_rgb(204, 51, 0))
jupitereye.setOutline(color_rgb(204, 51, 0))

# Saturn
saturnbody = Circle(Point(x / 2, y * 53 / 54), radius * 5)
saturnbody.setFill(color_rgb(197, 171, 110))
saturnbody.setWidth(6)

saturnring1 = Circle(Point(saturnbody.getP1().getX() - radius, saturnbody.getP2().getY()), radius)

planetlist = [jupiterbody, jupitereye, saturnbody]

# Rocket (not a planet)
rocketcap1 = Point(x * 1 / 3, y / 5)
rocketcap2 = Point(x * 1 / 3 + radius * 2, y / 7 - radius / 2)
rocketcap3 = Point(x * 1 / 3 + radius * 2, y / 4 + radius / 2)
rocketcap = Polygon(rocketcap1, rocketcap2, rocketcap3)
rocketcap.setWidth(6)
rocketcap.setFill('red')

rocketbody = Rectangle(Point(rocketcap2.getX(), rocketcap2.getY()), Point(rocketcap3.getX() + radius * 8, rocketcap3.getY()))
rocketbody.setFill('white')
rocketbody.setWidth(5)

rocketwindow = Circle(rocketbody.getCenter(), radius * 1.5)
rocketwindow.setFill('light blue')
rocketwindow.setWidth(6)

rocketfin1_1 = Point(rocketwindow.getCenter().getX(), rocketbody.getP1().getY())
rocketfin1_2 = Point(rocketbody.getP2().getX(), rocketfin1_1.getY() - radius * 2)
rocketfin1_3 = Point(rocketfin1_2.getX(), rocketfin1_1.getY())
rocketfin1 = Polygon(rocketfin1_1, rocketfin1_2, rocketfin1_3)
rocketfin1.setFill('red')
rocketfin1.setWidth(6)

rocketfin2_1 = Point(rocketwindow.getCenter().getX(), rocketbody.getP2().getY())
rocketfin2_2 = Point(rocketbody.getP2().getX(), rocketfin2_1.getY() + radius * 2)
rocketfin2_3 = Point(rocketfin2_2.getX(), rocketfin2_1.getY())
rocketfin2 = Polygon(rocketfin2_1, rocketfin2_2, rocketfin2_3)
rocketfin2.setFill('red')
rocketfin2.setWidth(6)

rocketfire1 = rocketfin1_3
rocketfire2 = rocketfin2_3
rocketfire3 = Point(rocketfire1.getX() + radius * 3, (rocketfire1.getY() + rocketfire2.getY()) / 2)

rocketfire = Polygon(rocketfire1, rocketfire2, rocketfire3)
rocketfire.setFill('orange')
rocketfire.setWidth(6)

rocketlist = [rocketbody, rocketwindow]
rocketpolygonlist = [rocketcap, rocketfin1, rocketfin2, rocketfire]


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

star1 = starcreator(Point(x / 5, y * 7 / 8), radius * 2)
star2 = starcreator(Point(x * 6 / 7, y * 9 / 10), radius * 3)
star3 = starcreator(Point(x * 9 / 10, y / 4), radius * 2.5)
star4 = starcreator(Point(x * 1 / 16, y / 8), radius * 2)
star5 = starcreator(Point(x * 2 / 3, y / 5), radius * 2.5)
starlist = [star1, star2, star3, star4, star5]

#['Stars', 'Rainbow', 'Epilepsy', 'Planets', 'Rocket', 'Pikachu as head', 'Eyepatch', 'Glasses', 'Kelp', 'Bubbles', 'Seafloor', 'Starfish']
# Marine
starfish = starcreator(Point(x / 8, y * 9 / 10), radius * 2)
starfish.setFill('pink')

seafloor = Rectangle(Point(-10, y * 5 / 6), Point(x + 10, y + 10))
seafloor.setFill(color_rgb(194, 178, 128))
seafloor.setWidth(6)

def bubblecreator(centre, size):
    bubble = Circle(centre, size)
    bubble.setWidth(3)
    bubble.setFill('sky blue')
    minibubble = Circle(Point(bubble.getCenter().getX() - size / 4, bubble.getCenter().getY() - size / 4), size / 4)
    minibubble.setOutline('white')
    minibubble.setFill('white')
    minibubblecover = Circle(Point(minibubble.getCenter().getX() + size / 8, minibubble.getCenter().getY() + size / 8), size / 4)
    minibubblecover.setOutline('sky blue')
    minibubblecover.setFill('sky blue')
    return [bubble, minibubble, minibubblecover]

bubble1 = bubblecreator(Point(ears5.getX() + radius * 2, ears5.getY() - radius * 3), radius * 0.9)
bubble2 = bubblecreator(Point(bubble1[0].getCenter().getX() + radius * 2, bubble1[0].getCenter().getY() - radius * 3), radius)
bubble3 = bubblecreator(Point(bubble2[0].getCenter().getX() - radius * 3, bubble2[0].getCenter().getY() - radius * 3), radius * 1.1)
bubble4 = bubblecreator(Point(bubble3[0].getCenter().getX() + radius * 3, bubble3[0].getCenter().getY() - radius * 4), radius)

bubblelist = bubble1 + bubble2 + bubble3 + bubble4
bubblelistodd = bubble1 + bubble3
bubblelisteven = bubble2 + bubble4

def kelpcreator(locationx, size):
    kelp = Rectangle(Point(locationx, y), Point(locationx + size * 3, y - size * 8))
    kelpcover = Line(Point(kelp.getP1().getX() + 3, kelp.getP1().getY()), Point(kelp.getP2().getX() - 3, kelp.getP1().getY()))
    for i in [kelp, kelpcover]:
        i.setFill('green')
        i.setWidth(6)
    return [kelp, kelpcover]
    
kelp1 = kelpcreator(x / 5, radius)
kelp2 = kelpcreator(x * 6 / 7, radius * 0.9)
kelp3 = kelpcreator(x / 5 - radius * 4, radius * 0.7)
kelp4 = kelpcreator(x * 6 / 7 + radius * 6, radius * 1.2)
kelp5 = kelpcreator(x / 2, radius)
kelp6 = kelpcreator(x / 2 - radius * 6, radius * 1.1)
kelp7 = kelpcreator(x / 3 - radius * 3, radius * 0.8)
kelp8 = kelpcreator(x * 2 / 3, radius * 1.3)
kelp9 = kelpcreator(x * 2 / 3 - radius * 3, radius * 0.8)

kelplist = kelp1 + kelp2 + kelp3 + kelp4 + kelp5 + kelp6 + kelp7 + kelp8 + kelp9

def movecat():
    global cattick
    global tick
    global tailtip
    # Poptart moves updown every full revolution of the head
    # The head moves slightly behind the feet
    tempeverything = leglist + taillist + ptbglist + ptlist + ptsprinklelist + headlist + mouthlist + eyelist + otherfeatureslist
    if cattick == 12:
        # move rainbow
        for i in rainbowlist:
            i.move(-50, 0)
        # move tail
        tailtip.move(0, 20)
        # move bubbles
        for i in bubblelistodd:
            i.move(-radius * 3, 10)
        for i in bubblelisteven:
            i.move(radius * 3, 10)
        # move cat
        for i in tempeverything:
            i.move(0, 10)
    elif cattick == 6:
        # move rainbow
        for i in rainbowlist:
            i.move(50, 0)
        # move tail
        tailtip.move(0, -20)
        # move bubbles
        for i in bubblelistodd:
            i.move(radius * 3, -10)
        for i in bubblelisteven:
            i.move(-radius * 3, -10)
        # move cat
        for i in tempeverything:
            i.move(0, -10)
    if cattick == 12:
        cattick = 0
    else:
        cattick += 1

# Shark
shark = Image(Point(x / 2 - radius * 5, y / 4), 'baby shark.gif')

def movebg():
    global tick
    if tick % 1 == 0:
        for i in planetlist + rocketlist + kelplist:
            i.move(-speed * 3, 0)
            if i.getP2().getX() <= 0:
                i.move(x, 0)
        for i in starlist + rocketpolygonlist + [starfish]:
            i.move(-speed * 3, 0)
            if i.getPoints()[2].getX() <= 0 or i.getPoints()[1].getX() <= 0:
                i.move(x, 0)

def movetail():
    global taillist
    global catlist
    global tailback
    global tailbackcover
    tailback1 = Point(tailtip.getCenter().getX(), tailtip.getCenter().getY() + radius)
    tailback2 = Point(tailtip.getCenter().getX(), tailtip.getCenter().getY() - radius)
    tailback = Polygon(tailback1, tailback2, tailback4, tailback3)
    tailback.setFill(color_rgb(166, 166, 166))
    tailback.setWidth(6)
    tailbackcover = Line(Point(tailback1.getX(), tailback1.getY() - 3), Point(tailback2.getX(), tailback2.getY() + 3))
    tailbackcover.setOutline(color_rgb(166, 166, 166))
    tailbackcover.setWidth(6)
    taillist = [tailtip, tailback, tailbackcover]
    catlist = rainbowlist + taillist + leglist + ptbglist + ptlist + ptsprinklelist + headlist + mouthlist + eyelist + otherfeatureslist

def movelegsface():
    if 1 <= cattick <= 3:
        for i in leglist + headlist + mouthlist + eyelist + otherfeatureslist:
            i.move(0, -2)
    elif 4 <= cattick <= 6:
        for i in leglist + headlist + mouthlist + eyelist + otherfeatureslist:
            i.move(2, 0)
    elif 7 <= cattick <= 9:
        for i in leglist + headlist + mouthlist + eyelist + otherfeatureslist:
            i.move(0, 2)
    elif 10 <= cattick <= 12:
        for i in leglist + headlist + mouthlist + eyelist + otherfeatureslist:
            i.move(-2, 0)

def music(mode):
    if mode != 'baby shark':
        playsound('./Nyan Cat [original].mp3')
    else:
        playsound('./baby shark.mp3')
    music(mode)
    
def init(mode):
    global cat
    global cattick
    global tick
    global everything
    global epilepsy
    global catlist
    
    win.setBackground('black')
    update()
    
    cat = Thread(target=music,args=(mode,))
    cat.start()
    if mode != 'baby shark':
        time.sleep(4)
    else:
        time.sleep(1.75)
    
    win.setBackground(color_rgb(41, 42, 121))
    if mode == 'default' or mode == 'epilepsy':
        everything = rainbowlist + starlist
    elif mode == 'full':
        everything = planetlist + starlist + rocketlist + rocketpolygonlist + [seafloor, starfish] + kelplist + bubblelist + rainbowlist
    elif mode == 'marine' or mode == 'truemarine':
        if mode == 'marine':
            everything = [seafloor, starfish] + kelplist + bubblelist + rainbowlist
        elif mode == 'truemarine':
            everything = [seafloor, starfish] + kelplist + bubblelist
        win.setBackground('royal blue')
        for i in kelplist:
            i.move(0, -y / 16)
    elif mode == 'empty':
        everything = []
    elif mode == 'original':
        everything = rainbowlist
    elif mode == 'config':
        everything = []
        if options[0]:
            everything += starlist
        if options[2]:
            epilepsy = True
        if options[3]:
            everything += planetlist
        if options[4]:
            everything += rocketlist + rocketpolygonlist
        if options[6]:
            everything += bubblelist
        if options[7]:
            everything += [seafloor]
        if options[8]:
            everything += [starfish]
        if options[5]:
            everything += kelplist
            if options[7]:
                for i in kelplist:
                    i.move(0, -y / 16)
        if options[1]:
            everything += rainbowlist
    else:
        everything = [seafloor, starfish] + kelplist + [shark] + bubblelist
        win.setBackground('royal blue')
        for i in [seafloor, starfish] + kelplist + bubblelist:
            i.setWidth(0)
        for i in kelplist:
            i.move(-50, -y / 16)
        starfish.move(90, 10)
        starfish.setOutline('pink')
        for i in bubblelist:
            i.move(radius * 10, -radius * 15)
        tick = 0

epilepsy = False
menu()

bubblex = 1
sharky = 3
sharktick = 0
while cat.is_alive():
    if win.checkKey() == 'Escape':
        exit()
    if mode != 'baby shark':
        for i in everything + catlist[6:]:
            i.undraw()
        if mode == 'epilepsy' or epilepsy:
            for i in everything + catlist[6:]:
                i.setFill(color_rgb(randint(0, 255), randint(0, 255), randint(0, 255)))
                i.setOutline(color_rgb(randint(0, 255), randint(0, 255), randint(0, 255)))
            win.setBackground(color_rgb(randint(0, 255), randint(0, 255), randint(0, 255)))
        # add whatever relies on ticks here
        movecat()
        movetail()
        movelegsface()
        movebg()
        for i in everything + catlist[6:]:
            i.draw(win)
    else:
        for i in everything:
            i.undraw()
        movebg()
        for i in [shark] + bubblelist:
            i.move(0, sharky)
        for i in bubblelistodd:
            i.move(bubblex, 0)
        for i in bubblelisteven:
            i.move(-bubblex, 0)
        for i in everything:
            i.draw(win)
        if sharktick == 24:
            sharktick = 0
            sharky *= -1
            bubblex *= -1
        sharktick += 1
    update(120)
    time.sleep(1/120)
    if mode != 'baby shark':
        tick += 1
    else:
        tick += 0.5