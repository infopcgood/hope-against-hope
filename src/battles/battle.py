from collections import defaultdict

import pygame.mixer

import src.constants.sound_constants as SoundConstants
from src.base.assets import assets
from src.base.space import Space
from src.events.scene_change_event import SceneChangeEvent
from src.scenes.game_over_scene import GameOverScene


# basic Battle scene.
class Battle(Space):
    def __init__(self, width=1024, height=576, start_x=512, start_y=288, background_image="textures/map/white.png",
                 upper_layer_image="textures/upper_layer/transparent.png", bgm="", will_fade_in=True,
                 will_fade_out=True, scale_screen=True, can_save=True, events_on_load=None,
                 events_on_boss_health=None,
                 event_on_clear=None, boss=None, enemies=None, terrain_rect=None, g_accel=0.0017):
        # call super method
        super().__init__(width, height, start_x, start_y, background_image, upper_layer_image, bgm, will_fade_in,
                         will_fade_out, scale_screen, can_save, events_on_load)
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
        # define attack delay idx
        self.attack_delay_idx = 0

    # add some stuff to load scene in order to make physics engine work
    def load(self, screen, main_player):
        super().load(screen, main_player)
        main_player.on_ground = False
        main_player.is_moving = True
        self.boss.on_ground = False
        self.boss.is_moving = True
        for enemy in self.enemies:
            enemy.on_ground = False
            enemy.is_moving = True

    # update physics for one character
    def update_physics_one(self, screen, main_player, dt, character, resistance=True):
        # gravity
        if not character.on_ground:
            character.vy += self.g_accel * dt
        # obstacle colllision
        for obstacle in self.terrain_rect:
            if character.rect.colliderect(obstacle):
                if character.rect.top < obstacle.top <= character.rect.bottom < obstacle.bottom:
                    character.vy = 0
                    character.rect.bottom = obstacle.top
                    character.on_ground = True
                elif obstacle.top < character.rect.top <= obstacle.bottom < character.rect.bottom:
                    character.rect.top = obstacle.bottom
                    character.vy *= -1
                elif character.rect.left < obstacle.left <= character.rect.right < obstacle.right:
                    character.vx = 0
                    character.rect.right = obstacle.left
                elif obstacle.left < character.rect.left <= obstacle.right < character.rect.right:
                    character.vy = 0
                    character.rect.left = obstacle.right
        # check if there is friction
        if resistance:
            character.vx *= 0.86
        # update pos by modified rect
        character.update_pos_by_rect()

    # update the entire physics of the scene
    def update_physics(self, screen, main_player, dt):
        self.update_physics_one(screen, main_player, dt, main_player, False)
        if self.boss:
            self.update_physics_one(screen, main_player, dt, self.boss)
        for enemy in self.enemies:
            self.update_physics_one(screen, main_player, dt, enemy)

    # update strategies of boss and enemies
    def update_strategy(self, screen, main_player, dt):
        if self.boss:
            self.boss.update_strategy(screen, self, main_player, dt)
        for enemy in self.enemies:
            enemy.update_strategy(screen, self, main_player, dt)

    # check events that are set to deploy under certain HP level
    def check_health_events(self, screen, main_player, dt):
        keys_pop_needed = []
        for key in self.event_on_boss_health.keys():
            if key * self.boss.max_hp >= self.boss.hp:
                main_player.add_event_queue(screen, self, main_player, self.event_on_boss_health[key])
                main_player.update_event_system(screen, self, main_player)
                keys_pop_needed.append(key)
        for key in keys_pop_needed:
            self.event_on_boss_health.pop(key)

    # update the whole mechanic of the battle scene
    def update_mechanics(self, screen, main_player, dt):
        self.update_physics(screen, main_player, dt)
        self.update_strategy(screen, main_player, dt)
        self.check_health_events(screen, main_player, dt)
        if main_player.hp <= 0:
            main_player.add_event_queue(screen, self, main_player, [(SceneChangeEvent, GameOverScene)])
        if self.attack_delay_idx > 0:
            self.attack_delay_idx -= 1

    # called when player presses attack key
    def attack(self, screen, main_player, dt):
        attacked_something = False
        if self.attack_delay_idx > 0:
            return
        check_attack_list = [self.boss] + self.enemies
        for enemy in check_attack_list:
            if main_player.rect.colliderect(enemy.rect):
                enemy.hp -= max(0, main_player.power)
                enemy.attacked(screen, main_player, dt)
                enemy.vx = 0.25 * (main_player.facing - 2)
                attacked_something = True
        if attacked_something:
            self.attack_delay_idx = 45
            pygame.mixer.Channel(SoundConstants.EFFECT_CHANNEL).play(assets.get_asset('sounds/effects/hit.mp3'))
