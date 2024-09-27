import pygame

from sprite import sprites   
from map import TileKind, Map
from camera import create_screen
pygame.init

screen = create_screen(1920, 1080, 'Night Dungeon')
clear_color = (0, 0, 0)
running = True
tile_kinds = [
    TileKind('floor', './img/brick-floor.jpg', False),
    TileKind('wall', './img/brick-wall.jpg', False)
]

map = Map('./maps/start.map',tile_kinds, 80)

# Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN: # S'active quand une touche est préssée
            input.keys_down.add(event.key)
        elif event.type == pygame.KEYUP:
            input.keys_down.remove(event.key)
            
    # Draw code
    screen.fill(clear_color)
    map.draw(screen)
    for s in sprites:
        s.draw(screen)
    pygame.display.flip()
    
    pygame.time.delay(70)
pygame.quit