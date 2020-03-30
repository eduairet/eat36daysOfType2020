side = 1080
thickness = side*0.2
frames = 42
st = 0.3

def skPts():
    points = []
    for i in range(int(side*0.3), int(side/2)):
        x = i
        y = 0.5 * (x - (side*0.3)) + (side*0.7)
        points.append((x, y))
    for i in range(int(side)):
        x = side/2
        y = side*0.8 - i
        points.append((x, y))
    return points
    
def shape(step, var, c):
    speed = 2 * pi * step / frames
    sAngle = 0 * sin(speed)
    eAngle = 360 * sin(speed + 0.5 * pi)
    fill(1-(c*10), 1, c*10, 0+c)
    stroke(1, 1, 1, 0+(c*10))
    strokeWidth(st)
    lineDash(st, st, st)
    shape = BezierPath()
    shape.oval(0 - (thickness/2), 0 - (thickness/2), thickness, thickness)
    with savedState():
        rotate(sAngle + (var*(10**-3)) * (eAngle - sAngle), center=(thickness/6, thickness/6))
        drawPath(shape)

points = skPts()
for i in range(int(-frames/2), int(frames/2)):
    if i != 0:
        newPage(side, side)
        fill(0)
        rect(0, 0, side, side)
        c = 0
        for j in range(0, len(points), 1):
            with savedState():
                translate(
                    points[j][0],
                    points[j][1]
                    )
                if j != 0:
                    shape(i, j, c)
            c += 0.0001

saveImage('~/Desktop/28_36_DAYS_OF_TYPE_2020.mp4')