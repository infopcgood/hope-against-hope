import src.constants.spritesheet_constants as SpriteSheet_Constants
from src.characters.npc import NPC
from src.events.basic_function_event import BasicFunctionEvent
from src.events.delay_event import DelayEvent
from src.events.dialogue_event import DialogueEvent
from src.events.scene_change_event import SceneChangeEvent
from src.scenes.game_over_scene import GameOverScene
from src.scenes.scene import Scene


def interact_with(screen, scene, main_player, npc_idx):
    if scene.interacted_with[npc_idx] == False:
        scene.talked_cnt += 1
        scene.interacted_with[npc_idx] = True


def move_main_player_one_tile(screen, scene, main_player, direction):
    main_player.move_one_tile(direction, screen, scene, main_player)


def set_anim_of_npc(screen, scene, main_player, npc_idx, anim):
    scene.npcs[npc_idx].anim = anim
    scene.npcs[npc_idx].playing_anim = True
    scene.npcs[npc_idx].anim_index = SpriteSheet_Constants.ACTION_INDEX_CNT[anim] - 1


def force_main_player_facing(screen, scene, main_player, facing):
    main_player.facing = facing


# bad ending scene.
class Scene90(Scene):

    def __init__(self, start_tile_x=13, start_tile_y=10):
        super().__init__(32, 18, start_tile_x, start_tile_y, "textures/map/hallway.png",
                         "textures/upper_layer/transparent.png", None, True,
                         True, True, True,
                         [(BasicFunctionEvent, set_anim_of_npc, (idx, SpriteSheet_Constants.ACTION_DEAD)) for idx in
                          range(6)] + [
                             (BasicFunctionEvent, force_main_player_facing, (SpriteSheet_Constants.FACING_RIGHT,)),
                             (DelayEvent, 1),
                             (DialogueEvent, '아뇨... 전 잘 모릅니다.', 'textures/characters/main_player_idle.png'),
                             (DialogueEvent, '...', 'textures/characters/Leader_idle.png'),
                             (DialogueEvent, '아 예, 그러면 뭐, 살펴 가세요.', 'textures/characters/Agent01_idle.png'),
                             (DialogueEvent, '...', 'textures/characters/main_player_idle.png'),
                             (DialogueEvent, '하...', 'textures/characters/main_player_idle.png'),
                             (DelayEvent, 1.5),
                             (SceneChangeEvent, GameOverScene, (16, 9))],
                         [NPC(9, 4, SpriteSheet_Constants.FACING_DOWN, 'textures/spritesheets/Leader.png'),
                          NPC(6, 7, SpriteSheet_Constants.FACING_UP, 'textures/spritesheets/Character01.png'),
                          NPC(9, 7, SpriteSheet_Constants.FACING_UP, 'textures/spritesheets/Character02.png'),
                          NPC(12, 7, SpriteSheet_Constants.FACING_UP, 'textures/spritesheets/Character03.png'),
                          NPC(7, 10, SpriteSheet_Constants.FACING_UP, 'textures/spritesheets/Character04.png'),
                          NPC(11, 10, SpriteSheet_Constants.FACING_UP, 'textures/spritesheets/Character05.png'),
                          NPC(5, 9, SpriteSheet_Constants.FACING_LEFT, 'textures/spritesheets/Agent01.png')])
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
