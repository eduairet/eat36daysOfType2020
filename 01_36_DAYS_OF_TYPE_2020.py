o = 0
w = 1080
h = 1080
hw = w/2
hh = h/2
divs = 72
minRan = 1
maxRan = 10
r, g, b = randint(0, 255)/( 255), randint(0, 255)/( 255), randint(0, 255)/( 255)

#Functions      
def drawCurve(step, thickness):
    reps = divs + 1
    stroke(r, g, b)
    fill(None)
    path = BezierPath()
    for i in range(step):
        strokeWidth(thickness)
        path.moveTo((o + (w/reps), o))
        path.arcTo((o + (w/reps), h - (w/reps)), (w, h - (w/reps)), (w - (w/reps)))
        drawPath(path)
        reps -= 1
def drawStraight(step, thickness):
    reps = divs + 1
    stroke(r, g, b)
    fill(None)
    path = BezierPath()
    for i in range(step):
        strokeWidth(thickness)
        path.moveTo((o + (w/reps), o))
        path.lineTo((o + (w/reps), h))
        drawPath(path)
        reps -= 1

# Create pages/frames
for i in range(divs):
    ranCol = randint(0, 255)/( 255)
    r, g, b = randint(0, 255)/( 255), randint(0, 255)/( 255), randint(0, 255)/( 255)    
    newPage(w, h)
    fill(0)
    stroke(None)
    rect(o, o, w, h)
    
    with savedState():
        scale(0.25)
        with savedState():
            translate(w, h*3)
            drawCurve(i, randint(minRan, maxRan))
        with savedState():
            rotate(-90 , (w*2, h*4))
            translate(w*2, h*4)
            drawCurve(i, randint(minRan, maxRan))
        with savedState():
            translate(w, o)
            drawStraight(i, randint(minRan, maxRan))
        with savedState():
            translate(w, h)
            drawStraight(i, randint(minRan, maxRan))
        with savedState():
            translate(w, h*2)
            drawStraight(i, randint(minRan, maxRan))
        with savedState():
            translate(w*2, o)
            rotate(-180, (hw, hh))
            drawStraight(i, randint(minRan, maxRan))
        with savedState():
            translate(w*2, h)
            rotate(-180, (hw, hh))
            drawStraight(i, randint(minRan, maxRan))
        with savedState():
            translate(w*2, h*2)
            rotate(-180, (hw, hh))
            drawStraight(i, randint(minRan, maxRan))
        
        with savedState():
            translate(w*2, hh)
            rotate(-90, (hw, hh))
            drawStraight(i, randint(minRan, maxRan))
        with savedState():
            translate(w*1, hh)
            rotate(-90, (hw, hh))
            drawStraight(i, randint(minRan, maxRan))
            
        with savedState():
            translate(w*2, h)
            rotate(90, (hw, hh))
            drawStraight(i, randint(minRan, maxRan))
        with savedState():
            translate(w*1, h)
            rotate(90, (hw, hh))
            drawStraight(i, randint(minRan, maxRan))

# save animation
saveImage('~/Desktop/01_36_DAYS_OF_TYPE_2020.mp4')