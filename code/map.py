import pygame
from camera import camera

class TileKind:
    def __init__(self, name, image, is_solid):
        #Initialise un type de tuile avec un nom, une image et une propriété solidité.
        self.name = name
        self.image = pygame.image.load(image)  # Charge l'image pour la tuile
        self.is_solid = is_solid  # Détermine si la tuile est traversable ou non

class Map:
    def __init__(self, map_file, tile_kinds, tile_size):
        """
        Initialise une carte en lisant un fichier texte de tuiles.
        - map_file: chemin vers le fichier de carte.
        - tile_kinds: une liste d'instances de TileKind.
        - tile_size: taille (en pixels) d'une tuile.
        """
        self.tile_kinds = tile_kinds  # Assigne les types de tuiles
        self.tile_size = tile_size  # Assigne la taille de chaque tuile

        # Lecture du fichier contenant la carte
        self.tiles = []
        with open(map_file, 'r') as file:
            data = file.read()
            for line in data.split('\n'):
                row = []
                for tile_number in line:
                    row.append(int(tile_number))
                self.tiles.append(row)  # Ajoute la ligne à la carte

        
    def draw(self, screen):
        # Dessine la carte sur l'écran en fonction de la caméra.
        for y, row in enumerate(self.tiles):  # Parcourt chaque ligne de tuiles
            for x, tile in enumerate(row):    # Parcourt chaque tuile de la ligne
                location = (x * self.tile_size - camera.x, y * self.tile_size - camera.y)  # Calcule la position de la tuile en tenant compte de la caméra
                image = self.tile_kinds[tile].image  # Récupère l'image de la tuile
                screen.blit(image, location)  # Dessine la tuile sur l'écran
