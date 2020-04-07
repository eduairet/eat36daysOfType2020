side = 1080
frames = 48

def fibonacci(n):
    points = []
    for i in range( n):
        x = -0.001 * cos(radians(i))*(2.71828183**(0.0053468 * i))
        y = 0.001 * sin(radians(i))*(2.71828183**(0.0053468 * i))
        points.append((x, y))
    return(points)

def shape(step, f):    
    stroke(None)
    path = BezierPath()
    path.moveTo(points[0])
    path.oval(0-thickness, 0-thickness, thickness, thickness)
    fill(1, 1, 1, f)
    with savedState():
        translate(side/1.8, side/1.5)
        drawPath(path)

n = 0
f = 0
thickness = 0
for i in range(frames):
    newPage(side, side)
    frameDuration(1/24)
    rect(0, 0, side, side)
    points = fibonacci(n)
    for point in points:
        with savedState():
            translate(point[0], point[1])
            shape(i, f)
    if i < frames/2:
        thickness += 216/(frames/2)
        f += 1/frames*0.2
    else:
        thickness -= 216/(frames/2)
        f -= 1/frames*0.2
    n += int(2560*2/frames)

saveImage('~/Desktop/36_36_DAYS_OF_TYPE_2020.mp4')