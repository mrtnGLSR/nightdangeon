import pygame
import pygame.freetype
from pygame.sprite import Sprite
from enum import Enum
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
import pygame_widgets
from pathlib import Path
# Variables
running = True
RED = (178, 34, 34)
WHITE = (255, 255, 255)
game_state = ""
vol_music = 0.5 # Variable volume de la musique
vol_buttons_sfx = 1
# Initialisation de Pygame
pygame.init()
screen_width = 1040
screen_height = 798
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Night Dungeon")

# Lancement de la musique et des sfx
pygame.mixer.init()
lobby_music = pygame.mixer.Sound('./music/SM_Lobby.mp3')
lobby_music.play()
lobby_music.set_volume(vol_music)

button_sfx = pygame.mixer.Sound('./sfx/button_sfx.mp3')
lobby_music.set_volume(vol_buttons_sfx)

# Chargement de l'image d'arrière-plan
background_image = pygame.image.load("./img/bg.png").convert()
bg_width = background_image.get_width()
scroll_x = 0
scroll_speed = 0.03


# functions
def create_surface_with_text(text,font_size, text_rgb, bg_rgb):
    font = pygame.freetype.Font(("." + "/fonts/OwreKynge.ttf"), font_size) # creation font variable
    _, text_rect = font.render(text=text, fgcolor=text_rgb)     # Render the text to get its dimensions
    surface = pygame.Surface((text_rect.width, text_rect.height), pygame.SRCALPHA) # Create a surface with dimensions to fit the text and enable transparency
    text_rect.center = (text_rect.width // 2, text_rect.height // 2) # Center the text on the surface
    font.render_to(surface, text_rect.topleft, text, fgcolor=text_rgb)# Render the text to the surface at the centered position
    return surface.convert_alpha()

class UIElement(Sprite):
    def __init__(self, center_position, text, font_size, bg_rgb, text_rgb, action=None):
        self.mouse_over = False
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

def starting_game():
    exec(Path("game.py").read_text())

def scrolling_bg():
    global scroll_x
    scroll_x -= scroll_speed
    if scroll_x <= -bg_width:
        scroll_x = 0
    screen.blit(background_image, (scroll_x, 0))
    screen.blit(background_image, (scroll_x + bg_width, 0))

def title_screen(screen):
    global running
    btn_start = UIElement(center_position=(520, 420), 
                          font_size=70, bg_rgb=WHITE, 
                          text_rgb=WHITE, text='Start!', 
                          action=starting_game)
    btn_options = UIElement(center_position=(520, 480),
                            font_size=35, bg_rgb=WHITE,
                            text_rgb=WHITE, text='Options',
                            action=GameState.OPTIONS)
    btn_quit = UIElement(center_position=(520, 520),
                         font_size=35, bg_rgb=WHITE,
                         text_rgb=WHITE, text='Quit',
                         action=GameState.QUIT)
    Title = UIElement(center_position=(520, 200),
                      font_size=80, bg_rgb=WHITE,
                      text_rgb=WHITE,
                      text='Night Dungeon')

    entitys = [btn_start, btn_options, btn_quit, Title]

    while running:
        mouse_up = False
        for event in pygame.event.get():
                
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pygame.mixer.Channel(0).play(pygame.mixer.Sound(button_sfx))# Joue le sfx de quannd on appuies sur la souris
                mouse_up = True
            if event.type == pygame.QUIT:
                return GameState.QUIT

        scrolling_bg()  # Dessiner l'arrière-plan

        for entity in entitys:
            ui_action = entity.update(pygame.mouse.get_pos(), mouse_up)
            entity.draw(screen)
            if ui_action is not None:
                return ui_action

        pygame.display.flip()

def options_screen(screen):
    btn_return = UIElement(center_position=(70, 700), font_size=30, bg_rgb=WHITE, text_rgb=WHITE, text='Return', action=GameState.TITLE)
    Title = UIElement(center_position=(520, 200), font_size=60, bg_rgb=WHITE, text_rgb=WHITE, text='Options')
    music_text = UIElement(center_position=(520, 250), font_size=40, bg_rgb=WHITE, text_rgb=WHITE, text='Music')
    slider_music = Slider(screen, 450, 300, 150, 15, min=0, max=100, step=1,colour=(255, 255, 255),  handleColour=(89, 110, 127))
    sfx_text = UIElement(center_position=(520, 350), font_size=40, bg_rgb=WHITE, text_rgb=WHITE, text='Sfx')
    slider_sfx = Slider(screen, 450, 400, 150, 15, min=0, max=100, step=1,colour=(255, 255, 255),  handleColour=(89, 110, 127))
    while running:
        mouse_up = False
        events = pygame.event.get()  # Récupérer tous les événements
        pygame_widgets.update(events)  # Mettre à jour les widgets avec tous les événements
        
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
                pygame.mixer.Channel(0).play(button_sfx) # Joue le sfx de quannd on appuies sur la souris
            if event.type == pygame.QUIT:
                return GameState.QUIT

        scrolling_bg()
        
        # Mettre à jour et dessiner les autres éléments de l'UI
        Title.update((0, 0), None)
        music_text.update((0, 0), None)
        sfx_text.update((0, 0), None)
        Title.draw(screen)
        music_text.draw(screen)
        sfx_text.draw(screen)
        lobby_music.set_volume((slider_music.getValue() / 100))
        button_sfx.set_volume((slider_sfx.getValue() / 100))
        ui_action = btn_return.update(pygame.mouse.get_pos(), mouse_up)
        if ui_action is not None:
            return ui_action
        btn_return.draw(screen)
        # Affichage du slider_music
        slider_music.draw()
        slider_sfx.draw()
        pygame.display.flip()

        

def main():
    global running
    game_state = GameState.TITLE
    
    while running:
        if game_state == GameState.TITLE:
            game_state = title_screen(screen)
        elif game_state == GameState.OPTIONS:
            game_state = options_screen(screen)
        elif game_state == GameState.QUIT:
            running = False
         

main()
