# api for the game

# constants
nbChunkX = 8
nbChunkY = 8
nbBlocksX = 9
nbBlocksY = 9

# define chunks
class Chunk:
    def __init__(self, chunkContent):
        self.chunkContent = chunkContent

class Solide:
    def __init__(self, draw, position, walkable, texture):
        self.draw = draw
        self.position = position
        self.walkable = walkable
        self.texture = texture

class Entity(Solide):
    def __init__(self, draw, position, walkable, texture):
        super().__init__(draw, walkable, texture)
        # fonction de mouvement
        def move(self, xMove, Ymove):
            print(position)

class Player(Entity):
    def __init__(self, health, position):
        Entity.__init__(self, [(-0.4, 0.4), (0.4, 0.4), (-0.4, -0.4), (0.4, -0.4)], position, health)

# définition de la map
map = []

for ymap in range(nbChunkY):
    map.append([])
    for xmap in range(nbChunkX):
        # définition des chuks
        tmpChunkTemplate = []
        for ychunk in range(nbBlocksY):
            tmpChunkTemplate.append([])
            for xchunk in range(nbBlocksX):
                tmpChunkTemplate[-1].append(0)
        
print(map)
print(tmpChunkTemplate)
testPlayer = Player(1, [1, 1, 1, 1])
testPlayer.move()
