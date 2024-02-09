import src.constants.spritesheet_constants as SpriteSheet_Constants
from src.characters.npc import NPC
from src.events.basic_function_event import BasicFunctionEvent
from src.events.delay_event import DelayEvent
from src.events.dialogue_event import DialogueEvent
from src.events.emote_event import PlayerEmoteEvent
from src.events.scene_change_event import SceneChangeEvent
from src.scenes.scene import Scene
from src.scenes.scene_03 import Scene03


def move_main_player_one_tile(screen, scene, main_player, direction):
    main_player.move_one_tile(direction, screen, scene, main_player)


# Second scene of game.
class Scene02(Scene):

    def __init__(self, start_tile_x=13, start_tile_y=10):
        # super init with dialogues and events
        super().__init__(32, 18, start_tile_x, start_tile_y, "textures/map/park.png",
                         "textures/upper_layer/park_upper.png", None, True,
                         True, True, True, None,
                         [NPC(7, 4, SpriteSheet_Constants.FACING_DOWN, 'textures/spritesheets/transparent.png',
                              [(DialogueEvent, "'자본주의의 절정', 자판기다.")]),
                          NPC(8, 4, SpriteSheet_Constants.FACING_DOWN, 'textures/spritesheets/transparent.png',
                              [(DialogueEvent, "'자본주의의 절정', 자판기다.")]),
                          NPC(7, 5, SpriteSheet_Constants.FACING_DOWN, 'textures/spritesheets/transparent.png',
                              [(DialogueEvent, "'자본주의의 절정', 자판기다."), (DelayEvent, 0.75),
                               (DialogueEvent, "...비타700은 무료니까 하나만 마셔볼까."), (DelayEvent, 1),
                               (PlayerEmoteEvent, SpriteSheet_Constants.EMOTE_LIKE), (DelayEvent, 1.5),
                               (DialogueEvent, '확실히 달긴 하다.')]),
                          NPC(8, 5, SpriteSheet_Constants.FACING_DOWN, 'textures/spritesheets/transparent.png',
                              [(DialogueEvent, "'자본주의의 절정', 자판기다."), (DelayEvent, 0.75),
                               (DialogueEvent, "...생수 살 돈도 없다니.")]),
                          NPC(7, 8, SpriteSheet_Constants.FACING_DOWN, 'textures/spritesheets/transparent.png',
                              [(DialogueEvent, "'자본주의의 절정', 자판기다.")]),
                          NPC(8, 8, SpriteSheet_Constants.FACING_DOWN, 'textures/spritesheets/transparent.png',
                              [(DialogueEvent, "'자본주의의 절정', 자판기다.")]),
                          NPC(7, 9, SpriteSheet_Constants.FACING_DOWN, 'textures/spritesheets/transparent.png',
                              [(DialogueEvent, "'자본주의의 절정', 자판기다."), (DelayEvent, 0.75),
                               (DialogueEvent, "...생수 살 돈도 없다니.")]),
                          NPC(8, 9, SpriteSheet_Constants.FACING_DOWN, 'textures/spritesheets/transparent.png',
                              [(DialogueEvent, "'자본주의의 절정', 자판기다."), (DelayEvent, 0.75),
                               (DialogueEvent, "...서민들의 음료수 콜라조차도 우리에겐 사치다."), ]),
                          NPC(7, 12, SpriteSheet_Constants.FACING_DOWN, 'textures/spritesheets/transparent.png',
                              [(DialogueEvent, "'자본주의의 절정', 자판기다.")]),
                          NPC(8, 12, SpriteSheet_Constants.FACING_DOWN, 'textures/spritesheets/transparent.png',
                              [(DialogueEvent, "'자본주의의 절정', 자판기다.")]),
                          NPC(7, 13, SpriteSheet_Constants.FACING_DOWN, 'textures/spritesheets/transparent.png',
                              [(DialogueEvent, "'자본주의의 절정', 자판기다."), (DelayEvent, 0.75),
                               (DialogueEvent, "...여기는 뭐 파는 것도 없네.")]),
                          NPC(8, 13, SpriteSheet_Constants.FACING_DOWN, 'textures/spritesheets/transparent.png',
                              [(DialogueEvent, "'자본주의의 절정', 자판기다."), (DelayEvent, 0.75),
                               (DialogueEvent, "...웬일로 텅텅 비어있지?"), ]),
                          NPC(18, 6, SpriteSheet_Constants.FACING_DOWN, 'textures/spritesheets/GrandpaWang.png',
                              [(DialogueEvent, "왕 할아버지!", 'textures/characters/main_player_idle.png'), (
                                  DialogueEvent, "아 그래, 건너편에 사는 철이구나. 무슨 일이니?",
                                  'textures/characters/GrandpaWang_idle.png'),
                               (DialogueEvent, '음...', 'textures/characters/main_player_idle.png'), (DelayEvent, 0.25),
                               (PlayerEmoteEvent, SpriteSheet_Constants.EMOTE_THINK), (DelayEvent, 1.5), (
                                   DialogueEvent, '그냥... 오늘따라 좀 알 수 없는 회의감이 드는 거 같아요...',
                                   'textures/characters/main_player_idle.png'),
                               (DialogueEvent, '그럴 때는 말이다... 음....', 'textures/characters/GrandpaWang_idle.png'),
                               (DialogueEvent, '그냥 신경 쓰지 말고 살렴.', 'textures/characters/GrandpaWang_idle.png'),
                               (DialogueEvent, '어차피 너가 바꿀 수 있는 건 없어.', 'textures/characters/GrandpaWang_idle.png'),
                               (DialogueEvent, '음... 알겠어요.', 'textures/characters/main_player_idle.png'),
                               (DialogueEvent, '(결국 이대로 사는 방법밖에 없는 건가...)', 'textures/characters/main_player_idle.png'),
                               (DelayEvent, 1),
                               (BasicFunctionEvent, move_main_player_one_tile, (SpriteSheet_Constants.FACING_LEFT,)),
                               (BasicFunctionEvent, move_main_player_one_tile, (SpriteSheet_Constants.FACING_LEFT,)),
                               (BasicFunctionEvent, move_main_player_one_tile, (SpriteSheet_Constants.FACING_LEFT,)),
                               (BasicFunctionEvent, move_main_player_one_tile, (SpriteSheet_Constants.FACING_LEFT,)),
                               (BasicFunctionEvent, move_main_player_one_tile, (SpriteSheet_Constants.FACING_LEFT,)),
                               (BasicFunctionEvent, move_main_player_one_tile, (SpriteSheet_Constants.FACING_LEFT,)),
                               (BasicFunctionEvent, move_main_player_one_tile, (SpriteSheet_Constants.FACING_LEFT,)),
                               (DelayEvent, 3), (PlayerEmoteEvent, SpriteSheet_Constants.EMOTE_QUESTION),
                               (DelayEvent, 1.75),
                               (DialogueEvent, '응? 웬 종이지?', 'textures/characters/main_player_idle.png'), (
                                   DialogueEvent, "'Résistance 활동 모집, 연락 주세요.'",
                                   'textures/characters/main_player_idle.png'), (DelayEvent, 0.5),
                               (PlayerEmoteEvent, SpriteSheet_Constants.EMOTE_THINK), (DelayEvent, 1.75),
                               (DialogueEvent, '일단 챙겨 둬야겠다.', 'textures/characters/main_player_idle.png'),
                               (DelayEvent, 1), (SceneChangeEvent, Scene03, (16, 9))])
                          ])
        self.movable_tiles = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0],
            [0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0],
            [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
            [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
            [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
            [0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0],
            [0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0],
            [0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    def add_event_system(self, screen, main_player):
        pass
