import pygame

import src.constants.base_constants as Constants
import src.constants.spritesheet_constants as SpriteSheet_Constants
from src.battles.battle import Battle
from src.characters.boss import Boss
from src.events.basic_function_event import BasicFunctionEvent
from src.events.delay_event import DelayEvent
from src.events.dialogue_event import DialogueEvent
from src.events.scene_change_event import SceneChangeEvent
from src.scenes.gunshot_scene import GunShotScene


# modify scale
def modify_scale(screen, scene, main_player):
    Constants.FOCUS_CAMERA_SCALE = 2


# static battle class
class BattleStatic(Battle):
    def __init__(self, start_x=362, start_y=350):
        # lots and lots of parameters!!!
        super().__init__(1024, 432, start_x, start_y, 'textures/map/battle_background.png',
                         'textures/upper_layer/transparent.png',
                         None, False, False, True, False,
                         [(BasicFunctionEvent, modify_scale, tuple()), (DelayEvent, 2),
                          (DialogueEvent, '마음껏 때려보세요, 저는 한 대도 안 때릴 겁니다.', 'textures/characters/Agent01_idle.png'),
                          (DialogueEvent, '어차피 당신이 성공할 수 없다는 걸 알기 때문이죠^^', 'textures/characters/Agent01_idle.png'),
                          (DialogueEvent, '...', 'textures/characters/main_player_idle.png'),
                          (DialogueEvent, 'WASD 또는 방향키를 사용해 움직이고, X 키를 사용해 상대를 공격하자.')],
                         {0.5: [(DialogueEvent, '계속 때려 보세요. 전 안 죽습니다.', 'textures/characters/Agent01_idle.png')],
                          0.13: [(DialogueEvent, '제 손에는 집중을 안 하시는 거 같군요.', 'textures/characters/Agent01_idle.png'),
                                 (DialogueEvent, '손?', 'textures/characters/main_player_idle.png'),
                                 (SceneChangeEvent, GunShotScene, None)]}, [],
                         Boss(589, 380, SpriteSheet_Constants.FACING_LEFT, 'textures/spritesheets/Agent01.png', 40, ),
                         [],
                         [pygame.Rect(0, 350, 1024, 32), pygame.Rect(0, 0, 32, 432), pygame.Rect(992, 0, 32, 432)],
                         0.0017)

    # player might be invisible here too.
    def load(self, screen, main_player):
        super().load(screen, main_player)
        main_player.visible = True
