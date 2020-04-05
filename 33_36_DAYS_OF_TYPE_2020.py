side = 1080
frames = 72
n = 2560

def fibonacci(n, step, s):
    points = []
    for i in range(0, n, 20):
        x = 0.001 * cos(radians(i))*(2.71828183**(0.0053468 * i))
        y = -0.001 * sin(radians(i))*(2.71828183**(0.0053468 * i))
        points.append((x, y))
    stroke(1)
    strokeWidth(1)
    fill(None)
    path = BezierPath()
    path.moveTo(points[0])
    path.curveTo(*points)
    for i in range(step):
        with savedState():
            rotate(s * i)
            drawPath(path)

s = 1
for i in range(1, frames + 1):
    newPage(side, side)
    frameDuration(1/24)
    rect(0, 0, side, side)
    with savedState():
        translate(side/2, side/2)
        fibonacci(n, i, s)
    s +=  360/frames

saveImage('~/Desktop/33_36_DAYS_OF_TYPE_2020.mp4')