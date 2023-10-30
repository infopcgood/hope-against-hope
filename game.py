"""Main game"""
import pygame
import src.constants.base_constants as Constants
from src.characters.player import Player
import src.constants.spritesheet_constants as SpriteSheet_Constants
from src.gui.testing_gui import TestingGUI
from src.scenes.base_scene import BaseScene
import src.constants.gui_constants as GUIConstants

### init and set global variables
pygame.init()
screen = pygame.display.set_mode((Constants.WINDOW_WIDTH, Constants.WINDOW_HEIGHT))
pygame.display.set_caption("Game")
clock = pygame.time.Clock()
running = True
scene_changed = True

### Fonts
GUIConstants.TESTING_GUI_FONT = pygame.font.SysFont('Comic Sans MS', 20)
GUIConstants.DIALOGUE_FONT = pygame.font.SysFont('Malgun Gothic', 20)

### set basic objects
scene = BaseScene()
main_player = Player()
testing_gui = TestingGUI()

while running:
    # delay amount of FPS and get delta_time for correct speed
    delta_time = clock.tick(Constants.FPS)
    # check for quit & dialogue interrupt event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        # continue dialogue
        if event.type == pygame.KEYDOWN and Player.dialogue_active:
            main_player.update_dialogues(screen, scene, main_player)
    if not running:
        break

    # check for keypress
    keys_pressed = pygame.key.get_pressed()
    if not main_player.dialogue_active and not main_player.is_moving and not main_player.dialogues_waiting: # process movement
        if keys_pressed[pygame.K_w]:
            main_player.move_one_tile(SpriteSheet_Constants.FACING_UP, scene)
        if keys_pressed[pygame.K_a]:
            main_player.move_one_tile(SpriteSheet_Constants.FACING_LEFT, scene)
        if keys_pressed[pygame.K_s]:
            main_player.move_one_tile(SpriteSheet_Constants.FACING_DOWN, scene)
        if keys_pressed[pygame.K_d]:
            main_player.move_one_tile(SpriteSheet_Constants.FACING_RIGHT, scene)
    # check if scene needs to be updated
    if scene_changed:
        scene.load(screen, main_player)
        main_player.force_instant_move(scene.start_tile_x, scene.start_tile_y)
        scene_changed = False
    # update screen in order of scene(map) -> player -> NPCs -> upper layer -> GUI -> pygame.display
    # scene(map)
    scene.update_map(screen)
    # player
    main_player.update(screen, scene, main_player, delta_time)
    # NPCs
    # upper_layer
    scene.update_upper_layer(screen)
    # GUI
    testing_gui.update(screen, main_player, scene.movable_tiles)
    if Player.dialogue_active:
        Player.dialogue_active.update(screen)
    # pygame.display
    pygame.display.update()

pygame.quit()
print("Thanks for playing!")
