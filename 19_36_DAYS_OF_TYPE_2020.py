side = 1080
step = 24
gr = 2000

def s(r, g, b, m):
    for i in range(2):
        points = []
        for j in range(-108, side + 108):
            x = m * cos(radians(j * 0.35 + 260)) * (randint(1, 10) *0.1)
            y = j + randint(-10, 10)
            points.append((x, y))
        fill(None)
        stroke(r, g, b)
        strokeWidth(1)
        blendMode("screen")
        with savedState():
            path = BezierPath()
            path.moveTo(points[0])
            path.curveTo(*points)
            translate(side/2, 0)
            drawPath(path)

m = 0
for i in range(step):
    newPage(side, side)
    fill(0)
    rect(0, 0, side, side)
    s(1, 1, 0, m)
    s(0, 1, 1, m)
    s(1, 0, 1, m)
    if i <= step/2:
        m += gr/step
    else:
        m -= gr/step

saveImage('~/Desktop/19_36_DAYS_OF_TYPE_2020.mp4')