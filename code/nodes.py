# add nodes

# modules
from API import Solide

# define wall
class Wall(Solide):
    def __init__(self):
        self.draw = [(-0.5, 0.5), (0.5, 0.5), (-0.5, -0.5), (0.5, -0.5)]
        self.walkable = False

# deifne floor
class floor(Solide):
    def __init__(self, form, position, walkable, texture):
        super().__init__(form, position, walkable, texture)
        self.draw = [(-0.5, 0.5), (0.5, 0.5), (-0.5, -0.5), (0.5, -0.5)]
        self.walkable = True
    

