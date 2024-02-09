import src.constants.spritesheet_constants as SpriteSheet_Constants
from src.events.basic_function_event import BasicFunctionEvent
from src.events.delay_event import DelayEvent
from src.events.dialogue_event import DialogueEvent
from src.events.emote_event import PlayerEmoteEvent
from src.events.scene_change_event import SceneChangeEvent
from src.scenes.scene import Scene
from src.scenes.scene_08 import Scene08


def interact_with(screen, scene, main_player, npc_idx):
    if scene.interacted_with[npc_idx] == False:
        scene.talked_cnt += 1
        scene.interacted_with[npc_idx] = True


def move_main_player_one_tile(screen, scene, main_player, direction):
    main_player.move_one_tile(direction, screen, scene, main_player)


def force_main_player_facing(screen, scene, main_player, facing):
    main_player.facing = facing


# seventh scene.
class Scene07(Scene):

    def __init__(self, start_tile_x=13, start_tile_y=10):
        # super init with dialogues and events
        super().__init__(32, 18, start_tile_x, start_tile_y, "textures/map/poor_village_upper_open.png",
                         "textures/upper_layer/transparent.png", 'sounds/bgm/sad.mp3', True,
                         True, True, True,
                         [(DelayEvent, 2.5),
                          (BasicFunctionEvent, force_main_player_facing, (SpriteSheet_Constants.FACING_DOWN,)),
                          (DialogueEvent, '다음 날.'), (DelayEvent, 1.5),
                          (PlayerEmoteEvent, SpriteSheet_Constants.EMOTE_THINK), (DelayEvent, 1.75),
                          (BasicFunctionEvent, move_main_player_one_tile, (SpriteSheet_Constants.FACING_DOWN,)),
                          (DelayEvent, 1), (DialogueEvent, '언제쯤 생명 유지 포드 말고 제대로 된 집에서 살 수 있을까...',
                                            'textures/characters/main_player_idle.png'),
                          (PlayerEmoteEvent, SpriteSheet_Constants.EMOTE_QUESTION), (DelayEvent, 1.75),
                          (DialogueEvent, '저쪽 골목에서 무슨 소리가 들리는 거 같은데...', 'textures/characters/main_player_idle.png')],
                         [])
        self.movable_tiles = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
            [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0],
            [0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0],
            [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0],
            [0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0],
            [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    def load(self, screen, main_player):
        main_player.visible = True
        super().load(screen, main_player)

    def add_event_system(self, screen, main_player):
        # make player move onto next scene
        self.event_tiles[(9, 32)] = [(SceneChangeEvent, Scene08, (1, 9))]
        self.event_tiles[(8, 32)] = [(SceneChangeEvent, Scene08, (1, 8))]
        self.event_tiles[(9, 1)] = [(DialogueEvent, '지금 공원에 가는 건 아닌 거 같아.', 'textures/characters/main_player_idle.png')]
        self.event_tiles[(8, 1)] = [(DialogueEvent, '지금 공원에 가는 건 아닌 거 같아.', 'textures/characters/main_player_idle.png')]
