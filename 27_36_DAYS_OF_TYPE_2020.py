side = 1080
thickness = side*0.4
frames = 84

def skPts():
    points = []
    for i in range(360):
        x = cos(radians(i))
        y = sin(radians(i))
        points.append((x, y))
    return points
    
def shape(step, var):
    speed = var/step
    fill(1, 1, 1, 0.05)
    stroke(None)
    shape = BezierPath()
    shape.oval(0 - (thickness/2), 0 - (thickness/2), thickness, thickness)
    with savedState():
        scale(0.8, 1, (side*0.5, side*0.5))
        translate(side*0.2 + (thickness/4), side*0.2 + (thickness/4))
        rotate(2 * pi + speed, center=(side*0.2, side*0.2))
        drawPath(shape)

points = skPts()
print(points)
for i in range(int(-frames/2), int(frames/2)):
    if i != 0:
        newPage(side, side)
        fill(0)
        rect(0, 0, side, side)
        for j in range(0, 360, 12):
            with savedState():
                translate(
                    points[j][0],
                    points[j][1]
                    )
                if j != 0:
                    shape(i, j)

saveImage('~/Desktop/27_36_DAYS_OF_TYPE_2020.mp4')