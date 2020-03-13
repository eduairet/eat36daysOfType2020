side = 1080
pressure = 0
thickness = 1
gap = thickness

def listOfPoints():
    points = []
    for i in range(int((side/thickness) + gap)):
        if i > side * (0.125 * 3) and i < side * (0.125 * 5):
            points.append(((i * thickness) + (gap * 4), randint(0, side)))
    points.append(None)
    return points

def lines():
    points = listOfPoints()
    stroke(1)
    strokeWidth(thickness)
    fill(None)
    path = BezierPath()
    path.qCurveTo(*points)   
    drawPath(path)

for i in range(48):    
    newPage(side, side)
    fill(0)
    rect(0, 0, side, side)
    with savedState():
        translate(randint(-10, 10), randint(-10, 10))    
        lines()

saveImage('~/Desktop/09_36_DAYS_OF_TYPE_2020.mp4')