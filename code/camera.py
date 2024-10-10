# import pygame
from mapgen import *
from screen import *

camera = pygame.Rect(0,0,0,0)
viewDistance = 4
zoom = 11

# constants
# charger les images
images = {"brickWall":pygame.image.load('./img/brick-wall.png'), "brickFloor":pygame.image.load('./img/brick-floor.png')}
# redimenssionner les images
print("hsdkjfhskjdfhjk------sdfgsdfgsdfg")
for i in images:
    images[i] = pygame.transform.scale(images[i], (10 * zoom, 10 * zoom))

# classe définisant la caméra du jeu
class Camera():
    def __init__(self, player):
        self.player = player
    # fonction de rafraichissement
    def refresh(self, position = False):
        # la position de la caméra est la même que le joueur si elle n'est pas précisée
        if not position:
            position = self.player.position

        # définition du bloque sur lequel se situe le joueur
        playerBlock = [position[0] // 1, position[1] // 1, position[2] // 1, position[3] // 1]

        # définir la position relative des bloques à charger
        chargedBlockList = []
        relativeChargedList = []
        for x in range((viewDistance + 1) * 2 + 1):
            for y in range((viewDistance + 1) * 2 + 1):
                # définir la position relative
                relativeCharged = [playerBlock[2] - viewDistance + x, playerBlock[3] - viewDistance + y]
                relativeChargedList.append(relativeCharged)
                # définir la position relative au bon format
                chargedBlockList.append([position[0] + relativeCharged[0] // (nbBlocksX - 1), position[1] + relativeCharged[1] // (nbBlocksY - 1), relativeCharged[0] % (nbBlocksX - 1), relativeCharged[1] % (nbBlocksY - 1)])

        #débug ---------------------
        # for y1 in range(nbChunkY):
        #     for y2 in range(nbBlocksY):
        #         text=""
        #         for x1 in range(nbChunkX):
        #             for x2 in range(nbBlocksX):
        #                 if [x1, y1, x2, y2] in chargedBlockList:
        #                     text += '\x1b[6;30;41m' + '[V]' + '\x1b[0m'
        #                 elif isinstance(map[x1][y1].chunkContent[x2][y2], BrickFloor):
        #                     text += '\x1b[6;30;42m' + '[F]' + '\x1b[0m'
        #                 elif isinstance(map[x1][y1].chunkContent[x2][y2], BrickWall):
        #                     text += '\x1b[6;30;44m' + '[W]' + '\x1b[0m'
        #                 else:
        #                     text += '\x1b[6;30;42m' + '[ ]' + '\x1b[0m'
        #         print(text)
        
        screen.fill((0, 0, 0))

        # charger les images sur l'écran
        index = 0
        for i in chargedBlockList:
            try:
                screen.blit(images[map[int(i[0])][int(i[1])].chunkContent[int(i[2])][int(i[3])].texture], [(i[2] + viewDistance + 1 - round(position[2], 1) + (i[0] - position[0]) * nbBlocksX) * 10 * zoom, (i[3] + viewDistance + 1 - round(position[3], 1) + (i[1] - position[1]) * nbBlocksY) * 10 * zoom])
            except:
                pass
            index += 1
        pygame.display.flip()