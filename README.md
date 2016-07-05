# Pacman

# graphics

Graphics - simple class for graphics

# graphicsShapes

Cirle, Rect - simple classes to draw a shape


# game.py

class GameStateData:

class GameState:

class Game:

class GameRules:

+

layout = Layout('layout/small.lay') #Layout('layout/big.lay')
display = PacmanGraphics()
rules = GameRules()
game = rules.newGame(layout, display)
game.run()