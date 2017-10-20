from Tkinter import *
from math import *

class graph:
    def __init__(self , f = None, domain = [-5, 5],origin = [ 250 , 250] , scale = 50, accuracy = 50.0,width = 502 , height = 502 ,grid ="yes"):
        # === initialisation of variables ===
        self.f = f
        self.domain = domain
        self.origin  = origin
        self.scale = scale
        self.accuracy = accuracy
        self.width = width
        self.height = height
        self.grid = grid
              
    def drawplane(self):
        x0 , y0 = self.origin[0] , self.height - self.origin[1]
        thick = 3 # thickness of axes 
        arl = 5     # arrow length
        # x - axis
        self.plane.create_line( 0 , y0 ,self.width  ,  y0  , width = thick,fill = "green")
        self.plane.create_line( 0 , y0 , 0 + arl  ,  y0 + arl   , width = thick,fill = "green")
        self.plane.create_line( 0     , y0   , 0 + arl   ,  y0 - arl  , width = thick,fill = "green")
        self.plane.create_line( self.width - arl    , y0 - arl  ,self.width     ,  y0   , width = thick,fill = "green")
        self.plane.create_line( self.width - arl    , y0 + arl  ,self.width     ,  y0  , width = thick,fill = "green")
        # y - axis
        self.plane.create_line(x0 , 0  , x0   , self.height   , width = thick ,fill = "green")
        self.plane.create_line(x0   , 0   , x0 + arl   ,  0 + arl  , width = thick,fill = "green")
        self.plane.create_line(x0   , 0    , x0 - arl   ,  0 + arl  , width = thick,fill = "green")
        self.plane.create_line(x0 - arl   ,self.height - arl  , x0    , self.height    , width = thick,fill = "green")
        self.plane.create_line( x0     , self.height    ,x0 + arl   ,self.height - arl  , width = thick,fill = "green")

        nw=int(self.width/self.scale)+int((self.height-self.origin[1])/self.scale)
        nh=int(self.height/self.scale)+int((self.width-self.origin[0])/self.scale)
        
        #labels
        self.plane.create_text(self.origin[0]+20,7,text= "y-axis")
        self.plane.create_text(self.width - 20,self.height-self.origin[1]+10,text= "x-axis")
        for i in range(-nw,nw+1,1):
            self.plane.create_text(self.origin[0]+i*self.scale + 5,self.height-self.origin[1]+10,text= str(i))
        for i in range(-nh,nh+1,1):
            self.plane.create_text(self.origin[0]- 5,self.height-self.origin[1]-7+i*self.scale ,text= str(-i),anchor = E)
        
        # the grid
        if self.grid == "yes":
            for i in range(-2*nw,2*nw+1,1):
                if i % 2==0:
                    self.plane.create_line(self.origin[0]+i/2.0*self.scale,0,self.origin[0]+i/2.0*self.scale,self.height,width = 1.5 ,fill = "green")
                else:
                    self.plane.create_line(self.origin[0]+i/2.0*self.scale,0,self.origin[0]+i/2.0*self.scale,self.height,width = 1 ,fill = "green")
            for i in range(-2*nh,2*nh+1,1):
                if i % 2 == 0:
                    self.plane.create_line(0,self.height-self.origin[1]+i/2.0*self.scale,self.width,self.height-self.origin[1]+i/2.0*self.scale ,width = 1.5 , fill= "green")
                else:
                    self.plane.create_line(0,self.height-self.origin[1]+i/2.0*self.scale,self.width,self.height-self.origin[1]+i/2.0*self.scale ,width = 1 , fill= "green")
        
         
    def draw(self  , f ,d = 1 ,domain = [-5,5],fill = "red",thick = 1):
        # === drawing the curve ===
        px  = domain[0]
        py  = f(px)
        while px <= domain[1] :
            nx = px + d
            try:
                    ny = f(px + d)
                    self.plane.create_line(self.origin[0]+self.scale*px   , self.height - self.origin[1] - self.scale*py   , self.origin[0]+self.scale*nx   , self.height - self.origin[1] -self.scale*ny    ,fill = fill , width = thick)
                    py = ny
            except :
                print "Error"
            px  = nx 
    
    def view(self):
        # === view the graph ===
        
        self.root = Tk()  
        self.root.title("pygraph")

        # === Creating cartesian plane === 
        self.plane = Canvas( self.root , width = self.width, height = self.height )
        self.drawplane()
        for m in self.f:
                self.draw(f = m , d = 1.0/self.accuracy , fill = "red",domain=self.domain )
        self.plane.grid(row = 0 ,columnspan = 4 , padx =20 , pady =20)
        self.root.mainloop()

    
