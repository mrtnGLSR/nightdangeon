import random
from Engine import *
import time

# Définir la taille de la carte
mapSize = (8 * 9, 8 * 9)  # 8 chunks x 9 blocks, par exemple
# Créer une carte de taille spécifiée, remplie d'objets Solide

# map = [[Solide([], (i, j), True, False, [100]) for j in range(mapSize[1])] for i in range(mapSize[0])]

# Position initiale du joueur
player_position = [20, 20]

# création d'une liste pour contenir les entités
entitiesList = []

# Classe représentant les mobs
class Mobs(Entity):
    def __init__(self, draw, position, texture, passif, viewDistance, damages, speed, health, textureState, mobile):
        # Initialisation de la classe parent Solide
        Entity.__init__(self, draw, position, True, texture, health)
        self.passif = passif # True si passifique, False si dangereux
        self.viewDistance = viewDistance # distance à la quelle le monstre peut voir
        self.damages = damages # dégats du mob
        self.speed = speed # distance parcourue en un cycle
        self.textureState = textureState # quel limage sera en cours de chargement
        self.mobile = mobile # définir si le joueur est en mouvement pour les positions
    
    # Calcule la distance entre le mob et le joueur
    def distance_to_player(self, player_position):
        return ((self.position[0] - player_position[0]) ** 2 + (self.position[1] - player_position[1]) ** 2) ** 0.5
    
    # Calcule la direction vers le joueur
    def move_towards_player(self, player_position):
        x_diff = player_position[0] - self.position[0]
        y_diff = player_position[1] - self.position[1]
        
        # Normaliser le déplacement
        distance = (x_diff ** 2 + y_diff ** 2) ** 0.5
        print(f"distance monstre - joueur : {distance}")
        if distance != 0:
            # Déplace le mob vers le joueur d'une distance fixe
            if x_diff != 0:
                xMove = (x_diff / abs(x_diff)) * self.speed
            else:
                xMove = 0
            if y_diff != 0:
                yMove = (y_diff / abs(y_diff)) * self.speed
            else:
                yMove = 0
            self.move(xMove, yMove)  # Appelle la méthode move pour actualiser la position
    
    # bouger de manière aléatoire en fonction de la distance du joueur
    def move_randomly(self, player_position):
        print("mouvement controllé")
        # Vérifie la distance au joueur pour décider du mouvement
        if self.distance_to_player(player_position) <= self.viewDistance:
            self.move_towards_player(player_position)  # Avance vers le joueur si à portée
        else:
            print("mouvement aléatoir")
            # Choisit des déplacements aléatoires si le joueur est hors portée
            xMove = random.choice([-self.speed, 0, self.speed])
            yMove = random.choice([-self.speed, 0, self.speed])
            self.move(xMove, yMove)  # Appelle la méthode move pour actualiser la position


# monstre gardian
class Guardian(Mobs):
    def __init__(self, position,):
        super().__init__([[-0.4, -0.4], [0.4, -0.4], [0.4, 0.4], [-0.4, 0.4]], # draw
                         position,
                         # textures
                         {"S":["guardian-sud-1", "guardian-sud-2", "guardian-sud-3"],
                          "N":["guardian-nord-1", "guardian-nord-2", "guardian-nord-3"],
                          "E":["guardian-est-1", "guardian-est-2", "guardian-est-3"],
                          "O":["guardian-west-1", "guardian-west-2", "guardian-west-3"],
                          "D":["guardian-death-1", "guardian-death-2", "guardian-death-3", "guardian-death-4"]}, 
                          False, # passif
                          5, # viewdistance
                          1, # dammages
                          0.1, # speed
                          10, # health
                          ["S", 0], #textureState
                          False) # mobile

# placer les créatures
Y = 0
print(chunkMap)
for chunkLine in chunkMap:
    X = 0
    for chunk in chunkLine:
        if chunk.chunkType != "Full":
            if random.randint(0, 100) <= 30 :
                entitiesList.append(Guardian([X * nbBlocksX + nbBlocksX / 2, Y * nbBlocksY + nbBlocksY / 2]))
            pass
        X += 1
    Y += 1
print(f"créatures : {entitiesList}")


    



# Création d'une instance de Mob à la position (2, 2)
#mob_instance = Mob(position=(random.randint(2, 78), random.randint(2, 78)), speed=0.2)
#while True:  # Boucle infinie pour le mouvement # Pause de 0.5 secondes entre les mouvements
#    time.sleep(0.5)
#    mob_instance.move_randomly(player_position)  # Déplace le mob selon la logique définie
#    print(mob_instance.position)  # Affiche la position actuelle du mob
