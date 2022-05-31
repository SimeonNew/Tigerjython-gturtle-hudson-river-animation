from gturtle import *
from random import randint

Options.setPlaygroundSize(1000, 1000)

def cloud(cloudX, cloudY):
    repeat(100):
        c = makeColor(randint(235, 255), randint(255, 255), randint(255, 255))
        setPenColor(c)
        setFillColor(c)
        x = randint (cloudX-100, cloudX+100)
        y = randint (cloudY-50, cloudY+50)
        setPos(x, y)
        dot(40)
        
def explosion(explosionX, explosionY):
    penUp()
    heading(0)
    repeat 8:
        releaseX = randint(explosionX-10,explosionY+10)
        setPos(releaseX,explosionY)
        speedX=1
        SPD = 1 + 0.1
        repeat(40):
            smokeVariety = randint(0,100)
            setH(randint(-100, -70))
            fd(speedX)
            penDown()
            smokeDotDraw(5,15)
            penUp()
            speedY=3
            speedY = speedY * smokeVariety/60
            speedX = speedX *SPD
            moveX = speedX + smokeVariety*2
    penDown()
            
    heading(90)



def smokeDotDraw(size1,size2):
    smokeSize = randint(size1,size2)
    smokeColor = makeColor(randint(255, 255), randint(75, 200), randint(0, 200))
    setPenColor(smokeColor)
    dot(smokeSize)
        
        
def draw_motor():
    repeat(5):
        dot(50)
        heading(90)
        fd(10)
    

def draw_spoiler(rotation):
    startPath()
    left(90)
    fd(100)
    right(90)
    fd(10)
    right(45)
    fd(100)
    fillPath()

    
def draw_window(x, y):
    windowX = x
    windowY = y-6
    setPenColor('lightBlue')

    repeat(12):
        heading(0)
        setPos(windowX, windowY)
        dot(15)
        fd(7)
        dot(15)
        heading(90)
        windowX = windowX+25
        
        
    
    
def draw_Airplane(x,y, rotation, count):
    setPos(x, y)
    setFillColor("white")
    dotSize = 71
    while count<(30):
        setPenColor("white")
        dot(75)
        fd(10)
        count = count+1
        
    while count<36 and count>=30:
        dot(dotSize)
        fd(5)
        heading(180)
        fd(1.2)
        heading(90)
        dotSize = dotSize-4
        count = count+1
    penUp()
    setPos(x-35, y)
    penDown()
    draw_spoiler(rotation)
    draw_window(x,y)
    penUp()
    setPos(x+100, y-40)
    penDown()
    draw_motor()
    
def draw_Bird(wingAngle, birdX, birdY):
    setPos(birdX, birdY)
    startPath()
    setPenColor('orange')
    setFillColor('orange')
    heading(260)
    fd(10)
    right(160)
    fd(10)
    right(98.4)
    fd(3.5)
    fillPath()
    startPath()
    setPenColor(makeColor(110, 72, 58))
    setFillColor(makeColor(110, 72, 58))
    leftArc(30, 60)
    heading(180)
    fd(10)
    right(90)
    fd(3)
    right(180)
    fd(3)
    heading(0)
    fd(10)
    right(100)
    leftArc(20, 30)
    fd(30)
    leftArc(3, 180)
    fd(5)
    right(180)
    fd(20)
    leftArc(3, 160)
    fd(40)
    right(80)
    leftArc(17, 190)
    fillPath()
    left(90)
    fd(20)
    draw_Wing(wingAngle)
    
def draw_Wing(orientation):
    startPath()
    setFillColor('gray')
    setPenColor('gray')
    heading(orientation)
    fd(40)
    rightArc(5, 160)
    fd(43)
    heading(270)
    rightArc(12, 180)
    fillPath()   
    


makeTurtle()
hideTurtle()
enableRepaint(False)
wingAngle = 90
birdX = 0
birdY = 0
x = -570
y = 0
count = 0
cloudX = 0
cloudY= 0
right(90)
clear('lightSkyBlue')
rotation = 90
while x < 550:
    draw_Airplane(x,y, rotation, count)
    x = x+10
    repaint()
    delay(100)
    clear('lightSkyBlue')
    cloud(cloudX+100, cloudY+300)
    cloud(cloudX-205, cloudY-389)
    cloud(cloudX+205, cloudY+329)
    cloud(cloudX-300, cloudY+0)
    y = y+1
    
while x >=550 and x<= 560:
    clear('black')
    repaint()
    x = x+1
    delay(100)
    
while x >=560 and x <= 570:
    
    repeat(4):
        clear('lightSkyBlue')
        cloud(cloudX-100, cloudY+300)
        cloud(cloudX-205, cloudY-389)
        cloud(cloudX+205, cloudY+329)
        cloud(cloudX-505, cloudY-290)
        cloud(cloudX-305, cloudY+50)
        cloud(cloudX-605, cloudY-329)
        cloud(cloudX-905, cloudY)
        draw_Bird(wingAngle, birdX, birdY)
        repaint()
        delay(100)
        cloudX = cloudX+5
        wingAngle = wingAngle -5
        birdY = birdY-3
    repeat(4):
        clear('lightSkyBlue')
        cloud(cloudX-100, cloudY+300)
        cloud(cloudX-205, cloudY-389)
        cloud(cloudX+205, cloudY+329)
        cloud(cloudX-505, cloudY-290)
        cloud(cloudX-305, cloudY+50)
        cloud(cloudX-605, cloudY-329)
        cloud(cloudX-905, cloudY+20)
        draw_Bird(wingAngle, birdX, birdY)
        repaint()
        delay(100)
        cloudX = cloudX+5
        wingAngle = wingAngle +5
        birdY = birdY+3
        
    x = x+1
    
    
while x >=570 and x<= 580:
    clear('black')
    repaint()
    x = x+1
    delay(100)
  
airplaneX = -100
airplaneY = 0  
birdX = 800
birdY = -15
while x >= 580 and x<= 582:
    repeat(4):
        draw_Airplane(airplaneX,airplaneY, rotation, count)
        cloud(cloudX+100, cloudY+300)
        cloud(cloudX-205, cloudY-389)
        cloud(cloudX+205, cloudY+329)
        cloud(cloudX-500, cloudY+0)
        draw_Bird(wingAngle, birdX, birdY)
        wingAngle = wingAngle -5
        birdY = birdY-3
        x = x+1
        cloudX = cloudX - 7
        repaint()
        delay(100)
        clear('lightSkyBlue')
        birdX = birdX-50
    repeat(4):
        draw_Airplane(airplaneX,airplaneY, rotation, count)
        cloud(cloudX+100, cloudY+300)
        cloud(cloudX-205, cloudY-389)
        cloud(cloudX+205, cloudY+329)
        cloud(cloudX-500, cloudY+0)
        draw_Bird(wingAngle, birdX, birdY)
        wingAngle = wingAngle +5
        birdY = birdY+3
        x = x-1
        cloudX = cloudX - 7
        repaint()
        delay(100)
        clear('lightSkyBlue')
        birdX = birdX-50
        
    x = x+1
    
    
while x > 582 and x<= 620:
    draw_Airplane(airplaneX,airplaneY, rotation, count)
    cloud(cloudX+100, cloudY+300)
    cloud(cloudX-205, cloudY-389)
    cloud(cloudX+205, cloudY+329)
    cloud(cloudX-500, cloudY+0)
    explosion(airplaneX+70, airplaneY-40)
    x = x+1
    cloudX = cloudX - 7
    repaint()
    delay(100)
    clear('lightSkyBlue')

    
    

    
    
    
    