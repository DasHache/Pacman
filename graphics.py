import Tkinter

class Pos(list):
    def __init__(self, x, y, size=1, grid_size=100):
        self.x = x * grid_size
        self.y = y * grid_size
        self.s = size * grid_size
        list.__init__(self, [self.x, self.y, self.s])

class Graphics():

    def __init__(self, width=640, height=480, bgColor='black'):
        self.bgColor = bgColor
        self.rootWindow = Tkinter.Tk()
        self.canvas = Tkinter.Canvas(self.rootWindow, width=width, height=height)
        self.canvas.pack()
        self.canvas.update()
        self.rootWindow.bind( "<KeyPress>", self.keypress )

    def keypress(self):
        pass

    def mainloop(self):
        self.rootWindow.mainloop()


#    def addCircle(self, pos, radius, color):
#        x, y = pos
#        c1 = Circle(self, x, y, radius, color)
#        
# test2        
# test3


        
    

        
