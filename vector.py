from math import *
class Vector2:
    def __init__(self, x = 0 ,y = 0 ):
        self.x = x
        self.y = y
        self.setlen()
        
    def __str__(self):
        return str(self.x)+" i  + "+str(self.y)+" j"
    def normalise(self):
        return self/self.length
    
    def setlen(self):
        self.length = sqrt( pow(self.x,2) + pow(self.y,2))

    def __add__(self, v ):
        return Vector2(self.x+v.x , self.y+v.y)

    def __sub__(self, v ):
        return Vector2(self.x-v.x , self.y-v.y )

    def __mul__(self ,v):
        return Vector2(self.x*v , self.y*v )

    def __div__(self,v):
        return Vector2(self.x/v , self.y/v)
                       
    def __rmul__(self ,v):
        return Vector2(self.x*v , self.y*v )

    def dot(self , v):
        return self.x*v.x + self.y*v.y
    
class Vector3:
    def __init__(self, x = 0 ,y = 0 ,z = 0):
        self.x = x
        self.y = y
        self.z = z
        self.setlen()

    def setlen(self):
        self.length = sqrt( pow(self.x,2) + pow(self.y,2) + pow(self.z,2))
    def normalise(self):
        return self/self.length
    def __str__(self):
        return str(self.x)+" i  + "+str(self.y)+" j"

    def __add__(self, v ):
        return Vector3(self.x+v.x , self.y+v.y , self.z+v.z)

    def __sub__(self, v ):
        return Vector3(self.x-v.x , self.y-v.y , self.z-v.z)

    def __mul__(self ,v):
        return Vector3(self.x*v , self.y*v , self.z*v)

    def __div__(self,v):
        return Vector2(self.x/v , self.y/v)

    def __rmul__(self ,v):
        return Vector3(self.x*v , self.y*v , self.z*v)

    def cross(self, v):
        x = self.y*v.z - self.z*v.y
        y = self.z*v.x - self.x*v.z 
        z = self.x*v.y - self.y*v.x
        return Vector3(x,y,z)

    def dot(self , v):
        return self.x*v.x + self.y*v.y + self.z*v.z
