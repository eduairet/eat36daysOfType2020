side = 1080
frames = 72

def shape():
    fill(0, 0, 1, 0.05)
    stroke(0, 0, 1)
    strokeWidth(2)
    blendMode('screen')
    newPath()
    moveTo((side*0.9, side*0.5-inc))
    lineTo((side*0.1, side*0.5-inc))
    lineTo((side*0.5+inc, side*0.9))
    lineTo((side*0.5+inc, side*0.1))
    drawPath()

steps = 1
for i in range(frames):
    newPage(side, side)
    fill(0)
    rect(0, 0, side, side)
    inc = 0
    if i < frames/2:
        for j in range(steps):
            shape()
            inc += side*0.8/frames
        steps += 1
    else:
        for j in range(steps):
            shape()
            inc += side*0.8/frames
        steps -= 1

saveImage('~/Desktop/31_36_DAYS_OF_TYPE_2020.mp4')