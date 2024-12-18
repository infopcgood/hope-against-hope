import gc
import os
import random

import pygame

import src.constants.asset_constants as Asset_Constants
import src.constants.base_constants as Constants
import src.constants.effect_constants as EffectConstants
import src.constants.gui_constants as GUIConstants
import src.constants.sound_constants as SoundConstants
import src.constants.spritesheet_constants as SpriteSheet_Constants
import src.constants.tilemap_constants as TileMap_Constants
from src.base.assets import assets
from src.base.preferences import preferences
from src.base.save import save
from src.battles.battle import Battle
from src.characters.player import Player
from src.events.delay_event import DelayEvent
from src.extra.functions import same_with_errors
from src.gui.battle_gui import BattleGUI
from src.gui.load_ui import LoadUI
from src.gui.option import Option
from src.gui.testing_gui import TestingGUI
from src.scenes.load_scene import LoadScene
from src.scenes.scene import Scene
from src.scenes.title_scene import TitleScene


def limit_bounds(x, lower, upper):
    if lower > upper:
        lower, upper = upper, lower
    return min(max(x, lower), upper)


# MAIN SOURCE OF GAME

# init and set global variables
pygame.init()
window = pygame.display.set_mode((Constants.WINDOW_WIDTH, Constants.WINDOW_HEIGHT), pygame.DOUBLEBUF, 8)
screen = pygame.Surface((Constants.WINDOW_WIDTH, Constants.WINDOW_HEIGHT), pygame.SRCALPHA)
pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN, pygame.KEYUP])
pygame.display.set_caption("Hope Against Hope")
for mixer_id in range(8):
    pygame.mixer.Channel(mixer_id).set_volume(preferences.get_preference('volume'))
clock = pygame.time.Clock()
options_menu = Option()

# set variables for event and ui
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
test_gui = TestingGUI()
battle_gui = BattleGUI()
load_menu = LoadUI()

# screen for scaled screen
scaled_cropped_screen = pygame.Surface((Constants.WINDOW_WIDTH, Constants.WINDOW_HEIGHT), pygame.SRCALPHA)
scene = LoadScene()
main_player = Player()
main_player.visible = False

# initialize save system
save_loaded = False
for idx in range(Constants.SAVE_COUNT):
    if not save.validate_integrity(f'save_{idx + 1:02}.gsvf'):
        save.save_data_to_file(f'save_{idx + 1:02}.gsvf', TitleScene(), main_player)
        save.mark_as_new_file(f'save_{idx + 1:02}.gsvf')

# game main loop
while running:
    # delay amount of FPS and get delta_time for correct speed
    delta_time = clock.tick(Constants.FPS)
    frame_index += 1
    # fill screen black
    scaled_cropped_screen.fill("black")
    # check if options or load ui menu is open
    if paused:
        # if save to load has been selected and scene load is needed
        if save.load_needed:
            save.load_needed = False
            print(save.load_data)
            main_player = (save.load_data[1])
            scene = save.load_data[0]
            main_player.scene_waiting = (save.load_data[0])
            paused = False
            initialized = True
            continue
        # check for event system
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            # check for key press
            if event.type == pygame.KEYDOWN:
                # loadui key check
                if isinstance(scene, LoadScene):
                    if event.key == pygame.K_ESCAPE:
                        paused = False
                        break
                    if event.key == pygame.K_UP:
                        pygame.mixer.Channel(SoundConstants.EFFECT_CHANNEL).play(
                            assets.get_asset('sounds/effects/option_selection.wav'))
                        if load_menu.selection_level == 1:
                            load_menu.change_selection(-1)
                    if event.key == pygame.K_DOWN:
                        pygame.mixer.Channel(SoundConstants.EFFECT_CHANNEL).play(
                            assets.get_asset('sounds/effects/option_selection.wav'))
                        if load_menu.selection_level == 1:
                            load_menu.change_selection(1)
                    if event.key == pygame.K_RETURN:
                        pygame.mixer.Channel(SoundConstants.EFFECT_CHANNEL).play(
                            assets.get_asset('sounds/effects/selection.mp3'))
                        if load_menu.selection_level == GUIConstants.OPTIONS_UI_TAB_DEPTH[load_menu.selected_tab] - 1:
                            load_menu.trigger_event(screen, scene, main_player)
                else:  # options ui key check
                    if event.key == pygame.K_ESCAPE:
                        pygame.mixer.Channel(SoundConstants.EFFECT_CHANNEL).play(
                            assets.get_asset('sounds/effects/option_selection.wav'))
                        paused = False
                        break
                    if event.key == pygame.K_UP:
                        pygame.mixer.Channel(SoundConstants.EFFECT_CHANNEL).play(
                            assets.get_asset('sounds/effects/option_selection.wav'))
                        if options_menu.selection_level == 0:
                            options_menu.change_selected_tab(scene, -1)
                        elif options_menu.selection_level == 1:
                            options_menu.change_selection(-1)
                    if event.key == pygame.K_DOWN:
                        pygame.mixer.Channel(SoundConstants.EFFECT_CHANNEL).play(
                            assets.get_asset('sounds/effects/option_selection.wav'))
                        if options_menu.selection_level == 0:
                            options_menu.change_selected_tab(scene, 1)
                        elif options_menu.selection_level == 1:
                            options_menu.change_selection(1)
                    if event.key == pygame.K_RETURN:
                        pygame.mixer.Channel(SoundConstants.EFFECT_CHANNEL).play(
                            assets.get_asset('sounds/effects/selection.mp3'))
                        if options_menu.selection_level == GUIConstants.OPTIONS_UI_TAB_DEPTH[
                            options_menu.selected_tab] - 1:
                            options_menu.trigger_event(screen, scene, main_player)
                        else:
                            options_menu.change_selection_level(1)
                    if event.key == pygame.K_LEFT:
                        pygame.mixer.Channel(SoundConstants.EFFECT_CHANNEL).play(
                            assets.get_asset('sounds/effects/option_selection.wav'))
                        options_menu.change_selection_level(-1)
                    if event.key == pygame.K_RIGHT:
                        pygame.mixer.Channel(SoundConstants.EFFECT_CHANNEL).play(
                            assets.get_asset('sounds/effects/option_selection.wav'))
                        options_menu.change_selection_level(1)
    else:
        # check for quit & dialogue interrupt event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_ESCAPE and not main_player.scene_needs_to_be_changed and not scene.fading and
                        not main_player.is_moving and not main_player.event_active and not main_player.events_waiting):
                    paused = True
                    break
            # continue dialogue
            if main_player.event_active and event.type == pygame.KEYDOWN and main_player.event_active.update_on_key:
                main_player.update_event_system(screen, scene, main_player)
            # check for any interactions
            if not main_player.event_active and not main_player.events_waiting and event.type == pygame.KEYDOWN and event.key == pygame.K_x:
                if isinstance(scene, Scene):
                    for npc in scene.npcs:
                        if (npc.tile_x, npc.tile_y) == (
                                main_player.tile_x + TileMap_Constants.MOVEMENT_X[main_player.facing],
                                main_player.tile_y + TileMap_Constants.MOVEMENT_Y[main_player.facing]):
                            main_player.add_event_queue(screen, scene, main_player, npc.events_on_interaction)
                            main_player.update_event_system(screen, scene, main_player)
                elif isinstance(scene, Battle):
                    scene.attack(screen, main_player, delta_time)
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
            if isinstance(scene, Scene):
                if not main_player.event_active and not main_player.is_moving and not main_player.events_waiting:  # process movement
                    if keys_pressed[pygame.K_w] or keys_pressed[pygame.K_UP]:
                        main_player.move_one_tile(SpriteSheet_Constants.FACING_UP, screen, scene, main_player)
                    elif keys_pressed[pygame.K_a] or keys_pressed[pygame.K_LEFT]:
                        main_player.move_one_tile(SpriteSheet_Constants.FACING_LEFT, screen, scene, main_player)
                    elif keys_pressed[pygame.K_s] or keys_pressed[pygame.K_DOWN]:
                        main_player.move_one_tile(SpriteSheet_Constants.FACING_DOWN, screen, scene, main_player)
                    elif keys_pressed[pygame.K_d] or keys_pressed[pygame.K_RIGHT]:
                        main_player.move_one_tile(SpriteSheet_Constants.FACING_RIGHT, screen, scene, main_player)
            elif isinstance(scene, Battle):
                if not main_player.event_active and not main_player.events_waiting and (
                        keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_w]) and main_player.on_ground:
                    main_player.vy = -0.6
                    main_player.on_ground = False
                    main_player.oncedowned = False
                if not main_player.event_active and not main_player.events_waiting and (keys_pressed[
                                                                                            pygame.K_LEFT] or
                                                                                        keys_pressed[
                                                                                            pygame.K_a]) and not (
                        keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]):
                    main_player.vx = -0.32
                    main_player.anim = SpriteSheet_Constants.ACTION_WALKING
                    main_player.facing = SpriteSheet_Constants.FACING_LEFT
                    main_player.playing_anim = True
                elif not main_player.event_active and not main_player.events_waiting and (
                        keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]) and not (
                        keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]):
                    main_player.vx = 0.32
                    main_player.anim = SpriteSheet_Constants.ACTION_WALKING
                    main_player.facing = SpriteSheet_Constants.FACING_RIGHT
                    main_player.playing_anim = True
                else:
                    main_player.vx = 0
                    if main_player.on_ground:
                        main_player.stop(screen, scene, main_player)
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
                    screen = pygame.Surface((scene.scene_width, scene.scene_height), pygame.SRCALPHA)
                    scene.fading = "in"
                    scene.has_been_shown = True
            if not skip_scene_load_flag:
                scene.load(screen, main_player)
                if not isinstance(scene, Battle):
                    main_player.force_instant_move(scene.start_tile_x, scene.start_tile_y)
                else:
                    main_player.force_instant_move(scene.start_x / TileMap_Constants.TILE_SIZE,
                                                   scene.start_y / TileMap_Constants.TILE_SIZE)
                main_player.scene_needs_to_be_changed = False
                initialized = True
    # update screen in order of scene(map) -> NPCs -> player -> upper layer -> GUI (DialogueEvent) -> pygame.display
    # scene(map)
    scene.update_map(screen)
    if isinstance(scene, Battle) and not scene.fading:
        scene.update_mechanics(screen, main_player, delta_time)
    # NPCs (behind player)
    if isinstance(scene, Scene):
        for npc in scene.npcs:
            if npc.tile_y < main_player.tile_y:
                npc.update(screen, scene, main_player, delta_time)
    # boss and projectiles
    if isinstance(scene, Battle):
        scene.boss.move(screen, scene, main_player, delta_time)
        scene.boss.update(screen, scene, main_player, delta_time)
        for enemy in scene.enemies:
            enemy.update(screen, scene, main_player, delta_time)
    # player
    main_player.update(screen, scene, main_player, delta_time, not paused, isinstance(scene, Battle))
    # NPCs (above player)
    if isinstance(scene, Scene):
        for npc in scene.npcs:
            if npc.tile_y >= main_player.tile_y:
                npc.update(screen, scene, main_player, delta_time)
    # upper_layer
    scene.update_upper_layer(screen)

    # check for fade in and out effect
    if scene.fading == "in":
        if scene.will_fade_in:
            scene.fade_percent += EffectConstants.FADE_SPEED
            if same_with_errors(scene.fade_percent, 100):
                scene.fading = ""
                scene.fade_percent = 100
                main_player.scene_waiting = None
        else:
            scene.fading = ""
            scene.fade_percent = 100
            main_player.scene_waiting = None
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

    # process end of fading
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
    if isinstance(scene, Battle):
        battle_gui.update(scaled_cropped_screen, scene, main_player)
    if isinstance(scene, LoadScene) and not scene.fading:
        load_menu.update(scaled_cropped_screen, scene, main_player)
        if not paused:
            paused = True
    elif paused and not isinstance(scene, LoadScene):
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
