from newMath import vector
from vector import *
import  time
from math import *
from painter import *

class body:
    def __init__(self , shape ="oval"  , color = "white" , mass =1.0 ,   dimension =[0,0,1,1] , pos = Vector2(0,0) , canvas = None):
        self.shape        =  shape                  #  shape : string
        self.color         =  color                  #  color : string
        self.m               =  mass                   # mass : float
        self.pos            =  pos                      # position : Vector 2D
        self.v                =  Vector2(0,0)      # velocity : Vector 2D
        self.a                =  Vector2(0,0)      # acceleration : Vector 2D
        # dimension : [x1,y1,x2,y2]
        a,b,c,d               =  dimension
        self.p1 , self.p2 = Vector2(a,b) , Vector2(c,d)
        self.shapes       = { "oval" : canvas.create_oval , "rect" : canvas.create_rectangle }
        self.uid             =  self.shapes[ self.shape ]( self.p1.x  ,  self.p1.y  ,  self.p2.x  ,  self.p2.y  ,  fill = self.color  )
        self.anim()
        
    def anim(self):
        self.v     +=  self.a*0.00000001  # v = u + at
        ds             =  self.v*0.00000001  # ds = vdt
        self.pos +=  ds           # s = s + ds
        self.p1   +=  ds          # s = s + ds
        self.p2   +=  ds          # s = s + ds
        self.shapes[ self.shape ]( self.p1.x  ,  self.p1.y  ,  self.p2.x  ,  self.p2.y  ,  fill = self.color  )
       
class collider:
    def __init__( self ,canvas):
        self.cols = (0 , 0) # denotes just previous collision
        self.canvas = canvas
    def collision(self , a , b , e = 1):# a,b : body , e = elastic coefficient.
        self.canvas.create_rectangle(a.p1.x-1,a.p1.y-1,a.p2.x+1,a.p2.y+1,outline = "red")
        self.canvas.create_rectangle(b.p1.x-1,b.p1.y-1,b.p2.x+1,b.p2.y+1,outline = "red")
        
        if self.cols != (a.uid,b.uid) and v :
            print "collision:",a.color,b.color
            m1 , m2  = a.m , b.m
            r    = (b.pos-a.pos).normalise()
            u1 ,  u2   = a.v.dot(r) , b.v.dot(r)
            v1   = (((1+e) * (u2 - u1)) / (m1/m2+1)) * r # change in velocity
            v2   = (((1+e) * (u1 - u2)) / (m2/m1+1)) * r # change in velocity
            a.v+=v1
            b.v+=v2
            self.cols = (a.uid,b.uid)
            
    def anim(self , bds):#bds:bodies
        for i in range(len(bds)):
            for j in range(i+1,len(bds)):
                self.collision(bds[i],bds[j])


### main
bodies = []
coll = None
def  setup(Canvas):
    global bodies , coll
    coll = collider(Canvas)
    bodies.append( body( shape = "oval" , color = "red" , mass = 2.0  , dimension = [200,200,210,210] , pos = Vector2(205,205) , canvas = Canvas ))
    bodies.append( body( shape = "oval" , color = "blue" , mass = 2.0  , dimension = [170,300,180,310] , pos = Vector2(255,105) , canvas = Canvas ))
    for i in range(10):
        bodies.append( body( shape = "rect" , color = "yellow" , mass = 100000.0  , dimension = [170+i*10 + 2,170,180+i*10,180] , pos = Vector2(175+i*5,175) , canvas = Canvas ))
    for i in range(1,10):
        bodies.append( body( shape = "rect" , color = "yellow" , mass = 100000.0  , dimension = [170+i*10 + 2,280,180+i*10,290] , pos = Vector2(175+i*5,285) , canvas = Canvas ))
    for i in range(1,10):
        bodies.append( body( shape = "rect" , color = "yellow" , mass = 100000.0  , dimension = [170,170+i*10 + 2,180,180+i*10] , pos = Vector2(175,175+i*5) , canvas = Canvas ))
    for i in range(9):
        bodies.append( body( shape = "rect" , color = "yellow" , mass = 100000.0  , dimension = [260,260-i*10 + 2,270,270-i*10] , pos = Vector2(265,265-i*5) , canvas = Canvas ))
    bodies[0].v = Vector2(1000000000,-100000)
    bodies[0].a = Vector2(0,10000)
    bodies[1].v = Vector2(1000,0)
    bodies[1].a = Vector2(5000,0)

def  draw(Canvas):
    global coll  
    for i in bodies:
        i.anim()
    coll.anim(bodies)
    

p = process(setup,draw,1500,1500)
