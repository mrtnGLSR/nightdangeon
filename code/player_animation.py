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
attack = False
walkCount = 0 # walkcount is the number of the frame during the animations
attackCount = 0
# 1=up, 2=down, 3=right, 4=left
last_movement = 2
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
attack_right = []
attack_left = []



# Class StatiSprite load all the static image for the animation
class StaticSprite():
    def __init__(self, name):
        super().__init__()
        image_static = pygame.image.load(os.path.join('./img', f'Player_{name}_static.png'))# load the image
        image_static = pygame.transform.scale(image_static, (110, 165))# resize the image
        walk_static.append(image_static) # add to the static list
# Call StaticSprite class
StaticSprite('up')
StaticSprite('down')
StaticSprite('right')
StaticSprite('left')



class AttackSprite():
    def __init__(self, name, list_add):
        super().__init__()
        for i in range(11):
            i += 1
            image_static = pygame.image.load(os.path.join('./img', f'Player_attack_{name}_{i}.png'))# load the image
            image_static = pygame.transform.scale(image_static, (110, 165))# resize the image
            list_add.append(image_static)

AttackSprite('right', attack_right)
AttackSprite('left', attack_left)


# This for load all images needed to make the animations
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






# The function redrawGameWindow draw all images of the animation and update the window
def redrawGameWindow():
    global walkCount, last_movement, attackCount
    # Apply a background color
    screen.fill((255,0,0))  
    # if the frame is over 7 the variable is reset
    if walkCount + 1 >= 7:
        walkCount = 0
    if attackCount + 1 >= 11:
        attackCount = 0
    if attack:
        if last_movement == 3:
            screen.blit(attack_right[attackCount], (image_cords['x'],image_cords['y']))
            attackCount += 1
        if last_movement == 4:
            screen.blit(attack_left[attackCount], (image_cords['x'],image_cords['y']))
            attackCount += 1
    elif up:  # If we are facing up
        screen.blit(walk_up[walkCount], (image_cords['x'],image_cords['y'])) 
        walkCount += 1
        last_movement = 1 
    elif down: # If we are facing down
        screen.blit(walk_down[walkCount], (image_cords['x'],image_cords['y']))
        walkCount += 1 
        last_movement = 2
    elif right: # If we are facing right
        pygame.time.delay(85)
        screen.blit(walk_right[walkCount], (image_cords['x'],image_cords['y']))
        walkCount += 1 
        last_movement = 3
    elif left: # If we are facing left
        pygame.time.delay(85)
        screen.blit(walk_left[walkCount], (image_cords['x'],image_cords['y']))
        walkCount += 1 
        last_movement = 4
    
    else:
        if attack == False:  # If we are facing static
            if last_movement == 1:# last direction the character move
                screen.blit(walk_static[0], (image_cords['x'],image_cords['y']))
            elif last_movement == 2:
                screen.blit(walk_static[1], (image_cords['x'],image_cords['y']))
            elif last_movement == 3:
                screen.blit(walk_static[2], (image_cords['x'],image_cords['y'])) 
            elif last_movement == 4:
                screen.blit(walk_static[3], (image_cords['x'],image_cords['y'])) 
    pygame.display.update() 

# adding the character on the window at the starting
redrawGameWindow()


running = True
while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # add keys event
    keys = pygame.key.get_pressed()
    
    if (keys[pygame.K_w] or keys[pygame.K_UP]) and (keys[pygame.K_s] or keys[pygame.K_DOWN]):
        # Static if up and down is pressed in the same time
        up = down = right = left = False
        walkCount = 0
    elif (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and (keys[pygame.K_a] or keys[pygame.K_LEFT]):
        # Static if right and left is pressed in the same time
        up = down = right = left = False
        walkCount = 0
    else:
        if keys[pygame.K_w] or keys[pygame.K_UP]: # if the keys to go up are pressed
            up = True
            right = False
            down = False
            left = False
            attack = False
        elif keys[pygame.K_s] or keys[pygame.K_DOWN]:  # if the keys to go down are pressed
            up = False
            right = False
            down = True
            left = False
            attack = False
        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]: # if the keys to go right are pressed
            up = False
            right = True
            down = False
            attack = False
            left = False
        elif keys[pygame.K_a] or keys[pygame.K_LEFT]: # if the keys to go left are pressed
            up = False
            right = False
            down = False
            left = True
            attack = False
        else:
            up = right = down = left= attack = False # if no keys is pressed he was static
            walkCount = 0
        if event.type == pygame.MOUSEBUTTONDOWN:
            attack = True
        
            

    redrawGameWindow()
# Uninitialize all pygame modules
pygame.quit()