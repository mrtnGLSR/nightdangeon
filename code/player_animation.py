# import
import pygame
import os

# pygame init
pygame.init()
clock = pygame.time.Clock()

# window configuration
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Player Animation")
pygame.mouse.set_visible(False)

# Variables
up = False
down = False
right = False
left = False
attack = False
walkCount = 0 # walkcount is the number of the frame during the animations for the walk
attackCount = 0 # walkcount is the number of the frame during the animations for the attack
<<<<<<< HEAD
<<<<<<< Updated upstream
=======
dieCount = 0
lifeState = 3

>>>>>>> Stashed changes
=======
lifeState = 3

>>>>>>> Develop
# 1=up, 2=down, 3=right, 4=left
last_movement = 2 # set default orientation
# Dictionary
image_cords = {
    'y' : ((screen.get_height()) / 2) - 82.5,# position of the player in height ([window height] / 2 - [Player image size /2])
    'x' : ((screen.get_width()) / 2) - 55 # position of the player in width ([window width] / 2 - [Player image size /2])
}

<<<<<<< Updated upstream
# Load sword sfx
<<<<<<< HEAD
=======

# Load sfx
>>>>>>> Stashed changes
=======


>>>>>>> Develop
sword_sfx = pygame.mixer.Sound('./sfx/sword_avoid_slash.mp3')
die_sfx = pygame.mixer.Sound('./sfx/die_SFX.mp3')

# Lists
walk_up = []
walk_down = []
walk_right = []
walk_left = []
walk_static = []
attack_right = []
attack_left = []
attack_down = []
attack_up = []
<<<<<<< HEAD
<<<<<<< Updated upstream
=======
heath = []
>>>>>>> Develop

=======
heath = []
die = []
>>>>>>> Stashed changes
# This for load all images needed to make the animations
class LoadSprites:
    def __init__(self, position, orientation, list_add, range_number, size):
        super().__init__()
        for i  in range(range_number):
            i += 1
            image = pygame.image.load(os.path.join('./img', f'Player_{position}_{orientation}_{i}.png'))
            image = pygame.transform.scale(image, size)
            list_add.append(image)
            
# All class calls
<<<<<<< Updated upstream
LoadSprites('run', 'up', walk_up, 6)
LoadSprites('run', 'down', walk_down, 6)
LoadSprites('run', 'left', walk_left, 6)
LoadSprites('run', 'right', walk_right, 6)
LoadSprites('attack', 'right', attack_right, 11)
LoadSprites('attack', 'left', attack_left, 11)
LoadSprites('attack', 'down', attack_down, 6)
LoadSprites('attack', 'up', attack_up, 3)
LoadSprites('static', 'up', walk_static, 1)
LoadSprites('static', 'down', walk_static, 1)
LoadSprites('static', 'right', walk_static, 1)
LoadSprites('static', 'left', walk_static, 1)
<<<<<<< HEAD


=======
LoadSprites('run', 'up', walk_up, 6, (110, 165))
LoadSprites('run', 'down', walk_down, 6, (110, 165))
LoadSprites('run', 'left', walk_left, 6, (110, 165))
LoadSprites('run', 'right', walk_right, 6, (110, 165))
LoadSprites('attack', 'right', attack_right, 11, (110, 165))
LoadSprites('attack', 'left', attack_left, 11, (110, 165))
LoadSprites('attack', 'down', attack_down, 6, (110, 165))
LoadSprites('attack', 'up', attack_up, 3, (110, 165))
LoadSprites('static', 'up', walk_static, 1, (110, 165))
LoadSprites('static', 'down', walk_static, 1, (110, 165))
LoadSprites('static', 'right', walk_static, 1, (110, 165))
LoadSprites('static', 'left', walk_static, 1, (110, 165))
LoadSprites('die', 'down', die, 2, (110, 165))
LoadSprites('die', 'floor', die, 1, (165, 110))
=======
 
>>>>>>> Develop
class LifeSprite():
    def __init__(self, name):
        super().__init__()
        image_hearth = pygame.image.load(os.path.join('./img', f'{name}.png'))
        image_hearth = pygame.transform.scale(image_hearth, (60, 60))
        heath.append(image_hearth)
LifeSprite('hearth')
LifeSprite('death_hearth')
<<<<<<< HEAD
>>>>>>> Stashed changes
=======
>>>>>>> Develop


# The function redrawGameWindow draw all images of the animation and update the window
def redrawGameWindow():
    global walkCount, last_movement, attackCount, dieCount
    # Apply a background color
<<<<<<< HEAD
<<<<<<< Updated upstream
    screen.fill((255,0,0))  
=======
=======
>>>>>>> Develop
    screen.fill((0,30,30))  
    if lifeState == 1:
        screen.blit(heath[0], (0,0))
        screen.blit(heath[1], (40,0))
        screen.blit(heath[1], (80,0))
    if lifeState == 2:
        screen.blit(heath[0], (0,0))
        screen.blit(heath[0], (40,0))
        screen.blit(heath[1], (80,0))
    if lifeState == 3:
        screen.blit(heath[0], (0,0))
        screen.blit(heath[0], (40,0))
        screen.blit(heath[0], (80,0))
<<<<<<< HEAD

=======
>>>>>>> Develop
    
    
    
    
    
    
    
    
    
    
    
    
<<<<<<< HEAD
>>>>>>> Stashed changes
=======
>>>>>>> Develop
    # if the frame is over 7 the variable is reset
    if walkCount + 1 >= 7:
        walkCount = 0
    # if the frame is over 11 the variable is reset
    if attackCount + 1 >= 11:
        attackCount = 0
    if attack:
        if last_movement == 1: # if the last movement is up
            if attackCount +1 >=4: # if the frame is over 3 the variable is reset
                attackCount = 0
            pygame.time.delay(160) # Delay for the sync of the animations
            if attackCount == 2: # if the animation is in the middle 
                sword_sfx.play()
            screen.blit(attack_up[attackCount], (image_cords['x'],image_cords['y'])) # Draw the animations
            attackCount += 1
        
        if last_movement == 2:# if the last movement is down
            if attackCount + 1 >=7: # if the frame is over 7 the variable is reset
                attackCount = 0
            pygame.time.delay(80)# Delay for the sync of the animations
            if attackCount == 3: # if the animation is in the middle 
                sword_sfx.play()
            screen.blit(attack_down[attackCount], (image_cords['x'],image_cords['y'])) # Draw the animations
            attackCount += 1
       
        if last_movement == 3:# if the last movement is right
            if attackCount == 6:# if the animation is in the middle 
                sword_sfx.play()
            screen.blit(attack_right[attackCount], (image_cords['x'],image_cords['y']))# Draw the animations
            attackCount += 1
       
        if last_movement == 4:# if the last movement is left
            if attackCount == 6:# if the animation is in the middle
                sword_sfx.play()
            screen.blit(attack_left[attackCount], (image_cords['x'],image_cords['y']))# Draw the animations
            attackCount += 1
    elif lifeState == 0:
        pygame.time.delay(500)
        if dieCount != 2:
            screen.blit(die[dieCount], (image_cords['x'],image_cords['y']))
            die_sfx.play() 
        if dieCount == 2:
            screen.blit(die[dieCount], (image_cords['x']-55,image_cords['y']+82.5))
        if dieCount < 2:
            dieCount += 1
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
    clock.tick(20)
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
        elif keys[pygame.K_o]:
            lifeState = 0
        else:
            up = right = down = left= attack = False # if no keys is pressed he was static
            walkCount = 0
        if event.type == pygame.MOUSEBUTTONDOWN: # if mouse boutton is pressed
            attack = True
        
            

    redrawGameWindow()
# Uninitialize all pygame modules
pygame.quit()