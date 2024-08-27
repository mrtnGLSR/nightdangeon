# api for the game

# modules
from player import player

# define chunks
class Chunk:
    def __init__(self, chunkContent):
    self.chunkContent = chunkContent

class Solide:
    def __init__(self, form, position, walkable, texture)
    self.form = form
    self.position = form
    self.walkable = walkable
    self.texture = texture

class Entity(Solide):
    def __init__(self)

class Player(Entity):
    def __init__(self, health)
    self.health = health
    form = [(-0.4, 0.4), (0.4, 0.4), (-0.4, -0.4), (0.4, -0.4)]
