# Following the Just Van Rossum's tutorial of the following link: https://vimeo.com/149247423

side = 1080
nShapes = 48
shapeDist = 0.5
frames = nShapes
mn, mx = -10, 10

def r():
    stroke(None)
    fill(0)
    stroke(1)
    path = BezierPath()
    path.beginPath((None))
    path.addPoint((324 + randint(mn, mx), 0 + randint(mn, mx)), 'line', False, None)
    path.addPoint((540 + randint(mn, mx), 0 + randint(mn, mx)), 'line', False, None)
    path.addPoint((540 + randint(mn, mx), 120 + randint(mn, mx)), 'line', True, None)
    path.addPoint((540 + randint(mn, mx), 208 + randint(mn, mx)), None, False, None)
    path.addPoint((496 + randint(mn, mx), 264 + randint(mn, mx)), None, False, None)
    path.addPoint((425 + randint(mn, mx), 299 + randint(mn, mx)), 'curve', False, None)
    path.addPoint((498 + randint(mn, mx), 307 + randint(mn, mx)), None, False, None)
    path.addPoint((540 + randint(mn, mx), 334 + randint(mn, mx)), None, False, None)
    path.addPoint((540 + randint(mn, mx), 405 + randint(mn, mx)), 'curve', True, None)
    path.addPoint((540 + randint(mn, mx), 621 + randint(mn, mx)), 'line', True, None)
    path.addPoint((540 + randint(mn, mx), 729 + randint(mn, mx)), None, False, None)
    path.addPoint((459 + randint(mn, mx), 756 + randint(mn, mx)), None, False, None)
    path.addPoint((337 + randint(mn, mx), 756 + randint(mn, mx)), 'curve', True, None)
    path.addPoint((0 + randint(mn, mx), 756 + randint(mn, mx)), 'line', False, None)
    path.addPoint((0 + randint(mn, mx), 0 + randint(mn, mx)), 'line', False, None)
    path.addPoint((216 + randint(mn, mx), 0 + randint(mn, mx)), 'line', False, None)
    path.addPoint((216 + randint(mn, mx), 264 + randint(mn, mx)), 'line', False, None)
    path.addPoint((304 + randint(mn, mx), 251 + randint(mn, mx)), None, False, None)
    path.addPoint((324 + randint(mn, mx), 213 + randint(mn, mx)), None, False, None)
    path.addPoint((324 + randint(mn, mx), 120 + randint(mn, mx)), 'curve', True, None)
    path.endPath()
    path.beginPath((None))
    path.addPoint((270 + randint(mn, mx), 648 + randint(mn, mx)), 'line', True, None)
    path.addPoint((297 + randint(mn, mx), 648 + randint(mn, mx)), None, False, None)
    path.addPoint((324 + randint(mn, mx), 631 + randint(mn, mx)), None, False, None)
    path.addPoint((324 + randint(mn, mx), 594 + randint(mn, mx)), 'curve', True, None)
    path.addPoint((324 + randint(mn, mx), 432 + randint(mn, mx)), 'line', True, None)
    path.addPoint((324 + randint(mn, mx), 395 + randint(mn, mx)), None, False, None)
    path.addPoint((297 + randint(mn, mx), 378 + randint(mn, mx)), None, False, None)
    path.addPoint((270 + randint(mn, mx), 378 + randint(mn, mx)), 'curve', True, None)
    path.addPoint((216 + randint(mn, mx), 378 + randint(mn, mx)), 'line', False, None)
    path.addPoint((216 + randint(mn, mx), 648 + randint(mn, mx)), 'line', False, None)
    path.endPath()
    with savedState():
        translate(229, 162)
        drawPath(path)

for frame in range(frames):
    newPage(side, side)
    frameDuration(1/24)
    fill(0)
    rect(0, 0, side, side)
    phase = 2 * pi * frame / nShapes
    startAngle = 27.5 * sin(phase)
    endAngle = 45 * sin(phase + 0.5 * pi)
    print(phase, startAngle, endAngle)
    translate(54, 0)
    for i in range(nShapes + 1):
        f = i / nShapes
        with savedState():
            rotate(startAngle + f * (endAngle - startAngle), (side/2, side/2))
            r()

saveImage("~/Desktop/StackOfSquares.mp4")