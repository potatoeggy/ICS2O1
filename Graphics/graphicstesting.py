from graphics import *
from math import *

x = 640
y = 480
win = GraphWin('sinewave testing', x, y, autoflush = False)
win.setBackground('black')

amp = 10 # lower is less of a wave
freq = 30 # lower is less waves
offsetx = 0 # moves it left or right the canvas
offsety = -50 # moves it up or down the canvas

for p in ['red', 'orange', 'yellow', 'lime', 'royal blue', 'blueviolet']:
    for i in range(15):
        offsety += 1
        for a in range(240): # range is the x value you want it to go to
            update()
            equation = y / 2 + (amp * sin((a - offsetx) / freq) + offsety)
            win.plot(a, equation, color = p)

