# import pygame
from mapgen import *
from screen import *

print("chargement de la camera ...", end = '')

camera = pygame.Rect(0,0,0,0)
viewDistance = 4
zoom = 11

# constants
# charger les images
images = {"brickWall":pygame.image.load('./img/brick-wall.png'), "brickFloor":pygame.image.load('./img/brick-floor.png', ), "test-player":pygame.image.load('./img/Test-cub.png')}
# redimenssionner les images
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
        playerBlock = [position[0] // 1, position[1] // 1]

        # définir la position relative des bloques à charger
        chargedBlockList = []
        relativeChargedList = []
        for x in range((viewDistance + 1) * 2 + 2):
            for y in range((viewDistance + 1) * 2 + 2):
                chargedBlockList.append([position[0] // 1 + x - 1 - viewDistance, position[1] // 1 + y - 1 - viewDistance])
        
        screen.fill((0, 0, 0))

        # charger les images sur l'écran
        index = 0
        for i in chargedBlockList:
            try:
                screen.blit(images[map[int(i[0])][int(i[1])].texture], [(int(i[0]) - position[0] + viewDistance + 0.5) * zoom * 10, (int(i[1]) - position[1] + viewDistance + 0.5) * zoom * 10])
            except:
                pass
            index += 1
            screen.blit(images["test-player"], [40 * zoom, 40 * zoom])
        pygame.display.flip()
print(" fait")