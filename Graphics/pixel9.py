# Daniel Chen
# 7 April 2019
# Draw the five Olympic rings

from graphics import *

x = 1280
y = 720

# They're scalable too! Replace x and y with any common 16:9 resolution (1280 x 720, 1920 x 1080, etc), but it gets less accurate as scaled. I don't want to fix that.

win = GraphWin('Olympics', x, y)
win.setBackground('white')

black = Circle(Point(x / 2, y / 3), x / 8)
black.setOutline('black')
black.setWidth((x + y) / 70)

blue = black.clone()
blue.move(-x * 7 / 24, 0)
blue.setOutline(color_rgb(62, 118, 236))

red = black.clone()
red.move(x * 7 / 24, 0)
red.setOutline(color_rgb(255, 0, 0))

yellow = black.clone()
yellow.move(-x * 7 / 48, y * 14 / 75)
yellow.setOutline(color_rgb(255, 206, 1))

green = black.clone()
green.move(x * 7 / 48, y * 14 / 75)
green.setOutline(color_rgb(23, 154, 19))

blue.draw(win)
yellow.draw(win)
black.draw(win)
green.draw(win)
red.draw(win)