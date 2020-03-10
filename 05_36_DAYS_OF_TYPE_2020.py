o = 0
w = 1080
h = 1080
hw = w/2
hh = h/2
divs = int(24*4)
minRan = 100
maxRan = 1000
scRan = 0.01
r, g, b = 255/255, 255/255, 255/255
ranMov = 50

#Functions      
def drawStraight(step, thickness):
    reps = step + 1
    stroke(r, g, b)
    fill(None)
    lineCap("round")
    lineDash(thickness, thickness, thickness, thickness)
    path = BezierPath()
    for i in range(step):
        strokeWidth(thickness)
        path.moveTo((o + (thickness * 3 * reps) + randint(-ranMov, ranMov), o + randint(-ranMov, ranMov)))
        path.lineTo((o + (thickness * 3 * reps ) + randint(-ranMov, ranMov), h + randint(-ranMov, ranMov)))
        drawPath(path)
        reps -= 1

# Create pages/frames
deg = 0
for i in range(divs):   
    newPage(w, h)
    fill(0)
    stroke(None)
    rect(o, o, w, h)
    with savedState():
        scale(0.25/2)
        #Stem
        for j in range(6):    
            with savedState():
                r, g, b = randint(200, 255)/255, randint(200, 255)/255, randint(0, 10)/255
                translate(w * 2, h * (j + 1))
                rotate(deg, (hw, hh))
                drawStraight(i, (randint(-ranMov, ranMov) * scRan))
        for j in range(4):    
            if j == 2:
                continue
            with savedState():
                r, g, b = randint(200, 255)/255, randint(200, 255)/255, randint(0, 10)/255
                translate(w * 2, h * (j + 2))
                rotate(deg + 180, (hw, hh))
                drawStraight(i, (randint(-ranMov, ranMov) * scRan))
        #Arm1
        for j in range(4):    
            with savedState():
                r, g, b = randint(200, 255)/255, randint(200, 255)/255, randint(0, 10)/255
                translate(w * (j + 2), h * 6)
                rotate(deg - 90, (hw, hh))
                drawStraight(i, (randint(-ranMov, ranMov) * scRan))
        for j in range(3):    
            with savedState():
                r, g, b = randint(200, 255)/255, randint(200, 255)/255, randint(0, 10)/255
                translate(w * (j + 3), h * 6)
                rotate(deg + 90, (hw, hh))
                drawStraight(i, (randint(-ranMov, ranMov) * scRan))
        with savedState():
            translate(w * 5, h * 6)
            rotate(deg + 180, (hw, hh))
            drawStraight(i, (randint(-ranMov, ranMov) * scRan))
        #Arm2
        for j in range(2):    
            with savedState():
                r, g, b = randint(200, 255)/255, randint(200, 255)/255, randint(0, 10)/255
                translate(w * (j + 3), h * 4)
                rotate(deg - 90, (hw, hh))
                drawStraight(i, (randint(-ranMov, ranMov) * scRan))
        for j in range(2):    
            with savedState():
                r, g, b = randint(200, 255)/255, randint(200, 255)/255, randint(0, 10)/255
                translate(w * (j + 3), h * 4)
                rotate(deg + 90, (hw, hh))
                drawStraight(i, (randint(-ranMov, ranMov) * scRan))
        with savedState():
            r, g, b = randint(200, 255)/255, randint(200, 255)/255, randint(0, 10)/255
            translate(w * 4, h * 4)
            rotate(deg + 180, (hw, hh))
            drawStraight(i, (randint(-ranMov, ranMov) * scRan))
        #Arm3
        for j in range(3):    
            with savedState():
                r, g, b = randint(200, 255)/255, randint(200, 255)/255, randint(0, 10)/255
                translate(w * (j + 3), h * 1)
                rotate(deg - 90, (hw, hh))
                drawStraight(i, (randint(-ranMov, ranMov) * scRan))
        for j in range(4):    
            with savedState():
                r, g, b = randint(200, 255)/255, randint(200, 255)/255, randint(0, 10)/255
                translate(w * (j + 2), h * 1)
                rotate(deg + 90, (hw, hh))
                drawStraight(i, (randint(-ranMov, ranMov) * scRan))
        with savedState():
            r, g, b = randint(200, 255)/255, randint(200, 255)/255, randint(0, 10)/255
            translate(w * 5, h * 1)
            rotate(deg + 180, (hw, hh))
            drawStraight(i, (randint(-ranMov, ranMov) * scRan))
    
    deg += randint(int(360 / divs * -1), int(360 / divs)) * 0.2
    print(i)

# save animation
saveImage('~/Desktop/05_36_DAYS_OF_TYPE_2020.mp4')
print('done')