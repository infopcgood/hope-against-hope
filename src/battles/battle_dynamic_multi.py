import math
import random

import pygame

import src.constants.base_constants as Constants
import src.constants.sound_constants as SoundConstants
import src.constants.spritesheet_constants as SpriteSheet_Constants
from src.base.assets import assets
from src.battles.battle import Battle
from src.characters.boss import Boss
from src.characters.projectile import Projectile
from src.events.basic_function_event import BasicFunctionEvent
from src.events.delay_event import DelayEvent
from src.events.dialogue_event import DialogueEvent
from src.events.scene_change_event import SceneChangeEvent
from src.scenes.game_over_scene import GameOverScene
from src.scenes.scene_16 import Scene16


# most comments are in src/battles/battle.py, since this is an almost exact copy of that scene.


def modify_scale(screen, scene, main_player):
    Constants.FOCUS_CAMERA_SCALE = 2


def reset_scale(screen, scene, main_player):
    Constants.FOCUS_CAMERA_SCALE = 4 / 3
    main_player.shake_screen = False


def boss_strategy(screen, scene, main_player, dt):
    if main_player.event_active or main_player.events_waiting:
        return
    if abs(scene.boss.vx) <= 0.066:
        scene.boss.playing_anim = False
    else:
        scene.boss.playing_anim = True
        scene.boss.anim = SpriteSheet_Constants.ACTION_WALKING
        if scene.boss.vx > 0:
            scene.boss.facing = SpriteSheet_Constants.FACING_RIGHT
        else:
            scene.boss.facing = SpriteSheet_Constants.FACING_LEFT
    if scene.boss.attack_blink_cnt == -1:
        scene.boss.vx = (main_player.x - scene.boss.x) / dt / 75
    if scene.projectile_idx == 0:
        has_gravity = True
        scene.projectiles = scene.projectiles + [
            Projectile(scene.boss.x, scene.boss.y, (0.96 if has_gravity else 0.48) * math.sin(2 * 3.14 * arg / 12),
                       (1 if has_gravity else 0.48) * math.cos(2 * 3.14 * arg / 12), has_gravity) for arg in range(12)]
        scene.projectile_idx = 135
    scene.projectile_idx -= 1


def enemy_strategy(screen, scene, main_player, dt, enemy):
    if main_player.event_active or main_player.events_waiting:
        return
    if abs(enemy.vx) <= 0.01:
        enemy.playing_anim = False
    else:
        enemy.playing_anim = True
        enemy.anim = SpriteSheet_Constants.ACTION_WALKING
        if enemy.vx > 0:
            enemy.facing = SpriteSheet_Constants.FACING_RIGHT
        else:
            enemy.facing = SpriteSheet_Constants.FACING_LEFT
    if enemy.attack_blink_cnt == -1:
        enemy.vx = (main_player.x - enemy.x) / dt / 216
    if scene.projectile_idx <= 0 and random.randint(0, 5) == 0:
        scene.projectiles = scene.projectiles + [
            Projectile(enemy.x, enemy.y, 0.32 * math.cos(2 * 3.14 * (arg) / 6),
                       0.12 * math.sin(2 * 3.14 * (arg) / 6), False) for arg in range(5)]


class BattleDynamicMulti(Battle):
    def __init__(self, start_x=362, start_y=350):
        self.projectiles = []
        self.projectile_idx = 135
        super().__init__(1024, 432, start_x, start_y, 'textures/map/battle_background_loopable.png',
                         'textures/upper_layer/transparent.png',
                         None, False, False, True, False,
                         [(BasicFunctionEvent, modify_scale, tuple()), (DelayEvent, 2),
                          (DialogueEvent, '후후... 진짜로 순순히 내주겠다는 말을 믿었다면 경기도 오산이다.',
                           'textures/characters/Agent01_idle.png'),
                          (DialogueEvent, '아 진짜!!!', 'textures/characters/main_player_idle.png')],
                         {0.75: [(DialogueEvent, '이번엔 쉽게 통하지 않을걸?', 'textures/characters/Agent01_idle.png')],
                          1 / 3: [(DialogueEvent, '으윽....', 'textures/characters/Agent01_idle.png')],
                          0.01: [(DialogueEvent, '*이...일단 후퇴다!!', 'textures/characters/Agent01_idle.png'),
                                 (DialogueEvent, '...이긴 건가?', 'textures/characters/main_player_idle.png'),
                                 (DelayEvent, 1), (BasicFunctionEvent, reset_scale, tuple()),
                                 (SceneChangeEvent, Scene16, (16, 9))]}, [],
                         Boss(589, 380, SpriteSheet_Constants.FACING_LEFT, 'textures/spritesheets/Agent01.png', 20,
                              boss_strategy),
                         [Boss(100 * (2 * i + 1), 380, SpriteSheet_Constants.FACING_DOWN,
                               'textures/spritesheets/Agent01.png', 8) for i in range(5)],
                         [pygame.Rect(-100, 350, 1224, 32)],
                         0.0017)

    def load(self, screen, main_player):
        super().load(screen, main_player)
        main_player.visible = True

    def update_physics(self, screen, main_player, dt):
        super().update_physics(screen, main_player, dt)
        for projectile in self.projectiles:
            projectile.move(screen, self, main_player, dt)

    def update_mechanics(self, screen, main_player, dt):
        for enemy in self.enemies:
            if enemy.hp <= 0:
                enemy.visible = False
            else:
                enemy_strategy(screen, self, main_player, dt, enemy)
        super().update_mechanics(screen, main_player, dt)
        if main_player.x > 1024:
            main_player.x -= 1024
            main_player.rect.move_ip(-1024, 0)
        if main_player.x < 64:
            main_player.x += 1024
            main_player.rect.move_ip(1024, 0)
        projectiles_to_delete = []
        for projectile in self.projectiles:
            if (projectile.x > 1024 or projectile.x < 0) or (projectile.y < 0 or projectile.y > 432):
                projectiles_to_delete.append(projectile)
            else:
                if projectile.rect.colliderect(main_player.rect):
                    projectiles_to_delete.append(projectile)
                    main_player.hp -= projectile.power
                    pygame.mixer.Channel(SoundConstants.EFFECT_CHANNEL).play(assets.get_asset('sounds/effects/hit.mp3'))
                    main_player.attacked(screen, self, dt)
        for projectile in projectiles_to_delete:
            self.projectiles.remove(projectile)

        for projectile in self.projectiles:
            projectile.update(screen, self, main_player, dt)
        if main_player.hp <= 0:
            main_player.add_event_queue(screen, self, main_player, [(BasicFunctionEvent, reset_scale, tuple()),
                                                                    (SceneChangeEvent, GameOverScene, (16, 9))])
            main_player.update_event_system(screen, self, main_player)
        if main_player.hp <= 8:
            main_player.shake_screen = True
        if self.boss.hp <= 0:
            self.boss.hp = 0
