from graphicsShapes import *

class Layout :
    def __init__(self,filename):
        f = open(filename ,'r')
        l = f.readlines()

        g = Graphics()
        canvas = g.canvas


        for x in l:
            for y in x:

                if y == '%':
                    x,y,r = Pos(1, 3)
                    rect = Rect(canvas, (x,y), r, 'blue')

                if y == 'P':
                    rad = 0.5
                    x,y,r = Pos(1, 1, rad)
                    c1 = Circle(canvas, (x, y), r, 'yellow')
                if y == '.':
                    rad = 0.2
                    x,y,r = Pos(1, 1, rad)
                    Circle(canvas, (x, y), r, 'purple')

                break

            break

        g.mainloop()


############################################ FIN DE TON CODE ######




Layout('layout/small.lay')
#Layout('layout/big.lay')






