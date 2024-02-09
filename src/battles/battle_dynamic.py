import math
import random

import pygame

import src.constants.base_constants as Constants
import src.constants.sound_constants as SoundConstants
import src.constants.spritesheet_constants as SpriteSheet_Constants
from src.base.assets import assets
from src.battles.battle import Battle
from src.battles.battle_dynamic_multi import BattleDynamicMulti
from src.characters.boss import Boss
from src.characters.projectile import Projectile
from src.events.basic_function_event import BasicFunctionEvent
from src.events.delay_event import DelayEvent
from src.events.dialogue_event import DialogueEvent
from src.events.scene_change_event import SceneChangeEvent
from src.scenes.game_over_scene import GameOverScene


# modifies screen scale for battle scenes
# dirty hack but works
def modify_scale(screen, scene, main_player):
    # never edit constants. we were short of time!
    Constants.FOCUS_CAMERA_SCALE = 2


# reset scale and stop screen shaking.
# oh my god.
def reset_scale(screen, scene, main_player):
    # please don't do this to me
    Constants.FOCUS_CAMERA_SCALE = 4 / 3
    main_player.shake_screen = False


# define boss strategy
def boss_strategy(screen, scene, main_player, dt):
    # if main player has active events ongoing
    if main_player.event_active or main_player.events_waiting:
        return
    # check if boss is actually 'moving' and update anim
    if abs(scene.boss.vx) <= 0.066:
        scene.boss.playing_anim = False
    else:
        scene.boss.playing_anim = True
        scene.boss.anim = SpriteSheet_Constants.ACTION_WALKING
        if scene.boss.vx > 0:
            scene.boss.facing = SpriteSheet_Constants.FACING_RIGHT
        else:
            scene.boss.facing = SpriteSheet_Constants.FACING_LEFT
    # make the boss move
    if scene.boss.attack_blink_cnt == -1:
        scene.boss.vx = (main_player.x - scene.boss.x) / dt / 75
    # decrement projectile_idx
    scene.projectile_idx -= 1
    # launch projectiles
    if scene.projectile_idx == 0:
        # randomly decide what projectile to launch depending on HP
        has_gravity = bool((random.randrange(0, 100000) / 100000) >= (scene.boss.hp / scene.boss.max_hp) * 0.6)
        scene.projectiles = scene.projectiles + [
            Projectile(scene.boss.x, scene.boss.y, (0.96 if has_gravity else 0.48) * math.sin(2 * 3.14 * arg / 12),
                       (1 if has_gravity else 0.48) * math.cos(2 * 3.14 * arg / 12), has_gravity) for arg in range(12)]
        scene.projectile_idx = 180


# actual class for battle
class BattleDynamic(Battle):
    def __init__(self, start_x=362, start_y=350):
        # initialize projectile stuff
        self.projectiles = []
        self.projectile_idx = 180
        # call init of super with lots and lots of scene-specific parameters.
        super().__init__(1024, 432, start_x, start_y, 'textures/map/battle_background.png',
                         'textures/upper_layer/transparent.png',
                         'sounds/bgm/battle.mp3', False, False, True, False,
                         [(BasicFunctionEvent, modify_scale, tuple()), (DelayEvent, 2),
                          (DialogueEvent, '이번에도 뭐, 간단히 발라드릴게요.', 'textures/characters/Agent01_idle.png'),
                          (DialogueEvent, '총도 안 쓰고.', 'textures/characters/Agent01_idle.png'),
                          (DialogueEvent, '저 자식이...', 'textures/characters/main_player_idle.png')],
                         {0.75: [(DialogueEvent, '운이 좀 좋으시군요.', 'textures/characters/Agent01_idle.png')],
                          1 / 3: [(DialogueEvent, '으윽....', 'textures/characters/Agent01_idle.png')],
                          0.01: [(DialogueEvent, '으윽... 내가 지다니...', 'textures/characters/Agent01_idle.png'), (
                              DialogueEvent, '하지만 내가 회복을 해버린다면?',
                              'textures/characters/Agent01_idle.png'),
                                 (DialogueEvent, '비겁하다!', 'textures/characters/main_player_idle.png'),
                                 (DialogueEvent, '*저희도 돕겠습니다!!', 'textures/characters/Agent01_idle.png'),
                                 (BasicFunctionEvent, reset_scale, tuple()),
                                 (SceneChangeEvent, BattleDynamicMulti, None)]}, [],
                         Boss(589, 380, SpriteSheet_Constants.FACING_LEFT, 'textures/spritesheets/Agent01.png', 40,
                              boss_strategy),
                         [],
                         [pygame.Rect(-100, 350, 1224, 32), pygame.Rect(0, 0, 32, 432), pygame.Rect(992, 0, 32, 432), ],
                         0.0017)

    # main_player might be invisible
    def load(self, screen, main_player):
        super().load(screen, main_player)
        main_player.visible = True

    # update projectile physics too
    def update_physics(self, screen, main_player, dt):
        super().update_physics(screen, main_player, dt)
        for projectile in self.projectiles:
            projectile.move(screen, self, main_player, dt)

    # add projectile mechanism
    def update_mechanics(self, screen, main_player, dt):
        super().update_mechanics(screen, main_player, dt)
        projectiles_to_delete = []
        for projectile in self.projectiles:
            # check if projectile is out of bounds
            if (projectile.x > 1024 or projectile.x < 0) or (projectile.y < 0 or projectile.y > 432):
                projectiles_to_delete.append(projectile)
            else:
                # check collision with player
                if projectile.rect.colliderect(main_player.rect):
                    projectiles_to_delete.append(projectile)
                    main_player.hp -= projectile.power
                    pygame.mixer.Channel(SoundConstants.EFFECT_CHANNEL).play(assets.get_asset('sounds/effects/hit.mp3'))
                    main_player.attacked(screen, self, dt)
        for projectile in projectiles_to_delete:
            self.projectiles.remove(projectile)

        for projectile in self.projectiles:
            projectile.update(screen, self, main_player, dt)
        # events based on main_player hp
        if main_player.hp <= 8:
            main_player.shake_screen = True
        if main_player.hp <= 0:
            main_player.add_event_queue(screen, self, main_player, [(BasicFunctionEvent, reset_scale, tuple()),
                                                                    (SceneChangeEvent, GameOverScene, (16, 9))])
            main_player.update_event_system(screen, self, main_player)
        # correct boss hp smalller than 0
        if self.boss.hp <= 0:
            self.boss.hp = 0
