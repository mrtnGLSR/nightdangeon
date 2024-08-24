import pygame
import time
pygame.init()
# Window
window_size = (800,600)
game_window = pygame.display.set_mode(window_size)
# Rectangle
x = 50
y = 50
width = 64
height = 64
vel = 5
# Game Loop
run = True
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] or keys[pygame.K_a]:
        x -= vel
    if keys[pygame.K_UP] or keys[pygame.K_d]:
        x += vel
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        y -= vel
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        y += vel
    # Draw Rectangle and Update Display
    game_window.fill((0,0,0))
    pygame.draw.rect(game_window, (255,0,0), (x, y, width, height))
    pygame.display.update()
# Quit Pygame
pygame.quit()