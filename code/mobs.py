import random
from nodes import Solide
import time

# Définir la taille de la carte
mapSize = (8 * 9, 8 * 9)  # 8 chunks x 9 blocks, par exemple
map = [[Solide([], (i, j), True, False, [100]) for j in range(mapSize[1])] for i in range(mapSize[0])]  # Exemple de map

player_position = [2, 2]

class Mobs(Solide):
    def __init__(self, draw, position, walkable, texture, health):
        super().__init__(draw, position, walkable, texture, [100])
        self.health = health

    def move(self, xMove, yMove):
        if xMove == 0 and yMove == 0:
            return
        
        wayDistance = abs(xMove) if xMove else abs(yMove)
        
        direction = "E" if xMove > 0 else "O" if xMove < 0 else "S" if yMove > 0 else "N"
        
        distances = [0, 0, 0, 0]
        index = 0
        
        for i in self.draw:
            for j in range(int((xMove**2 + yMove**2) ** 0.5) + 2):
                block = [
                    int(self.position[0] + i[0]) // 1 + j * {"E": 1, "O": -1, "N": 0, "S": 0}[direction],
                    int(self.position[1] + i[1]) // 1 + j * {"E": 0, "O": 0, "N": -1, "S": 1}[direction]
                ]
                if 0 < block[0] < mapSize[0] - 1 and 0 < block[1] < mapSize[1] - 1:
                    if map[block[0]][block[1]].walkable:
                        distances[index] += 1
                    else:
                        break
            distances[index] += {
                "N": self.draw[1][1], "S": -self.draw[3][1], "E": -self.draw[2][0], "O": self.draw[0][0]
            }[direction] + round(self.position[{"N": 1, "S": 1, "E": 0, "O": 0}[direction]] * {
                "N": 1, "S": -1, "E": -1, "O": 1
            }[direction] % 1, 1)
            index += 1
        
        if min(distances) < wayDistance:
            if direction in ["N", "S"]:
                yMove = min(distances) * {"N": -1, "S": 1}[direction]
            else:
                xMove = min(distances) * {"E": 1, "O": -1}[direction]
        if min(distances) <= 0:
            xMove = yMove = 0

        self.position = [round(self.position[0] + xMove, 1), round(self.position[1] + yMove, 1)]


class Mob(Mobs):
    def __init__(self, position):
        super().__init__(draw=[[-0.4, -0.4], [0.4, -0.4], [0.4, 0.4], [-0.4, 0.4]], position=position, walkable=False, texture=False, health=100)

    def move_randomly(self):
        # Choisir des déplacements aléatoires
        xMove = random.choice([-0.2, 0, 0.2])
        yMove = random.choice([-0.2, 0, 0.2])
        
        # Utiliser la méthode de mouvement définie dans Mobs
        self.move(xMove, yMove)

# Exemple d'utilisation
mob_instance = Mob(position=(2, 2))
while True :
    time.sleep(0.5)
    mob_instance.move_randomly()
    print(mob_instance.position)



