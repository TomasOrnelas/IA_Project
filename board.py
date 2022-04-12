# Código para representar tabuleiro

class board:
    max_x = 0
    max_y = 0
    walls = []

    def __init__(self,max_x,max_y):
        self.max_x = max_x
        self.max_y = max_y

    def setWall(self,a,b):
        self.walls = self.walls + [[a,b]]
