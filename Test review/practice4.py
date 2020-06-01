# Daniel Chen
# 17 May 2019
# DVD
from graphics import *
from random import randint

# Adjust settings
x = 1280
y = 720
radius = 40
balls = 5 # Generally it starts lagging after ~20, but adjusting speed may help accomodate for it
speed = balls * 200 # Adjust as necessary, speeds up because lag
epilepsy = False
less_epilepsy = True # epilepsy needs to be on for this to work
random_bouncing = True
wobble = 0 # Wobbliness. 1-10 is cool
# End adjust settings

win = GraphWin('DVDs', x, y, autoflush=False)
win.setBackground('black')

# lists for multiball support
dvds = []
mx = []
my = []

for i in range(balls):
    # for each number in range(balls) make a new entry in the lists above and assign them mostly random values
    dvds.append(i)
    mx.append(i)
    my.append(i)
    # if lists are confusing ignore the above and pretend var[i] is like assigning var0, var1, var2, var3 the following values
    dvds[i] = Circle(Point(randint(radius, x - radius), randint(radius, y - radius)), radius)
    dvds[i].setFill(color_rgb(randint(0, 255), randint(0, 255), randint(0, 255)))
    dvds[i].setWidth(0)
    dvds[i].draw(win)
    mx[i] = 5
    my[i] = 2

while True:
    for i in range(balls):
        dvds[i].move(mx[i] + randint(-wobble, wobble), my[i] + randint(-wobble, wobble))
        dvds[i].undraw()
        dvds[i].draw(win)
        centerx = dvds[i].getCenter().getX()
        centery = dvds[i].getCenter().getY()

# Calculate collision in X
        # if left/right edge of ball is outside of canvas
        if centerx - radius <= 0 or centerx + radius >= x:
            if centerx - radius < 0:
                # move it so that it is inside the canvas + 5
                dvds[i].move(0 - (centerx - radius) + 5, 0)
            elif centerx + radius > x:
                dvds[i].move(x - (centerx + radius) - 5, 0)
            # change direction
            mx[i] *= -1
            dvds[i].setFill(color_rgb(randint(0, 255), randint(0, 255), randint(0, 255)))

# Bonus feature random bouncing in X
            if random_bouncing == True:
                # randomly decide whether to increase/decrease speed up to a max of 8px/s, and if not moving, reset to default
                if mx[i] < -8:
                    mx[i] += 1
                elif mx[i] > 8:
                    mx[i] -= 1
                else:
                    mx[i] += randint(-1, 1)
                if mx[i] == 0:
                    mx[i] = 5

# Bonus feature epilepsy in X
            if epilepsy == True:
                win.setBackground(color_rgb(randint(0, 255), randint(0, 255), randint(0, 255)))
                if less_epilepsy != True:
                    speed += 10

# Calculate collision in Y
        if centery - radius <= 0 or centery + radius >= y:
            if centery - radius < 0:
                dvds[i].move(0, 0 - (centery - radius) + 5)
            elif centery + radius > y:
                dvds[i].move(0, y - (centery + radius) - 5)
            my[i] *= -1
            dvds[i].setFill(color_rgb(randint(0, 255), randint(0, 255), randint(0, 255)))

# Bonus feature random bouncing in Y
            if random_bouncing == True:
                if my[i] < -5:
                    my[i] += 1
                elif my[i] > 5:
                    my[i] -= 1
                else:
                    my[i] += randint(-1, 1)
                if my[i] == 0:
                    my[i] = 2

# Bonus feature epilepsy in Y
            if epilepsy == True:
                win.setBackground(color_rgb(randint(0, 255), randint(0, 255), randint(0, 255)))
                if less_epilepsy != True:
                    speed += 10
        update(speed)