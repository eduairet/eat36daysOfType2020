side = 1080

def listPoints(ran):
    points = [
            (side * 0.1 + randint(-ran, ran), side * 0.3 + randint(-ran, ran)),
            (side * 0.8 + randint(-ran, ran), side * 0.6 + randint(-ran, ran)),
            (side * 0.6 + randint(-ran, ran), side * 1.1 + randint(-ran, ran)),
            (side * 0.2 + randint(-ran, ran), side * 0.2 + randint(-ran, ran)),
            (side * 0.31 + randint(-ran, ran), side * 0.1 + randint(-ran, ran)),
            (side * 0.31 + randint(-ran, ran), side * 0.48 + randint(-ran, ran)),
            (side * 0.7 + randint(-ran, ran), side * 0.5 + randint(-ran, ran)),
            (side * 0.4 + randint(-ran, ran), side * 0.3 + randint(-ran, ran)),
            (side * 0.35 + randint(-ran, ran), side * 0.35 + randint(-ran, ran)),
            (side * 0.356 + randint(-ran, ran), side * 0.39 + randint(-ran, ran)),
            (side * 0.44 + randint(-ran, ran), side * 0.40 + randint(-ran, ran)),
            (side * 0.6 + randint(-ran, ran), side * -0.01 + randint(-ran, ran)),
            (side * 0.8 + randint(-ran, ran), side * 0.2 + randint(-ran, ran))
            ]
    return points

def path(steps, pressure = 0.5):  
    stroke(1)
    lineCap("round")
    fill(None)
    ran=10
    for i in range(steps):
        strokeWidth(pressure)
        lineDash(pressure/2, pressure*2)
        path = BezierPath()
        points = listPoints(ran)
        path.moveTo((side*0.1, side/2))
        path.curveTo(*points)
        drawPath(path)
        ran += int(1 ** (pressure * 1000000))
        pressure += 0.01

for i in range(96):
    newPage(side, side)
    fill(0)
    rect(0, 0, side, side)
    path(i*4)

saveImage('~/Desktop/11_36_DAYS_OF_TYPE_2020.mp4')