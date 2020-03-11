side = 1080
beg = -1
fin = 1
radius = side * 0.4

def drawShape(radius, beg, fin):
    
    def listOfPoints(points=[]):
        for i in range(beg, fin):
            pointX = radius * cos(i) + i
            pointY = radius * sin(i) + i
            point = pointX, pointY
            points.append(point)
        points.append(None)
        return points
    
    points = listOfPoints()
    
    path = BezierPath()
    stroke(1)
    strokeWidth(0.5)
    fill(None)
    with savedState():
        path.qCurveTo(*points)
        path.closePath()
        drawPath(path)

for i in range(50):
    newPage(side, side)
    fill(0)
    rect(0, 0, side, side)
    
    with savedState():
        translate(0, side/2)
        rotate(45)
        drawShape(radius, beg, fin)
    with savedState():
        translate(side, side/2)
        rotate(45)
        drawShape(radius, beg, fin)
    with savedState():
        translate(side/2, side/8)
        rotate(-45)
        drawShape(radius, beg, fin)
    with savedState():
        translate(side/2, side/1.2)
        rotate(-225)
        drawShape(radius, beg, fin)
    
    beg -= i
    fin += i

saveImage("~/Desktop/08_36_DAYS_OF_TYPE_2020.mp4")