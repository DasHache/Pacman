import Tkinter
from graphicsShapesExt import *

DEFAULT_GRID_SIZE = 50

#
# class Pos(list):
#     def __init__(self, x, y, size=1, grid_size=100):
#         self.x = x * grid_size
#         self.y = y * grid_size
#         self.s = size * grid_size
#         list.__init__(self, [self.x, self.y, self.s])

class Graphics():

    def __init__(self, width=640, height=480, bgColor='black'):
        self.bgColor = bgColor
        #self.width = width
        #self.height = height
        self.gridSize = DEFAULT_GRID_SIZE
        self.canvas = None

    def initialize(self, state):
        self.rootWindow = Tkinter.Tk()
        wl = state.layout.width
        hl = state.layout.height
        w = wl * self.gridSize
        h = hl * self.gridSize
        print('Display: w = '+str(wl)+', h = '+str(hl) + ', gridsize = '+ str(self.gridSize))
        self.canvas = Tkinter.Canvas(self.rootWindow, width=w, height=h)

        for wi in range(wl):
            vert_line = CellLine(self.canvas, (wi, 0), angle_=90, span_=hl)
        for hi in range(hl):
            hor_line = CellLine(self.canvas, (0, hi), span_=wl)

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


class CellShape():
    def __init__(self, canvas, pos, scale=1.):
        self.c = canvas
        self.x = pos[0]
        self.y = pos[1]
        self.scale = scale
        self.color = 'black'
        self.size = DEFAULT_GRID_SIZE
        self.offset = self.size * (1.-self.scale) /2.


        self.x1 = self.x * self.size + self.offset
        self.y1 = self.y * self.size + self.offset
        self.x2 = (self.x+1) * self.size - self.offset
        self.y2 = (self.y+1) * self.size - self.offset
        print('CellShape: '+str([self.x1, self.y1, self.x2, self.y2]))

        self.items = []
        #self.__draw__()

    def __draw__(self):
        pass
        # x1,y1 = self.x-self.size, self.y-self.size
        # x2,y2 = self.x+self.size, self.y+self.size
        # l1 = self.c.create_line(x1,y1,x2,y2,fill=self.color)
        # l2 = self.c.create_line(x1,y2,x2,y1,fill=self.color)
        # self.items.append(l1)
        # self.items.append(l2)

    def __delete__(self):
        for l in self.items:
            self.c.delete(l)

    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy
        self.__delete__()
        self.__draw__()

    def paint(self, color):
        self.color = color
        self.__draw__()

        
    

class CellRect(CellShape):

    def __init__(self, canvas, pos, color, scale=1):
        CellShape.__init__(self, canvas, pos, scale)
        self.color = color
        self.__draw__()

    def __draw__(self):
        #print('CellCircle.__draw__: ' + str([self.x1, self.y1, self.x2, self.y2]))
        self.c.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill=self.color)


class CellCircle(CellShape):

    def __init__(self, canvas, pos, color, scale=1):
        CellShape.__init__(self, canvas, pos, scale)
        self.color = color
        self.__draw__()

    def __draw__(self):
        #print('CellCircle.__draw__: ' + str([self.x1, self.y1, self.x2, self.y2]))
        self.c.create_oval(self.x1, self.y1, self.x2, self.y2, fill=self.color)


class CellLine(CellShape):
    def __init__(self, canvas, pos, color_='gray', angle_=0, span_=1):
        CellShape.__init__(self, canvas, pos)
        self.color = color_
        self.angle = angle_
        self.span = span_
        self.__draw__()

    def __draw__(self):
        if self.angle == 0:
            x1, y1 = self.x*self.size, self.y*self.size
            x2, y2 = self.x*self.size + self.span*self.size, self.y*self.size
            print('Horizontal line: ' +str([x1, y1, x2, y2]))
            self.c.create_line(x1, y1, x2, y2, fill=self.color)

        elif self.angle == 90:
            x1, y1 = self.x*self.size, self.y*self.size
            x2, y2 = self.x*self.size, self.y*self.size + self.span * self.size
            print('Vertical line: ' +str([x1, y1, x2, y2]))
            self.c.create_line(x1, y1, x2, y2, fill=self.color)

        else:
            raise RuntimeError('Unknown line angle')
        
