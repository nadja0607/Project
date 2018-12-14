import random,time,os
path = os.getcwd()

add_library('minim')
minim = Minim(this)

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
        

#creating balloon class
class Balloon(Object):
    def __init__(self,x,y,Width,Height,img,BColor):
        Object.__init__(self,x,y,Width,Height)
        self.img= loadImage(path+'/images/'+img) 
        self.BColor=BColor
        #self.bottomLeft=Point(self.x,self.y+self.Height)
        #self.bottomRight=Point(self.bottomLeft.x+self.Width,self.bottomLeft.y)
                            
    def display(self):
        image(self.img, self.x, self.y, self.Width, self.Height)
        
# class RedBalloon(Balloon):
#     def __init__(self,x,y,Width,Height,img):
#         Balloon.__init__(self,x,y,Width,Height,img)
#         self.img=loadImage(path+'/images/'+'4.png')
           
# class BlueBalloon(Balloon):
#     def __init__(self,x,y,Width,Height,img):
#         Balloon.__init__(self,x,y,Width,Height,img)
#         self.img=loadImage(path+'/images/'+'3.png')


class Boy(Object):
    def __init__(self,x,y,Width,Height):
        Object.__init__(self,x,y,Width,Height)
        self.points = 0
        self.arrows = []
        
        #defining keys to move the boy character - "a" for left and "d" for right
        self.keyHandler={65:False, 68:False} 
        self.imgBoy=loadImage(path+'/images/'+'boy.png')
    
    
    def display(self):
        image(self.imgBoy, self.x, self.y, self.Width, self.Height)
    
    #defining the character movements and direction 
    def update(self):
        if self.keyHandler[65]:
            #negative value for left
            self.vX =-20
            self.dir = -1
        elif self.keyHandler[68]:
            #positive value for right
            self.vX = 20
            self.dir = 1
        else:
            self.vX = 0
        # if self.keyHandler[87]:
        #     self.arrows.append(BlueArrow(self.x,self.y-80,100,100))
        #     self.keyHandler[87]=False
        #     print ("Boy: "+str(len(self.arrows)))
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
        self.keyHandler={LEFT:False, RIGHT:False}
        self.imgGirl = loadImage(path+'/images/'+'girl.png')
        self.points = 0
        self.arrows = []
    
    
    def display(self):
        image(self.imgGirl, self.x, self.y, self.Width, self.Height)
        
    def update(self):
        if self.keyHandler[LEFT]:
            self.vX = - 20
            self.dir = -1
        elif self.keyHandler[RIGHT]:
            self.vX = 20
            self.dir = 1
        else:
            self.vX = 0
        # if self.keyHandler[UP]:
        #     self.arrows.append(RedArrow(self.x,self.y-80,100,100))
        #     self.keyHandler[UP]=False
        #     print ("Girl: "+str(len(self.arrows)))
        self.x += self.vX
        
        #limiting the movement of characters, so they do not go off screen
        if self.x+self.Width > game.w:
            self.x = game.w-self.Width
        
        if self.x<0:
            self.x=0
            
            
poppedR=0
poppedB=0
gameover=0
   
class RedArrow(Object):
    def __init__(self,x,y,Width,Height):
        Object.__init__(self,x,y,Width,Height)
        self.imgArrow=loadImage(path+'/images/'+'arrow.png')
        self.keyHandler={UP:False}
        self.flying = 0
        self.score= 0
        # self.topCenter=Point(self.x+self.Width/2,self.y)
        # self.velocityConstant=15
        # self.vY-=self.velocityConstant
    
    def display(self):
        if self.score==numBalloons/2:
            image(self.imgGameOver,game.w/2-130,game.h/2-130,260,260)
            #displaying winner
            textSize(60)
            fill(255,0,0)
            text("Girl WON - Congratulations!!",game.w/2-380,game.h/2-200)
            global gameover
            gameover=1
            soundover.play()
        
        if gameover==0:
            if self.flying != 1:
                image(self.imgArrow, game.girl.x, self.y, self.Width, self.Height)
            else:
                image(self.imgArrow, self.x, self.y, self.Width, self.Height)
        
        #image(self.imgArrow, self.x, self.y, self.Width, self.Height) 
    def update(self):
        # if self.flying:
        #     self.y -=  self.velocityConstant
        #     # self.checkCollisions()
        #     return
        
        if self.keyHandler[UP]:
            self.flying = 1
            self.vY = -20
            self.dir = -1
            #print(self.x,self.y)
        else:
            self.x = game.girl.x
            self.vY = 0
            self.flying=0
            
        if self.flying==1:
            self.y += self.vY
        
    # def checkCollisions(self):
    #     for redBalloon in game.redBalloons:
    #         if (self.topCenter.y - redBalloon.bottomLeft.y<=0):                
    #             if (self.topCenter.x < redBalloon.bottomRight.x or self.topCenter.x > redBalloon.bottomLeft.x):
    #                 print("Collision detected")
    #                 game.redBalloons.remove(redBalloon)
    #                 del redBalloon
    #                 game.girl.arrows.remove(self)
        
         #checking red balloons 
        global poppedR 
        if poppedR==1: 
            self.x=game.girl.x
            self.y=game.girl.y-80
            self.flying=0
            self.vY=0
            self.keyHandler[UP]=False
            poppedR=0
        #limiting the movement of arrow, so it doesn't go off screen
        if self.y<0:
            poppedR=1
            
         #game.balloons.pop(1)
        for b in game.balloons:
            if (b.BColor==1 and self.x>=b.x-b.Width/2 and self.x<=b.x+b.Width/2 and self.y>=b.y and self.y<=b.y+b.Height):
                game.balloons.remove(b)
                self.score+=1
                poppedR=1
                popsound.rewind()
                popsound.play()
  
        
class BlueArrow(Object):
    def __init__(self,x,y,Width,Height):
        Object.__init__(self,x,y,Width,Height)
        self.imgArrow=loadImage(path+'/images/'+'arrow.png')
        self.imgGameOver=loadImage(path+'/images/'+'gameover.png')
        self.keyHandler={87:False} #87
        self.flying = 0
        self.score=0
        
    
    def display(self):
        # image(self.imgArrow, self.x, self.y, self.Width, self.Height)  
        if self.score==numBalloons/2:
            image(self.imgGameOver,game.w/2-130,game.h/2-130,260,260)
            #displaying winner
            textSize(60)
            fill(255,0,0)
            text("Boy WON - Congratulations!!",game.w/2-380,game.h/2-200)
            global gameover
            gameover=1
            soundover.play()
            
        if gameover==0:
            if self.flying != 1:
                image(self.imgArrow, game.boy.x, self.y, self.Width, self.Height)
            else:
                image(self.imgArrow, self.x, self.y, self.Width, self.Height) 
        
    def update(self):
        if self.keyHandler[87]:
            self.flying = 1
            self.vY = -20
            self.dir = -1
        else:
            self.x = game.boy.x
            self.vY = 0
            self.flying=0
            
        if self.flying==1:
            self.y += self.vY
        
        global poppedB
        if poppedB==1:
            self.x=game.boy.x
            self.y=game.boy.y-80
            self.flying=0
            self.vY=0
            self.keyHandler[87]=False
            poppedB=0
        #limiting the movement of arrow, so it doesn't go off screen
        if self.y<0:
            poppedB=1
        
    #def checkCollisions(self):
        # for blueBalloon in game.blueBalloons:
        #     if (self.topCenter.y - blueBalloon.bottomLeft.y<=0):                
        #         if (self.topCenter.x < blueBalloon.bottomRight.x and self.topCenter.x > blueBalloon.bottomLeft.x):
        #             print("Collision detected")
        #             game.blueBalloons.remove(blueBalloon)
        #             del blueBalloon
        #             game.girl.arrows.remove(self)
                    
          #game.balloons.pop(1)
        for b in game.balloons:
            if (b.BColor==0 and self.x>b.x-b.Width/2 and self.x<b.x+b.Width/2 and self.y>b.y and self.y<b.y+b.Height):
                game.balloons.remove(b)
                self.score+=1
                poppedB=1
                popsound.rewind()
                popsound.play()
        
        if self.score==numBalloons/2:
            print("Boy Won")   

#creating the main game class
class Game:
    def __init__(self,w,h):
        self.w=w
        self.h=h
        self.bImage1=loadImage(path+'/images/'+'2.png')
        self.bImage2=loadImage(path+'/images/'+'1.png')
        self.startButton=loadImage(path+'/images/'+'startbutton.jpg')
        self.mainMenu=0
        
        self.balloons=[]
        for i in range (numBalloons/2):
            self.balloons.append(Balloon(random.randint(0,self.w-255),random.randint(0,300),100,100,'3.png',0)) #0 red
            self.balloons.append(Balloon(random.randint(0,self.w-255),random.randint(0,300),100,100,'4.png',1)) #1 blue
            
            #self.balloons.shuffle() 
    #self.arrows=[]
    #for i in range (2):
        #self.arrows.append(Arrow)
            
        #creating the characters and arrows                       
        self.boy=Boy(0,600,100,150)
        self.girl=Girl(300,600,100,150)
        self.redArrow=RedArrow(self.girl.x,self.girl.y-80,100,100)
        self.blueArrow=BlueArrow(self.boy.x,self.boy.y-80,100,100)
        
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
        
        # for arrow in self.girl.arrows:        
        #     arrow.update()
        # for arrow in self.boy.arrows:        
        #     arrow.update()
        self.redArrow.update()
        self.blueArrow.update()
            
    
            
    def display(self):
        print("game disolay coede")
        
        self.bgDisplay()
        if self.mainMenu==1:
            self.boy.display()
            self.girl.display()
            self.redArrow.display()
            self.blueArrow.display()
            
        #displaying score
            textSize(32)
            fill(255,0,0)
            text("GIRL:"+str(self.redArrow.score),10,30)
            fill(0,0,255)
            text("BOY:"+str(self.blueArrow.score),10,70)
    
            if gameover==0:
                for b in self.balloons:
                    b.display()
            else:
            #Instructions to play
                textSize(25)
                fill(255,255,255)
                text("Player 1 - Boy moves with WASD",10,30)
                text("Player 2 - Girl moves with the keyboard arrows",10,60)
                text("The player that shoots his balloons first WINS the game!",10,90)
                text("Click START to begin the game",10,200)
            
                image(self.startButton,game.w/2-100,game.h/2-50,200,100)
            
       
        
game=Game(1000,800)
        
def setup():
    size(game.w,game.h)
    global birdsound
    global popsound
    global arrowshoot
    global soundover
    
    birdsound = minim.loadFile("birdsong.mp3")
    popsound = minim.loadFile("kill.mp3")
    arrowshoot = minim.loadFile("arrowshoot.mp3")
    soundover= minim.loadFile("gameover.wav")
    
    birdsound.loop()
    
def draw():
    background(10,250,200)
    game.update()
    game.display()
    
def mousePressed():
    if (mouseX>=game.w/2-100 and mouseX<=game.w/2+100 and mouseY>=game.h/2-50 and mouseY<=game.h/2+50):
        print("Mouse pressed")
        game.mainMenu=1
        draw()
    
def stop():
    minim.stop()
    
    
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
        if game.blueArrow.flying==0:
            arrowshoot.rewind()
            arrowshoot.play()
            game.blueArrow.keyHandler[87] = True
    elif keyCode == UP: 
        if game.redArrow.flying==0:
            arrowshoot.rewind()
            arrowshoot.play()
            #arrowshoot.close()
            game.redArrow.keyHandler[UP] = True

def keyReleased():
    if keyCode == 65: #a
        game.boy.keyHandler[65] = False
    if keyCode == 68: #d
        game.boy.keyHandler[68] = False
    if keyCode == LEFT:
        game.girl.keyHandler[LEFT] = False
    elif keyCode == RIGHT:
        game.girl.keyHandler[RIGHT] = False
