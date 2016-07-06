from graphicsShapes import *

class Layout :

    def __init__(self,filename):
        f = open(filename ,'r')
        lines = f.readlines()
        self.height = len(lines)
        self.width = len(lines[0])

        self.walls =[]#[[0,0],[0,1],[0,3],[1,0],[2,0],[3,3]]
        self.food =[]
        self.Pacman = []
        self.Fantom = []
        for y in range(len(lines)):  # <--- pour obtenir une ligne tu peux utiliser une boucle "for"
            ligne = lines[y]   # <--- la variable "ligne" va etre une chaine des characteres
            for x in range(len(ligne)):  # <--- pour obtenir une charactere tu peux utiliser une boucle "for"
                charactere = ligne[x] # <--- la variable "charactere" va etre une characteres "%" ou "." ou "P"
                if charactere == "%":
                    self.walls.append([x,y])
                if charactere == ".":
                    self.food.append([x,y])
                if charactere == "P":
                    self.Pacman.append([x,y])
                if charactere == "F":
                    self.Fantom.append([x,y])



############################################ FIN DE TON CODE ######










