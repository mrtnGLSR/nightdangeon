import pygame
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect
from enum import Enum
import math
# Variables
running = True
RED = (178, 34, 34)
WHITE = (255, 255, 255)
game_state = ""



# functions
def create_surface_with_text(text,font_size, text_rgb, bg_rgb):
    # creation font variable
    font = pygame.freetype.Font("./fonts/Ancient Medium.ttf", font_size)
     # Render the text to get its dimensions
    _, text_rect = font.render(text=text, fgcolor=text_rgb)

    # Create a surface with dimensions to fit the text and enable transparency
    surface = pygame.Surface((text_rect.width, text_rect.height), pygame.SRCALPHA)
    
    # Center the text on the surface
    text_rect.center = (text_rect.width // 2, text_rect.height // 2)
    
    # Render the text to the surface at the centered position
    font.render_to(surface, text_rect.topleft, text, fgcolor=text_rgb)
    return surface.convert_alpha()

class UIElement(Sprite):

    def __init__(self, center_position, text, font_size, bg_rgb, text_rgb, action=None):
        super().__init__()
        self.mouse_over = False

        # Créez les images par défaut et sur survol de la souris
        default_image = create_surface_with_text(text, font_size, text_rgb, bg_rgb)
        highlight_image = create_surface_with_text(text, font_size * 1.2, text_rgb, bg_rgb)
        self.images = [default_image, highlight_image]
        self.rects = [default_image.get_rect(center=center_position), 
                      highlight_image.get_rect(center=center_position)]
        self.action = action

    @property
    def image(self):
        return self.images[1] if self.mouse_over else self.images[0]
    
    @property
    def rect(self):
        return self.rects[1] if self.mouse_over else self.rects[0]
    
    def update(self, mouse_position, mouse_up):

        if self.rect.collidepoint(mouse_position):
            self.mouse_over = True

            if mouse_up:
                return self.action
        else:
            self.mouse_over = False

        return None  

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class GameState(Enum):
    QUIT = -1
    TITLE = 0
    OPTIONS = 1

def main():
    global running
    pygame.init()
    screen = pygame.display.set_mode((1040, 1040))
    game_state = GameState.TITLE
    
    while running:
        if game_state == GameState.TITLE:
            game_state = title_screen(screen)
        elif game_state == GameState.OPTIONS:
            game_state = options_screen(screen)
        elif game_state == GameState.QUIT:
            running = False  # Arrête la boucle principale
            return

def title_screen(screen):
     global running, game_state
    #  load images
     background_image = pygame.image.load("./img/background.jpg")
     btn_start = UIElement(
        center_position=(520, 420),
        font_size=70,
        bg_rgb=WHITE,
        text_rgb=WHITE,
        text='Start!',
        action=None
    )

     btn_options = UIElement(
        center_position=(520, 480),
        font_size=35,
        bg_rgb=WHITE,
        text_rgb=WHITE,
        text='Options',
        action=GameState.OPTIONS
    )

     btn_quit = UIElement(
        center_position=(520, 520),
        font_size=35,
        bg_rgb=WHITE,
        text_rgb=WHITE,
        text='Quit',
        action=GameState.QUIT
    )
     Title = UIElement(
        center_position=(520, 200),
        font_size=80,
        bg_rgb=WHITE,
        text_rgb=WHITE,
        text='Night Dungeon',

    )
    
     entitys = [btn_start, btn_options, btn_quit] 

     while running:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
            
            if event.type == pygame.QUIT:
                return GameState.QUIT

            # Blit l'image de fond
            screen.blit(background_image, (0, 0))

            # Mettre à jour et dessiner tous les éléments de l'interface
            for entity in entitys:
                ui_action = entity.update(pygame.mouse.get_pos(), mouse_up)
                if ui_action is not None:
                    return ui_action  # Retourne l'action pour changer d'état
                entity.draw(screen)
                
            ui_action = Title.update((0, 0), None)
            Title.draw(screen)
            if ui_action is not None:
                return ui_action  # Retourner l'action pour changer d'état
            
            pygame.display.flip()


def options_screen(screen):
    btn_return = UIElement(
        center_position=(100, 900),
        font_size=30,
        bg_rgb=WHITE,
        text_rgb=WHITE,
        text='Return',
        action=GameState.TITLE
    )

    Title = UIElement(
        center_position=(520, 200),
        font_size=60,
        bg_rgb=WHITE,
        text_rgb=WHITE,
        text='Options',

    )
    running = True
    while running:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:

                mouse_up = True

            if event.type == pygame.QUIT:
                return GameState.QUIT

        screen.fill((0, 0, 0))
        background_image = pygame.image.load("./img/background.jpg")
        screen.blit(background_image, (0, 0))
        ui_action = Title.update((0, 0), None)
        Title.draw(screen)
        # Met à jour et vérifie l'action du bouton
        ui_action = btn_return.update((pygame.mouse.get_pos()), mouse_up)
        if ui_action is not None:
            return ui_action

        btn_return.draw(screen)
        pygame.display.flip()



main()
