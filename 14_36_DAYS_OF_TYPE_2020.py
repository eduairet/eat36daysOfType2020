side = 1080

def poly(step):
    def polyPoints(disp):
        points = [
            (side/2 + (disp*1), 0),
            (0 - disp, side/2 + (disp * 1)),
            (0 - disp, 0)
            ]
        return points
    fill(None)
    strokeWidth(4)
    lineDash(2, 2)
    blendMode("screen")
    disp = 0 
    for i in range(step):
        stroke(randint(100, 255)/255, 0, randint(100, 255)/255)
        points = polyPoints(disp)
        polygon(*points, close=False)
        disp += 10

for i in range(0, 540, 12):    
    newPage(side, side)
    fill(0)
    rect(0, 0, side, side)
    with savedState():
        translate(216, 0)
        poly(i + 1)
    with savedState():
        rotate(180, (side/2, side/2))
        translate(216, 0)
        poly(i + 1)
    
    
saveImage('~/Desktop/14_36_DAYS_OF_TYPE_2020.mp4')