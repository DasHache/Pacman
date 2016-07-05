from graphicsShapes import *

class Layout :

    def __init__(self,filename):
        f = open(filename ,'r')
        l = f.readlines()
        self.height = len(l)
        self.width = len(l[0])

        self.walls = [[1,1],[3,1],[5,1]]
        print(self.walls[0])
        [x,y] = self.walls[0]


############################################ FIN DE TON CODE ######








