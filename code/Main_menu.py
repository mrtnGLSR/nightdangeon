import pygame
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect
from enum import Enum
# Variables
running = True
RED = (178, 34, 34)
WHITE = (255, 255, 255)

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
        #init
        super().__init__()
        # if the mouse is over the text
        self.mouse_over = False

        # when the mouse isn't over the default image was call
        default_image = create_surface_with_text(text, font_size, text_rgb, bg_rgb)

        # when the mouse is over the highlighit image was call
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
    #update if the mouse over it
    def update(self, mouse_position, mouse_up):
        if self.rect.collidepoint(mouse_position):
            self.mouse_over = True
            if mouse_up:
                return self.action
        else:
            self.mouse_over = False
    def draw(self, surface):
        surface.blit(self.image, self.rect)

class GameState(Enum):
    QUIT = -1
    TITLE = 0
    NEWGAME = 1

def main():
    global running
    # init pygame window
    pygame.init()
    screen = pygame.display.set_mode((1040,1040))


    # create buttons
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
        action=None
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

    


    while running:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
            # init window name
            pygame.display.set_caption('Night Dungeon')

            # load images
            background_image = pygame.image.load("code/img/background.jpg")

            screen.blit(background_image, (0, 0))
            # update all buttons
            pygame.display.flip()
            if event.type == pygame.QUIT:
                running = False


main()
