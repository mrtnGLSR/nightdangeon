# modules
from time import time

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
# Définition des types de tuiles, avec une image et une propriété 
# tile_kinds = [
#     TileKind('floor', './img/brick-floor.jpg', False),  # Sol 
#     TileKind('wall', './img/brick-wall.jpg', False)     # Mur 
# ]

# importer la camera
from Engine import *

# génération de la map
GenMap()

# création du joueur
print("startpoint:")
print(startPoint)
player = Player([3.6,4])
# Chargement de la carte 
# Taille des tuiles = 80 pixels

# map = Map('./maps/start.map', tile_kinds, 80)

# Boucle principale du jeu
while running:
    startTime = time()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #arrêtez le jeu
            running = False  
    screen.fill(clear_color)  # Efface l'écran en remplissant avec la couleur de fond (noir)
    
    # map.draw(screen)  # Dessine la carte (tuiles de sol, murs) sur l'écran
    
    # for s in sprites:  # Parcourt tous les sprites du jeu
    #     s.draw(screen)  # Dessine chaque sprite sur l'écran
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
            attack_state = False
        elif keys[pygame.K_s] or keys[pygame.K_DOWN]:  # if the keys to go down are pressed
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
        elif keys[pygame.K_o]:
            lifeState = 0
        else:
            up = right = down = left= attack_state = False # if no keys is pressed he was static
            walkCount = 0
        if event.type == pygame.MOUSEBUTTONDOWN: # if mouse boutton is pressed
            attack_state = True

    player.refresh(direction_up=up,direction_down=down,direction_left=left,direction_right=right, attack=attack_state)
    # player.move(0.1, 0)
    #pygame.display.flip()  # Rafraîchit l'écran, montre tout ce qui a été dessiné
    # Pause pour limiter la vitesse d'exécution de la boucle à 0.1s
    while time() < startTime + 0.05:
        pass
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        player.move(0, -0.2)
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        player.move(0, 0.2)
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player.move(-0.2, 0)
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        player.move(0.2, 0)
    print("player-position" + str(player.position))
pygame.quit()
