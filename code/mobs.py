import random
from nodes import Solide
import time

# Définir la taille de la carte
mapSize = (8 * 9, 8 * 9)  # 8 chunks x 9 blocks, par exemple
# Créer une carte de taille spécifiée, remplie d'objets Solide
map = [[Solide([], (i, j), True, False, [100]) for j in range(mapSize[1])] for i in range(mapSize[0])]

# Position initiale du joueur
player_position = [80, 80]

# Classe représentant les mobs
class Mobs(Solide):
    def __init__(self, draw, position, walkable, texture, health):
        # Initialisation de la classe parent Solide
        super().__init__(draw, position, walkable, texture, [100])
        self.health = health  # Attribut de santé du mob

    def move(self, xMove, yMove):
        # Vérifie si le mob doit se déplacer
        if xMove == 0 and yMove == 0:
            return
        
        wayDistance = abs(xMove) if xMove else abs(yMove)  # Distance de mouvement

        # Déterminer la direction du mouvement
        direction = "E" if xMove > 0 else "O" if xMove < 0 else "S" if yMove > 0 else "N"
        
        distances = [0, 0, 0, 0]  # Liste pour stocker les distances
        index = 0
        
        # Vérifie les blocs sur le chemin du mouvement
        for i in self.draw:
            for j in range(int((xMove**2 + yMove**2) ** 0.5) + 2):
                block = [
                    int(self.position[0] + i[0]) // 1 + j * {"E": 1, "O": -1, "N": 0, "S": 0}[direction],
                    int(self.position[1] + i[1]) // 1 + j * {"E": 0, "O": 0, "N": -1, "S": 1}[direction]
                ]
                # Vérifie si le bloc est dans les limites et s'il est praticable
                if 0 < block[0] < mapSize[0] - 1 and 0 < block[1] < mapSize[1] - 1:
                    if map[block[0]][block[1]].walkable:
                        distances[index] += 1
                    else:
                        break
            # Met à jour les distances en fonction de la direction
            distances[index] += {
                "N": self.draw[1][1], "S": -self.draw[3][1], "E": -self.draw[2][0], "O": self.draw[0][0]
            }[direction] + round(self.position[{"N": 1, "S": 1, "E": 0, "O": 0}[direction]] * {
                "N": 1, "S": -1, "E": -1, "O": 1
            }[direction] % 1, 1)
            index += 1
        
        # Ajuste le mouvement si des obstacles sont rencontrés
        if min(distances) < wayDistance:
            if direction in ["N", "S"]:
                yMove = min(distances) * {"N": -1, "S": 1}[direction]
            else:
                xMove = min(distances) * {"E": 1, "O": -1}[direction]
        if min(distances) <= 0:
            xMove = yMove = 0  # Arrête le mouvement si aucun espace n'est disponible

        # Met à jour la position du mob
        self.position = [round(self.position[0] + xMove, 1), round(self.position[1] + yMove, 1)]


# Classe représentant un mob spécifique, héritant de Mobs
class Mob(Mobs):
    def __init__(self, position,):
        # Initialise la classe parent Mobs
        super().__init__(draw=[[-0.4, -0.4], [0.4, -0.4], [0.4, 0.4], [-0.4, 0.4]], position=position, walkable=False, texture=False, health=100)

    def distance_to_player(self, player_position):
        # Calcule la distance entre le mob et le joueur
        return ((self.position[0] - player_position[0]) ** 2 + (self.position[1] - player_position[1]) ** 2) ** 0.5

    def move_towards_player(self, player_position):
        # Calcule la direction vers le joueur
        x_diff = player_position[0] - self.position[0]
        y_diff = player_position[1] - self.position[1]
        
        # Normaliser le déplacement
        distance = (x_diff ** 2 + y_diff ** 2) ** 0.5
        if distance > 0:
            # Déplace le mob vers le joueur d'une distance fixe
            xMove = (x_diff / distance) * 0.2
            yMove = (y_diff / distance) * 0.2
            self.move(xMove, yMove)  # Appelle la méthode move pour actualiser la position

    def move_randomly(self, player_position):
        # Vérifie la distance au joueur pour décider du mouvement
        if self.distance_to_player(player_position) <= 10:
            self.move_towards_player(player_position)  # Avance vers le joueur si à portée
        else:
            # Choisit des déplacements aléatoires si le joueur est hors portée
            xMove = random.choice([-0.2, 0, 0.2])
            yMove = random.choice([-0.2, 0, 0.2])
            self.move(xMove, yMove)  # Appelle la méthode move pour actualiser la position

# Création d'une instance de Mob à la position (2, 2)
mob_instance = Mob(position=(2, 2))
while True:  # Boucle infinie pour le mouvement # Pause de 0.5 secondes entre les mouvements
    mob_instance.move_randomly(player_position)  # Déplace le mob selon la logique définie
    print(mob_instance.position)  # Affiche la position actuelle du mob
