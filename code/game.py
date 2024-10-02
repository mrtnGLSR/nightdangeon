# modules


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

# Définition des types de tuiles, avec une image et une propriété 
# tile_kinds = [
#     TileKind('floor', './img/brick-floor.jpg', False),  # Sol 
#     TileKind('wall', './img/brick-wall.jpg', False)     # Mur 
# ]

# importer la camera
from Engine import *

# création du joueur
player = Player([5, 5, 5, 5])

# Chargement de la carte 
# Taille des tuiles = 80 pixels

# map = Map('./maps/start.map', tile_kinds, 80)

# Boucle principale du jeu
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #arrêtez le jeu
            running = False  
    # screen.fill(clear_color)  # Efface l'écran en remplissant avec la couleur de fond (noir)
    
    # map.draw(screen)  # Dessine la carte (tuiles de sol, murs) sur l'écran
    
    # for s in sprites:  # Parcourt tous les sprites du jeu
    #     s.draw(screen)  # Dessine chaque sprite sur l'écran
    

    player.refresh()
    player.move(0.1, 0)
    #pygame.display.flip()  # Rafraîchit l'écran, montre tout ce qui a été dessiné
    # Pause pour limiter la vitesse d'exécution de la boucle à environ 70 ms
    pygame.time.delay(1000)
pygame.quit()
