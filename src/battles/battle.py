from collections import defaultdict

import pygame

from src.base.assets import assets
import src.constants.sound_constants as SoundConstants
from src.extra.functions import same_with_errors


class Battle:
    def __init__(self, start_x=128, start_y=448):
        # bgm
        self.bgm_name = None
        # fade settings
        self.will_fade_in = True
        self.will_fade_out = True
        self.fade_percent = 0
        self.fading = ""
        self.has_been_shown = False
        # set scene size
        self.scene_width = 1024
        self.scene_height = 576
        # load background and upper_layer image
        self.background_image = assets.get_asset("textures/map/white.png")
        self.upper_layer_image = assets.get_asset("textures/map/white.png")
        # set start pos
        self.start_x = start_x
        self.start_y = start_y
        # set events on health (cur/full)
        self.event_on_boss_health = {}
        self.event_on_load = []
        self.event_on_clear = []
        # set enemy
        self.boss = None
        self.enemies = []
        # define terrain bodies
        self.terrain_rect = [pygame.Rect(0, 448, self.scene_width, self.scene_height - 448)]
        # define gravity
        self.g_accel = 10
        # define if screen should be scaled
        self.scale_screen = True

    def load(self, screen, main_player):
        main_player.event_active = False
        main_player.events_waiting = []
        if self.event_on_load:
            main_player.add_event_queue(screen, self, main_player, self.event_on_load)
            main_player.update_event_system(screen, self, main_player)
        if self.bgm_name:
            if pygame.mixer.Channel(SoundConstants.BGM_CHANNEL).get_busy():
                pygame.mixer.Channel(SoundConstants.BGM_CHANNEL).stop()
            pygame.mixer.Channel(SoundConstants.BGM_CHANNEL).play(assets.get_asset(self.bgm_name))

    def update_map(self, screen):
        screen.blit(self.background_image, (0, 0))

    def update_upper_layer(self, screen):
        screen.blit(self.upper_layer_image, (0, 0))

    def update_physics_one(self, screen, main_player, dt, character):
        pass

    def update_physics(self, screen, main_player, dt):
        self.update_physics_one(screen, main_player, dt, main_player)
        self.update_physics_one(screen, main_player, dt, self.boss)
        for enemy in self.enemies:
            self.update_physics_one(screen, main_player, dt, enemy)

    def update_strategy(self, screen, main_player, dt):
        self.boss.update_strategy(screen, self, main_player, dt)
        for enemy in self.enemies:
            enemy.update_strategy(screen, self, main_player, dt)

    def check_health_events(self, screen, main_player, dt):
        for key in self.event_on_boss_health.keys():
            if key * self.boss.hp <= self.boss.max_hp:
                main_player.add_event_queue(screen, self, main_player, self.event_on_boss_health[key])
                self.event_on_boss_health.pop(key)

    def update_mechanics(self, screen, main_player, dt):
        self.update_physics(screen, main_player, dt)
        self.update_strategy(screen, main_player, dt)
