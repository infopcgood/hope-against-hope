import src.constants.spritesheet_constants as SpriteSheet_Constants
from src.characters.npc import NPC
from src.events.basic_function_event import BasicFunctionEvent
from src.events.delay_event import DelayEvent
from src.events.dialogue_event import DialogueEvent
from src.events.emote_event import NPCEmoteEvent
from src.events.scene_change_event import SceneChangeEvent
from src.scenes.scene import Scene
from src.scenes.scene_12 import Scene12


def move_main_player_one_tile(screen, scene, main_player, direction):
    main_player.move_one_tile(direction, screen, scene, main_player)


def set_anim_of_npc(screen, scene, main_player, npc_idx, anim):
    scene.npcs[npc_idx].anim = anim
    scene.npcs[npc_idx].playing_anim = True
    scene.npcs[npc_idx].anim_index = SpriteSheet_Constants.ACTION_INDEX_CNT[anim] - 1


def set_anim_of_player(screen, scene, main_player, anim):
    main_player.anim = anim
    main_player.playing_anim = True
    main_player.anim_index = SpriteSheet_Constants.ACTION_INDEX_CNT[anim] - 1


# 11th scene of game.
class Scene11(Scene):

    def __init__(self, start_tile_x=16, start_tile_y=9):
        # super init with long dialogue
        super().__init__(32, 18, start_tile_x, start_tile_y, "textures/map/shelter_positive.png",
                         "textures/upper_layer/transparent.png", 'sounds/bgm/hopeful.mp3', True,
                         True, False, True,
                         [(BasicFunctionEvent, set_anim_of_player, (SpriteSheet_Constants.ACTION_DEAD,)),
                          (DelayEvent, 2),
                          (DialogueEvent, '자네 이틀 동안이나 여기서 사경을 헤맸어.', 'textures/characters/GrandpaWang_idle.png'),
                          (DialogueEvent, '도대체 뭘 하다가 총에 맞은 거야?', 'textures/characters/GrandpaWang_idle.png'),
                          (DialogueEvent, '...', 'textures/characters/main_player_idle.png'),
                          (DialogueEvent, '이 도시에서 총을 가지고 있는 사람들은...', 'textures/characters/GrandpaWang_idle.png'),
                          (DialogueEvent, 'SCALE 놈들밖에 없죠.', 'textures/characters/Character04_idle.png'),
                          (NPCEmoteEvent, SpriteSheet_Constants.EMOTE_QUESTION, 0),
                          (DelayEvent, 1.75),
                          (DialogueEvent, '...SCALE?', 'textures/characters/GrandpaWang_idle.png'),
                          (DialogueEvent, '뭐, 이번에 같이 무슨 운동 하다가 걸렸나 보죠.', 'textures/characters/Character04_idle.png'),
                          (DialogueEvent, '아마 감옥에서 몇 년 썩을 정도의 죄목이에요.', 'textures/characters/Character04_idle.png'),
                          (DialogueEvent, '안 잡혀간 게 다행이죠 뭐, 죽을 줄 알고 놔둔 거 같아 보이는데.',
                           'textures/characters/Character04_idle.png'),
                          (DialogueEvent, '...사실이에요.', 'textures/characters/main_player_idle.png'),
                          (DialogueEvent, '우리 사회의 마지막 희망이나 좀 구경해 보려고 했었는데...',
                           'textures/characters/main_player_idle.png'),
                          (DialogueEvent, '...뭐, 이젠 그것도 사라졌겠죠.', 'textures/characters/main_player_idle.png'),
                          (DialogueEvent, '허허...', 'textures/characters/GrandpaWang_idle.png'),
                          (DialogueEvent, '내가 지난번에 너무 부정적인 얘기만 했나 보군.', 'textures/characters/GrandpaWang_idle.png'),
                          (DialogueEvent, '나도 한창 어릴 때는 자네랑 같은 꿈을 꿨어.', 'textures/characters/GrandpaWang_idle.png'),
                          (DialogueEvent, '물론 난 자네보다 인내심이 한참 부족했지. 노력도.', 'textures/characters/GrandpaWang_idle.png'),
                          (DialogueEvent, '그래서, 새로 해 보라는 건가요?', 'textures/characters/main_player_idle.png'),
                          (DialogueEvent, '이미 희망은 사라졌어요. 그냥 없다고요. 우리는 그냥 여기서 이렇게 썩다가...',
                           'textures/characters/main_player_idle.png'),
                          (DialogueEvent, '...죽어갈 거에요.', 'textures/characters/main_player_idle.png'),
                          (DialogueEvent, '총 맞아 죽을 뻔 하더니 또 이번엔 중2병까지 걸린 거야?',
                           'textures/characters/Character04_idle.png'),
                          (DialogueEvent, '뭐?', 'textures/characters/main_player_idle.png'),
                          (
                              DialogueEvent, '너무 그렇게 말하진 말게. 자네라면 충분히 할 수 있어.',
                              'textures/characters/GrandpaWang_idle.png'),
                          (DialogueEvent, '한 번 목표가 정해지면 끝까지 가보려는 사람들은 말이야...',
                           'textures/characters/GrandpaWang_idle.png'),
                          (DialogueEvent, '...그 과정 속에서, 어떤 고통도 이겨내고 감수하고 버텨내곤 하지.',
                           'textures/characters/GrandpaWang_idle.png'),
                          (DialogueEvent, '전구도 어둠 속에서 빛을 발하는 것처럼,',
                           'textures/characters/GrandpaWang_idle.png'),
                          (DialogueEvent, '희망도 외로움과 절망 속에서 빛나는 법이야.',
                           'textures/characters/GrandpaWang_idle.png'),
                          (DialogueEvent, '자네는 그런 어둠 속에서 전구를 끼워넣는 사람이 되었으면 하네.',
                           'textures/characters/GrandpaWang_idle.png'),
                          (DialogueEvent, '어쩌면 그게 마지막 전구일지도 모르니까.',
                           'textures/characters/GrandpaWang_idle.png'),
                          (DialogueEvent, '...',
                           'textures/characters/main_player_idle.png'),
                          (DialogueEvent, '너보고 뭐라도 해 보라는 소리잖아, 멍청아!',
                           'textures/characters/Character04_idle.png'),
                          (DialogueEvent, '야!', 'textures/characters/main_player_idle.png'), (DelayEvent, 1),
                          (SceneChangeEvent, Scene12, (16, 9))],
                         [NPC(17, 9, SpriteSheet_Constants.FACING_LEFT, 'textures/spritesheets/GrandpaWang.png'),
                          NPC(18, 9, SpriteSheet_Constants.FACING_LEFT, 'textures/spritesheets/Character04.png')])
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
