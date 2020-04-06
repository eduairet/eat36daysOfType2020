side = 1080
frames = 72

def lsPts(inc):
    steps = 1 + inc
    size = 2.5
    tr = 431
    points = []
    for i in range(steps):
        t = i / 25 * pi
        x = (size * t) * cos(t)
        y = (size * t) * sin(t) - (tr/2)
        points.append((x, y))
    for i in range(-steps, 0):
        t = i / 23 * pi
        x = (size * t) * cos(t)
        y = (-size * t) * sin(t) + (tr/2)
        points.append((x, y))
    return points

def spiral():
    stroke(randint(int(255*0.75), 255)/255, 0, randint(0, 255)/255)
    strokeWidth(5)
    fill(None)
    lineCap('round')
    path = BezierPath()
    path.moveTo(points[0])
    path.curveTo(*points)
    with savedState():
        translate(side/2, side/2 + 13.5)
        rotate(angle)
        drawPath(path)

inc = 0
exp = 45
f =  exp / frames * exp
angle = 0
for i in range(1, frames):
    newPage(side, side)
    frameDuration(1/24)
    fill(0)
    rect(0, 0, side, side)
    points = lsPts(inc)
    spiral()
    if i < frames/2:
        inc += int(f)
    else:
        inc -= int(f)
    angle += 360/frames

saveImage('~/Desktop/35_36_DAYS_OF_TYPE_2020.mp4')