from graphics import *

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
        self.drawFood(self.layout.food)
        self.drawPacman(self.layout.Pacman)
        self.drawFantom(self.layout.Fantom)
        self.graphics.refresh()

    def drawWalls(self, walls):
        #w0 = walls[0]
        #self.drawWall(w0)
        for w in walls:
            self.drawWall(w)

    def drawFood(self, food):
        for f in food:
            canvas = self.graphics.canvas
            [x,y] = f
            oval = CellCircle(canvas, (x,y), 'red', 0.5)

    def drawPacman(self, pacmans):
        for p in pacmans:
            canvas = self.graphics.canvas
            [x,y] = p
            oval = CellCircle(canvas, (x,y), 'yellow', 1)

    def drawFantom(self, fantoms):
        for F in fantoms:
            canvas = self.graphics.canvas
            [x,y] = F
            oval = CellCircle(canvas, (x,y), 'purple', 1)

    def drawWall(self, wall):
        canvas = self.graphics.canvas
        [x,y] = wall
        rect = CellRect(canvas, (x,y), 'blue', 1.0)
        #rect = CellCircle(canvas, (x,y), 'red', 0.5)

    def mainloop(self):
        self.graphics.mainloop()


################################################## MAIN ###        

if __name__ == '__main__':

    print 'pacmangraphics'
    pg = PacmanGraphics()
    pg.initialize()
    
    print 'done'
