import math

side = 1080
pressure = 0
thickness = 0.5
grav = 9.81

def listOfPoints(incr = -540):
    points = []
    points.append((-side*5, side*4))
    incr = incr
    for i in range(side):
        v = int((incr * sin(math.radians(incr*randint(0,10)))) * 0.1)
        if i < side * (0.125 * 3):
            points.append((i, v))
        if i >= side * (0.125 * 3) and i <= side * (0.125 * 5):
            points.append((i, v))
        if i > side * (0.125 * 5):
            points.append((i, v))
        incr += 1
    points.append((side*6, side*4))
    points.append(None)
    return points
def lines(points):
    stroke(1)
    strokeWidth(thickness)
    fill(None)
    path = BezierPath()
    path.qCurveTo(*points)
    drawPath(path)

for i in range(24):    
    newPage(side, side)
    fill(0)
    rect(0, 0, side, side)
    mov = side
    rot = 0
    exp = 0
    for j in range(162):
        points = listOfPoints()
        with savedState():
            scale(x=1.5, y=1.3, center=(side/2, 0))
            translate(0, mov)
            if j > 34:
                translate(rot, 0)
                rotate(rot, (side/2, 0))
            lines(points)
            rot -= (exp * (2.72**(10*0.1))) * 0.001
            exp += 1
        mov -= 10

saveImage('~/Desktop/10_36_DAYS_OF_TYPE_2020.mp4')