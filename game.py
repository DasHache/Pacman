from layout import Layout
from graphicsDisplay import PacmanGraphics


class GameStateData:
    def __init__(self):
        pass

    def initialize(self, layout):
        self.layout = layout



class GameState:
    def __init__(self):
        self.data = GameStateData()

    def initialize(self, layout):
        self.data.initialize(layout)




class Game:
    def __init__(self, display):
        self.state = GameState()
        self.display = display

    def run(self):
        self.display.initialize(self.state.data)
        self.display.mainloop()




class GameRules:
    def __init__(self):
        pass

    def newGame(self, layout, display):
        initState = GameState()
        initState.initialize(layout)

        game = Game(display)
        game.state = initState

        return game


layout = Layout('layout/dasha.lay') #Layout('layout/big.lay')
#layout = Layout('layout/small.lay') #Layout('layout/big.lay')
display = PacmanGraphics()

rules = GameRules()
game = rules.newGame(layout, display)
game.run()