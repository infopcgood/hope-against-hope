"""Main game"""
import pygame
import src.constants.base_constants as Constants
from src.characters.player import Player
import src.constants.spritesheet_constants as SpriteSheet_Constants
from src.gui.testing_gui import TestingGUI
from src.scenes.start_scene import StartScene
import src.constants.gui_constants as GUIConstants
from src.events.delay_event import DelayEvent

### init and set global variables
pygame.init()
screen = pygame.display.set_mode((Constants.WINDOW_WIDTH, Constants.WINDOW_HEIGHT))
pygame.display.set_caption("Game")
clock = pygame.time.Clock()
running = True
initialized = False

### Fonts
GUIConstants.TESTING_GUI_FONT = pygame.font.SysFont('Comic Sans MS', 20)
GUIConstants.DIALOGUE_FONT = pygame.font.Font('fonts/Malgun Gothic Regular.ttf', 20)

### set basic objects
scene = StartScene()
main_player = Player()

while running:
    # delay amount of FPS and get delta_time for correct speed
    delta_time = clock.tick(Constants.FPS)
    # check for quit & dialogue interrupt event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        # continue dialogue
        if main_player.event_active and event.type == pygame.KEYDOWN and main_player.event_active.update_on_key:
            main_player.update_event_system(screen, scene, main_player)
    if not running:
        break
    if main_player.event_active and not main_player.event_active.update_on_key:
        main_player.update_event_system(screen, scene, main_player)

    # check for delay
    if main_player.event_active and isinstance(main_player.event_active, DelayEvent):
        delaying = True
    else:
        delaying = False

    # check for keypress
    if not delaying:
        keys_pressed = pygame.key.get_pressed()
        if not main_player.event_active and not main_player.is_moving and not main_player.events_waiting: # process movement
            if keys_pressed[pygame.K_w] or keys_pressed[pygame.K_UP]:
                main_player.move_one_tile(SpriteSheet_Constants.FACING_UP, screen, scene, main_player)
            elif keys_pressed[pygame.K_a] or keys_pressed[pygame.K_LEFT]:
                main_player.move_one_tile(SpriteSheet_Constants.FACING_LEFT, screen, scene, main_player)
            elif keys_pressed[pygame.K_s] or keys_pressed[pygame.K_DOWN]:
                main_player.move_one_tile(SpriteSheet_Constants.FACING_DOWN, screen, scene, main_player)
            elif keys_pressed[pygame.K_d] or keys_pressed[pygame.K_RIGHT]:
                main_player.move_one_tile(SpriteSheet_Constants.FACING_RIGHT, screen, scene, main_player)
    # check if scene needs to be updated
    if Player.scene_needs_to_be_changed or not initialized:
        if Player.scene_needs_to_be_changed:
            scene = Player.scene_waiting
        if not initialized:
            initialized = True
        scene.load(screen, main_player)
        main_player.force_instant_move(scene.start_tile_x, scene.start_tile_y)
        Player.scene_needs_to_be_changed = False
    # update screen in order of scene(map) -> NPCs -> player -> upper layer -> GUI (DialogueEvent) -> pygame.display
    # scene(map)
    scene.update_map(screen)
    # NPCs
    for npc in scene.npcs:
        npc.update(screen, scene, main_player, delta_time)
    # player
    main_player.update(screen, scene, main_player, delta_time)
    # upper_layer
    scene.update_upper_layer(screen)
    # GUI
    if Player.event_active and Player.event_active.needs_to_be_updated:
        Player.event_active.object.update(screen)
    # pygame.display
    pygame.display.update()

pygame.quit()
print("Thanks for playing!")
