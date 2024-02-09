import src.constants.spritesheet_constants as SpriteSheet_Constants
from src.characters.npc import NPC
from src.events.delay_event import DelayEvent
from src.events.dialogue_event import DialogueEvent
from src.events.scene_change_event import SceneChangeEvent
from src.scenes.ending_credit_scene import EndingCreditScene
from src.scenes.scene import Scene


def interact_with(screen, scene, main_player, npc_idx):
    if not scene.interacted_with[npc_idx]:
        scene.talked_cnt += 1
        scene.interacted_with[npc_idx] = True


def move_main_player_one_tile(screen, scene, main_player, direction):
    main_player.move_one_tile(direction, screen, scene, main_player)


# scene 16
class Scene16(Scene):

    def __init__(self, start_tile_x=13, start_tile_y=10):
        # call super init, celebrate victory dialogue
        super().__init__(32, 18, start_tile_x, start_tile_y, "textures/map/poor_village.png",
                         "textures/upper_layer/transparent.png", 'sounds/bgm/happy.mp3', True,
                         True, True, True,
                         [(DelayEvent, 2.75), (DialogueEvent, '여러분 안녕하세요, 잠시 안내말씀 드리겠습니다.'),
                          (DialogueEvent, '더 이상 여러분은 SCALE의 지배 밑에서 살 필요가 없습니다.'),
                          (DialogueEvent, '현 시간부로 SCALE은 이곳에서 철수했습니다.'),
                          (DialogueEvent, '설마...', 'textures/characters/Leader_idle.png'),
                          (DialogueEvent, '허허...', 'textures/characters/GrandpaWang_idle.png'),
                          (DialogueEvent, '그리고 앞으로도 우리는 이런 불공평한 사회에 저항할 것입니다.'),
                          (DialogueEvent, '희망은 계속되어야 하기 때문이죠.'),
                          (DialogueEvent, '어둠 속에서도 전구를 밝혀줄 사람을,'),
                          (DialogueEvent, '절망 속에서 희망을 찾을 사람을,'),
                          (DialogueEvent, '한겨울 밤에도 창을 열고, 별을 노래할 사람을 위해서...'),
                          (DelayEvent, 2),
                          (SceneChangeEvent, EndingCreditScene, (16, 9))],
                         [
                             NPC(20, 9, SpriteSheet_Constants.FACING_LEFT, 'textures/spritesheets/Character02.png',
                                 []),
                             NPC(16, 5, SpriteSheet_Constants.FACING_DOWN, 'textures/spritesheets/Character03.png',
                                 []),
                             NPC(4, 4, SpriteSheet_Constants.FACING_DOWN, 'textures/spritesheets/Character04.png',
                                 []),
                             NPC(28, 1, SpriteSheet_Constants.FACING_UP, 'textures/spritesheets/Character05.png', []),
                             NPC(23, 12, SpriteSheet_Constants.FACING_UP, 'textures/spritesheets/Character01.png',
                                 [])])
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

    def load(self, screen, main_player):
        super().load(screen, main_player)
        main_player.visible = False

    def add_event_system(self, screen, main_player):
        pass
