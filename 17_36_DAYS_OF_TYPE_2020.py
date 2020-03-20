side = 1080

def lsPts(num):
    points = []
    m = side*0.3
    if num == 1:
        for i in range(0, side, 12):
            if i <= side*0.1:
                x = i
                y = sin((i*(randint(1, 3))))
                points.append((x, y))
            if i > side*0.1 and i <= side*0.4:
                x = i
                y = i*sin(radians(i*(randint(-100, 100))))/(10**1)
                if y < 0:
                    points.append((x, y * -1))
                else:
                    points.append((x, y))
            if i > side*0.4 and i <= side*0.7:
                x = i
                y = m*sin(radians(m*(randint(-100, 100))))/(10**1)
                if y < 0:
                    points.append((x, y * -1))
                else:
                    points.append((x, y))
                m -= 1
            if i > side*0.7 and i <= side*0.8:
                x = i
                y = sin((i*(randint(1, 3))))
                points.append((x, y))
    if num == 2:
        for i in range(0, side, 12):
            if i <= side*0.1:
                x = i
                y = sin((i*(randint(1, 3))))
                points.append((x, y))
            if i > side*0.1 and i <= side*0.3:
                x = i
                y = i*sin(radians(i*(randint(-100, 100))))/(10**1)
                if y < 0:
                    points.append((x, y * -1))
                else:
                    points.append((x, y))
            if i > side*0.3 and i <= side*0.5:
                x = i
                y = sin((i*(randint(1, 3))))
                points.append((x, y))
            if i > side*0.5 and i <= side*0.7:
                x = i
                y = m*sin(radians(m*(randint(-100, 100))))/(10**1)
                if y < 0:
                    points.append((x, y * -1))
                else:
                    points.append((x, y))
                m -= 1
            if i > side*0.7 and i <= side*0.8:
                x = i
                y = sin((i*(randint(1, 3))))
                points.append((x, y))
    if num == 3:
        for i in range(0, side, 12):
            if i <= side*0.1:
                x = i
                y = sin((i*(randint(1, 3))))
                points.append((x, y))
            if i > side*0.1 and i <= side*0.4:
                x = i
                y = i*sin(radians(i*(randint(-100, 100))))/(10**1)
                if y < 0:
                    points.append((x, y * -1))
                else:
                    points.append((x, y))
            if i > side*0.4 and i <= side*0.8:
                x = i
                y = m*sin(radians(m*(randint(-100, 100))))/(10**1)
                if y < 0:
                    points.append((x, y * -1))
                else:
                    points.append((x, y))
                m -= 1
    return points

def lineGrid(steps):
    for j in range(steps):
        newPage(side, side)
        fill(0)
        rect(0, 0, side, side)
        m = 0
        fill(None)
        stroke(0, 1, 1)
        strokeWidth(1)
        shadow((0, 0), 1, (1, 1, 1))
        for i in range(int(side*0.8/13.5)):
            if i <= 14:
                points = lsPts(3)
                path = BezierPath()
                with savedState():
                    translate(side*0.1, side*0.1 + m)
                    path.moveTo((0, 0))
                    path.curveTo(*points)
                    drawPath(path)
            if i > 14 and i <= 50:
                points = lsPts(2)
                path = BezierPath()
                with savedState():
                    translate(side*0.1, side*0.1 + m)
                    path.moveTo((0, 0))
                    path.curveTo(*points)
                    drawPath(path)
            if i > 50:
                points = lsPts(1)
                path = BezierPath()
                with savedState():
                    translate(side*0.1, side*0.1 + m)
                    path.moveTo((0, 0))
                    path.curveTo(*points)
                    drawPath(path)
            m += 13.5

for i in range(6):
    lineGrid(i)

saveImage('~/Desktop/17_36_DAYS_OF_TYPE_2020.mp4')