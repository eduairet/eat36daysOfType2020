side = 1080
frames = 24
thickness = side*0.04 
divs = 4
exp = 30
radius = 260

def sklPts():
    points = []
    for i in range(0, int(side*0.4)):
        x = side*0.7 - i
        y = side*0.85
        points.append((x, y))
    for i in range(0, int(side*0.3)):
        x = side*0.3
        y = side*0.82 - i
        points.append((x, y))
    for i in range(-160, 140, int(divs/4)):
        x = radius * cos(radians(i)) + (side/2)
        y = radius * sin(radians(i)) + (370)
        points.append((x, y))
    return points
    
def shape(num, c):
    blendMode('screen')
    fill(randint(200, 255)/255, 1-c, randint(0, 255)/255, 0.3)
    if num == 1:
        with savedState():
            rotate(angle, center=(thickness/4, thickness/4))
            rect(-thickness/2, -thickness/2, thickness, thickness)
    if num == 2:
        with savedState():
            rotate(angle, center=(thickness/4, thickness/4))
            oval(-thickness/2, -thickness/2, thickness, thickness)
    if num == 3:
        with savedState():
            rotate(angle, center=(thickness/4, thickness/4))
            polygon(
                (-thickness/2, -thickness/2),
                (thickness/2, -thickness/2),
                (0, sqrt(3*thickness)/2 + (thickness/2)),
                (-thickness/2, -thickness/2),
                close=True
                )

points = sklPts()
for i in range(frames):
    newPage(side, side)
    fill(0)
    rect(0, 0, side, side)
    inc = 0
    c = 0
    for point in points:
        angle = 360 / frames * i + inc
        num = randint(1, 3)
        with savedState():
            translate(point[0] + randint(-exp, exp), point[1] + randint(-exp, exp))
            shape(num, c)
        inc += 1
        c += 0.001

saveImage('~/Desktop/32_36_DAYS_OF_TYPE_2020.mp4')