import src.constants.spritesheet_constants as SpriteSheet_Constants
from src.characters.npc import NPC
from src.events.basic_function_event import BasicFunctionEvent
from src.events.delay_event import DelayEvent
from src.events.dialogue_event import DialogueEvent
from src.events.emote_event import PlayerEmoteEvent
from src.events.scene_change_event import SceneChangeEvent
from src.scenes.scene import Scene
from src.scenes.scene_02 import Scene02


def interact_with(screen, scene, main_player, npc_idx):
    if not scene.interacted_with[npc_idx]:
        scene.talked_cnt += 1
        scene.interacted_with[npc_idx] = True


def move_main_player_one_tile(screen, scene, main_player, direction):
    main_player.move_one_tile(direction, screen, scene, main_player)


# First scene of game.
class Scene01(Scene):

    def __init__(self, start_tile_x=13, start_tile_y=10):
        # super init with dialogues and events
        super().__init__(32, 18, start_tile_x, start_tile_y, "textures/map/poor_village.png",
                         "textures/upper_layer/transparent.png", 'sounds/bgm/sad.mp3', True,
                         True, True, True,
                         [(DelayEvent, 1), (PlayerEmoteEvent, SpriteSheet_Constants.EMOTE_THINK), (DelayEvent, 2.5),
                          (DialogueEvent, '하...', 'textures/characters/main_player_idle.png'), (DelayEvent, 0.75),
                          (DialogueEvent, '오늘도 똑같은 하루가 시작되는 건가.', 'textures/characters/main_player_idle.png'),
                          (DelayEvent, 0.75),
                          (DialogueEvent, '매일 똑같은 밥, 똑같은 집, 똑같은 인생...', 'textures/characters/main_player_idle.png'),
                          (DelayEvent, 0.75), (DialogueEvent, '이젠 지쳤어...', 'textures/characters/main_player_idle.png'),
                          (DelayEvent, 0.75), (DialogueEvent, 'WASD 또는 방향키로 이동, Esc 키로 메뉴 열기, X 키로 상호작용하세요.')],
                         [NPC(17, 8, SpriteSheet_Constants.FACING_DOWN, 'textures/spritesheets/transparent.png',
                              [(DialogueEvent, '늘 이 자리에 서 있는 보급품 가판대일 뿐이다.')]),
                          NPC(16, 8, SpriteSheet_Constants.FACING_DOWN, 'textures/spritesheets/transparent.png',
                              [(DialogueEvent, '늘 이 자리에 서 있는 보급품 가판대일 뿐이다.')]),
                          NPC(15, 9, SpriteSheet_Constants.FACING_DOWN, 'textures/spritesheets/transparent.png',
                              [(DialogueEvent, '늘 이 자리에 서 있는 보급품 가판대일 뿐이다.')]),
                          NPC(16, 9, SpriteSheet_Constants.FACING_DOWN, 'textures/spritesheets/transparent.png',
                              [(DialogueEvent, '늘 이 자리에 서 있는 보급품 가판대일 뿐이다.')]),
                          NPC(17, 9, SpriteSheet_Constants.FACING_DOWN, 'textures/spritesheets/transparent.png',
                              [(DialogueEvent, '늘 이 자리에 서 있는 보급품 가판대일 뿐이다.')]),
                          NPC(20, 9, SpriteSheet_Constants.FACING_LEFT, 'textures/spritesheets/Character02.png',
                              [(DialogueEvent, '인생은 참으로 힘들지... 더 나아질 길은 없을까.',
                                'textures/characters/Character02_idle.png'),
                               (BasicFunctionEvent, interact_with, (0,))]),
                          NPC(16, 5, SpriteSheet_Constants.FACING_DOWN, 'textures/spritesheets/Character03.png',
                              [(DialogueEvent, '뭔가 변화가 필요해.', 'textures/characters/Character03_idle.png'),
                               (DialogueEvent, '너도 그렇게 생각하는구나.', 'textures/characters/main_player_idle.png'), (
                                   DialogueEvent, '언제나 생각 뿐이지... 할 수 있는 건 아무것도 없잖아?',
                                   'textures/characters/Character03_idle.png'),
                               (BasicFunctionEvent, interact_with, (1,))]),
                          NPC(4, 4, SpriteSheet_Constants.FACING_DOWN, 'textures/spritesheets/Character04.png',
                              [(DialogueEvent, '고민할 게 있으면 왕 아저씨에게 가봐.', 'textures/characters/Character04_idle.png'), (
                                  DialogueEvent, '저...절대로 새로 생긴 가게를 홍보하는 건 아니야!!',
                                  'textures/characters/Character04_idle.png'),
                               (DialogueEvent, '(보통 공원에 앉아계시던데...)', 'textures/characters/main_player_idle.png'),
                               (BasicFunctionEvent, interact_with, (2,))]),
                          NPC(28, 1, SpriteSheet_Constants.FACING_UP, 'textures/spritesheets/Character05.png', [(
                              DialogueEvent,
                              '안녕, 힘세고 강한 아침! 만일 내게 묻는다면 나는...',
                              'textures/characters/Character05_idle.png'),
                              (
                                  DialogueEvent,
                                  '...부정적이야.',
                                  'textures/characters/Character05_idle.png'),
                              (
                                  DialogueEvent,
                                  '인생이 다 그렇지 뭐.',
                                  'textures/characters/main_player_idle.png'),
                              (
                                  DialogueEvent,
                                  '설계된 삶을 사는데도 행복할 수 없다니...',
                                  'textures/characters/Character05_idle.png'),
                              (
                                  DialogueEvent,
                                  '(설계된 삶...)',
                                  'textures/characters/main_player_idle.png'),
                              (
                                  BasicFunctionEvent,
                                  interact_with,
                                  (3,))]),
                          NPC(23, 12, SpriteSheet_Constants.FACING_UP, 'textures/spritesheets/Character01.png',
                              [(DialogueEvent, '빈민가의 삶은 변하지 않아.', 'textures/characters/Character01_idle.png'), (
                                  DialogueEvent, '어떤 짓을 하든, 더 안 좋은 결과만 기다리고 있을 뿐이라구.',
                                  'textures/characters/Character01_idle.png'), (
                                   DialogueEvent, '그냥 희망을 갖지 마. 사회는 온통 어둠밖에 없어.',
                                   'textures/characters/Character01_idle.png'),
                               (BasicFunctionEvent, interact_with, (4,))])])
        self.movable_tiles = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
            [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0],
            [0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0],
            [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0],
            [0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0],
            [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        # scene variables to check if player talked to NPCs
        self.talked_cnt = 0
        self.interacted_with = [False, False, False, False, False, ]

    def load(self, screen, main_player):
        # make player visible
        main_player.visible = True
        super().load(screen, main_player)

    def add_event_system(self, screen, main_player):
        # add event system to move on to next scene
        self.event_tiles[(9, 1)] = [((DialogueEvent, '최소 5명과 얘기를 나누고 오도록 하자.'), "args[0].talked_cnt < 5", (self,)), (
            (BasicFunctionEvent, move_main_player_one_tile, (SpriteSheet_Constants.FACING_RIGHT,)),
            "args[0].talked_cnt < 5", (self,)),
                                    ((SceneChangeEvent, Scene02, (31, 9)), 'args[0].talked_cnt >= 5', (self,))]
        self.event_tiles[(8, 1)] = [((DialogueEvent, '최소 5명과 얘기를 나누고 오도록 하자.'), "args[0].talked_cnt < 5", (self,)), (
            (BasicFunctionEvent, move_main_player_one_tile, (SpriteSheet_Constants.FACING_RIGHT,)),
            "args[0].talked_cnt < 5", (self,)),
                                    ((SceneChangeEvent, Scene02, (31, 8)), 'args[0].talked_cnt >= 5', (self,))]
