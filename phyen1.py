from Tkinter import *
from newMath import vector
from vector import *
import  time
from math import *

class field:
    def __init__(self):
        self.fields = []
    def getRange(self,i):
        pass
    def getForce(self , m):
        for i in self.fields:
            pass

class ball_collider:
    def __init__(self , center , a , b):
        self.center = center
        self.a  = a
        self.b = b
    def noCollision(self , pos):
        v = pos  -  self.center
        if pow(v.x/self.a,2) + pow(v.y/self.b,2) > 1:
            return True
        else:
            return False

class box_collider:
    def __init__(self , center , l , b):
        self.center = center
        self.l  = l
        self.b = b
    def noCollision(self , pos):
        v = pos  -  self.center
        if fabs(v.x) > self.l/2.0 and fabs(v.y) > self.b/2.0: # doubts about it.
            print "center:",self.center.x,self.center.y
            print "position:",pos.x,pos.y
            print "relpos:",v.x,v.y
            print "l,b:",self.l,self.b
            print "true"
            return True
        else:
            print "center:",self.center.x,self.center.y
            print "position:",pos.x,pos.y
            print "relpos:",v.x,v.y
            print "l,b:",self.l,self.b
            print "false"
            return False
    
class body:
    def __init__(self,canvas,uid,collider ,  mass):
        self.canvas = canvas
        self.uid = uid
        self.collider = collider
        self.v = Vector2(0,0)
        self.a = Vector2(0,0)   #unit = pixel per milli-(second)^2
        self.m = mass
        self.move()
    def move(self):
        t = 0.001
        self.v +=  self.a*t  # unit of velocity pixel per milli-second
        self.canvas.move(self.uid,self.v.x,-self.v.y)
        self.collider.center  += self.v
        global bodies
        for i in bodies:
            if  not(i.uid==self.uid) and not(self.collider.noCollision(i.center)):
                oncollision(self,i,1)
                print "collision!"
        self.canvas.after(int(1000*t),self.move)

bodies = []

class ball(body):
    def __init__(self,canvas,center,r,mass,color = "blue"):
        self.uid = canvas.create_oval(center.x-r,center.y-r,center.x+r,center.y+r,fill = color)
        col = ball_collider(center,r,r)
        self.center = center
        body.__init__(self,canvas,self.uid,col,mass)
        global  bodies
        bodies.append(self)

class box(body):
    def __init__(self,canvas,center,l,b,mass,color = "blue"):
        self.uid = canvas.create_rectangle(center.x-l/2.0,center.y-b/2.0,center.x+l/2.0,center.y+b/2.0,fill = color)
        col = box_collider(center,l,b)
        self.center = center
        body.__init__(self,canvas,self.uid,col,mass)
        global  bodies
        bodies.append(self)

def  oncollision(body1,  body2,  e):
    m1 = body1.m
    m2 = body2.m
    v1 = body1.v
    v2 = body2.v
    body2.v = (m1*v1 + m2*v2  -  e*m1*(v1-v2))/(m1+m2)
    body1.v = (m1*v1 + m2*v2  -  e*m2*(v2-v1))/(m1+m2)

root = Tk()
                 
plane  = Canvas(root , width = 1000 , height = 600)
plane.pack()
                 
b = ball(plane,Vector2(300,300),5.0,2.0,color = "red")
b.v = Vector2(1,1)
b.a = Vector2(0,-10)

r = box(plane,Vector2(500,400),200.0,2.0,2.0,color = "green")

root.mainloop()


