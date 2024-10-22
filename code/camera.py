# import pygame
from mapgen import *
from screen import *
import os

print("chargement de la camera ...", end = '')

camera = pygame.Rect(0,0,0,0)
viewDistance = 4
zoom = 11
#Variables
walkCount = 0 # walkcount is the number of the frame during the animations for the walk
attackCount = 0 # walkcount is the number of the frame during the animations for the attack
attack = False
dieCount = 0






# 1=up, 2=down, 3=right, 4=left
last_movement = 2 # set default orientation
# Dictionary
image_cords = {
    'y' : ((screen.get_height()) / 2) - 82.5,# position of the player in height ([window height] / 2 - [Player image size /2])
    'x' : ((screen.get_width()) / 2) - 55 # position of the player in width ([window width] / 2 - [Player image size /2])
}


# Load sfx
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
heath = []
die = []
# constants
# charger les images
images = {"brickWall":pygame.image.load('./img/brick-wall.png'), "brickFloor":pygame.image.load('./img/brick-floor.png', ), "test-player":pygame.image.load('./img/Test-cub.png')}
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
class LifeSprite():
    def __init__(self, name):
        super().__init__()
        image_hearth = pygame.image.load(os.path.join('./img', f'{name}.png'))
        image_hearth = pygame.transform.scale(image_hearth, (60, 60))
        heath.append(image_hearth)
LifeSprite('hearth')
LifeSprite('death_hearth')


def redrawGameWindow(direction_up,direction_down,direction_left,direction_right,attack, life_state):
    global walkCount, last_movement, attackCount, dieCount
    # Apply a background color
    if life_state == 1:
        screen.blit(heath[0], (0,0))
        screen.blit(heath[1], (40,0))
        screen.blit(heath[1], (80,0))
    if life_state == 2:
        screen.blit(heath[0], (0,0))
        screen.blit(heath[0], (40,0))
        screen.blit(heath[1], (80,0))
    if life_state == 3:
        screen.blit(heath[0], (0,0))
        screen.blit(heath[0], (40,0))
        screen.blit(heath[0], (80,0))
    if life_state == 0:
        pygame.time.delay(500)
        if dieCount != 2:
            screen.blit(die[dieCount], (image_cords['x'],image_cords['y']))
            death_screen()
            die_sfx.play() 
        if dieCount == 2:
            screen.blit(die[dieCount], (image_cords['x']-55,image_cords['y']+82.5))
            death_screen()
            
        if dieCount < 2:
            dieCount += 1
            
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
    if direction_up:  # If we are facing up
        screen.blit(walk_up[walkCount], (image_cords['x'],image_cords['y'])) 
        walkCount += 1
        last_movement = 1 
    elif direction_down: # If we are facing down
        screen.blit(walk_down[walkCount], (image_cords['x'],image_cords['y']))
        walkCount += 1 
        last_movement = 2
    elif direction_right: # If we are facing right
        screen.blit(walk_right[walkCount], (image_cords['x'],image_cords['y']))
        walkCount += 1 
        last_movement = 3
    elif direction_left: # If we are facing left
            screen.blit(walk_left[walkCount], (image_cords['x'],image_cords['y']))
            walkCount += 1 
            last_movement = 4
    
    else:
        if attack == False and life_state > 0:  # If we are facing static
                if last_movement == 1:# last direction the character move
                    screen.blit(walk_static[0], (image_cords['x'],image_cords['y']))
                elif last_movement == 2:
                    screen.blit(walk_static[1], (image_cords['x'],image_cords['y']))
                elif last_movement == 3:
                    screen.blit(walk_static[2], (image_cords['x'],image_cords['y'])) 
                elif last_movement == 4:
                    screen.blit(walk_static[3], (image_cords['x'],image_cords['y']))
# redimenssionner les images
for i in images:
    images[i] = pygame.transform.scale(images[i], (10 * zoom, 10 * zoom))

# classe définisant la caméra du jeu
class Camera():
    def __init__(self, player):
        self.player = player
    # fonction de rafraichissement
    def refresh(self, direction_up,direction_down,direction_left,direction_right, attack, life_state, position = False):
        # la position de la caméra est la même que le joueur si elle n'est pas précisée
        if not position:
            position = self.player.position
        # définition du bloque sur lequel se situe le joueur
        playerBlock = [position[0] // 1, position[1] // 1]

        # définir la position relative des bloques à charger
        chargedBlockList = []
        relativeChargedList = []
        for x in range((viewDistance + 1) * 2 + 2):
            for y in range((viewDistance + 1) * 2 + 2):
                chargedBlockList.append([position[0] // 1 + x - 1 - viewDistance, position[1] // 1 + y - 1 - viewDistance])
        
        screen.fill((0, 0, 0))
        
        # charger les images sur l'écran
        index = 0
        for i in chargedBlockList:
            try:
                screen.blit(images[map[int(i[0])][int(i[1])].texture], [(int(i[0]) - position[0] + viewDistance + 0.5) * zoom * 10, (int(i[1]) - position[1] + viewDistance + 0.5) * zoom * 10])
            except:
                pass
            index += 1
        redrawGameWindow(direction_up,direction_down,direction_left,direction_right, attack, life_state)
        pygame.display.flip()

print(" fait")