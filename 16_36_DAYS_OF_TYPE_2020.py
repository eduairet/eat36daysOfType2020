import random

side = 1080

def shape(step):
    r, g, b = 255, 255, randint(200 + step, 255)/255
    fill(r, g, b)
    rotate(360/12 * (step + random.choice((-1, 1)) * 0.3), (side/12, side/12))
    shadow((0, 0), 50, (r, g, b))
    oval(0 , 0, side/16, side/16)

for i in range(12):
    newPage(side, side)
    fill(0)
    rect(0, 0, side, side)  
    x = 0
    y = 0
    for j in range(7):
        if j <= 2:
            for k in range(7): 
                with savedState():
                    translate(side/8 + x, side/8 + y)
                    shape(i)
                y += side/10
        if j > 2 and j <= 4:
            for k in range(7):
                if k != 4 and k > 1:
                    with savedState():
                        translate(side/8 + x, side/8 + y)
                        shape(i)
                y += side/10
        if j == 5:
            for k in range(7):
                if k > 1:
                    with savedState():
                        translate(side/8 + x, side/8 + y)
                        shape(i)
                y += side/10
        if j == 6:
            for k in range(7):
                if k > 2 and k < 6:
                    with savedState():
                        translate(side/8 + x, side/8 + y)
                        shape(i)
                y += side/10
        y = 0
        x += side/10
    
saveImage('~/Desktop/16_36_DAYS_OF_TYPE_2020.mp4')