from gturtle import * 

from random import randint 

 

Options.setPlaygroundSize(1000, 1000) 

# eine liste von wo die gebäude sind und wie sie aussehen
def nyc(height):
    building(-500,height,70,50,0) 
    
    
    building(-445,height,40,30,False) 

    building(-410,height,30,30,False) 
    
    building(-370,height,90,30,True) 

    building(-355,height,50,30,False) 

    building(-320,height,20,20,False) 

    building(-295,height,70,35,False) 

    building(-258,height,50,35,False) 

    building(-220,height,140,35,True) 

    building(-182,height,70,30,False) 

    building(-150,height,50,40,False) 

    building(-108,height,40,30,False) 

    building(-75,height,70,30,False) 

    building(-40,height,120,30,True) 

    building(-6,height,30,30,False) 

    building(30,height,65,35,True) 

    building(70,height,65,35,True) 

    building(110,height,77,50,False) 

    building(162,height,55,45,False) 

    building(210,height,30,30,False) 

    building(245,height,50,30,False) 

    building(280,height,100,45,True) 

    building(332,height,50,40,False) 
    
    building(379,height,70,30,True)
    
    building(420,height,90,30,False)
    
    building(452,height,50,40,False)
    
    repaint()


# template für die gebäude
def building(buildingX,buildingY,height,width,ifStrich): 
    
    home()
    
    setPos(buildingX,buildingY) 

    setPenColor("black") 

    fillToPoint() 

    forward(height) 

    right(90) 

    fd(width) 

    rt(90) 

    fd(height) 

    fillOff() 
    

    if (ifStrich == True): 

        setPos(buildingX+width/2,buildingY+height) 

        setHeading(0) 

        setPenWidth(1) 

        fd(20) 

        dot(5) 
        
    
 
#eine random generierte wolke
def cloud(cloudX, cloudY): 

    repeat(100): 

        c = makeColor(randint(235, 255), randint(255, 255), randint(255, 255)) 

        setPenColor(c) 

        setFillColor(c) 

        x = randint (cloudX-100, cloudX+100) 

        y = randint (cloudY-50, cloudY+50) 

        setPos(x, y) 

        dot(40) 

#einfache nichtbewegende welle  
def wave():
    repeat(10):
        leftArc(50,85)
        rightArc(50,85)
        
#welle die sich bewegt
def draw_wave(y):
    setPos(-440,y)
    setLineWidth(5)
    right(42.5)
    rightArc(50,90)
    waveX= -445-50
    increment = 0
    repeat(200):
        clear()
        setPos(waveX,y)
        wave()
        if increment < 25:
            waveX = waveX-5
            increment = increment+1
        else: 
            waveX = -445-50
            increment = 0
            
        setPos(waveX,y-100)
        wave()
        if increment < 25:
            waveX = waveX-5
            increment = increment+1
        else: 
            waveX = -445-50
            increment = 0
            
        
        setPos(waveX,y-50)
        wave()
        repaint()
        delay(100)
        if increment < 25:
            waveX = waveX-5
            increment = increment+1
        else: 
            waveX = -445-50
            increment = 0

         
#particle system für explosion
def explosion(explosionX, explosionY): 

    penUp() 

    heading(0) 

    repeat 8: 

        releaseX = randint(round(explosionX-10, 0), round(explosionX+10, 0)) 

        setPos(releaseX,explosionY) 

        speedX=1 

        SPD = 1 + 0.1 

        repeat(40): 

            particleVariety = randint(0,100) 

            setH(randint(-100, -70)) 

            fd(speedX) 

            penDown() 

            particle(5,15) 

            penUp() 

            speedY=3 

            speedY = speedY * particleVariety/60 

            speedX = speedX *SPD 

            moveX = speedX + particleVariety*2 

    penDown() 

             

    heading(90) 

 

 

 
#dot der random farbe und random grösse
def particle(size1,size2): 

    particleSize = randint(size1,size2) 

    particleColor = makeColor(randint(255, 255), randint(75, 200), randint(0, 200)) 

    setPenColor(particleColor) 

    dot(particleSize) 

         

         
#motor des flugzeuges
def draw_motor(rotation, size): 

    heading(rotation) 

    repeat(5): 

        dot(size*0.7142) 

        fd(size*0.143) 

     

 
#der sploiler
def draw_spoiler(rotation, size): 

    heading(rotation) 

    startPath() 

    left(90) 

    fd(size*1.42857) 

    right(90) 

    fd(size*0.142857) 

    right(45) 

    fd(size*1.42857) 

    fillPath() 

 

     
#reihe an fenstern
def draw_window(windowX, windowY, rotation, size): 

    heading(rotation) 

    setPenColor('lightBlue') 

    setPos(windowX, windowY) 

    left(90) 

    repeat(12): 

        penDown() 

        dot(size*0.211) 

        fd(size*0.0986) 

        dot(size*0.211) 

        penUp() 

        right(180) 

        fd(size*0.0986) 

        left(90) 

        fd(size*0.3521) 

        left(90) 

     

             
#das ganze flugzeug
def draw_Airplane(x,y, rotation, count, size): 

    heading(rotation) 

    setPos(x, y) 

    setFillColor("white") 

    dotSize = size 

    while count<(30): 

        setPenColor("white") 

        dot(size+4) 

        fd(size/7) 

        count = count+1 

         

    while count<36 and count>=30: 

        dot(dotSize) 

        fd(size/14) 

        heading(180) 

        fd(size/58.3) 

        heading(90) 

        dotSize = dotSize-4 

        count = count+1 

    penUp() 

    setPos(x-size*0.4929, y) 

    penDown() 

    draw_spoiler(rotation, size) 

    draw_window(x,y, rotation, size) 

    penUp() 

    setPos(x+size*1.4084, y-size*0.563380) 

    penDown() 

    draw_motor(rotation, size) 

     
#der vogel ohne animation
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

     
#der flügel vom flugzeug
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

     

 


nycHeight = 0

wingAngle = 90 

birdX = 0 

birdY = 0 

x = -600

y = 0 

count = 0 

cloudX = 0 

cloudY= 0 

rotation = 90 

airplaneSize = 71 

def scene1(x,y, rotation, count, airplaneSize):
    repeat(115): 

        draw_Airplane(x,y, rotation, count, airplaneSize) 

        x = x+10 

        repaint() 

        delay(100) 

        clear('lightSkyBlue') 

        cloud(cloudX+100, cloudY+300) 

        cloud(cloudX-205, cloudY-389) 

        cloud(cloudX+205, cloudY+329) 

        cloud(cloudX-300, cloudY+0) 

        y = y+1 

     
def blackScreen():
    repeat(10): 

        clear('black') 

        repaint() 

        delay(100) 

     
def scene2(x, cloudX, cloudY, wingAngle, birdX, birdY):
    repeat(10): 
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

   


def scene3(x, rotation, count, airplaneSize, wingAngle, cloudX):
    airplaneX = -100 
    airplaneY = 0   
    birdX = 800 
    birdY = -15 
    repeat(2): 
        repeat(4): 

            draw_Airplane(airplaneX,airplaneY, rotation, count, airplaneSize) 

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

            draw_Airplane(airplaneX,airplaneY, rotation, count, airplaneSize)

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

     

     

 

     

def scene4(x, count, airplaneSize, cloudY):
    cloudX = -120
    airplaneX = -100
    airplaneY = 0
    rotation = 90   
    x = 582  
    repeat(38): 
        draw_Airplane(airplaneX,airplaneY, rotation, count, airplaneSize) 
    
        explosion(airplaneX+airplaneSize, airplaneY-airplaneSize*0.525) 
    
        cloud(cloudX+100, cloudY+300) 

        cloud(cloudX-205, cloudY-389) 

        cloud(cloudX+205, cloudY+329) 

        cloud(cloudX-500, cloudY+0) 

    


        airplaneY = airplaneY-20 

        cloudX = cloudX - 7 

        repaint() 

        delay(100) 

        clear('lightSkyBlue')  
        print(x)
        if x > 582 and x < 592: 

            rotation = rotation+1   
        
        x = x+1 


def scene5(x):
    increment = 0  
    y = -50   
    waveX= 750 
    repeat(20): 
        clear('lightSkyBlue')
        nyc(nycHeight)
        x = x+1 
        setPos(-440,y)
        setPenColor('blue')
        setLineWidth(5)
        right(42.5+90)
        setPos(waveX,y)
        wave()
        
        setPos(waveX,y-50)
        wave()
        
        setPos(waveX,y-100)
        wave() 
        
        setPos(waveX,y-150)
        wave()
    
        setPos(waveX,y-200)
        wave()
    
        setPos(waveX,y-250)
        wave()
    
        setPos(waveX,y-300)
        wave()
    
        setPos(waveX,y-350)
        wave()
    
        setPos(waveX,y-350)
        wave()
    
        setPos(waveX,y-400)
        wave()
    
        setPos(waveX,y-450)
        wave()
    
        setPos(waveX,y-500)
        wave()
        repaint()
        delay(100)
        if increment < 67:
            waveX = waveX-2
            increment = increment+1
        else:
            waveX = 750
            increment = 0
    
    
 

def scene6(x, count, airplaneSize): 
    rotation = 100 
    nycHeight= -600
    airplaneY = 0
    airplaneX = -400
    waveX = 750   
    increment = 0
    repeat(60): 
        clear('lightSkyBlue')
        nyc(nycHeight)
    
        setPenColor('blue')
        setLineWidth(5)
        right(42.5+90)
        setPos(waveX,nycHeight-50)
        wave()
        
        setPos(waveX,nycHeight-100)
        wave() 
        
        setPos(waveX,nycHeight-150)
        wave()
    
        setPos(waveX,nycHeight-200)
        wave()
    
        setPos(waveX,nycHeight-250)
        wave()
    
        setPos(waveX,nycHeight-300)
        wave()
    
        setPos(waveX,nycHeight-350)
        wave()
    
        setPos(waveX,nycHeight-350)
        wave()
    
        setPos(waveX,nycHeight-400)
        wave()
    
        setPos(waveX,nycHeight-450)
        wave()
    
        setPos(waveX,nycHeight-500)
        wave()
    
        repaint()
    
    
        draw_Airplane(airplaneX,airplaneY, rotation, count, airplaneSize*0.571428)
        explosion(airplaneX+41, airplaneY-airplaneSize+50) 
        delay(100)
        if increment < 67:
            waveX = waveX-2
            increment = increment+1
        else:
            waveX = 750
            increment = 0
        x = x+1
        airplaneX = airplaneX+5
        nycHeight= nycHeight+12


def scene7(x, airplaneSize): 
    nycHeight=120
    airplaneX = -100
    airplaneY = 0
    rotation = 90 
    waveX = 750 
    increment = 0 
    repeat(20): 
        clear('lightSkyBlue')
        nyc(nycHeight)
    
        setPenColor('blue')
        setLineWidth(5)
        right(42.5+90)
        setPos(waveX,nycHeight-50)
        wave()
        
        setPos(waveX,nycHeight-100)
        wave() 
        
        setPos(waveX,nycHeight-150)
        wave()
    
        setPos(waveX,nycHeight-200)
        wave()
    
        setPos(waveX,nycHeight-250)
        wave()
    
        setPos(waveX,nycHeight-300)
        wave()
    
        setPos(waveX,nycHeight-350)
        wave()
    
        setPos(waveX,nycHeight-350)
        wave()
    
        setPos(waveX,nycHeight-400)
        wave()
    
        setPos(waveX,nycHeight-450)
        wave()
    
        setPos(waveX,nycHeight-500)
        wave()
    
        repaint()
    
    
        draw_Airplane(airplaneX,airplaneY, rotation, count, airplaneSize*0.571428)
        explosion(airplaneX+41, airplaneY-airplaneSize+50) 
        delay(100)
        if increment < 67:
            waveX = waveX-2
            increment = increment+1
        else:
            waveX = 750
            increment = 0
        x = x+1
        airplaneX = airplaneX+5
        
   
makeTurtle() 

hideTurtle() 

enableRepaint(False) 
  
right(90) 

clear('lightSkyBlue')          
            
#alle scenen abgespielt       
scene1(x, y, rotation, count, airplaneSize)
blackScreen()
scene2(x, cloudX, cloudY, wingAngle, birdX, birdY)
blackScreen()
scene3(x, rotation, count, airplaneSize, wingAngle, cloudX)
scene4(x, count, airplaneSize, cloudY)
scene5(x)
scene6(x, count, airplaneSize)
scene7(x, airplaneSize)
   
     
