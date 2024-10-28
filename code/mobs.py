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
    def __init__(self, draw, position, texture, passif, viewDistance, damages, speed, health, textureState, mobile,attack_power, attack_range, attack_cooldown):
        # Initialisation de la classe parent Solide
        Entity.__init__(self, draw, position, True, texture, health)
        self.passif = passif # True si passifique, False si dangereux
        self.viewDistance = viewDistance # distance à la quelle le monstre peut voir
        self.damages = damages # dégats du mob
        self.speed = speed # distance parcourue en un cycle
        self.textureState = textureState # quel limage sera en cours de chargement
        self.mobile = mobile # définir si le joueur est en mouvement pour les positions
        self.attack_power = attack_power  # Dégâts infligés par attaque
        self.attack_range = attack_range  # Portée d'attaque
        self.attack_cooldown = attack_cooldown  # Temps d'attente entre les attaques
        self.last_attack_time = 0  # Dernière attaque enregistrée
    
    # perte de vie
    def take_damage(self, damage):
        self.health -= damage

        if self.health <= 0:
            self.die()  # Gérer la mort du mob
    
    # mort
    def die(self):
        # Actions à effectuer lors de la mort du mob (ex. : disparition, suppression de la liste des mobs)
        if self in entitiesList:
            entitiesList.remove(self)
        # Vous pouvez également ajouter des actions comme supprimer le mob de la liste active
    
    #attaque sur le joueur
    def attack(self, player):
        # Vérifie si le mob peut attaquer en fonction du temps écoulé
        current_time = time.time()
        if current_time - self.last_attack_time >= self.attack_cooldown:
            player.take_damage(self.attack_power)  # Réduit la santé du joueur
            self.last_attack_time = current_time  # Met à jour le dernier moment d'attaque

    # Calcule la distance entre le mob et le joueur
    def distance_to_player(self, player_position):
        # Calcule la distance entre le mob et le joueur
        return ((self.position[0] - player_position[0]) ** 2 + (self.position[1] - player_position[1]) ** 2) ** 0.5

    def attack(self, player):
        # Vérifie si le mob peut attaquer en fonction du temps écoulé
        current_time = time.time()
        if current_time - self.last_attack_time >= self.attack_cooldown:
            player.take_damage(self.attack_power)  # Réduit la santé du joueur
            self.last_attack_time = current_time  # Met à jour le dernier moment d'attaque

    def move_towards_player(self, player_position):
        # Calcule la direction vers le joueur
        x_diff = player_position[0] - self.position[0]
        y_diff = player_position[1] - self.position[1]
        
        # Normaliser le déplacement
        distance = (x_diff ** 2 + y_diff ** 2) ** 0.5
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
            if xMove == 0 and yMove == 0:
                self.mobile = False
            else:
                self.mobile = True

            self.textureState[0] = self.move(xMove, yMove)  # Appelle la méthode move pour actualiser la position
    
    # bouger de manière aléatoire en fonction de la distance du joueur
    def move_randomly(self, player):
        player_position = player.position
        # Si le joueur est à portée d'attaque, le mob attaque au lieu de bouger
        if self.distance_to_player(player_position) <= self.attack_range:
            self.attack(player)
        elif self.distance_to_player(player_position) <= 10:
            # Avance vers le joueur si à portée de mouvement
            self.move_towards_player(player_position)
        else:
            # Choisit des déplacements aléatoires si le joueur est hors portée
            xMove = random.choice([-self.speed, 0, self.speed])
            yMove = random.choice([-self.speed, 0, self.speed])
            self.textureState[0] = self.move(xMove, yMove)  # Appelle la méthode move pour actualiser la position
    
    # mettre à jour l'image
    def updateIMG(self):
        if self.mobile:
            # passer à l'animation suivante
            self.textureState[1] = (self.textureState[1] + 1) % len(self.texture[self.textureState[0]])
        else:
            # passer ou rester à la première annimation
            self.textureState[1] = 0


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
                          3, # health
                          ["S", 0], #textureState
                          False, # mobile
                          2, # AttackDamage
                          1, # AttackRange
                          1.5) # AttackCooldown
        

# placer les créatures
X = 0
for chunkLine in chunkMap:
    Y = 0
    for chunk in chunkLine:
        if chunk.chunkType != "Full":
            if random.randint(0, 100) <= 30 :
                entitiesList.append(Guardian([X * nbBlocksX + nbBlocksX / 2, Y * nbBlocksY + nbBlocksY / 2]))
            pass
        Y += 1
    X += 1

    




