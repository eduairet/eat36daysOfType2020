side = 1080
thickness = 108
mnr, mxr = -50, 50
frames = 60

def shape():
    newPath()
    moveTo((side/2 - thickness + randint(mnr, mxr), side * 0.1 + randint(mnr, mxr)))
    lineTo((side/2 + thickness + randint(mnr, mxr), side * 0.1 + randint(mnr, mxr)))
    lineTo((side/2 + thickness + randint(mnr, mxr), side * 0.8 + randint(mnr, mxr))) 
    lineTo((side * 0.8 + randint(mnr, mxr), side * 0.8 + randint(mnr, mxr)))
    lineTo((side * 0.8 + randint(mnr, mxr), side * 0.8 + thickness + randint(mnr, mxr)))
    lineTo((side * 0.2 + randint(mnr, mxr), side * 0.8 + thickness + randint(mnr, mxr)))
    lineTo((side * 0.2 + randint(mnr, mxr), side * 0.8 + randint(mnr, mxr)))
    lineTo((side/2 - thickness + randint(mnr, mxr), side * 0.8 + randint(mnr, mxr)))
    closePath()
    drawPath()
def T():
    stroke(None)
    linearGradient(
        (100, 100), (m, m), [(1, randint(0, 100)/255, 0, 0.2), (1, 0, randint(100, 255)/255, 0.2), (0, randint(100, 255)/255, 1, 0.2)], [0, .5, 1])
    shape()
def cT():
    linearGradient(None)
    fill(None)
    stroke(1)
    strokeWidth(2)
    shape()   

m = side/2
for i in range(frames):
    newPage(side, side)
    fill(0)
    rect(0, 0, side, side)
    blendMode('screen')
    T()
    T()
    T()
    cT()
    cT()
    cT()
    if i < frames/2:
        m += 10
    elif i > frames/2:
        m -= 10
    
saveImage('~/Desktop/20_36_DAYS_OF_TYPE_2020.mp4')