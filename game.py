### imports
import pygame
import src.constants.base_constants as Constants
from src.characters.player import Player
import src.constants.spritesheet_constants as SpriteSheet_Constants
from src.gui.testing_gui import TestingGUI
from src.scenes.base_scene import BaseScene

### init and set global variables
pygame.init()
main_font = pygame.font.SysFont('Comic Sans MS', 20)
screen = pygame.display.set_mode((Constants.WINDOW_WIDTH, Constants.WINDOW_HEIGHT))
pygame.display.set_caption("Game")
clock = pygame.time.Clock()
running = True
scene_changed = True

### set basic objects
scene = BaseScene()
main_player = Player()
testing_gui = TestingGUI(main_font)

while running:
    # delay amount of FPS and get delta_time for correct speed
    delta_time = clock.tick(Constants.FPS)
    
    # check for quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    # check for keypress
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_w] and not main_player.is_moving:
        main_player.move_one_tile(SpriteSheet_Constants.FACING_UP, scene.movable_tiles)
    elif keys_pressed[pygame.K_a] and not main_player.is_moving:
        main_player.move_one_tile(SpriteSheet_Constants.FACING_LEFT, scene.movable_tiles)
    elif keys_pressed[pygame.K_s] and not main_player.is_moving:
        main_player.move_one_tile(SpriteSheet_Constants.FACING_DOWN, scene.movable_tiles)
    elif keys_pressed[pygame.K_d] and not main_player.is_moving:
        main_player.move_one_tile(SpriteSheet_Constants.FACING_RIGHT, scene.movable_tiles)
    
    # check if scene needs to be updated
    if scene_changed:
        main_player.force_instant_move(scene.start_tile_x, scene.start_tile_y)
        scene_changed = False
    # update screen in order of scene(map) -> player -> NPCs -> upper layer -> GUI -> pygame.display
    # scene(map)
    scene.update_map(screen)
    # player
    main_player.update(screen, delta_time)
    # NPCs
    # upper_layer
    scene.update_upper_layer(screen)
    # GUI
    testing_gui.update(screen, main_player, scene.movable_tiles)
    # pygame.display
    pygame.display.update()

pygame.quit()
print("Thanks for playing!")