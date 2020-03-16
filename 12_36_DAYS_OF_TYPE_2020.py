#It couldn't be possible without this code: https://gist.github.com/justvanrossum/5546cafd3c239623764fe586cebc9811

side = 1080
frames = 24
sqSize = side/10

def rotSquare(angle):
    offsetSin = sqSize * sin(radians(angle))
    fill(1)
    save()
    rotate(angle, (sqSize, sqSize))
    translate(0, offsetSin)
    rect(0, 0, sqSize, sqSize)
    restore()
 
for frame in range(frames):

    newPage(side, side)
    fill(0)
    rect(0, 0, side, side)
    
    angle = 90 * frame / frames
    offset = sqSize * (sin(radians(angle)) + cos(radians(angle)))
    for i in range(frames):
        x = 0
        y = 0
        for k in range(8):
            if k <= 4:
                for j in range(8):
                    with savedState():
                        translate(sqSize + x, sqSize + y)
                        rotSquare(angle)
                    y += sqSize
            if k > 4:
                for l in range(3):
                    with savedState():
                        translate(sqSize + x, sqSize + y)
                        rotSquare(angle)
                    y += sqSize
            y = 0
            x += sqSize


saveImage("~/Desktop/12_36_DAYS_OF_TYPE_2020.mp4")