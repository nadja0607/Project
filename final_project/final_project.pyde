import random,time,os
path = os.getcwd()

class Object:
    def __init__(self,x,y,Gravity,Width,Height):
        self.x=x
        self.y=y
        self.Gravity=Gravity
        self.Width=Width
        self.Height=Height
        self.velocityX=0
        self.velocityY=0
 
class Boy(Object):
    def __init__(self,x,y,Gravity,Width,Height):
        Object.__init__(self,x,y,Gravity,Width,Height)
        self.keyHandler={LEFT:False, RIGHT:False, UP:False}
        self.imgBoy=loadImage(path+'/images/'+'boy.png')

def setup():
    size(800,800)
    
def draw():
    background(0)
    
