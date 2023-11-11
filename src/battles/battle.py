from collections import defaultdict

import pygame

from src.base.assets import assets
import src.constants.sound_constants as SoundConstants
from src.base.space import Space
from src.characters.enemy import Enemy
from src.extra.functions import same_with_errors


class Battle(Space):
    def __init__(self, width=1024, height=576, start_x=512, start_y=288, background_image="textures/map/white.png",
                 upper_layer_image="textures/upper_layer/transparent.png", bgm="", will_fade_in=True,
                 will_fade_out=True, scale_screen=True, can_save=True, events_on_load=None,
                 events_on_boss_health=None,
                 event_on_clear=None, boss=None, enemies=None, terrain_rect=None, g_accel=10):
        super().__init__(width, height, start_x, start_y, background_image, upper_layer_image, bgm, will_fade_in,
                         will_fade_out, scale_screen, events_on_load)
        # set events on health (cur/full)
        self.event_on_boss_health = events_on_boss_health if events_on_boss_health else defaultdict(float)
        self.event_on_clear = event_on_clear if event_on_clear else []
        # set enemy
        self.boss = boss
        self.enemies = enemies if enemies else []
        # define terrain bodies
        self.terrain_rect = terrain_rect if terrain_rect else []
        # define gravity
        self.g_accel = g_accel

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
