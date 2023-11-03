"""Main game"""
import gc

import pygame
import random
import os
import src.constants.base_constants as Constants
from src.base.assets import assets
from src.characters.player import Player
import src.constants.spritesheet_constants as SpriteSheet_Constants
import src.constants.effect_constants as EffectConstants
from src.gui.testing_gui import TestingGUI
from src.scenes.start_scene import StartScene
import src.constants.gui_constants as GUIConstants
import src.constants.sound_constants as SoundConstants
import src.constants.tilemap_constants as TileMap_Constants
import src.constants.asset_constants as Asset_Constants
from src.events.delay_event import DelayEvent


def limit_bounds(x, lower, upper):
    if lower > upper:
        lower, upper = upper, lower
    return min(max(x, lower), upper)


# init and set global variables
pygame.init()
window = pygame.display.set_mode((Constants.WINDOW_WIDTH, Constants.WINDOW_HEIGHT))
screen = pygame.Surface((Constants.WINDOW_WIDTH, Constants.WINDOW_HEIGHT))
pygame.display.set_caption("Game")
for mixer_id in range(8):
    pygame.mixer.Channel(mixer_id).set_volume(SoundConstants.VOLUME)
clock = pygame.time.Clock()
running = True
initialized = False
frame_index = 0

# load assets
window.blit(pygame.image.load('textures/extra/loading.png'), (0, 0))
pygame.display.update()
for asset_folder_name in Asset_Constants.ASSET_FOLDERS:
    for dir_name, _, files in os.walk(asset_folder_name):
        for file_name in files:
            assets.load_asset(os.path.join(os.path.relpath(dir_name), file_name))
for font_folder_name in Asset_Constants.FONT_FOLDERS:
    for dir_name, _, files in os.walk(font_folder_name):
        for file_name in files:
            for font_size in Asset_Constants.FONT_SIZES_TO_LOAD:
                assets.load_asset(os.path.join(os.path.relpath(dir_name), file_name), font_size)

# set basic objects
scene = StartScene()
main_player = Player()

# screen for scaled screen
scaled_cropped_screen = pygame.Surface((Constants.WINDOW_WIDTH, Constants.WINDOW_HEIGHT))

while running:
    # delay amount of FPS and get delta_time for correct speed
    delta_time = clock.tick(Constants.FPS)
    frame_index += 1
    # check for quit & dialogue interrupt event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        # continue dialogue
        if main_player.event_active and event.type == pygame.KEYDOWN and main_player.event_active.update_on_key:
            main_player.update_event_system(screen, scene, main_player)
        # check for any interactions
        if not main_player.event_active and not main_player.events_waiting and event.type == pygame.KEYDOWN and event.key == pygame.K_x:
            for npc in scene.npcs:
                if (npc.tile_x, npc.tile_y) == (main_player.tile_x + TileMap_Constants.MOVEMENT_X[main_player.facing],
                                                main_player.tile_y + TileMap_Constants.MOVEMENT_Y[main_player.facing]):
                    main_player.add_event_queue(npc.events_on_interaction)
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
        if not main_player.event_active and not main_player.is_moving and not main_player.events_waiting:  # process movement
            if keys_pressed[pygame.K_w] or keys_pressed[pygame.K_UP]:
                main_player.move_one_tile(SpriteSheet_Constants.FACING_UP, screen, scene, main_player)
            elif keys_pressed[pygame.K_a] or keys_pressed[pygame.K_LEFT]:
                main_player.move_one_tile(SpriteSheet_Constants.FACING_LEFT, screen, scene, main_player)
            elif keys_pressed[pygame.K_s] or keys_pressed[pygame.K_DOWN]:
                main_player.move_one_tile(SpriteSheet_Constants.FACING_DOWN, screen, scene, main_player)
            elif keys_pressed[pygame.K_d] or keys_pressed[pygame.K_RIGHT]:
                main_player.move_one_tile(SpriteSheet_Constants.FACING_RIGHT, screen, scene, main_player)
    # check if scene needs to be updated
    if main_player.scene_needs_to_be_changed or not initialized:
        if main_player.scene_needs_to_be_changed:
            scene = main_player.scene_waiting
        if not initialized:
            initialized = True
        scene.load(screen, main_player)
        main_player.force_instant_move(scene.start_tile_x, scene.start_tile_y)
        main_player.scene_needs_to_be_changed = False
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
    # focus in to player
    if scene.scale_screen and Constants.FOCUS_CAMERA_SCALE != 1:
        if Constants.SMOOTH_SCALE:
            raw_scaled_screen = pygame.transform.smoothscale_by(screen, Constants.FOCUS_CAMERA_SCALE)
        else:
            raw_scaled_screen = pygame.transform.scale_by(screen, Constants.FOCUS_CAMERA_SCALE)

        scaled_screen_blit_location = (
            - limit_bounds(
                main_player.x * Constants.FOCUS_CAMERA_SCALE - Constants.WINDOW_WIDTH // 2,
                0, Constants.WINDOW_WIDTH * (Constants.FOCUS_CAMERA_SCALE - 1)),
            - limit_bounds(
                main_player.y * Constants.FOCUS_CAMERA_SCALE - Constants.WINDOW_HEIGHT // 2,
                0, Constants.WINDOW_HEIGHT * (Constants.FOCUS_CAMERA_SCALE - 1)))
        scaled_cropped_screen.blit(raw_scaled_screen, scaled_screen_blit_location)
    else:
        scaled_cropped_screen = screen.copy()
    # post-processing before gui
    post_processed_before_gui_screen = scaled_cropped_screen.copy()
    # GUI
    if main_player.event_active and main_player.event_active.needs_to_be_updated:
        main_player.event_active.object.update(post_processed_before_gui_screen)
    # post processing after gui
    dest = (0, 0)
    if main_player.shake_screen:
        dest = (random.randint(-EffectConstants.SCREEN_SHAKE_AMOUNT, EffectConstants.SCREEN_SHAKE_AMOUNT),
                random.randint(-EffectConstants.SCREEN_SHAKE_AMOUNT, EffectConstants.SCREEN_SHAKE_AMOUNT))
    post_processed_after_gui_screen = post_processed_before_gui_screen.copy()
    window.blit(post_processed_after_gui_screen, dest)
    # update display
    pygame.display.update()

    # manual garbage collection
    if Constants.GARBAGE_COLLECTION_INTERVAL_FRAMES and frame_index % Constants.GARBAGE_COLLECTION_INTERVAL_FRAMES == 0:
        gc.collect()

pygame.quit()
print("Thanks for playing!")
