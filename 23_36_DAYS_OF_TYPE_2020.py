side = 1080
frames = 48

def shape(thickness):
    fill(0)
    stroke(1)
    strokeWidth(1)
    with savedState():
        rotate(startAngle + f * (endAngle - startAngle), (thickness*0.1, thickness*0.1))
        rect(0 - (thickness/2), 0 - (thickness/2), thickness, thickness)

for i in range(frames):
    phase = 2 * pi * i / frames
    startAngle = 90 * sin(phase)
    endAngle = 180 * sin(phase + 0.5 * pi)
    f = i / side
    
    points = []
    x = side * 0.1
    y = side * 0.9
    points.append((x, y))
    while x < side*0.9:
        x += 2
        if x < side*0.25:
            y = (-5.3333 * (x - (side * 0.1))) + (side * 0.9)
        elif x < side*0.5:
            y = (3.2 * (x - (side * 0.25))) + (side * 0.1)
        elif x < side*0.75:
            y = (-3.2 * (x - (side * 0.5))) + (side * 0.9)
        elif x < side*0.9:
            y = (5.3333 * (x - (side * 0.75))) + (side * 0.1)
        points.append((x, y))    
    
    newPage(side, side)
    fill(0)
    rect(0, 0, side, side)
    for point in points:
        with savedState():
            translate(point[0], point[1])
            shape(side*0.1)

saveImage('~/Desktop/23_36_DAYS_OF_TYPE_2020.mp4')