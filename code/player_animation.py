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
right = False
left = False
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
walk_right = []
walk_left = []
walk_static = []


class StaticSprite():
    def __init__(self, name):
        super().__init__()
        image_static = pygame.image.load(os.path.join('./img', f'Player_{name}_static.png'))
        image_static = pygame.transform.scale(image_static, (110, 165))
        walk_static.append(image_static) 
StaticSprite('up')
StaticSprite('down')
StaticSprite('right')
StaticSprite('left')





# list of sprites
for i  in range(6):
    i += 1
    image_up = pygame.image.load(os.path.join('./img', f'Player_run_up_{i}.png'))
    image_up = pygame.transform.scale(image_up, (110, 165))
    walk_up.append(image_up)
    image_down = pygame.image.load(os.path.join('./img', f'Player_run_down_{i}.png'))
    image_down = pygame.transform.scale(image_down, (110, 165))
    walk_down.append(image_down)
    image_right = pygame.image.load(os.path.join('./img', f'Player_run_right_{i}.png'))
    image_right = pygame.transform.scale(image_right, (110, 165))
    walk_right.append(image_right)
    image_left = pygame.image.load(os.path.join('./img', f'Player_run_left_{i}.png'))
    image_left = pygame.transform.scale(image_left, (110, 165))
    walk_left.append(image_left)







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
    elif right:
        pygame.time.delay(85)
        screen.blit(walk_right[walkCount], (image_cords['x'],image_cords['y']))
        walkCount += 1 
        last_movement = 3
    elif left:
        pygame.time.delay(85)
        screen.blit(walk_left[walkCount], (image_cords['x'],image_cords['y']))
        walkCount += 1 
        last_movement = 4
    else:
        if last_movement == 1:
            screen.blit(walk_static[0], (image_cords['x'],image_cords['y']))
        elif last_movement == 2:
            screen.blit(walk_static[1], (image_cords['x'],image_cords['y']))
        elif last_movement == 3:
            screen.blit(walk_static[2], (image_cords['x'],image_cords['y'])) 
        elif last_movement == 4:
            screen.blit(walk_static[3], (image_cords['x'],image_cords['y'])) 
    pygame.display.update() 

running = True
while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    
    if (keys[pygame.K_w] or keys[pygame.K_UP]) and (keys[pygame.K_s] or keys[pygame.K_DOWN]):
        # Statique si up et down sont enfoncés simultanément
        up = down = right = left = False
        walkCount = 0
    elif (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and (keys[pygame.K_a] or keys[pygame.K_LEFT]):
        # Statique si up et down sont enfoncés simultanément
        right = left = up = down = False
        walkCount = 0
    else:
        if keys[pygame.K_w] or keys[pygame.K_UP]: 
            up = True
            right = False
            down = False
            left = False
        elif keys[pygame.K_s] or keys[pygame.K_DOWN]:  
            up = False
            right = False
            down = True
            left = False
        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]: 
            up = False
            right = True
            down = False
            left = False
        elif keys[pygame.K_a] or keys[pygame.K_LEFT]: 
            up = False
            right = False
            down = False
            left = True
        else:
            up = right = down = left = False
            walkCount = 0

    redrawGameWindow()
# Uninitialize all pygame modules
pygame.quit()