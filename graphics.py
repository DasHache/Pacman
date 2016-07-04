import Tkinter

DEFAULT_GRID_SIZE = 300


class Pos(list):
    def __init__(self, x, y, size=1, grid_size=100):
        self.x = x * grid_size
        self.y = y * grid_size
        self.s = size * grid_size
        list.__init__(self, [self.x, self.y, self.s])

class Graphics():

    def __init__(self, width=640, height=480, bgColor='black'):
        self.bgColor = bgColor
        #self.width = width
        #self.height = height
        self.gridSize = DEFAULT_GRID_SIZE
        self.canvas = None

    def initialize(self, state):
        self.rootWindow = Tkinter.Tk()
        w = state.layout.width * self.gridSize
        h = state.layout.height * self.gridSize
        self.canvas = Tkinter.Canvas(self.rootWindow, width=w, height=h)

        self.canvas.pack()
        self.canvas.update()
        self.rootWindow.bind( "<KeyPress>", self.keypress )

    def keypress(self):
        pass

    def refresh(self):
        self.canvas.update_idletasks()

    def mainloop(self):
        self.rootWindow.mainloop()


#    def addCircle(self, pos, radius, color):
#        x, y = pos
#        c1 = Circle(self, x, y, radius, color)
#        
# test2        
# test3


        
    

        
