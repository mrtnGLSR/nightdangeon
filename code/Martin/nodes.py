# add nodes

# modules
from Engine import Solide

# define wall
class Wall(Solide):
    def __init__(self, texture):
        Solide.__init__(self, [-0.5, 0.5, 0.5, -0.5], False, False, texture)
#self, draw, position, walkable, texture

# deifne floor
class Floor(Solide):
    def __init__(self, texture):
        super().__init__([-0.5, 0.5, 0.5, -0.5], False, True, texture)

# brick define brick wall
class BrickWall(Wall):
    def __init__(self):
        Wall.__init__(self, False)

# brick define brick floor
class BrickFloor(Floor):
    def __init__(self):
        Floor.__init__(self, False)
    

