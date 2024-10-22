import pygame

# initialiser pygame
pygame.init()
screen_width = 1040
screen_height = 1040
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Night Dungeon")

# définir la camera
camera = pygame.Rect(0,0,0,0)

# fonction de création de l'écran
def create_screen(width, heigh, title):
    pygame.display.set_caption(title)
    
    screen = pygame.display.set_mode((width, heigh))
    camera.width = width
    camera.height = heigh
    return screen
create_screen(screen_width, screen_height, "test")