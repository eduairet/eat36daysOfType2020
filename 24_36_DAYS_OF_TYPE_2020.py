side = 1080
frames = 96
chars = 1260
myFont = "OCRAStd"
fSize = 5

text = 'abcdefghijklmnopqrstuvwxyz'
textUpper = ''
for letter in text:
     textUpper += letter.upper()
text += textUpper

path = BezierPath()
path.text("x", font=myFont, fontSize=500)
indent = 108
minx, miny, maxx, maxy = path.bounds()
w = maxx - minx
h = maxy - miny
boxWidth = width() - indent * 2
boxHeight = height() - indent * 2
s = min([boxWidth / float(w), boxHeight / float(h)])

dec = 0
for i in range(frames):
    newPage(side, side)
    fill(0)
    rect(0, 0, side, side)
    translate(width()*.5, height()*.5)
    scale(s)
    translate(-minx, -miny)
    translate(-w*.5, -h*.5)
    drawPath(path)
    
    if i < frames*0.333:
        t = FormattedString()
        t.font(myFont)
        t.fontSize(fSize)
        for j in range(int(i*(chars/(frames/3)))):
            t.fill(0, 1, randint(0, 200)/255)    
            t += choice(text)
        textBox(t, path)
    
    elif frames*0.333 < i < frames*0.666:
        t = FormattedString()
        t.font(myFont)
        t.fontSize(fSize)
        for k in range(chars):
            t.fill(0, 1, randint(0, 200)/255)    
            t += choice(text)
        textBox(t, path)
    
    else:
        t = FormattedString()
        t.font(myFont)
        t.fontSize(fSize)
        for l in range(int(frames/3*(chars/(frames/3)))):
            t.fill(0, 1, randint(0, 200)/255)    
            t += choice(text)
        t = t[:int(-chars/(frames/3)) - dec]
        textBox(t, path)
        dec += chars/(frames/3)

saveImage('~/Desktop/24_36_DAYS_OF_TYPE_2020.mp4')