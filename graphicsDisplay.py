from graphics import Graphics, Pos
from graphicsShapes import *
class PacmanGraphics():

    def __init__(self):
        self.graphics = Graphics()

    def initialize(self, state):
        self.layout = state.layout
        self.startGraphics(state)
        self.drawObjects()

    def startGraphics(self, state):
        self.graphics.initialize(state)

    def drawObjects(self):
        self.drawWalls(self.layout.walls)
        self.graphics.refresh()

    def drawWalls(self, walls):
        #w0 = walls[0]
        #self.drawWall(w0)
        for w in walls:
            self.drawWall(w)

    def drawWall(self, wall):
        canvas = self.graphics.canvas
        [wx,wy] = wall
        x,y,r = Pos(wx, wy)
        rect = Rect(canvas, (x,y), r, 'blue')

    def mainloop(self):
        self.graphics.mainloop()


################################################## MAIN ###        

if __name__ == '__main__':

    print 'pacmangraphics'
    pg = PacmanGraphics()
    pg.initialize()
    
    print 'done'
