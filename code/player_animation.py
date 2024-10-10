import pygame
import os

# pygame init
pygame.init()
clock = pygame.time.Clock()

# window configuration
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Player Animation")

# Variables
up = False
down = False
walkCount = 0
# 1=up, 2=down
last_movement = 0
# Dictionary

image_cords = {
    "y" : ((screen.get_height()) / 2) - 82.5,
    "x" : ((screen.get_width()) / 2) - 55
}

# Lists
walk_up = []
walk_down = []
walk_static = []


class StaticSprite():
    def __init__(self, name):
        super().__init__()
        image_static = pygame.image.load(os.path.join('./img', f'Player_{name}_static.png'))
        image_static = pygame.transform.scale(image_static, (110, 165))
        walk_static.append(image_static) 
StaticSprite('up')
StaticSprite('down')





# list of sprites
for i  in range(6):
    i += 1
    image_up = pygame.image.load(os.path.join('./img', f'Player_run_up_{i}.png'))
    image_up = pygame.transform.scale(image_up, (110, 165))
    walk_up.append(image_up)
    image_down = pygame.image.load(os.path.join('./img', f'Player_run_down_{i}.png'))
    image_down = pygame.transform.scale(image_down, (110, 165))
    walk_down.append(image_down)







def redrawGameWindow():
    global walkCount, last_movement
    
    screen.fill((255,0,0))  

    if walkCount + 1 >= 7:
        walkCount = 0
        
    if up:  # If we are facing up
        screen.blit(walk_up[walkCount], (image_cords['x'],image_cords['y'])) 
        walkCount += 1
        last_movement = 1 
    elif down:
        screen.blit(walk_down[walkCount], (image_cords['x'],image_cords['y']))
        walkCount += 1 
        last_movement = 2
    else:
        if last_movement == 1:
            screen.blit(walk_static[0], (image_cords['x'],image_cords['y']))
        elif last_movement == 2:
            screen.blit(walk_static[1], (image_cords['x'],image_cords['y']))
        
    pygame.display.update() 

running = True
while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_w] or keys[pygame.K_UP]: 
        up = True
        down = False

    elif keys[pygame.K_s] or keys[pygame.K_DOWN]:  
        up = False
        down = True
        
    else: # If the character is not moving we will set both up and down false and reset the animation counter (walkCount)
        up = False
        down = False
        walkCount = 0
    
    redrawGameWindow()
# Uninitialize all pygame modules
pygame.quit()