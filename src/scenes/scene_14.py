import src.constants.spritesheet_constants as SpriteSheet_Constants
from src.characters.npc import NPC
from src.events.delay_event import DelayEvent
from src.events.dialogue_event import DialogueEvent
from src.events.emote_event import PlayerEmoteEvent
from src.events.scene_change_event import SceneChangeEvent
from src.scenes.scene import Scene
from src.scenes.scene_15 import Scene15


def move_main_player_one_tile(screen, scene, main_player, direction):
    main_player.move_one_tile(direction, screen, scene, main_player)


# 14th scene of game.
class Scene14(Scene):

    def __init__(self, start_tile_x=14, start_tile_y=10):
        # call super init with dialogues depending on interactions with objects/NPCs.
        super().__init__(32, 18, start_tile_x, start_tile_y, "textures/map/park_open.png",
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
                              [(DialogueEvent, "...마음을 먹은 게로구나.", 'textures/characters/GrandpaWang_idle.png'),
                               (DialogueEvent, '...네.', 'textures/characters/main_player_idle.png'),
                               (DialogueEvent, "...알겠네.", 'textures/characters/GrandpaWang_idle.png'),
                               (DialogueEvent, "본부는 바로 왼쪽에 있어. 건투를 비네.", 'textures/characters/GrandpaWang_idle.png')])])
        self.movable_tiles = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0],
            [0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0],
            [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
            [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
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
        # move onto next scene
        self.event_tiles[(9, 1)] = [(SceneChangeEvent, Scene15, (32, 9))]
        self.event_tiles[(8, 1)] = [(SceneChangeEvent, Scene15, (32, 8))]
