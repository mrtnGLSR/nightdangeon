# constants
nbBlocksX = 8
nbBlocksY = 8
nbChunkX = 8
nbChunkY = 8
map = []
nbMapPoints = 5

# modules
import random
from nodes import *

# define chunks
class Chunk:
    def __init__(self, chunkContent, chunkOutput):
        self.chunkContent = chunkContent
        self.chunkOutput = chunkOutput


# fonction de génération de la map
def GenMap():
    # positionnement des chunks sur la map
    for ymap in range(nbChunkY):
        map.append([])
        for xmap in range(nbChunkX):
            # définition des chuks
            # tmpChunkTemplate = []
            # for ychunk in range(nbBlocksY):
            #     tmpChunkTemplate.append([])
            #     for xchunk in range(nbBlocksX):
            #         tmpChunkTemplate[-1].append(Wall)
            #
            map[ymap].append(Chunk(None, None))
    
    # définition des chemins
    pointMap = [] # liste contenant les points de repère
    wayMap = [] # liste des chemins
    
    # créer les points de connection des chemins
    for point in range(nbMapPoints):
        pointMap.append([random.randint(0, nbChunkY), random.randint(0, nbChunkX)])
        print(pointMap[point])
    
    # relier les points entre eux
    for point in range(nbMapPoints):
        # x et y
        for sens in range(2):
            # si l'analyse des chemins commence (point à 0 et sens à 0), initialiser mon point fixe comme étant l'axe qui ne sera pas encore analysé
            if point + sens == 0:
                fixPoint = point1 = pointMap[point][abs(sens - 1)]

            point1 = pointMap[point][sens]
            point2 =pointMap[point + 1][sens]
            # ajout des chemins pour chaque chunks
            for i in range(abs(point1 - point2) + 1):
                print(str(sens) + ": " + str(i) + " = " + str(point1) + " - " + str(point2))

                # entrer chunks qui se trouvent entre les deux points en fonction de l'axe
                if point1 < point2:
                    wayMap.append([{0:(point1 + i), 1:(fixPoint)}[sens], {1:(point1 + i), 0:(fixPoint)}[sens]])
                if point1 > point2:
                    wayMap.append([{0:(point1 - i), 1:(fixPoint)}[sens], {1:(point1 - i), 0:(fixPoint)}[sens]])

            # définir le point qui ne bougera pas pour le prochaine analyse.
            # (si la direction du chemin est x, le y ne changera pas et inversément)
            fixPoint = point1 + i * {True:1, False:-1}[point1 < point2]
        print(wayMap)
                
                
GenMap()