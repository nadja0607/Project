import random,time,os
path = os.getcwd()

class Object:
    def __init__(self,x,y,Width,Height):
        self.x=x
        self.y=y
        self.Width=Width
        self.Height=Height
        self.velocityX=0
        self.velocityY=0
 
class Boy(Object):
    def __init__(self,x,y,Width,Height):
        Object.__init__(self,x,y,Width,Height)
        self.keyHandler={LEFT:False, RIGHT:False}
        self.imgBoy=loadImage(path+'/images/'+'boy.png')
    
    def display(self):
        image(self.imgBoy, self.x, self.y, self.Width, self.Height)
        
class Girl(Object):
    def __init__(self,x,y,Width,Height):
        Object.__init__(self,x,y,Width,Height)
        self.keyHandler={LEFT:False, RIGHT:False}
        self.imgGirl = loadImage(path+'/images/'+'girl.png')
    
    def display(self):
        image(self.imgGirl, self.x, self.y, self.Width, self.Height)

#skontati kako da ubacimo iznad glava arrow i kako da na klik idu prema gore    
class Arrow(Object):
    def __init__(self,x,y,Width,Height):
        Object.__init__(self,x,y,Gravity,Width,Height)
        self.keyHandler={UP:False}
        self.imgArrow=loadImage(path+'/images/'+'arrow.png')
    def display(self):
        image(self.imgArrow, self.x, self.y, self.Width, self.Height)

class Game:
    def __init__(self,w,h):
        self.w=w
        self.h=h
        self.bImage1=loadImage(path+'/images/'+'2.png')
        self.bImage2=loadImage(path+'/images/'+'1.png')
        
                                
        self.boy=Boy(0,600,200,150)
        self.girl=Girl(300,600,100,150)

    def bgDisplay(self):
            image(self.bImage1,0,0)
            image(self.bImage2,0,300)
            
    def display(self):
        self.bgDisplay()
        self.boy.display()
        self.girl.display()
        
        
game=Game(1280,720)
        
def setup():
    size(800,800)
    
def draw():
    background(10,250,200)
    game.display()
    
def keyPressed():
    if key == "a":
        print("a was pressed")
        
#kako odabrati razlicite tipoke za boy and girl da idu lijevo desno i za arrow
