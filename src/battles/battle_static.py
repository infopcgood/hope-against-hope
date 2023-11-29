import pygame

from src.battles.battle import Battle
import src.constants.spritesheet_constants as SpriteSheet_Constants
from src.characters.boss import Boss
from src.characters.npc import NPC
from src.events.delay_event import DelayEvent
from src.events.dialogue_event import DialogueEvent

class BattleStatic(Battle):
    def __init__(self, start_x=512, start_y=300):
        super().__init__(1024, 432, start_x, start_y, 'textures/map/basic_background_with_houses.png',
                         'textures/upper_layer/transparent.png',
                         'sounds/empty.wav', True, True, True, False, [(DelayEvent, 2), (DialogueEvent, '마음껏 때려보세요, 저는 한 대도 안 때릴 겁니다.', 'textures/characters/Agent01_idle.png'), (DialogueEvent, '어차피 당신이 성공할 수 없다는 걸 알기 때문이죠^^', 'textures/characters/Agent01_idle.png'), (DialogueEvent, '...', 'textures/characters/main_player_idle.png')], [], [],
                         Boss(589, 300, SpriteSheet_Constants.FACING_LEFT, 'textures/spritesheets/Agent01.png', 99, ), [],
                         [pygame.Rect(0, 300, 1024, 132)], 0.0017)

    def load(self, screen, main_player):
        super().load(screen, main_player)
        main_player.visible = True
