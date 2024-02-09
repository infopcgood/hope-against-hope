import src.constants.spritesheet_constants as SpriteSheet_Constants
from src.characters.npc import NPC
from src.events.basic_function_event import BasicFunctionEvent
from src.events.delay_event import DelayEvent
from src.events.dialogue_event import DialogueEvent
from src.events.emote_event import NPCEmoteEvent
from src.events.scene_change_event import SceneChangeEvent
from src.scenes.scene import Scene
from src.scenes.scene_07 import Scene07


def interact_with(screen, scene, main_player, npc_idx):
    if scene.interacted_with[npc_idx] == False:
        scene.talked_cnt += 1
        scene.interacted_with[npc_idx] = True


def move_main_player_one_tile(screen, scene, main_player, direction):
    main_player.move_one_tile(direction, screen, scene, main_player)


def force_main_player_facing(screen, scene, main_player, facing):
    main_player.facing = facing


# 6th scene of game. It's getting boring now. Why do you need comments in the first place??
class Scene06(Scene):
    def __init__(self, start_tile_x=13, start_tile_y=10):
        # super init with long dialogue
        super().__init__(32, 18, start_tile_x, start_tile_y, "textures/map/hallway.png",
                         "textures/upper_layer/transparent.png", None, True,
                         True, True, True,
                         [(BasicFunctionEvent, force_main_player_facing, (SpriteSheet_Constants.FACING_RIGHT,)),
                          (DelayEvent, 2),
                          (DialogueEvent, '저랑 비슷한 생각을 가지고 계신다고요.', 'textures/characters/Leader_idle.png'),
                          (DialogueEvent, '네...', 'textures/characters/main_player_idle.png'),
                          (DialogueEvent, '흠...', 'textures/characters/Leader_idle.png'),
                          (DialogueEvent, '일단은 저희와 함께 투쟁해 보시겠어요?', 'textures/characters/Leader_idle.png'),
                          (DialogueEvent, '물론이죠. 그런데 하나 걱정되는 거는...', 'textures/characters/main_player_idle.png'), (
                              DialogueEvent, '...이 노력이 다 헛된 일이 되어 버릴까 하는 두려움?',
                              'textures/characters/main_player_idle.png'),
                          (DialogueEvent, '흠...', 'textures/characters/Leader_idle.png'),
                          (NPCEmoteEvent, SpriteSheet_Constants.EMOTE_THINK, 0), (DelayEvent, 1.75),
                          (DialogueEvent, '저도 그런 고민을 많이 했죠...', 'textures/characters/Leader_idle.png'),
                          (DialogueEvent, '그런데 모든 건 다 믿으면 되더라고요.', 'textures/characters/Leader_idle.png'),
                          (DialogueEvent, '희망이라는 건 사실, 되게 난해한 거잖아요.', 'textures/characters/Leader_idle.png'),
                          (DialogueEvent, '어느 순간은 내 앞에 바로 있는 것 같다가도,', 'textures/characters/Leader_idle.png'),
                          (DialogueEvent, '조금 이따가 바람처럼 사라져 버리고.', 'textures/characters/Leader_idle.png'),
                          (DialogueEvent, '약간 잠깐씩 찾아오는 순례자 느낌이랄까요.', 'textures/characters/Leader_idle.png'), (
                              DialogueEvent, '그런데 중요한 건, 희망을 잃으면 그 찾아오는 희망마저도 보이지 않는다는 거에요.',
                              'textures/characters/Leader_idle.png'),
                          (DialogueEvent, '그래서 우리는 언제나, 희망을 가지고 살아가야 하는 겁니다.', 'textures/characters/Leader_idle.png'),
                          (NPCEmoteEvent, SpriteSheet_Constants.EMOTE_THINK, 0), (DelayEvent, 1.75),
                          (DialogueEvent, '지금이야 많이 힘들고, 처음부터 쭉 힘들었지만...', 'textures/characters/Leader_idle.png'),
                          (DialogueEvent, '희망의 끈을 놓지 않는다면 반드시 희망은 찾아온다..?', 'textures/characters/main_player_idle.png'),
                          (DialogueEvent, '뭐 그런 느낌인 거죠.', 'textures/characters/Leader_idle.png'),
                          (DialogueEvent, '지금은 희망이 없어보일지라도, ', 'textures/characters/Leader_idle.png'),
                          (DialogueEvent, '언젠간 사회는 바뀔 겁니다.', 'textures/characters/Leader_idle.png'),
                          (DialogueEvent, '흠...', 'textures/characters/main_player_idle.png'),
                          (DialogueEvent, '좋은 말씀 감사합니다.', 'textures/characters/main_player_idle.png'),
                          (DialogueEvent, '천만에요. 날이 저물었으니 얼른 가보시죠.', 'textures/characters/Leader_idle.png'),
                          (DialogueEvent, '넵.', 'textures/characters/main_player_idle.png'),
                          (DialogueEvent, '(내일 다시 와봐야겠다.)', 'textures/characters/main_player_idle.png'),
                          (DelayEvent, 1), (SceneChangeEvent, Scene07, (14, 12))],
                         [NPC(17, 10, SpriteSheet_Constants.FACING_LEFT, 'textures/spritesheets/Leader.png')])
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
