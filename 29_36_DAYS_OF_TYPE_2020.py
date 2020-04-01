side = 1080
thickness = 4
frames = 60

def sklPts(step):
    points = []
    for i in range(0, int(360/frames*step), 8):
        x = (side*0.5) - (side*0.3) * cos(radians(i))
        y = (side*0.6) + (side*0.3) * sin(radians(i))
        points.append((x, y))
    return points

def sklPts2(step):
    points = []
    for i in range(0, int(360/frames*step)):
        x = (side*0.5) - (side*0.4) * cos(radians(i))
        y = (side*0.6) + (side*0.4) * sin(radians(i))
        points.append((x, y))
    return points
    
def shape(step):
    stroke(None)
    fill(1, 1, randint(0, 1), 0.5) 
    points = sklPts2(step)
    path = BezierPath()
    path.moveTo(points[0])
    path.curveTo(*points)
    blendMode('screen')
    with savedState():
        scale(randint(5, 15)*0.1, center=(side/2, side/2))
        drawPath(path)

for i in range(frames):
    if i == 0:
        continue
    
    newPage(side, side)
    fill(0)
    rect(0, 0, side, side)
    
    linearGradient(
        (0, 0), (0, 108), [(1, randint(0, 100)/255, 0), (1, randint(100, 200)/255, 1), (1, 1, 1)], [0, .5, 1])
    rect(0, 0, side, side*0.1)
    linearGradient(None)
    
    shape(i)
    
    stroke(0, randint(200,255)/255, randint(200,255)/255)
    strokeWidth(2)
    lineCap('round')
    lineDash(0.25, 4)
    fill(None)
    newPath()
    moveTo((side, side*0.1))
    lineTo((0, side*0.1))
    curveTo((side*0.1, 430), (side*0.9, 80), (side*0.9, 640))
    curveTo((side*0.9, 930), (760, side*0.95), (560, side*0.95))
    curveTo((230, side*0.95), (side*0.1, side*0.8), (side*0.1, side*0.6))
    lineTo((side*0.1, side*0.5))
    for numbs in range(i):
        for m in range(3):
            with savedState():
                translate(0, randint(-50, 50))
                drawPath()
    
    strokeWidth(thickness)
    lineDash(0.25, 8)
    lineCap('round')
    offset = 0
    for j in range(i):
        for k in range(1,54):
            stroke(randint(100,255)/255, 0.5, 0)
            line((offset, side*0.1), (offset, side*0.15+(offset*0.1)))
            offset += j/(side*0.8/(i*k)) 
    for j in range(i):
        points = sklPts(j)
        for point in points:
            stroke(randint(100,255)/255, 0.5, 0)
            line((side*0.5, side*0.5), (point))
        
saveImage('~/Desktop/29_36_DAYS_OF_TYPE_2020.mp4')