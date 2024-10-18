
# constants
nbBlocksX = 9
nbBlocksY = 9
nbChunkX = 8
nbChunkY = 8
map = []
nbMapPoints = 6
mapNoise = 20 # définit la quantité de chemins aléatoires. Plus le nombre est petit, plus le chemin est directe et plus le nombre est grand plus le chemin est chaotique
startPoint = []
endPoint = []
mapSize =[nbBlocksX * nbChunkX, nbBlocksY * nbChunkY]

# modules
import copy
import random
from nodes import *

print("génération de la map ...", end = '')

# define chunks
class Chunk:
    def __init__(self, chunkContent, chunkType):
        self.chunkContent = chunkContent
        self.chunkType = chunkType # définit si c'est un chunk plein, un coulloir ou une sale


# fonction de génération de la map
def GenMap():
    global startPoint, endPoint, map

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
    
    startPoint = pointMap[0]
    endPoint = pointMap[-1]
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

    # définir les types de chunks
    for x in range(nbChunkX):
        for y in range(nbChunkY):
            chunkType = None
            if [x, y] in wayMap:
                chunkType = ["Coridor", "Room"][random.randint(0, 1)]
            else:
                chunkType = "Full"
            map[x][y].chunkType = chunkType

    # Carré dans le chunk
    def square(pos1, pos2):
        posList = []
        # pour l'axe parcourir le tableau en fonction de la différence entière entre la position 1 et la position 2
        for x in range(int(((pos2[0] - pos1[0])**2)**0.5) + 1):
            for y in range(int(((pos2[1] - pos1[1])**2)**0.5) + 1):
                # insérer dans la liste les cohordonées x et y en fonction de si l'écart est positif ou négatif
                posList.append([pos1[0] + x * {True:1, False:-1}[pos1[0] < pos2[0]], pos1[1] + y * {True:1, False:-1}[pos1[1] < pos2[1]]])
        return[posList]

    # fonction pour creuser dans les mures de façon à créer des salles et des couloires
    def grind(side, type, chunkContent):
        finalContent = copy.copy(chunkContent)
        # définir un carré contenant en fonction du type de chunk et de la direction à creuser
        grindedPosList = {"Coridor":{"left":[[0, 3], [2, 5]], "right":[[6, 3], [8, 5]], "top":[[3, 0], [5, 2]], "bottom":[[3, 6], [5, 8]], "center":[[3, 3], [5, 5]]}[side], "Room":{"left":[[0, 3], [0, 5]], "right":[[8, 3], [8, 5]], "top":[[3, 0], [5, 0]], "bottom":[[3, 8], [5, 8]], "center":[[1, 1], [7, 7]]}[side]}[type]
        grindedBlocks = square(grindedPosList[0], grindedPosList[1])[0]
        for i in grindedBlocks:
            finalContent[i[0]][i[1]] = BrickFloor()
        return finalContent

    # ajouter les bloques dans les chunks en fonction des chemins et du type
    for x in range(nbChunkX):
        for y in range(nbChunkY):
            chunkContent = []
            # remplire le chunk avec des mures
            for xchunk in range(nbBlocksX):
                chunkContent.append([])
                for ychunk in range(nbBlocksY):
                    chunkContent[xchunk].append(BrickWall())
            if map[x][y].chunkType == "Full":
                pass
            else:
                # creuser le centre en fonction du type de chunk
                chunkContent = grind("center", map[x][y].chunkType, chunkContent)
                # creuser chaque côté en fonction de ses voisins        vvvvvvv------désigue la position relative des chunks à vérifier
                for i in [["left", [-1, 0]], ["right", [1, 0]], ["top", [0, -1]], ["bottom", [0, 1]]]:
                    # vérifier que les voisins  sont des vides et les creuser si c'est vrai
                    if [x + i[1][0], y + i[1][1]] in wayMap:
                        chunkContent = grind(i[0], map[x][y].chunkType, chunkContent)
            map[x][y].chunkContent = chunkContent
    
    # changer le format de la map
    mapTmp = copy.copy(map)
    map = []
    for ychunk in range(nbChunkY):
        for yBlock in range(nbBlocksY):
            map.append([])
            for xchunk in range(nbChunkX):
                for xBlock in range(nbBlocksX):
                    map[-1].append(mapTmp[xchunk][ychunk].chunkContent[xBlock][yBlock])
    
    print(" fait", end = '\n')
    




            
GenMap()