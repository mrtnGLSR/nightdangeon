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
    def __init__(self, draw, position, walkable, texture, health):
        Solide.__init__(self, draw, position, walkable, texture)
        self.health = health
        # fonction de mouvement
        def move(self, xMove, yMove):
            nonlocal position
            # détection des changementes de chunks
            if position + xMove > nbBlocksX + 1:
                position[0] += ((position + xMove) % nbBlocksX) // nbBlocksX
            if position + xMove < nbBlocksX + 1:
                position[0] -= ((position + xMove) % nbBlocksX) // nbBlocksX
            if position + yMove > nbBlocksY + 1:
                position[0] += ((position + yMove) % nbBlocksY) // nbBlocksY
            if position + yMove < nbBlocksY + 1:
                position[0] -= ((position + yMove) % nbBlocksY) // nbBlocksY
            # changement de position
            position[2] += (xMove % (nbBlocksX + 1))
            position[3] += (yMove % (nbBlocksY + 1))

class Player(Entity):
    def __init__(self, health, position, texture):
        Entity.__init__(self, [(-0.4, 0.4), (0.4, 0.4), (-0.4, -0.4), (0.4, -0.4)], position, False,  texture, health)


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
testPlayer = Player(1, [1, 1, 1, 1], False)
testPlayer.move(1, 1)
