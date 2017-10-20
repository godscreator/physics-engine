from Tkinter import *
class process:
    def __init__(self,setup,draw,height,width):
        self.height = height
        self.width = width
        self.setup = setup
        self.draw = draw
        self.fps = 50
        self.execute()
    def  calldraw(self):
        self.canvas.delete(ALL)
        self.draw(self.canvas)
        self.canvas.after(1000/self.fps,self.calldraw)
    def execute(self):
        self.root = Tk()
        self.canvas = Canvas(self.root , width = self.width ,height= self.height )
        self.canvas.pack()
        self.setup(self.canvas)
        self.calldraw()
        self.root.mainloop()


