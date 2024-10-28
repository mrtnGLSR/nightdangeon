# modules
from time import time
import sys

# définir le niveau
level = "easy"
try:
    level = sys.argv[1]
except:
    pass

print(level)

# from sprite import sprites   # Liste ou collection des sprites (objets visuels animés ou statiques)
# from map import TileKind, Map # TileKind : Définit les types de tuiles (sol, mur, etc.)
# Map : Définit la carte ou niveau de jeu
# charger le menu principal
# from Main_menu import *

# Création de la fenêtre du jeu avec une résolution de 1920x1080 et un titre 'Night Dungeon'
# screen = create_screen(1920, 1080, 'Night Dungeon')
# Couleur de fond (noir)
clear_color = (0, 0, 0)
# Variable de la boucle
running = True
up = False
down = False
right = False
left = False
attack_state = False
lifeState = 3
victory = False

# importer la camera
from camera import *

# génération de la map
GenMap(level)

mobSpawn(level)

# création du joueur
player = Player([mapgen.startPoint[0] * nbBlocksX + 4, mapgen.startPoint[1] * nbBlocksY + 4], attack_power=1, attack_range=2, attack_cooldown=1)
# Boucle principale du jeu
while running:
    startTime = time.time()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #arrêtez le jeu
            running = False  
    screen.fill(clear_color)# Clear the screen 
    # add keys event
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_w] or keys[pygame.K_UP]) and (keys[pygame.K_s] or keys[pygame.K_DOWN]) and keys[pygame.K_d] == False and keys[pygame.K_RIGHT] == False and keys[pygame.K_a] == False and keys[pygame.K_LEFT] == False :
        # Static if up and down is pressed in the same time
        up = down = right = left = False
        walkCount = 0

    elif (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and (keys[pygame.K_a] or keys[pygame.K_LEFT]) and keys[pygame.K_w] == False and keys[pygame.K_UP] == False and keys[pygame.K_s] == False and keys[pygame.K_DOWN] == False:
        # Static if right and left is pressed in the same time
        up = down = right = left = False
        walkCount = 0
    else:
        if keys[pygame.K_w] or keys[pygame.K_UP] :# if the keys to go up are pressed 
            if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and keys[pygame.K_a] == False and keys[pygame.K_LEFT] == False :
                up = False
                right = True
                down = False
                left = False
                attack_state = False
            elif (keys[pygame.K_a] or keys[pygame.K_LEFT]) and  keys[pygame.K_d] == False and keys[pygame.K_RIGHT] == False:
                up = False
                right = False
                down = False
                left = True
                attack_state = False
            else:
                up = True
                right = False
                down = False
                left = False
                attack_state = False

        elif keys[pygame.K_s] or keys[pygame.K_DOWN]:  # if the keys to go down are pressed
            if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and keys[pygame.K_a] == False and keys[pygame.K_LEFT] == False:
                up = False
                right = True
                down = False
                left = False
                attack_state = False
            elif (keys[pygame.K_a] or keys[pygame.K_LEFT]) and  keys[pygame.K_d] == False and keys[pygame.K_RIGHT] == False:
                up = False
                right = False
                down = False
                left = True
                attack_state = False
            else:
                up = False
                right = False
                down = True
                left = False
                attack_state = False
        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]: # if the keys to go right are pressed
            up = False
            right = True
            down = False
            attack_state = False
            left = False
        elif keys[pygame.K_a] or keys[pygame.K_LEFT]: # if the keys to go left are pressed
            up = False
            right = False
            down = False
            left = True
            attack_state = False

        else:
            up = right = down = left= attack_state = False # if no keys is pressed he was static
            walkCount = 0
        if event.type == pygame.MOUSEBUTTONDOWN: # if mouse boutton is pressed
            for i in entitiesList:
                player.attack(i)
            attack_state = True

    player.refresh(direction_up=up,direction_down=down,direction_left=left,direction_right=right , attack=attack_state,life_state=player.health)
    for i in entitiesList:
        if float(float(float(i.position[0] - player.position[0]) ** 2 ) ** 0.5) <= 10 and float(float(float(i.position[1] - player.position[1]) ** 2 ) ** 0.5) <= 10:
            i.move_randomly(player)
    # Pause pour limiter la vitesse d'exécution de la boucle à 0.1s
    while time.time() < startTime + 0.05:
        pass
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        player.move(0, -0.2)
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        player.move(0, 0.2)
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player.move(-0.2, 0)
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        player.move(0.2, 0)

    if isinstance(mapgen.map[int(player.position[0] // 1)][int(player.position[1] // 1)], Chest):
        victory = True
        running = False

if victory:
    screen.blit(images["victory"], [screen.get_height() // 2 - 275, screen.get_width() // 2 - 55])
    pygame.display.flip()
    pygame.time.wait(3000)

pygame.quit()
