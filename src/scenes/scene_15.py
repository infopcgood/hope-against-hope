import src.constants.spritesheet_constants as SpriteSheet_Constants
from src.battles.battle_dynamic import BattleDynamic
from src.characters.npc import NPC
from src.events.basic_function_event import BasicFunctionEvent
from src.events.delay_event import DelayEvent
from src.events.dialogue_event import DialogueEvent
from src.events.scene_change_event import SceneChangeEvent
from src.scenes.scene import Scene


def move_main_player_one_tile(screen, scene, main_player, direction):
    main_player.move_one_tile(direction, screen, scene, main_player)


def find_keys(screen, scene, main_player):
    scene.found_keys = True


# 15th scene of game.
class Scene15(Scene):
    def __init__(self, start_tile_x=14, start_tile_y=10):
        # call super init with dialogue.
        super().__init__(32, 18, start_tile_x, start_tile_y, "textures/map/scale_1st.png",
                         "textures/upper_layer/scale_1st_upper.png", None, True,
                         True, True, True, [
                             (DelayEvent, 1.75),
                             (DialogueEvent, 'SCALE은 내 칼을 받아라!!!', 'textures/characters/main_player_idle.png'),
                             (DelayEvent, 2),
                             (DialogueEvent, '...아무도 없네.', 'textures/characters/main_player_idle.png'),
                             (DialogueEvent, '여긴 빈민가만 관리하는 지사라서 그런가 보다.', 'textures/characters/main_player_idle.png'),
                             (DialogueEvent, '독재에도 빈부 격차가 있다니...', 'textures/characters/main_player_idle.png'),
                             (DialogueEvent, '아이러니하군.', 'textures/characters/main_player_idle.png'),
                             (DialogueEvent, '옥상에 한번 올라가 봐야겠어.', 'textures/characters/main_player_idle.png')],
                         [NPC(3, 9, SpriteSheet_Constants.FACING_UP, 'textures/spritesheets/transparent.png',
                              [(DialogueEvent, '카드 키를 발견했다.'),
                               (DialogueEvent, '이거면 옥상에 올라갈 수 있겠지.', 'textures/characters/main_player_idle.png'),
                               (BasicFunctionEvent, find_keys, tuple())])])
        self.movable_tiles = [
            [1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
            [1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
        # make variable for key
        self.found_keys = False

    def add_event_system(self, screen, main_player):
        # add events to find card keys and then interact with Agents.
        self.event_tiles[(11, 13)] = [((DialogueEvent, '카드 키가 필요합니다.'), "not args[0].found_keys", (self,)), (
            (DialogueEvent, '쩝...', 'textures/characters/main_player_idle.png'), "not args[0].found_keys", (self,)), (
                                          (DialogueEvent, '한번 천천히 주위를 찾아보자.',
                                           'textures/characters/main_player_idle.png'),
                                          "not args[0].found_keys", (self,)), (
                                          (DialogueEvent, '주변 사물들과 상호작용해 보며 카드키를 찾아보자.'),
                                          "not args[0].found_keys", (self,)),
                                      ((DialogueEvent, '[SYSTEM] 카드키 인식 성공, 개문합니다.'), "args[0].found_keys", (self,)),
                                      ((DialogueEvent, '옥상으로 한번 가 볼까..', 'textures/characters/main_player_idle.png'),
                                       "args[0].found_keys", (self,)),
                                      ((DelayEvent, 1), "args[0].found_keys", (self,)),
                                      ((DialogueEvent, '*뭐 하시는 겁니까?', 'textures/characters/Agent01_idle.png'),
                                       "args[0].found_keys", (self,)),
                                      ((DialogueEvent, '윽, 기습이다...', 'textures/characters/main_player_idle.png'),
                                       "args[0].found_keys", (self,)),
                                      ((DialogueEvent, '*순순히 내려오시죠. 저희 10명이나 있습니다.',
                                        'textures/characters/Agent01_idle.png'), "args[0].found_keys", (self,)),
                                      ((DialogueEvent, '그럴 순 없어.', 'textures/characters/main_player_idle.png'),
                                       "args[0].found_keys", (self,)),
                                      ((DialogueEvent, '(꼼짝없이 이렇게 당하고 마는 건가...)',
                                        'textures/characters/main_player_idle.png'),
                                       "args[0].found_keys", (self,)),
                                      ((DialogueEvent, '잠깐.',
                                        'textures/characters/Agent01_idle.png'),
                                       "args[0].found_keys", (self,)),
                                      ((DialogueEvent, '제가 상대하도록 하죠?',
                                        'textures/characters/Agent01_idle.png'),
                                       "args[0].found_keys", (self,)),
                                      ((DialogueEvent, '*?',
                                        'textures/characters/Agent01_idle.png'),
                                       "args[0].found_keys", (self,)),
                                      ((DialogueEvent, '요즘 본부에 인력도 부족하고 하니까... 여기 같은 지사 정도는 버려도 돼요.',
                                        'textures/characters/Agent01_idle.png'),
                                       "args[0].found_keys", (self,)),
                                      ((DialogueEvent, "...물론 저 '방해 요소'를 먼저 제거한다면 좋겠지만.",
                                        'textures/characters/Agent01_idle.png'),
                                       "args[0].found_keys", (self,)),
                                      ((DialogueEvent, "10명 낭비하기는 싫으니까, 저 혼자서 깔끔하게 쓰러트려 드리겠습니다.",
                                        'textures/characters/Agent01_idle.png'),
                                       "args[0].found_keys", (self,)),
                                      ((DialogueEvent, "이기면 순순히 넘겨드리죠. 물론 봐드리는 건 없습니다.",
                                        'textures/characters/Agent01_idle.png'),
                                       "args[0].found_keys", (self,)),
                                      ((DialogueEvent, "...",
                                        'textures/characters/main_player_idle.png'),
                                       "args[0].found_keys", (self,)),
                                      ((DelayEvent, 1.5),
                                       "args[0].found_keys", (self,)),
                                      ((SceneChangeEvent, BattleDynamic, None),
                                       "args[0].found_keys", (self,))
                                      ]
        pass
