from graphics import *
from random import randint

whichone = 'special' # original or special

def original():
    # Original code
    x = 1280
    y = 720
    radius = 40
    mx = 5
    my = 2
    win = GraphWin('DVD original', x, y, autoflush = False)
    speed = 120

    dvd = Circle(Point(randint(radius, x - radius), randint(radius, y - radius)), radius)
    dvd.setFill('blue')
    dvd.setWidth(0)
    dvd.draw(win)
    
    while True:
        dvd.move(mx, my)
        dvd.undraw()
        dvd.draw(win)
        if dvd.getCenter().getX() - radius < 0 or dvd.getCenter().getX() + radius > x:
            mx = mx * -1
        elif dvd.getCenter().getY() - radius < 0 or dvd.getCenter().getY() + radius > y:
            my = my * -1
        update(speed)

def special():
    # Adjust settings
    x = 1280
    y = 720
    radius = 40
    balls = 2 # Generally it starts lagging after ~20, but adjusting speed may help accomodate for it
    speed = balls * 100 # Adjust as necessary, speeds up because lag
    epilepsy = True
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
                    speed += 10
            update(speed)

if whichone == 'special':
    special()
elif whichone == 'original':
    original()
else:
    original()