# The code that helped me to achive this is from Just Van Rossum: https://gist.github.com/justvanrossum/b65f4305ffcf2690bc65

def drawShape(shapePhase, shapeRadius):
    
    def variation(pt, radius, phase):
        x, y = pt
        dx = radius * cos(phase)
        dy = radius * sin(phase)
        return x + dx, y + dy
    
    points = []
    
    for i in range(numShapePoints):
        a = 2 * pi * i / numShapePoints
        x = shapeRadius * cos(a)
        y = shapeRadius * sin(a)
        rPhase, rSign = randomPhases[i]
        points.append(variation((x, y), 0.1 * shapeRadius, rPhase + rSign * 2 * pi * shapePhase))
        
    points.append(None)
    path = BezierPath()
    path.qCurveTo(*points)
    path.closePath()
    drawPath(path)
    
    #Counter shape
    with savedState():
        cp = 20
        fill(0)
        stroke(1)
        clipPath(path)
        polygon(
            (-100 + randint(-cp, cp), 200 + randint(-cp, cp)),
            (-100 + randint(-cp, cp), -200 + randint(-cp, cp)),
            (100 + randint(-cp, cp), -200 + randint(-cp, cp)),
            (100 + randint(-cp, cp), -150 + randint(-cp, cp)),
            (0 + randint(-cp, cp), -150 + randint(-cp, cp)),
            (0 + randint(-cp, cp), 50 + randint(-cp, cp)),
            (1000 + randint(-cp, cp), 50 + randint(-cp, cp)),
            (1000 + randint(-cp, cp), 150 + randint(-cp, cp)),
            (100 + randint(-cp, cp), 100 + randint(-cp, cp)),
            (100 + randint(-cp, cp), 200 + randint(-cp, cp)),
            (-100 + randint(-cp, cp), 200 + randint(-cp, cp)),
            close=True
            )

numShapePoints = 5
randomPhases = [(2 * pi * random(), randint(-100, 100)) for i in range(numShapePoints)]

canvasSize = 1080
nShapes = 60
nFrames = 48

for frame in range(nFrames):
    framePhase = frame / nFrames
    newPage(canvasSize, canvasSize)
    frameDuration(1/24)
    fill(0)
    rect(0, 0, canvasSize, canvasSize)
    translate(canvasSize/2, canvasSize/2)
    strokeWidth(1)
    stroke(1)
    fill(None)
    for i in range(nShapes):
        shapePhase = i / nShapes
        radius = 20 + i * 10
        drawShape(framePhase + shapePhase * 0.5, radius)

saveImage("~/Desktop/07_36_DAYS_OF_TYPE_2020.mp4")
