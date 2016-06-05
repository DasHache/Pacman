#import Tkinter
from graphics import Graphics, Pos


# Toutes les figures doit avoir
# 1. canvas - le canvas, ou elle se dessine
# 2. pos    - la position, les coordonees (x,y) ou exactement elle doit se dessiner
# 3. size   - la taille (en pixels)
# 4. color  - la couleur
#
# Pour dessiner les cercles, je veux avoir une classe 'Circle'
# Ma classe va avoir:
# 1. canvas - ...
# 2. pos    - ...
# 3. size   - Qu'est ce que c'est la taiile d'une cercle?
# 4. color  - ...
#
# en plus, il me faut 2 fonctions:
# __init__  - pour cree l'objet de ma classe
# __draw__  - pour le dessiner
#
# Voila:
#
class Circle():

    def __init__(self, canvas, pos, rad, color):
        self.c = canvas
        self.x = pos[0]
        self.y = pos[1]
        self.color = color
        self.size = rad
        self.__draw__()

    def __draw__(self):
        x1, y1 = self.x-self.size, self.y-self.size
        x2, y2 = self.x+self.size, self.y+self.size
        self.c.create_oval(x1,y1,x2,y2,fill=self.color)

class Rect():

    def __init__(self, canvas, pos, size_, color):
        self.c = canvas
        self.x = pos[0]
        self.y = pos[1]
        self.color = color
        self.size = size_
        self.__draw__()

    def __draw__(self):
        x1, y1 = self.x-self.size, self.y-self.size
        x2, y2 = self.x+self.size, self.y+self.size
        self.c.create_rectangle(x1,y1,x2,y2,fill=self.color)



### MAIN ###
if __name__ == '__main__':

    grid_size = 100
    rad = 0.5
    g = Graphics()
    canvas = g.canvas

############################################ TON CODE ICI ######

    x,y,r = Pos(1, 1, rad)
    c1 = Circle(canvas, (x, y), r, 'yellow')

    x,y,r = Pos(1, 2, rad)
    Circle(canvas, (x, y), r, 'red')

    x,y,r = Pos(1, 4)
    rect = Rect(canvas, (x,y), r, 'blue')


############################################ FIN DE TON CODE ######

    g.mainloop()