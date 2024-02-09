import src.constants.spritesheet_constants as SpriteSheet_Constants
from src.characters.npc import NPC
from src.events.basic_function_event import BasicFunctionEvent
from src.events.delay_event import DelayEvent
from src.events.dialogue_event import DialogueEvent, AutoContinuedDialogueEvent
from src.events.scene_change_event import SceneChangeEvent
from src.scenes.scene import Scene
from src.scenes.scene_09 import Scene09


def interact_with(screen, scene, main_player, npc_idx):
    if scene.interacted_with[npc_idx] == False:
        scene.talked_cnt += 1
        scene.interacted_with[npc_idx] = True


def move_main_player_one_tile(screen, scene, main_player, direction):
    main_player.move_one_tile(direction, screen, scene, main_player)


def set_anim_of_npc(screen, scene, main_player, npc_idx, anim):
    scene.npcs[npc_idx].anim = anim
    scene.npcs[npc_idx].playing_anim = True


def force_npc_facing(screen, scene, main_player, npc_idx, facing):
    scene.npcs[npc_idx].facing = facing


# 8th scene of the game
class Scene08(Scene):

    def __init__(self, start_tile_x=13, start_tile_y=10):
        # call super init with long, long dialogue and events
        super().__init__(32, 18, start_tile_x, start_tile_y, "textures/map/hallway.png",
                         "textures/upper_layer/transparent.png", None, True,
                         True, True, True,
                         [(BasicFunctionEvent, set_anim_of_npc, (idx, SpriteSheet_Constants.ACTION_DEAD)) for idx in
                          range(6)] + [(DialogueEvent, '???', 'textures/characters/main_player_idle.png'),
                                       (DialogueEvent, '뭐야...', 'textures/characters/main_player_idle.png'),
                                       (DialogueEvent, '이런 이런, 한 분이 더 계셨군요.',
                                        'textures/characters/silhouette.png'),
                                       (BasicFunctionEvent, force_npc_facing, (6, SpriteSheet_Constants.FACING_LEFT)),
                                       (DelayEvent, 2),
                                       (DialogueEvent, 'SCALE에서 나왔습니다.', 'textures/characters/Agent01_idle.png'),
                                       (DialogueEvent, 'Social Control And Life Establishment, 정부 기관인 건 아시겠죠?',
                                        'textures/characters/Agent01_idle.png'),
                                       (DialogueEvent, '아무튼 반란 모의 조직을 발견해서 소탕하려던 참이였는데, 같은 편이신가요?',
                                        'textures/characters/Agent01_idle.png'),
                                       (DialogueEvent, '어...', 'textures/characters/main_player_idle.png'),
                                       (AutoContinuedDialogueEvent, '어제 한 번 찾아오긴 했는',
                                        'textures/characters/main_player_idle.png'),
                                       (DialogueEvent, '어제 찾아 오셨다고요? 몇 가지만 물어봅시다.',
                                        'textures/characters/Agent01_idle.png'),
                                       (DialogueEvent, '사회에 불만 같은 거, 혹시 있으세요?',
                                        'textures/characters/Agent01_idle.png'),
                                       (DialogueEvent, '어...', 'textures/characters/main_player_idle.png'),
                                       (DelayEvent, 0.25), (SceneChangeEvent, Scene09, (16, 9))],
                         [NPC(9, 4, SpriteSheet_Constants.FACING_DOWN, 'textures/spritesheets/Leader.png'),
                          NPC(6, 7, SpriteSheet_Constants.FACING_UP, 'textures/spritesheets/Character01.png'),
                          NPC(9, 7, SpriteSheet_Constants.FACING_UP, 'textures/spritesheets/Character02.png'),
                          NPC(12, 7, SpriteSheet_Constants.FACING_UP, 'textures/spritesheets/Character03.png'),
                          NPC(7, 10, SpriteSheet_Constants.FACING_UP, 'textures/spritesheets/Character04.png'),
                          NPC(11, 10, SpriteSheet_Constants.FACING_UP, 'textures/spritesheets/Character05.png'),
                          NPC(5, 9, SpriteSheet_Constants.FACING_UP, 'textures/spritesheets/Agent01.png')])
        self.movable_tiles = [
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]]

    def load(self, screen, main_player):
        main_player.visible = True
        super().load(screen, main_player)

    def add_event_system(self, screen, main_player):
        pass
