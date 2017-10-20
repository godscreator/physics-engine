from newMath import vector
from vector import *
import  time
from math import *
from painter import *

class shape:
    def __init__(self,body,shape,dimension,color,canvas):
        self.body = body
        self.shape = shape
        a,b,c,d = dimension
        self.p1 = Vector2(a,b)
        self.p2 = Vector2(c,d)
        self.color  = color
        self.shapes = {"oval":canvas.create_oval,"rect":canvas.create_rectangle}
        self.uid = self.shapes[self.shape](self.p1.x,self.p1.y,self.p2.x,self.p2.y,fill=color)

    def sync(self):
        self.p1 += self.body.ds
        self.p2 += self.body.ds
        uid = self.shapes[self.shape](self.p1.x,self.p1.y,self.p2.x,self.p2.y,fill=self.color)
    
    def  anim(self):
        self.sync()
        self.body.move()

cols = (0,0)
def collision(a,b,e = 1):
    #(((a.p1.x <= b.p1.x and b.p1.x <= a.p2.x)or (a.p1.x <= b.p2.x and b.p2.x <= a.p2.x))and ((a.p1.y <= b.p1.y and b.p1.y <= a.p2.y) or (a.p1.y <= b.p2.y and b.p2.y <= a.p2.y)) or ((b.p1.x <= a.p1.x and a.p1.x <= b.p2.x)or (b.p1.x <= a.p2.x and a.p2.x <= b.p2.x))and ((b.p1.y <= a.p1.y and a.p1.y <= b.p2.y) or (b.p1.y <= a.p2.y and a.p2.y <= b.p2.y)))
    p = (a.p1 + a.p2)/2.0
    o = fabs((a.p1.x - a.p2.x)/2.0)
    n = fabs((a.p1.y - a.p2.y)/2.0)
    l = (b.p1 + b.p2)/2.0
    k = fabs((b.p1.x - b.p2.x)/2.0)
    m= fabs((b.p1.y - b.p2.y)/2.0)
    global cols
    if cols != (a.uid,b.uid) and ( p-l).length <= o+k  :
        print "collision :",a.color,b.color
        v1=a.body.onCollision(b.body,e)
        v2=b.body.onCollision(a.body,e)
        a.body.v+=v1
        b.body.v+=v2
        cols = (a.uid,b.uid)
            
def colmech(bds):#bds:bodies
    for i in range(len(bds)):
        for j in range(i+1,len(bds)):
            collision(bds[i],bds[j])

                             
class body:
    def __init__(self ,pos ,mass ):
        self.m = mass #float
        self.pos = pos # vector 2D
        self.v = Vector2(0,0)
        self.a = Vector2(0,0)
        self.ds = Vector2(0,0)
        self.move()
    def move(self):
        self.v += self.a*0.001
        self .ds = self.v*0.001
        self.pos += self.ds
    def  onCollision(self,other,e =1):
        m1 = self.m
        m2 = other.m
        r = (self.pos-other.pos).normalise()
        v1 = self.v.dot(r)
        v2 = other.v.dot(r)
        v = (m2*(1+e)*(v2-v1))/(1.0*(m1+m2))
        return fabs(v)*r


class ball:
    def __init__(self,canvas,h,k,r,m,ux=0.0,uy=0.0,color = "black"):
        self.body = body(Vector2(h,k),m)
        self.body.v = Vector2(ux,uy)
        self.shape = shape(self.body,"oval",[h-r,k-r,h+r,k+r],color,canvas)
class box:
    def __init__(self,canvas,h,k,l,b,m,ux=0.0,uy=0.0,color = "black"):
        self.body = body(Vector2(h+l/2.0,k+b/2.0),m)
        self.body.v = Vector2(ux,uy)
        self.shape = shape(self.body,"rect",[h,k,h+l,k+b],color,canvas)
### main


bodies = []
def  setup(canvas):
    global bodies
    bodies.append(ball(canvas,200,200,10,2.0,-1000.0,0.0,"green"))
    bodies.append(ball(canvas,150,200,10,2.0,0,0.0,"blue"))
    bodies.append(ball(canvas,300,200,10,2.0,-2000.0,0.0,"yellow"))
##    bodies.append(box(canvas,100,100,200,5,1000000.0,0,0,"red"))
##    bodies.append(box(canvas,100,300,200,5,1000000.0,0,0,"red"))
##    bodies.append(box(canvas,100,100,5,200,1000000.0,0,0,"red"))
##    bodies.append(box(canvas,300,100,5,205,1000000.0,0,0,"red"))
        
counter = 0
def  draw(canvas):
    global counter
    b = [i.shape for i in bodies]
    colmech(b)
    for i in bodies:
        i.shape.anim()
    

p = process(setup,draw,1500,1500)
