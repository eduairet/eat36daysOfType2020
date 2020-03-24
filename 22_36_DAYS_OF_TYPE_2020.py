side = 1080
frames = 12
mnr, mxr = -5, 5

def shape(m, thickness):
    linearGradient(
        (-thickness/2, -thickness/2), (thickness/2, thickness/2), [(1, 1, 1), (0, 0, 1), (0, 1, 1)], [0, .5, 1])
    stroke(None)
    strokeWidth(1)
    with savedState():
        rotate(m, (thickness*0.1, thickness*0.1))
        translate(randint(mnr, mxr), randint(mnr, mxr))
        oval(0 - (thickness/2), 0 - (thickness/2), thickness, thickness)

m = 0
s = 0.1
for i in range(frames):
    points = []
    x = side * 0.1
    y = side * 0.9
    points.append((x, y))
    while x < side/2:
        x += 1
        y = (-2 * (x - (side * 0.1))) + (side * 0.9)
        points.append((x, y))
    while x < side * 0.9:
        x += 1
        y = (2 * x) - (side * 0.9)
        points.append((x, y))    
    
    newPage(side, side)
    fill(0)
    rect(0, 0, side, side)
    for point in points:
        with savedState():
            translate(point[0], point[1])
            shape(m, side*s)
    m += 360/frames
    if i < (frames/2):
        s += 0.08
    elif i > (frames/2):
        s -= 0.08

saveImage('~/Desktop/22_36_DAYS_OF_TYPE_2020.mp4')