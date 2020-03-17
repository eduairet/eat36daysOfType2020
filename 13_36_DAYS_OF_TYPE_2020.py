side = 1080
g = -9.81
t = 5
angle = atan(0.18167) * (180/pi)
print('angle =', angle)
v = 135 / cos(radians(angle))
v = 24.525 / sin(radians(angle))
print('v =', v)
vx = v * (cos(radians(angle)))
print('vx =', vx)
vy = v * (sin(radians(angle)))
print('vy =', vy)

r = []
ts = 5/120
for i in range(t * 24):
    r.append(g * 0.5 * (((i + 1) * ts)**2))
#print(r)
    
def fountain():
    x = 0
    y = 0
    ts = 5/120
    points = []
    points.append((x, y))
    for i in range(t * 24):
        x = vx * ((i + 1) * ts)
        y = (vy * ((i + 1) * ts)) + r[i]
        points.append((x, y))
    points.append(None)
    return points

def projectile(step):
    stroke(1)
    strokeWidth(0.1)
    fill(None)
    lineCap("round")
    points = fountain()
    sc = 1.0
    for i in range(step):
        path = BezierPath()
        path.moveTo((0, 0))
        path.qCurveTo(*points)
        path.closePath() 
        with savedState(): 
            scale(x=1, y=sc, center=(0, 0))
            drawPath(path)
        sc += i
        
for i in range(60):
    newPage(side, side)
    fill(0)
    rect(0, 0, side, side)
    projectile(i)
    translate(1080 - 674.9876149061486, 0)
    projectile(i)

saveImage("~/Desktop/13_36_DAYS_OF_TYPE_2020.mp4")