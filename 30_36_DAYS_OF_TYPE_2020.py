side = 1080
frames = 120
speed = 4000

def lsPts(inc):
    steps = 1 + inc
    size = 2
    tr = 106.5
    points = []
    for i in range(steps):
        t = i / 21 * pi
        x = (size * t) * cos(t)
        y = (size * t) * sin(t) - (tr/2)
        points.append((x, y))
    for i in range(-steps, 0):
        t = i / 21 * pi
        x = (-size * t) * cos(t)
        y = (-size * t) * sin(t) + (tr/2)
        points.append((x, y))
    return points

def spiral(s, sw):
    stroke(s, 1, 1)
    strokeWidth(sw)
    fill(None)
    lineCap('round')
    path = BezierPath()
    path.moveTo(points[0])
    path.curveTo(*points)
    with savedState():
        translate(side/2, side/2)
        drawPath(path)

inc = 0
exp = 1
f =  speed / frames * exp
s = 0

for i in range(frames):
    newPage(side, side)
    frameDuration(1/24)
    fill(0)
    rect(0, 0, side, side)
    points = lsPts(179)
    spiral(0, 3)
    points = lsPts(inc)
    spiral(s, 1)
    if i < frames/2:
        inc += int(f)
        exp += 10
        s += 0.01
    else:
        inc -= int(f)
        exp -= 10
        s -= 0.01

saveImage('~/Desktop/30_36_DAYS_OF_TYPE_2020.mp4')