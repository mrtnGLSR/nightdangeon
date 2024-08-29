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
<<<<<<< Updated upstream
        def move(self, xMove, Ymove):
            print(position)
=======
    def move(self, xMove, yMove):
        # détection des changementes de chunks
        #   position x
        if self.position[0] + xMove >= nbBlocksX:
            self.position[2] += int((self.position[0] + xMove) // nbBlocksX)
        if self.position[0] + xMove < nbBlocksX:
            self.position[2] -= int((self.position[0] + xMove) // nbBlocksX)
        #   position y
        if self.position[1] + yMove >= nbBlocksY:
            self.position[3] += int((self.position[1] + yMove) // nbBlocksY)
        if self.position[1] + yMove < nbBlocksY:
            self.position[3] -= int((self.position[1] + yMove) // nbBlocksY)
        # changement de position
        self.position[0] += (xMove % (nbBlocksX))
        self.position[1] += (yMove % (nbBlocksY))

        # arrondire les nombres
        for i in range(2):
            self.position[i] = (round(self.position[i], 1))
>>>>>>> Stashed changes

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
<<<<<<< Updated upstream
testPlayer = Player(1, [1, 1, 1, 1])
testPlayer.move()
=======
testPlayer = Player(1, [1, 1, 1, 1], False)
for i in range(100):
    testPlayer.move(0.1, 0)
    print (testPlayer.position)
>>>>>>> Stashed changes
