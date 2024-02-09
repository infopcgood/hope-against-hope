import src.constants.base_constants as Constants
from src.events.basic_function_event import BasicFunctionEvent
from src.events.delay_event import DelayEvent
from src.events.dialogue_event import DialogueEvent
from src.events.scene_change_event import SceneChangeEvent
from src.scenes.scene import Scene
from src.scenes.scene_11 import Scene11


# i hate this code snippet so much.
def modify_scale(screen, scene, main_player):
    Constants.FOCUS_CAMERA_SCALE = 4 / 3


# gunshot scene.
class GunShotScene(Scene):
    def __init__(self, start_tile_x=16, start_tile_y=9):  # warning ignored because everything has to be redefined
        super().__init__(32, 18, start_tile_x, start_tile_y, "textures/map/black.png",
                         "textures/upper_layer/transparent.png", 'sounds/empty.wav', True,
                         True, False, False,
                         [(BasicFunctionEvent, modify_scale, tuple()), (DelayEvent, 3),
                          (DialogueEvent, '이런 비겁한, 총을 쓰다니...', 'textures/characters/main_player_idle.png'),
                          (DialogueEvent, '그나저나, 난 이렇게 죽는 걸까...', 'textures/characters/main_player_idle.png'),
                          (DialogueEvent, '사회에 남아있던 유일한 희망도...', 'textures/characters/main_player_idle.png'),
                          (DialogueEvent, '사람들은 다 잡혀갔겠지...', 'textures/characters/main_player_idle.png'),
                          (DialogueEvent, '어쩌면 이번이 마지막이었을지도 몰라.', 'textures/characters/main_player_idle.png'),
                          (DialogueEvent, '더 이상, 희망은 없을지도 모른다고.', 'textures/characters/main_player_idle.png'),
                          (DialogueEvent, '처음부터 잘못된 말이었어. 헛된 꿈이었다고.', 'textures/characters/main_player_idle.png'),
                          (DialogueEvent, '그래도 다시 일어날 수 있다면...', 'textures/characters/main_player_idle.png'),
                          (DialogueEvent, '한번쯤은 다시 꿔 보고 싶은 꿈...', 'textures/characters/main_player_idle.png'),
                          (DelayEvent, 2),
                          (DialogueEvent, '얜 왜 이렇게 잠꼬대가 심해?', 'textures/characters/GrandpaWang_idle.png'),
                          (DialogueEvent, '(...뭐지?)', 'textures/characters/main_player_idle.png'),
                          (DialogueEvent, '정신이 좀 드나?', 'textures/characters/GrandpaWang_idle.png'),
                          (DelayEvent, 0.5),
                          (SceneChangeEvent, Scene11, (16, 9))],
                         None)
        self.movable_tiles = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    def load(self, screen, main_player):
        super().load(screen, main_player)
        # hide player to make it feel like a cutscene
        main_player.visible = False
