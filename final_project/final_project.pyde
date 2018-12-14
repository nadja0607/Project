import random,time,os
path = os.getcwd()

numBalloons=20

#general character
class Object:
    def __init__(self,x,y,Width,Height):
        self.x=x
        self.y=y
        self.Width=Width
        self.Height=Height
        self.vX=0
        self.vY=0
        self.dir=1
        
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

#creating balloon class
class Balloon:
    def __init__(self,x,y,Width,Height,img):
        self.x=x
        self.y=y
        self.Width=Width
        self.Height=Height
        self.img= loadImage(path+'/images/'+img) 
        self.bottomLeft=Point(self.x,self.y+self.Height)
        self.bottomRight=Point(self.bottomLeft.x+self.Width,self.bottomLeft.y)
                            
    def display(self):
        image(self.img, self.x, self.y, self.Width, self.Height)
        
class RedBalloon(Balloon):
    def __init__(self,x,y,Width,Height,img):
        Balloon.__init__(self,x,y,Width,Height,img)
        self.img=loadImage(path+'/images/'+'4.png')
           
class BlueBalloon(Balloon):
    def __init__(self,x,y,Width,Height,img):
        Balloon.__init__(self,x,y,Width,Height,img)
        self.img=loadImage(path+'/images/'+'3.png')


class Boy(Object):
    def __init__(self,x,y,Width,Height):
        Object.__init__(self,x,y,Width,Height)
        self.points = 0
        self.arrows = []
        #defining keys to move the boy character - "a" for left and "d" for right
        self.keyHandler={65:False, 68:False,87:False} 
        self.imgBoy=loadImage(path+'/images/'+'boy.png')
        self.velocityConstant = 30
    
    def display(self):
        image(self.imgBoy, self.x, self.y, self.Width, self.Height)
    
    #defining the character movements and direction 
    def update(self):
        if self.keyHandler[65]:
            #negative value for left
            self.vX -= self.velocityConstant
            self.dir = -1
        elif self.keyHandler[68]:
            #positive value for right
            self.vX = self.velocityConstant
            self.dir = 1
        else:
            self.vX = 0
        if self.keyHandler[87]:
            self.arrows.append(BlueArrow(self.x,self.y-80,100,100))
            self.keyHandler[87]=False
            print ("Boy: "+str(len(self.arrows)))
        #changing the location of the character    
        self.x += self.vX
        
        #limiting the movement of characters, so they do not go off screen
        if self.x+self.Width > game.w:
            self.x = game.w-self.Width
        
        if self.x<0:
            self.x=0
    
#same comments apply for the girl character    
class Girl(Object):
    def __init__(self,x,y,Width,Height):
        Object.__init__(self,x,y,Width,Height)
        self.keyHandler={LEFT:False, RIGHT:False,UP:False}
        self.imgGirl = loadImage(path+'/images/'+'girl.png')
        self.points = 0
        self.arrows = []
        self.velocityConstant = 30
    
    def display(self):
        image(self.imgGirl, self.x, self.y, self.Width, self.Height)
        
    def update(self):
        if self.keyHandler[LEFT]:
            self.vX -= self.velocityConstant
            self.dir = -1
        elif self.keyHandler[RIGHT]:
            self.vX = self.velocityConstant
            self.dir = 1
        else:
            self.vX = 0
        if self.keyHandler[UP]:
            self.arrows.append(RedArrow(self.x,self.y-80,100,100))
            self.keyHandler[UP]=False
            print ("Girl: "+str(len(self.arrows)))
        self.x += self.vX
        
        #limiting the movement of characters, so they do not go off screen
        if self.x+self.Width > game.w:
            self.x = game.w-self.Width
        
        if self.x<0:
            self.x=0
   
class RedArrow(Object):
    def __init__(self,x,y,Width,Height):
        Object.__init__(self,x,y,Width,Height)
        self.imgArrow=loadImage(path+'/images/'+'arrow.png')
        self.keyHandler={UP:False}
        self.flying = True
        self.topCenter=Point(self.x+self.Width/2,self.y)
        self.velocityConstant=15
        self.vY-=self.velocityConstant
    
    def display(self):
        image(self.imgArrow, self.x, self.y, self.Width, self.Height) 
    def update(self):
        if self.flying:
            self.y -=  self.velocityConstant
            return
        
        if self.keyHandler[UP]:
            self.flying = True
            self.vY = -self.velocityConstant
            self.dir = -1
        else:
            self.x = game.girl.x
            self.vY = 0
            
        self.y += self.vY
        
  
        
class BlueArrow(Object):
    def __init__(self,x,y,Width,Height):
        Object.__init__(self,x,y,Width,Height)
        self.imgArrow=loadImage(path+'/images/'+'arrow.png')
        self.keyHandler={87:False} #87
        self.flying = True
        self.topCenter=Point(self.x+self.Width/2,self.y)
        self.velocityConstant=15
        self.vY-=self.velocityConstant
        
    
    def display(self):
        image(self.imgArrow, self.x, self.y, self.Width, self.Height)  
        
    def update(self):
        if self.flying:
            self.y -=  self.velocityConstant
            self.checkCollisions()
            return
        
        if self.keyHandler[87]:
            self.flying = True
            self.vY = -self.velocityConstant
            self.dir = -1
        else:
            self.x = game.boy.x
            self.vY = 0
            
        self.y += self.vY
        
    def checkCollisions(self):
        for blueBalloon in game.blueBalloons:
            print(abs(self.topCenter.y - blueBalloon.bottomLeft.y))
            if (abs(self.topCenter.y - blueBalloon.bottomLeft.y)<=0):
                #print(abs(self.topCenter.y - blueBalloon.bottomLeft.y))
                if (self.topCenter.x < blueBalloon.bottomRight.x or self.topCenter.x > blueBalloon.bottomLeft.x):
                    print("Collision detected")
                    game.blueBalloons.remove(blueBalloon)
                    del blueBalloon
            

#creating the main game class
class Game:
    def __init__(self,w,h):
        self.w=w
        self.h=h
        self.bImage1=loadImage(path+'/images/'+'2.png')
        self.bImage2=loadImage(path+'/images/'+'1.png')
        
        self.redBalloons=[]
        self.blueBalloons=[]
        for i in range (numBalloons/2):
            self.blueBalloons.append(Balloon(random.randint(0,self.w-255),random.randint(0,300),100,100,'3.png'))
            self.redBalloons.append(Balloon(random.randint(0,self.w-255),random.randint(0,300),100,100,'4.png'))
            
        
    #self.arrows=[]
    #for i in range (2):
        #self.arrows.append(Arrow)
            
        #creating the characters and arrows                       
        self.boy=Boy(0,600,100,150)
        self.girl=Girl(300,600,100,150)# na press dodajemo u list
        self.girl.arrows.append(RedArrow(self.girl.x,self.girl.y-80,100,100))
        self.boy.arrows.append(BlueArrow(self.boy.x,self.boy.y-80,100,100))
        
        #self.redArrow=RedArrow(self.girl.x,self.girl.y-80,100,100)
        #self.blueArrow=BlueArrow(self.boy.x,self.boy.y-80,100,100)
        
    
    #displaying background images
    def bgDisplay(self):
            image(self.bImage1,0,0)
            image(self.bImage2,0,200,1000,800)
    
    def update(self):
        print("game.update code")
        self.boy.update()
        print("boy.update code")
        self.girl.update()
        print("girl.update code")
        
        for arrow in self.girl.arrows:        
            arrow.update()
        for arrow in self.boy.arrows:        
            arrow.update()
    
            
    def display(self):
        print("game disolay coede")
        self.bgDisplay()
        self.boy.display()
        self.girl.display()
        
        for arrow in self.boy.arrows:        
            arrow.display()
        for arrow in self.girl.arrows:        
            arrow.display()
        for b in self.redBalloons:
            b.display()
        for b in self.blueBalloons:
            b.display()
        
game=Game(1000,800)
        
def setup():
    size(game.w,game.h)
    
def draw():
    background(10,250,200)
    game.update()
    game.display()
    
def keyPressed():
    print("key pressed", keyCode)
    if keyCode == LEFT: #37
        game.girl.keyHandler[LEFT] = True
    elif keyCode == RIGHT: #39
        game.girl.keyHandler[RIGHT] = True
    elif keyCode == 65: #a
        game.boy.keyHandler[65] = True
    elif keyCode == 68: #d
        game.boy.keyHandler[68] = True
    elif keyCode == 87: #w
        game.boy.keyHandler[87] = True
    elif keyCode == UP: 
        game.girl.keyHandler[UP] = True #ne radi nam zbog liste
        print("Girl Key hander up pressed")


def keyReleased():
    if keyCode == 65: #a
        game.boy.keyHandler[65] = False
    if keyCode == 68: #d
        game.boy.keyHandler[68] = False
    if keyCode == LEFT:
        game.girl.keyHandler[LEFT] = False
    elif keyCode == RIGHT:
        game.girl.keyHandler[RIGHT] = False

#To Do List:
#Create a condition for shooting - if it touches a balloon and goes off screen, the arrow generates again / nova slicica strelice svaki put kad se klikne key
#pocetni menu
#Adding a score counter; the score will be shown in the end
#Adding sounds: click, win and gameover
#napraviti da se strijela vraca nazad do likova- vise stijela
#______________________________
#trebamo imati counter i da vidimo ko ima veci skor- da se pokaze ko je winner
