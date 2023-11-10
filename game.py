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
from src.extra.functions import same_with_errors
from src.gui.option import Option
from src.gui.testing_gui import TestingGUI
from src.scenes.start_scene import StartScene
import src.constants.gui_constants as GUIConstants
import src.constants.sound_constants as SoundConstants
import src.constants.tilemap_constants as TileMap_Constants
import src.constants.asset_constants as Asset_Constants
from src.events.delay_event import DelayEvent
from src.base.preferences import preferences


def limit_bounds(x, lower, upper):
    if lower > upper:
        lower, upper = upper, lower
    return min(max(x, lower), upper)


# init and set global variables
pygame.init()
window = pygame.display.set_mode((Constants.WINDOW_WIDTH, Constants.WINDOW_HEIGHT), pygame.DOUBLEBUF, 8)
screen = pygame.Surface((Constants.WINDOW_WIDTH, Constants.WINDOW_HEIGHT))
pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN, pygame.KEYUP])
pygame.display.set_caption("Game")
for mixer_id in range(8):
    pygame.mixer.Channel(mixer_id).set_volume(preferences.get_preference('volume'))
clock = pygame.time.Clock()
options_menu = Option()
running = True
initialized = False
paused = False
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
test_gui = TestingGUI()
main_player = Player()

# screen for scaled screen
scaled_cropped_screen = pygame.Surface((Constants.WINDOW_WIDTH, Constants.WINDOW_HEIGHT))

while running:
    # delay amount of FPS and get delta_time for correct speed
    delta_time = clock.tick(Constants.FPS)
    frame_index += 1
    # fill screen black
    scaled_cropped_screen.fill("black")

    if paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False
                    break
                if event.key == pygame.K_UP:
                    if options_menu.selection_level == 0:
                        options_menu.change_selected_tab(scene, -1)
                if event.key == pygame.K_DOWN:
                    if options_menu.selection_level == 0:
                        options_menu.change_selected_tab(scene, 1)
                if event.key == pygame.K_RETURN:
                    if options_menu.selection_level == 0:
                        pass
    else:
        # check for quit & dialogue interrupt event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE and not main_player.scene_needs_to_be_changed:
                    paused = True
                    break
            # continue dialogue
            if main_player.event_active and event.type == pygame.KEYDOWN and main_player.event_active.update_on_key:
                main_player.update_event_system(screen, scene, main_player)
            # check for any interactions
            if not main_player.event_active and not main_player.events_waiting and event.type == pygame.KEYDOWN and event.key == pygame.K_x:
                for npc in scene.npcs:
                    if (npc.tile_x, npc.tile_y) == (
                            main_player.tile_x + TileMap_Constants.MOVEMENT_X[main_player.facing],
                            main_player.tile_y + TileMap_Constants.MOVEMENT_Y[main_player.facing]):
                        main_player.add_event_queue(screen, scene, main_player, npc.events_on_interaction)
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
        skip_scene_load_flag = False
        if (main_player.scene_needs_to_be_changed and scene.fading not in ["in", "out"]) or not initialized:
            if main_player.scene_needs_to_be_changed and not skip_scene_load_flag:
                if scene.fade_percent and scene.has_been_shown:
                    scene.fading = "out"
                    skip_scene_load_flag = True
                else:
                    if initialized:
                        scene = main_player.scene_waiting
                    screen = pygame.Surface((scene.scene_width, scene.scene_height))
                    scene.fading = "in"
                    scene.has_been_shown = True
            if not skip_scene_load_flag:
                scene.load(screen, main_player)
                main_player.force_instant_move(scene.start_tile_x, scene.start_tile_y)
                main_player.scene_needs_to_be_changed = False
                initialized = True
    # update screen in order of scene(map) -> NPCs -> player -> upper layer -> GUI (DialogueEvent) -> pygame.display
    # scene(map)
    scene.update_map(screen)
    # NPCs
    for npc in scene.npcs:
        npc.update(screen, scene, main_player, delta_time)
    # player
    main_player.update(screen, scene, main_player, delta_time, not paused)
    # upper_layer
    scene.update_upper_layer(screen)

    # check for fade in and out effect
    if scene.fading == "in":
        if scene.will_fade_in:
            scene.fade_percent += EffectConstants.FADE_SPEED
            if same_with_errors(scene.fade_percent, 100):
                scene.fading = ""
                scene.fade_percent = 100
        else:
            scene.fading = ""
            scene.fade_percent = 100
    elif scene.fading == "out":
        if scene.will_fade_out:
            scene.fade_percent -= EffectConstants.FADE_SPEED
            if same_with_errors(scene.fade_percent, 0):
                scene.fading = ""
                scene.fade_percent = 0
                scene.has_been_shown = False
        else:
            scene.fading = ""
            scene.fade_percent = 0
            scene.has_been_shown = False

    if scene.fade_percent == 0 and screen.get_alpha() != 0:
        screen.set_alpha(0)
    elif scene.fade_percent == 100 and screen.get_alpha() != 255:
        screen.set_alpha(255)
    else:
        screen.set_alpha(max(0, min(255, int(scene.fade_percent * 255 / 100))))

    # focus in to player
    if scene.scale_screen and Constants.FOCUS_CAMERA_SCALE != 1:
        if Constants.SMOOTH_SCALE:
            raw_scaled_screen = pygame.transform.smoothscale_by(screen, Constants.FOCUS_CAMERA_SCALE)
        else:
            raw_scaled_screen = pygame.transform.scale_by(screen, Constants.FOCUS_CAMERA_SCALE)

        if Constants.WINDOW_WIDTH <= scene.scene_width * Constants.FOCUS_CAMERA_SCALE:
            limit_bounds_x = - limit_bounds(
                main_player.x * Constants.FOCUS_CAMERA_SCALE - Constants.WINDOW_WIDTH // 2,
                0, scene.scene_width * Constants.FOCUS_CAMERA_SCALE - Constants.WINDOW_WIDTH)
        else:
            limit_bounds_x = - Constants.WINDOW_WIDTH // 2 + scene.scene_width * Constants.FOCUS_CAMERA_SCALE
        if Constants.WINDOW_HEIGHT <= scene.scene_height * Constants.FOCUS_CAMERA_SCALE:
            limit_bounds_y = - limit_bounds(
                main_player.y * Constants.FOCUS_CAMERA_SCALE - Constants.WINDOW_HEIGHT // 2,
                0, scene.scene_height * Constants.FOCUS_CAMERA_SCALE - Constants.WINDOW_HEIGHT)
        else:
            limit_bounds_y = - Constants.WINDOW_HEIGHT // 2 + scene.scene_height * Constants.FOCUS_CAMERA_SCALE
        scaled_screen_blit_location = (limit_bounds_x, limit_bounds_y)
        scaled_cropped_screen.blit(raw_scaled_screen, scaled_screen_blit_location)
    else:
        scaled_cropped_screen.blit(screen, (0, 0))

    # GUI
    if paused:
        options_menu.update(scaled_cropped_screen, scene, main_player)
    else:
        if main_player.event_active and main_player.event_active.needs_to_be_updated:
            main_player.event_active.object.update(scaled_cropped_screen)
    # post processing after gui
    dest = (0, 0)
    if main_player.shake_screen:
        dest = (random.randint(-EffectConstants.SCREEN_SHAKE_AMOUNT, EffectConstants.SCREEN_SHAKE_AMOUNT),
                random.randint(-EffectConstants.SCREEN_SHAKE_AMOUNT, EffectConstants.SCREEN_SHAKE_AMOUNT))
    window.blit(scaled_cropped_screen, dest)
    # update display
    pygame.display.update()

    # manual garbage collection
    if Constants.GARBAGE_COLLECTION_INTERVAL_FRAMES and frame_index % Constants.GARBAGE_COLLECTION_INTERVAL_FRAMES == 0:
        gc.collect()

pygame.quit()
print("Thanks for playing!")
