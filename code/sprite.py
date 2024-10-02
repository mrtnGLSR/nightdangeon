import pygame
from camera import camera

# Liste globale pour stocker tous les sprites à dessiner
sprites = []

# Dictionnaire pour stocker les images déjà chargées (pour éviter de recharger plusieurs fois la même image)
loaded = {}

class Sprite:
    def __init__(self, image, x, y):
        """
        Initialise un sprite avec une image et des coordonnées (x, y).
        
        :param image: Chemin vers l'image à charger.
        :param x: Position X du sprite.
        :param y: Position Y du sprite.
        """
        # Vérification si l'image a déjà été chargée
        if image in loaded:
            self.image = loaded[image] 
        else:
            self.image = pygame.image.load(image)  # Chargement de l'image depuis le fichier
            loaded[image] = self.image  # Stockage de l'image chargée dans le cache
        
        self.x = x  # Position X du sprite
        self.y = y  # Position Y du sprite

        # Ajout du sprite à la liste globale
        sprites.append(self)
