import pygame
camera = pygame.Rect(0,0,0,0)

def create_screen(width, heigh, title):
    pygame.display.set_caption(title)
    
    screen = pygame.display.set_mode((width, heigh))
    camera.width = width
    camera.height = heigh
    return screen