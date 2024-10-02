# api for the game

# modules
from camera import *
from nodes import Solide
from copy import copy

# constants
nbChunkX = 8
nbChunkY = 8
nbBlocksX = 9
nbBlocksY = 9

# définitions des entités (objets mobiles)
class Entity(Solide):
    def __init__(self, draw, position, walkable, texture, health):
        Solide.__init__(self, draw, position, walkable, texture, [100])
        self.health = health
        self.camera = Camera(self)

    # fonction  de rafraichissement
    def refresh(self):
        self.camera.refresh(self.position)


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
                        positionInChunk[2] += 1
                    # traiter le chunk block par block
                    for i in range(nbBlocksX):
                        # terminer le traitement du chunk si l'index arrive à la fin
                        if i + positionInChunk[0] == nbBlocksX:
                            break
                        # ajouter le block à la liste de blocks en fonction des objets sur la map
                        blocklist.append(map[positionInChunk[3]][positionInChunk[2] + chunkCheckNumber].chunkContent[int(positionInChunk[1])][i + int(positionInChunk[0])])
            
            # vérification Ouest
            if direction == "O":
                nbChunkChecked = 2
                if self.position[2] == 0:
                    nbChunkChecked = 1
                for chunkCheckNumber in range(nbChunkChecked):
                    positionInChunk = copy(self.position)
                    if chunkCheckNumber == 1:
                        positionInChunk[0] = nbBlocksX -1
                        positionInChunk[2] -= 1
                    for i in range(nbBlocksX):
                        if positionInChunk[0] - i <= 0:
                            break
                        print(chunkCheckNumber)
                        blocklist.append(map[positionInChunk[3]][positionInChunk[2] - chunkCheckNumber].chunkContent[int(positionInChunk[1])][int(positionInChunk[0]) - i])

            # vérification Sude
            if direction == "S":
                nbChunkChecked = 2
                if self.position[1] == nbChunkY:
                    nbChunkChecked = 1
                for chunkCheckNumber in range(nbChunkChecked):
                    positionInChunk = copy(self.position)
                    if chunkCheckNumber == 1:
                        positionInChunk[1] = 0
                        positionInChunk[3] += 1
                    for i in range(nbBlocksY):
                        if i + positionInChunk[1] == nbBlocksY:
                            break
                        blocklist.append(map[positionInChunk[3] + chunkCheckNumber ][positionInChunk[2]].chunkContent[i + int(positionInChunk[1])][int(positionInChunk[0])])

            # vérification Nord
            if direction == "N":
                nbChunkChecked = 2
                if self.position[1] == 0:
                    nbChunkChecked = 1
                for chunkCheckNumber in range(nbChunkChecked):
                    positionInChunk = copy(self.position)
                    if chunkCheckNumber == 1:
                        positionInChunk[1] = nbBlocksY -1
                        positionInChunk[3] -= 1
                    for i in range(nbBlocksY):
                        if positionInChunk[1] - i <= 0:
                            break
                        blocklist.append(map[positionInChunk[3] - chunkCheckNumber][positionInChunk[2]].chunkContent[int(positionInChunk[1]) - i][int(positionInChunk[0])])
            return(blocklist)
        
        # fonction de calcule de la distance
        def checkCloserobject(self, blocksList, direction):
            distance = 0.0
            # ajouter un bloque à chaque case ou le joueur pourait marcher
            for i in blocksList:
                if i.walkable:
                    distance += 1
                else:
                    break # si le joueur n'a pas la posibilité de marcher sur la case analysée, le compteur s'arrête
            
            # réduire la distance en fonction de la position du joueur sur le bloque
            distance -= (self.position[{"N":1, "S":1, "E":0, "O":0}[direction]]) % 1

            # réduire la distance en fonction de la forme du joueur
            distance -= (((self.draw[{"N":1, "S":3, "E":0, "O":2}[direction]]) **2) **0.5 + 0.5)
            return(round(distance, 1))
        
        # identifier le sens de mouvement
        sens = 0
        if xMove > 0:
            sens = "E"
        elif xMove < 0:
            sens = "O"
        if yMove > 0:
            sens = "N"
        elif yMove < 0:
            sens = "S"
        
        # définir l'objet le plus proche en fonction du sens
        closerBlock = checkCloserobject(self, defineBlockList(self, sens), sens)

        # identifier si la distance est plus grande que le mouvement
        if sens in ["E", "O"]:
            if closerBlock <= (xMove ** 2) ** 0.5:
                xMove = closerBlock * {"E":1, "O":-1}[sens]
        if sens in ["N", "S"]:
            if closerBlock <= (yMove ** 2) ** 0.5:
                yMove = closerBlock * {"N":1, "S":-1}[sens]

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

# définition du joueur
class Player(Entity):
    def __init__(self, position):
        Entity.__init__(self, [-0.4, 0.4, 0.4, -0.4], position, False, False, 100)
