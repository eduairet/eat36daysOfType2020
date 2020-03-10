o = 0
w = 1080
h = 1080
hw = w/2
hh = h/2
divs = 96
minRan = 100
maxRan = 5000
r, g, b = randint(0, 10)/( 255), randint(0, 10)/( 255), randint(0, 255)/( 255)

#Functions      
def drawCurve(step, thickness):
    reps = step + 1
    stroke(r, g, b)
    fill(None)
    path = BezierPath()
    for i in range(step):
        strokeWidth(thickness)
        path.moveTo((o + (thickness * 3 * reps), o))
        path.arcTo((o + (thickness * 3 * reps), h - (thickness * 3 * reps)), (w, h - (thickness * 3 * reps)), (w - (thickness * 3 * reps)))
        drawPath(path)
        reps -= 1
def drawStraight(step, thickness):
    reps = step + 1
    stroke(r, g, b)
    fill(None)
    path = BezierPath()
    for i in range(step):
        strokeWidth(thickness)
        path.moveTo((o + (thickness * 3 * reps), o))
        path.lineTo((o + (thickness * 3 * reps ), h))
        drawPath(path)
        reps -= 1

# Create pages/frames
for i in range(divs):
    ranCol = randint(0, 255)/( 255)
    #r, g, b = randint(0, 255)/( 255), randint(0, 255)/( 255), randint(0, 255)/( 255)
    r, g, b = randint(0, 10)/( 255), randint(200, 255)/( 255), randint(0, 255)/( 255)   
    newPage(w, h)
    fill(0)
    stroke(None)
    rect(o, o, w, h)
    
    with savedState():
        scale(0.25)
        with savedState():
            translate(w, h*3)
            drawStraight(i, randint(minRan, maxRan) / 1000)
        with savedState():
            translate(w, h*2)
            drawStraight(i, randint(minRan, maxRan) / 1000)
        with savedState():
            translate(w, h)
            drawStraight(i, randint(minRan, maxRan) / 1000)
        with savedState():
            translate(w, o)
            drawStraight(i, randint(minRan, maxRan) / 1000)
        
        with savedState():
            translate(w*2, h*3)
            rotate(-90, (hw, hh))
            drawCurve(i, randint(minRan, maxRan) / 1000)
        with savedState():
            translate(w*2, h*2)
            rotate(-180, (hw, hh))
            drawCurve(i, randint(minRan, maxRan) / 1000)
        with savedState():
            translate(w*2, h)
            rotate(-90, (hw, hh))
            drawCurve(i, randint(minRan, maxRan) / 1000)
        with savedState():
            translate(w*2, o)
            rotate(-180, (hw, hh))
            drawCurve(i, randint(minRan, maxRan) / 1000)
        
        with savedState():
            translate(w, h*3)
            rotate(-90, (hw, hh))
            drawStraight(i, randint(minRan, maxRan) / 1000)
        with savedState():
            translate(w, h)
            rotate(-90, (hw, hh))
            drawStraight(i, randint(minRan, maxRan) / 1000)
        with savedState():
            translate(w, h*2)
            rotate(90, (hw, hh))
            drawStraight(i, randint(minRan, maxRan) / 1000)
        with savedState():
            translate(w, o)
            rotate(90, (hw, hh))
            drawStraight(i, randint(minRan, maxRan) / 1000)
        

# save animation
saveImage('~/Desktop/02_36_DAYS_OF_TYPE_2020.mp4')