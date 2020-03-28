side = 1080
frames = 48

def shape(inc, deg):
    fill(1)
    stroke(1)
    strokeWidth(1)
    path = BezierPath()
    path.moveTo((side/2, 0))
    path.lineTo((side/2 - inc, side/2))
    path.lineTo((0, side))
    path.lineTo((side/2 , side/2 + (inc * 1.5)))
    path.lineTo((side, side))
    path.lineTo((side/2 + inc, side/2))
    path.closePath()
    radialGradient(
        (side/3, side/2), (side, side),
        [(0, 0, 0), (0.2, 0.2, 0.2), (1, 1, 1)],
        [0, .1 + deg, 1], side*0.05, side
        )
    drawPath(path)

inc = (side*0.5) / frames
deg = 0
for i in range(frames):
    newPage(side, side)
    fill(0)
    rect(0, 0, side, side)
    with savedState():
        scale(randint(8, 12)/10, center=(side/2, side/2))
        shape(inc, deg)
    if i < frames/2:
        inc += (side*0.5) / frames
        deg += 0.9 / frames
    else:
        inc -= (side*0.5) / frames
        deg -= 0.9 / frames
        
    for j in range(100):
        radialGradient(None)
        fill(1)
        with savedState():
            translate(randint(0, side), randint(0, side))
            oval(0, 0, randint(1, 2), randint(1, 2))


saveImage('~/Desktop/25_36_DAYS_OF_TYPE_2020.mp4')