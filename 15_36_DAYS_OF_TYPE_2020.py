side = 1080

def lsOfPoints():
    points = []
    for i in range(648):
        t = i / 20 * pi
        x = (1 + 5 * t) * cos(t)
        y = (1 + 5 * t) * sin(t)
        if i > 648/2:
            points.append((x, y))
    return points

def lsOfPointsC():
    pointsC = []
    for i in range(1080):
        t = i / 20 * pi
        x = (1 + 5 * t) * cos(t)
        y = (1 + 5 * t) * sin(t)
        pointsC.append((x, y))
    return pointsC

def spiral():
    stroke(1)
    strokeWidth(12)
    fill(None)
    lineCap('round')
    points = lsOfPoints()
    path = BezierPath()
    path.moveTo(points[0])
    path.curveTo(*points)
    with savedState():
        translate(side/2, side/2)
        drawPath(path)

def spiralC():
    stroke(1)
    strokeWidth(2)
    fill(None)
    lineCap('round')
    points = lsOfPointsC()
    path = BezierPath()
    path.moveTo(points[0])
    path.curveTo(*points)
    with savedState():
        translate(side/2, side/2)
        drawPath(path)
    
for i in range(60):
    newPage(1080, 1080)
    fill(0)
    rect(0, 0, side, side)
    with savedState():
        rotate(360/60*i, (side/2, side/2))
        spiralC()
        spiral()
        
saveImage('~/Desktop/15_36_DAYS_OF_TYPE_2020.mp4')