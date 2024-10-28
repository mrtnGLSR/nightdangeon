import pygame
icon = pygame.image.load('./img/icon_x64.png')

# initialiser pygame
pygame.init()
screen_width = 1040
screen_height = 1040
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Night Dungeon")
pygame.display.set_icon(icon)

red_filter = pygame.Surface((screen_width, screen_height))
red_filter.fill((255, 0, 0))  # Remplir avec du rouge
red_filter.set_alpha(128)
# définir la camera
camera = pygame.Rect(0,0,0,0)

# fonction de création de l'écran
def create_screen(width, heigh, title):
    pygame.display.set_caption(title)
    
    screen = pygame.display.set_mode((width, heigh))
    camera.width = width
    camera.height = heigh
    return screen
create_screen(screen_width, screen_height, "Night Dungeon")

def death_screen():
    screen.blit(red_filter, (0, 0))