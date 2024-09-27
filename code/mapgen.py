# constants
nbBlocksX = 9
nbBlocksY = 9
nbChunkX = 8
nbChunkY = 8
map = []
nbMapPoints = 4
mapNoise = 15 # définit la quantité de chemins aléatoires. Plus le nombre est petit, plus le chemin est directe et plus le nombre est grand plus le chemin est chaotique

# modules
import copy
import random
from nodes import *

# define chunks
class Chunk:
    def __init__(self, chunkContent, chunkType):
        self.chunkContent = chunkContent
        self.chunkType = chunkType # définit si c'est un chunk plein, un coulloir ou une sale


# fonction de génération de la map
def GenMap():
    # positionnement des chunks sur la map
    for ymap in range(nbChunkY):
        map.append([])
        for xmap in range(nbChunkX):
            # ajouter un chunk sur chaque bloque de la map
            map[ymap].append(Chunk(None, None))
    
    # définition des chemins
    pointMap = [] # liste contenant les points de repère
    wayMap = [] # liste des chemins
    
    # créer les points de connection des chemins
    for point in range(nbMapPoints):
        pointMap.append([random.randint(0, nbChunkY - 1), random.randint(0, nbChunkX - 1)])
    
    # relier les points entre eux
    for point in range(nbMapPoints - 1):
        # x et y
        for sens in range(2):
            # si l'analyse des chemins commence (point à 0 et sens à 0), initialiser mon point fixe comme étant l'axe qui ne sera pas encore analysé
            if point + sens == 0:
                fixPoint = point1 = pointMap[point][abs(sens - 1)]

            point1 = pointMap[point][sens]
            point2 = pointMap[point + 1][sens]
            # ajout des chemins pour chaque chunks
            for i in range(abs(point1 - point2) + 1):

                # entrer chunks qui se trouvent entre les deux points en fonction de l'axe
                if point1 < point2:
                    wayMap.append([{0:(point1 + i), 1:(fixPoint)}[sens], {1:(point1 + i), 0:(fixPoint)}[sens]])
                if point1 > point2:
                    wayMap.append([{0:(point1 - i), 1:(fixPoint)}[sens], {1:(point1 - i), 0:(fixPoint)}[sens]])

            # définir le point qui ne bougera pas pour le prochaine analyse.
            # (si la direction du chemin est x, le y ne changera pas et inversément)
            fixPoint = point1 + i * {True:1, False:-1}[point1 < point2]

    # ajouter des chemins aléatoires
    for i in range(mapNoise):
        # sélectionner une case au hasard dans la map
        noiseChunk = copy.copy(wayMap[random.randint(0, len(wayMap) - 1)])
        # choisire si la direction du nouveau chunk est en X ou en Y
        XorY = random.randint(0, 1)
        # choisir si en X ou en Y, nous devons soustraire ou additionner exemple si X: choisir entre -X ou +X
        moreOrLess = [-1, 1][random.randint(0, 1)]
        # entrer un nouveau chunk dans la map en fonction de XorYet de moreOrLess en vérifiant que le chunk ne soit pas en dehors de la map
        if noiseChunk[XorY] + moreOrLess > 0 and noiseChunk[XorY] < [nbChunkX, nbChunkY][XorY]:
            noiseChunk[XorY] = noiseChunk[XorY] + moreOrLess
            wayMap.append(noiseChunk)
    
    # débugage d'affichage de la map
    # for x in range(nbChunkX):
    #     textX = ""
    #     for y in range(nbChunkY):
    #         if [x, y] in wayMap:
    #             if [x, y] == pointMap[-1]:
    #                 textX += '\x1b[6;30;42m' + '[E]' + '\x1b[0m'
    #             elif [x, y] == pointMap[0]:
    #                 textX += '\x1b[6;30;42m' + '[S]' + '\x1b[0m'
    #             else:
    #                 textX += '\x1b[6;30;44m' + '[ ]' + '\x1b[0m'
    #         else:
    #             textX += '\x1b[6;30;43m' + '[#]' + '\x1b[0m'
    #     print(textX)

    # définir les types de chunks
    for x in range(nbChunkX):
        for y in range(nbChunkY):
            chunkType = None
            if [x, y] in wayMap:
                chunkType = ["Coridor", "Room"][random.randint(0, 1)]
            else:
                chunkType = "Full"
            map[x][y].chunkType = chunkType

    # TODO fonction pour creuser dans les mures de façon à créer des salles et des couloires
    def grind():
        pass

    # TODO ajouter les bloques dans les chunks en fonction des chemins et du type
    for x in range(nbChunkX):
        for y in range(nbChunkY):
            chunkContent = []
            # remplire le chunk avec des mures
            for xchunk in range(nbBlocksX):
                chunkContent.append([])
                for ychunk in range(nbBlocksY):
                    chunkContent[xchunk].append(BrickWall)
            if map[x][y].chunkType != "Full":
                pass


    
    
            
                
GenMap()