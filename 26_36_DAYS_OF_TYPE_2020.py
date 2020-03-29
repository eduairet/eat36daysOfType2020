# Cannot be possible without this code https://gist.github.com/justvanrossum/b9b931c25921bdb015f4af87aee9ef68

side = 1080
frames = 36
radius = side * 0.4

def zPts(a, b, phase, radius):
    numSteps = 1000
    points = []
    for i in range(numSteps):
        angle = 2 * pi * i / numSteps
        x = radius * cos(a * angle + phase)
        y = radius * sin(b * angle + phase)
        points.append((x, y))
    return points

def shape(steps): 
    t = 3/frames
    for i in range(steps):  
        stroke(randint(0, 255)/255, randint(0, 255)/255, randint(0, 255)/255,)
        strokeWidth(2)
        lineJoin("round")
        lineDash(2, 2, 2, 2)
        fill(None)
        for a in range(1, 2):
            for b in range(3, 4):
                with savedState():
                    translate(side * 0.5, side * 0.5)
                    points = zPts(b, a, 2 * pi * t, radius)
                    polygon(*points)
        t += 0.025 / frames

step = 1
inc = 5
for frame in range(frames):
    newPage(side, side)
    fill(0)
    rect(0, 0, side, side)
    shape(step)
    if frame < frames/2:
        step += inc
    else:
        step -= inc

saveImage('~/Desktop/26_36_DAYS_OF_TYPE_2020.mp4')