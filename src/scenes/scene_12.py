import src.constants.spritesheet_constants as SpriteSheet_Constants
from src.events.basic_function_event import BasicFunctionEvent
from src.events.delay_event import DelayEvent
from src.events.dialogue_event import DialogueEvent
from src.events.emote_event import PlayerEmoteEvent
from src.events.scene_change_event import SceneChangeEvent
from src.scenes.scene import Scene
from src.scenes.scene_13 import Scene13


def move_main_player_one_tile(screen, scene, main_player, direction):
    main_player.move_one_tile(direction, screen, scene, main_player)


def set_anim_of_npc(screen, scene, main_player, npc_idx, anim):
    scene.npcs[npc_idx].anim = anim
    scene.npcs[npc_idx].playing_anim = True
    scene.npcs[npc_idx].anim_index = SpriteSheet_Constants.ACTION_INDEX_CNT[anim] - 1


def set_anim_of_player(screen, scene, main_player, anim):
    main_player.anim = anim
    main_player.playing_anim = bool(not anim == SpriteSheet_Constants.ACTION_IDLE)
    main_player.anim_index = SpriteSheet_Constants.ACTION_INDEX_CNT[anim] - 1


# 12nd scene of game.
class Scene12(Scene):

    def __init__(self, start_tile_x=16, start_tile_y=9):
        # super init with self-talking dialogue and events.
        super().__init__(32, 18, start_tile_x, start_tile_y, "textures/map/shelter_positive.png",
                         "textures/upper_layer/transparent.png", None, True,
                         True, False, True,
                         [(BasicFunctionEvent, set_anim_of_player, (SpriteSheet_Constants.ACTION_IDLE,)),
                          (DelayEvent, 2),
                          (DialogueEvent, '...가버렸네.', 'textures/characters/main_player_idle.png'),
                          (PlayerEmoteEvent, SpriteSheet_Constants.EMOTE_THINK),
                          (DelayEvent, 1.75),
                          (DialogueEvent, '...할아버지 말이 맞을 수도 있어.', 'textures/characters/main_player_idle.png'),
                          (DialogueEvent, '어쩌면 이 사회에는 아직 희망이 남아 있을지도 몰라.', 'textures/characters/main_player_idle.png'),
                          (DialogueEvent, '절망을 모두 태워버릴 자그마한 불씨...', 'textures/characters/main_player_idle.png'),
                          (DialogueEvent, '...그게 바로 나라면?', 'textures/characters/main_player_idle.png'),
                          (PlayerEmoteEvent, SpriteSheet_Constants.EMOTE_THINK),
                          (DelayEvent, 1.75),
                          (DialogueEvent, '...그래, 뭐라도 해봐야겠어.', 'textures/characters/main_player_idle.png'),
                          (
                              DialogueEvent, '당당하게 문을 박차고 들어가서, 그놈의 목을 따는 거야.',
                              'textures/characters/main_player_idle.png'),
                          (DialogueEvent, '좋아, 가보자!', 'textures/characters/main_player_idle.png'), ],
                         [])
        self.movable_tiles = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    def load(self, screen, main_player):
        super().load(screen, main_player)
        main_player.visible = True

    def add_event_system(self, screen, main_player):
        # move on to next scene
        self.event_tiles[(17, 16)] = [(SceneChangeEvent, Scene13, (16, 1))]
        self.event_tiles[(17, 17)] = [(SceneChangeEvent, Scene13, (17, 1))]
