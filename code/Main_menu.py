import pygame
# initialisation
pygame.init()
running = True 
background_color = (234, 212, 252) 


window = pygame.display.set_mode((1280,1280))
window.fill(background_color)
# load image
bg_image = pygame.image.load(".\img\hearth")

pygame.display.set_caption('Night Dungeon')
pygame.display.flip()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False