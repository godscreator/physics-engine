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
        self.uid             =  self.shapes[ self.shape ]( self.p1.x  ,  self.p1.y  ,  self.p2.x  ,  self.p2.y  ,  fill = self.color  ,outline = "")
        self.anim()
        
    def anim(self):
        self.v     +=  self.a*1  # v = u + at
        ds             =  self.v*1  # ds = vdt
        self.pos +=  ds           # s = s + ds
        self.p1   +=  ds          # s = s + ds
        self.p2   +=  ds          # s = s + ds
        self.shapes[ self.shape ]( self.p1.x  ,  self.p1.y  ,  self.p2.x  ,  self.p2.y  ,  fill = self.color  ,outline = "" )
       
class collider:
    def __init__( self ,canvas):
        self.cols = (0 , 0) # denotes just previous collision
        self.canvas = canvas
    def collision(self , a , b , e = 1):# a,b : body , e = elastic coefficient.
##        self.canvas.create_rectangle(a.p1.x-1,a.p1.y-1,a.p2.x+1,a.p2.y+1,outline = "red")
##        self.canvas.create_rectangle(b.p1.x-1,b.p1.y-1,b.p2.x+1,b.p2.y+1,outline = "red")
        p = (a.p1 + a.p2)/2.0
        q = (b.p1 + b.p2)/2.0
        r  = p - q
        
        ax = fabs((a.p1.x - a.p2.x)/2.0)
        ay = fabs((a.p1.y - a.p2.y)/2.0)
        bx = fabs((b.p1.x - b.p2.x)/2.0)
        by= fabs((b.p1.y - b.p2.y)/2.0)
        
        if  (r.length <= ax+bx) :
##            print "collision:",a.color,b.color
            m1 , m2  = a.m , b.m
            r    = (b.pos-a.pos).normalise()
            u1 ,  u2   = a.v.dot(r) , b.v.dot(r)
            v1   = (((1+e) * (u2 - u1)) / (m1/m2+1)) * r # change in velocity
            v2   = (((1+e) * (u1 - u2)) / (m2/m1+1)) * r # change in velocity
            a.v+=v1
            b.v+=v2
            
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
    bodies.append( body( shape = "rect" , color = "violet" , mass = 7.0  , dimension = [200,200,270,270] , pos = Vector2(235,235) , canvas = Canvas ))
    bodies.append( body( shape = "rect" , color = "blue" , mass = 6.0  , dimension = [300,300,360,360] , pos = Vector2(330,330) , canvas = Canvas ))
    bodies.append( body( shape = "rect" , color = "skyblue" , mass = 5.0  , dimension = [400,400,450,450] , pos = Vector2(425,425) , canvas = Canvas ))
    bodies.append( body( shape = "rect" , color = "green" , mass = 4.0  , dimension = [500,500,540,540] , pos = Vector2(520,520) , canvas = Canvas ))
    bodies.append( body( shape = "rect" , color = "yellow" , mass = 3.0  , dimension = [300,500,330,530] , pos = Vector2(315,515) , canvas = Canvas ))
    bodies.append( body( shape = "rect" , color = "orange" , mass = 2.0  , dimension = [300,400,320,420] , pos = Vector2(310,410) , canvas = Canvas ))
    bodies.append( body( shape = "rect" , color = "red" , mass = 1.0  , dimension = [100,500,110,510] , pos = Vector2(105,505) , canvas = Canvas ))
    bodies[0].v = Vector2(1,5)
 

def  draw(Canvas):
    global coll  
    for i in bodies:
        i.anim()
        if (i.p1.x<=0 ) :
            if i.v.x <0:
                i.v.x *= -1
        if (i.p2.x >= 600 ):
            if i.v.x >0:
                i.v.x *= -1
        if (i.p1.y<=0 ) :
            if i.v.y <0:
                i.v.y *= -1
        if (i.p2.y >= 600 ):
            if i.v.y >0:
                i.v.y *= -1
    coll.anim(bodies)
    

p = process(setup,draw,600,600)
p.root.title("bounce")
p.fps = 100
p.execute()
