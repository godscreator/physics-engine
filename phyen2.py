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
        self.v     +=  self.a*1  # v = u + at
        ds             =  self.v*1  # ds = vdt
        self.pos +=  ds           # s = s + ds
        self.p1   +=  ds          # s = s + ds
        self.p2   +=  ds          # s = s + ds
        self.shapes[ self.shape ]( self.p1.x  ,  self.p1.y  ,  self.p2.x  ,  self.p2.y  ,  fill = self.color  )
       
    def  onCollision(self,other,e =1):
        m1 , m2  = self.m , other.m
        r    = (self.pos-other.pos).normalise()
        v1 = self.v.dot(r)
        v2 = other.v.dot(r)
        v   = ( m2 * (1+e) * (v2 - v1)) / (m1+m2)
        return fabs(v)*r

class collider:
    def __init__( self ):
        self.cols = (0 , 0) # denotes just previous collision
        
    def collision(self , a , b , e = 1):# a,b : body , e = elastic coefficient.
        p = (a.p1 + a.p2)/2.0
        q = (b.p1 + b.p2)/2.0
        r  = p - q
        
        ax = fabs((a.p1.x - a.p2.x)/2.0)
        ay = fabs((a.p1.y - a.p2.y)/2.0)
        bx = fabs((b.p1.x - b.p2.x)/2.0)
        by= fabs((b.p1.y - b.p2.y)/2.0)
        
        if self.cols != (a.uid,b.uid) and (r.length <= ax+bx) :
            print "collision :",a.color,b.color
            v1 = a.onCollision(b , e)
            v2 = b.onCollision(a , e)
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
    coll = collider()
    bodies.append( body( shape = "oval" , color = "green" , mass = 2.0  , dimension = [100,100,110,110] , pos = Vector2(105,105) , canvas = Canvas ))
    bodies.append( body( shape = "oval" , color = "blue" , mass = 2.0  , dimension = [150,100,160,110] , pos = Vector2(155,105) , canvas = Canvas ))
    bodies.append( body( shape = "rect" , color = "yellow" , mass = 2.0  , dimension = [170,170,180,180] , pos = Vector2(175,175) , canvas = Canvas ))
    bodies[0].v = Vector2(1,0)
    bodies[2].v = Vector2(0,-1)   
def  draw(Canvas):
    global coll
    coll.anim(bodies)
    for i in bodies:
        i.anim()
    

p = process(setup,draw,1500,1500)
