# api for the game

# modules
from mapgen import *
from nodes import Solide
from copy import copy
import time

# constants
nbChunkX = 8
nbChunkY = 8
nbBlocksX = 9
nbBlocksY = 9

# déclaration de la camera
class Camera():
    def __init__(self, player):
        self.player = player

# définitions des entités (objets mobiles)
class Entity(Solide):
    def __init__(self, draw, position, walkable, texture, health):
        Solide.__init__(self, draw, position, walkable, texture, [100])
        self.health = health
        self.camera = Camera(self)

    # fonction  de rafraichissement
    def refresh(self, direction_up, direction_down, direction_left, direction_right, attack, life_state):
        self.camera.refresh(direction_up,direction_down,direction_left,direction_right, attack, life_state, self.position)


    # fonction de mouvement
    def move(self, xMove, yMove):

        # vérifier que le mouvement ne se fasse pas dans le vide
        if xMove == 0 and yMove == 0:
            return
        
        # définition de la distance 
        wayDistance = 0
        if xMove:
            wayDistance = xMove ** 2 // xMove
        else:
            wayDistance = yMove ** 2 // yMove
        
        # définition de la direction
        if xMove > 0:
            direction = "E"
        elif xMove < 0:
            direction = "O"
        elif yMove > 0:
            direction = "S"
        else:
            direction = "N"
        


        # définition de la distance que le joueur peut parcourir
        distances=[0, 0, 0, 0]
        index = 0
        # pour chaque point du joueur
        for i in self.draw:
            # pour la l'entier de la distance à parcourir
            #                   vvvvvvvvvvv---convertion en float pour ne pas avoir de nombes complex
            for j in range(int((float(float(xMove + yMove) ** 2) ** 0.5) // 1 + 2)):
                # définir le bloque à analyser
                block = [int(self.position[0] + i[0]) // 1 + j * {"E":1, "O":-1, "N":0, "S":0}[direction], int(self.position[1] + i[1]) // 1 + j * {"E":0, "O":0, "N":-1, "S":1}[direction]]
                # vérifier que le bloque est dans la map et si il est est emprintable
                if 0 < block[0] < mapSize[0] -1 and 0 < block[1] < mapSize[1] - 1:
                    if map[block[0]][block[1]].walkable:
                        distances[index] += 1
                    else:
                        break
            # ajouter la forme du joueur
            distances[index] += {"N":self.draw[1][1], "S":-self.draw[3][1], "E":-self.draw[2][0], "O":self.draw[0][0]}[direction] + round(self.position[{"N":1, "S":1, "E":0, "O":0}[direction]] * {"N":1, "S":-1, "E":-1, "O":1}[direction] % 1, 1)
            index += 1
        # redéfinition de la distance à parcourir en fonction des obstacles
        if min(distances) < wayDistance:
            if direction in ["N", "S"]:
                yMove = min(distances) * {"N":-1, "S":1}[direction]
            else:
                xMove = min(distances) * {"E":1, "O":-1}[direction]
        if min(distances) <= 0:
            xMove = yMove = 0


        self.position = [round(self.position[0] + xMove, 1), round(self.position[1] + yMove, 1)]

# définition du joueur
class Player(Entity):
    def __init__(self, position, attack_range, attack_power, attack_cooldown, ):
        super().__init__([[-0.4, -0.4], [0.4, -0.4], [0.4, 0.4], [-0.4, 0.4]], position, False, False, 100)
        self.health = 3  # Santé initiale du joueur
        self.attack_range = attack_range  # Portée d'attaque du joueur
        self.attack_cooldown = attack_cooldown # cooldown entre chaque attaque
        self.attack_power = attack_power  # Puissance d'attaque du joueur
        self.last_attack_time = 0
    def take_damage(self, damage):
        self.health -= damage

    def attack(self, mob):
        # Vérifie si le mob est à portée d'attaque
        distance_to_mob = ((self.position[0] - mob.position[0]) ** 2 + (self.position[1] - mob.position[1]) ** 2) ** 0.5
        current_time = time.time()

        if distance_to_mob <= self.attack_range:
            # Vérifie si le cooldown est respecté
            if current_time - self.last_attack_time >= self.attack_cooldown:
                print("Le joueur attaque le mob !")
                mob.take_damage(self.attack_power)  # Inflige des dégâts au mob
                self.last_attack_time = current_time  # Met à jour le dernier moment d'attaque
            else:
                print("Attaque en cooldown, veuillez patienter.")


