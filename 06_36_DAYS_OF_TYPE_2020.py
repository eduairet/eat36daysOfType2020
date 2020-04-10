canvasSize = 1080
strokeThickness = 3
mod = canvasSize * 0.125

def drawf(step, thickness, shFill, sFill):
    reps = step + 1
    stroke(sFill)
    fill(shFill)
    strokeWidth(thickness)
    path = BezierPath()
    for i in range(step):
        sep = thickness * 3 * reps
        path.moveTo((mod * 2 + sep, mod + sep))
        path.lineTo((mod * 2 + sep, mod * 7 - sep))
        path.lineTo((mod * 6 - sep, mod * 7 - sep))
        path.lineTo((mod * 6 - sep, mod * 5 + sep))
        path.lineTo((mod * 4 - sep, mod * 5 + sep))
        path.lineTo((mod * 4 - sep, mod * 4 - sep))
        path.lineTo((mod * 5 - sep, mod * 4 - sep))
        path.lineTo((mod * 5 - sep, mod * 2 + sep))
        path.lineTo((mod * 4 - sep, mod * 2 + sep))
        path.lineTo((mod * 4 - sep, mod * 1 + sep))
        path.lineTo((mod * 2 + sep, mod + sep))
        path.closePath()
        drawPath(path)
        reps -= 1
        
for i in range(29):
    newPage(canvasSize, canvasSize)
    rect(0, 0, canvasSize, canvasSize)
    with savedState():
        translate(randint(-10, 10), randint(-10, 10))
        if i <= 14:
            with savedState():
                drawf(i, strokeThickness, None, 1)
        else:
            with savedState():
                drawf(i - 14, strokeThickness, 1, 0)

# save animation
saveImage('~/Desktop/06_36_DAYS_OF_TYPE_2020.mp4')
