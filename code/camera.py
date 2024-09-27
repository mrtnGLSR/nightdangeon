import pygame
camera = pygame.Rect(0,0,0,0)
viewDistance = 4

def create_screen(width, heigh, title):
    pygame.display.set_caption(title)
    
    screen = pygame.display.set_mode((width, heigh))
    camera.width = width
    camera.height = heigh
    return screen

# debug
class DebugClass():
    def __init__(self, position):
        self.position = position
        self.camera = Camera(self)
    
    def refresh(self):
        print("salut")
    #    self.camera.refresh(5)

# classe définisant la caméra du jeu
class Camera():
    def __init__(self, player):
        self.player = player
    
    # fonction de rafraichissement
    def refresh(self, distance):
        position = self.player.position

        # définition du bloque sur lequel se situe le joueur
        playerBlock = [position[0] // 1, position[1] // 1]

        # définir la position relative des bloques à charger
        chargedBlockList = []
        for x in range(viewDistance * 2 + 1):
            for y in range(viewDistance* 2 + 1):
                chargedBlockList.append([playerBlock[0] - viewDistance + x, playerBlock[1] - viewDistance + y])

        print(chargedBlockList)

debugPlayer = DebugClass

debugPlayer.refresh()

