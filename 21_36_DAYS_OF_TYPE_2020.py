side = 1080
steps = 24

def u(step, exp, ex, ey):
    points = []
    for i in range(360):
        x = 10 ** ex * cos(radians(i*exp)) + randint(-2, 2)
        y = 10 ** ey * sin(radians(i*exp)) + randint(-2, 2)
        points.append((x, y))
    fill(None)
    stroke(randint(0, 10)/255, randint(200, 255)/255, randint(200, 255)/255)
    strokeWidth(2)
    for i in range(step):
        path = BezierPath()
        path.moveTo(points[0])
        path.curveTo(*points)
        with savedState():
            translate(side/2, side)
            drawPath(path)

exp = 0.0
ex = 1.0
ey = 2.0
for i in range(steps):
    newPage(side, side)
    fill(0)
    rect(0, 0, side, side)
    if i < steps/2:
        for j in range(4):
            u(i + 1, exp, ex, ey)
            u(i + 1, exp, ex, ey)
            exp += 1
            ex += 33/steps * 0.1
            ey += 18/steps * 0.1
            u(i + 1, exp, ex, ey)
            u(i + 1, exp, ex, ey)
    if i > steps/2:
        for j in range(4):
            u(i + 1, exp, ex, ey)
            u(i + 1, exp, ex, ey)
            exp -= 1
            ex -= 33/steps * 0.1
            ey -= 18/steps * 0.1
            u(i + 1, exp, ex, ey)
            u(i + 1, exp, ex, ey)

saveImage('~/Desktop/21_36_DAYS_OF_TYPE_2020.mp4')