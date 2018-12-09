import random,time,os
path = os.getcwd()

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

class Boy(Object):
    def __init__(self,x,y,Width,Height):
        Object.__init__(self,x,y,Width,Height)
        #defining keys to move the boy character - "a" for left and "d" for right
        self.keyHandler={65:False, 68:False} 
        self.imgBoy=loadImage(path+'/images/'+'boy.png')
    
    def display(self):
        image(self.imgBoy, self.x, self.y, self.Width, self.Height)
    
    #defining the character movements and direction 
    def update(self):
        if self.keyHandler[65]:
            #negative value for left
            self.vX = -5
            self.dir = -1
        elif self.keyHandler[68]:
            #positive value for right
            self.vX = 5
            self.dir = 1
        else:
            self.vX = 0
        #changing the location of the character    
        self.x += self.vX
    
#same comments apply for the girl character    
class Girl(Object):
    def __init__(self,x,y,Width,Height):
        Object.__init__(self,x,y,Width,Height)
        self.keyHandler={LEFT:False, RIGHT:False}
        self.imgGirl = loadImage(path+'/images/'+'girl.png')
    
    def display(self):
        image(self.imgGirl, self.x, self.y, self.Width, self.Height)
        
    def update(self):
        if self.keyHandler[LEFT]:
            self.vX = -5
            self.dir = -1
        elif self.keyHandler[RIGHT]:
            self.vX = 5
            self.dir = 1
        else:
            self.vX = 0
            
        self.x += self.vX
   
class Arrow(Object):
    def __init__(self,x,y,Width,Height):
        Object.__init__(self,x,y,Gravity,Width,Height)
        self.keyHandler={UP:False}
        self.imgArrow=loadImage(path+'/images/'+'arrow.png')
    
    def display(self):
        image(self.imgArrow, self.x, self.y, self.Width, self.Height)

#creating the main game class
class Game:
    def __init__(self,w,h):
        self.w=w
        self.h=h
        self.bImage1=loadImage(path+'/images/'+'2.png')
        self.bImage2=loadImage(path+'/images/'+'1.png')
        
        #creating the characters                        
        self.boy=Boy(0,600,200,150)
        self.girl=Girl(300,600,100,150)
    
    #displaying background images
    def bgDisplay(self):
            image(self.bImage1,0,0)
            image(self.bImage2,0,300)
    
    def update(self):
        self.boy.update()
        self.girl.update()
            
    def display(self):
        self.bgDisplay()
        self.boy.display()
        self.girl.display()
        
        
game=Game(1280,720)
        
def setup():
    size(800,800)
    
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


def keyReleased():
    if keyCode == 65: #a
        game.boy.keyHandler[65] = False
    if keyCode == 68: #d
        game.boy.keyHandler[68] = False
    if keyCode == LEFT:
        game.girl.keyHandler[LEFT] = False
    elif keyCode == RIGHT:
        game.girl.keyHandler[RIGHT] = False

#TO Do List
#kako arrow da nam puca - shooting the arrows??
#limit the characters so they don't go off screen
#randomly placing balloons
#add score count
#add timer
#add sounds- on click and winning/losing/gameover
#what to do if they shoot from the same place
