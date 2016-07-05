from graphicsShapes import *

class Layout :

    def __init__(self,filename):
        f = open(filename ,'r')
        l = f.readlines()
        self.height = len(l)
        self.width = len(l[0])

        self.walls = [[0,0],[0,1],[0,3],[1,0],[2,0],[3,3]]
        print(self.walls[0])
        [x,y] = self.walls[0]


############################################ FIN DE TON CODE ######








