class Shape():

    def __init__(self, canvas, pos):
        self.c = canvas
        self.x = pos[0]
        self.y = pos[1]
        self.color = 'black'
        self.size = 10
        self.items = []
        self.__draw__()

    def __draw__(self):
        pass

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




class Round(Shape):

    def __init__(self,canvas,pos,size_,color):
        Shape.__init__(self,canvas ,pos)
        self.size=size_
        self.color=color
        self.__draw__()

    def __draw__(self):
        raise RuntimeError("Not implemented yet")
        x1,y1 = self.x-self.size, self.y-self.size
        x2,y2 = self.x+self.size, self.y+self.size
        c1 = self.c.create_oval(x1,y1,x2,y2,fill=self.color)
        self.items.append(c1)


#
# ################################################## MAIN ###
# if __name__ == '__main__':
#     grid_size = 100
#     rad = 0.5
#     g = Graphics()
#     canvas = g.canvas
#
#     ############################## Shape
#     x,y,r = Pos(3, 3)
#     s = Shape(canvas, (x,y))
#
#     x,y,r = Pos(1,3)
#     c = Round(canvas, (x,y), 100, 'red')
#
#     print '1'
#     import time
#     time.sleep(1)
#
#
#     print '2'
#     s.move(0,50)
#     s.paint('red')
#     #time.sleep(5)
#
#    g.mainloop()




