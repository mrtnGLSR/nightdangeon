# api for the game

# modules
from copy import copy

# constants
nbChunkX = 8
nbChunkY = 8
nbBlocksX = 9
nbBlocksY = 9

# variables
map = []

# define chunks
class Chunk:
    def __init__(self, chunkContent):
        self.chunkContent = chunkContent

# définition des objets affichés
class Solide:
    def __init__(self, draw, position, walkable, texture):
        self.draw = draw
        self.position = position
        self.walkable = walkable
        self.texture = texture

# définitions des entités (objets mobiles)
class Entity(Solide):
    def __init__(self, draw, position, walkable, texture, health):
        Solide.__init__(self, draw, position, walkable, texture)
        self.health = health
    # fonction de mouvement
    def move(self, xMove, yMove):
        # détection des collisions
        def defineBlockList(self, direction):
            blocklist=[]

            # vérification Est 
            if direction == "E":
                # vérification de la position dans l'espace pour ne pas sortir de la map
                nbChunkChecked = 2
                if self.position[2] == nbChunkX:
                    nbChunkChecked = 1
                # boucle par chunk traité
                for chunkCheckNumber in range(nbChunkChecked):
                    # définir une position virtuelle comme point de départ en terme de traitment des chunks
                    positionInChunk = copy(self.position)
                    # changer la position si le chunk à traiter change
                    if chunkCheckNumber == 1:
                        positionInChunk[0] = 0
                        positionInChunk[1] += 1
                        positionInChunk[3] += 1
                    # traiter le chunk block par block
                    for i in range(nbBlocksX):
                        print(i)
                        # terminer le traitement du chunk si l'index arrive à la fin
                        if i + positionInChunk[0] == nbBlocksX:
                            print("break")
                            break
                        # ajouter le block à la liste de blocks en fonction des objets sur la map
                        blocklist.append(map[positionInChunk[3]][positionInChunk[2] + chunkCheckNumber].chunkContent[int(positionInChunk[1])][i + int(positionInChunk[0])])
                        print(blocklist)

            # vérification Oest
            if direction == "O":
                nbChunkChecked = 2
                if self.position[2] == 0:
                    nbChunkChecked = 1
                for chunkCheckNumber in range(nbChunkChecked):
                    positionInChunk = copy(self.position)
                    if chunkCheckNumber == 1:
                        positionInChunk[0] = 0
                        positionInChunk[1] += 1
                        positionInChunk[3] += 1
                    for i in range(nbBlocksX):
                        print(i)
                        if i + positionInChunk[0] == nbBlocksX:
                            print("break")
                            break
                        blocklist.append(map[positionInChunk[3]][positionInChunk[2] + chunkCheckNumber].chunkContent[int(positionInChunk[1])][i + int(positionInChunk[0])])
                        print(blocklist)

            # TODO vérification Nord
            if direction == "N":
                nbChunkChecked = 2
                if self.position[2] == nbChunkX:
                    nbChunkChecked = 1
                for chunkCheckNumber in range(nbChunkChecked):
                    positionInChunk = copy(self.position)
                    if chunkCheckNumber == 1:
                        positionInChunk[0] = 0
                        positionInChunk[1] += 1
                        positionInChunk[3] += 1
                    for i in range(nbBlocksX):
                        print(i)
                        if i + positionInChunk[0] == nbBlocksX:
                            print("break")
                            break
                        blocklist.append(map[positionInChunk[3]][positionInChunk[2] + chunkCheckNumber].chunkContent[int(positionInChunk[1])][i + int(positionInChunk[0])])
                        print(blocklist)

            # TODO vérification Sude
            if direction == "S":
                nbChunkChecked = 2
                if self.position[2] == nbChunkX:
                    nbChunkChecked = 1
                for chunkCheckNumber in range(nbChunkChecked):
                    positionInChunk = copy(self.position)
                    if chunkCheckNumber == 1:
                        positionInChunk[0] = 0
                        positionInChunk[1] += 1
                        positionInChunk[3] += 1
                    for i in range(nbBlocksX):
                        print(i)
                        if i + positionInChunk[0] == nbBlocksX:
                            print("break")
                            break
                        blocklist.append(map[positionInChunk[3]][positionInChunk[2] + chunkCheckNumber].chunkContent[int(positionInChunk[1])][i + int(positionInChunk[0])])
                        print(blocklist)

            return(blocklist)
        def checkCloserobject(self, blocksList):
            pass
        print(defineBlockList(self, "E"))
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

class Player(Entity):
    def __init__(self, position):
        Entity.__init__(self, [(-0.4, 0.4), (0.4, 0.4), (-0.4, -0.4), (0.4, -0.4)], position, False, False, 100)
