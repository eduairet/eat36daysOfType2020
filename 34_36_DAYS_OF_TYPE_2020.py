side = 1080
frames = 48
turn = 360

def shapes(angle):
    fill(0, 1, 0.5)
    stroke(0, 1, 0.5)
    strokeWidth(0.1)
    def shape1(angle):
        rotate(angle, center=(side*0.05/2, side*0.05/2))
        rect(0, side*0.05/2, side*0.05, side*0.05/2)
    for i in range(int((side*0.9)/(side*0.05))):
        for j in range(i):
            with savedState():
                translate((side*0.1) + side*0.05*i, side*0.05*j)
                shape1(angle+90+(j*8))
    for i in range(int((side*0.9)/(side*0.05))):
        for j in range(i):
            with savedState():
                translate((side*0.9)-(side*0.05*(i+1)), (side*0.9)-(side*0.05*(j+1)))
                shape1(angle+(j*8))

angle = 0
for i in range(frames):
    newPage(side, side)
    frameDuration(1/24)
    fill(0)
    rect(0, 0, side, side)
    shapes(angle)
    angle += turn/frames
        

saveImage('~/Desktop/34_36_DAYS_OF_TYPE_2020.mp4')