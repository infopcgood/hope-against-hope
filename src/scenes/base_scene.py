"""Base Scene only used in testing"""
from collections import defaultdict
import pygame

from src.base.assets import assets
from src.characters.npc import NPC
from src.events.delay_event import DelayEvent
from src.scenes.scene import Scene
import src.scenes.start_scene as start_scene
from src.events.scene_change_event import SceneChangeEvent
import src.constants.spritesheet_constants as SpriteSheet_Constants
from src.characters.character import Character
from src.characters.player import Player
from src.events.dialogue_event import DialogueEvent
from src.events.wait_until_event import WaitUntilEvent
from src.events.basic_function_event import BasicFunctionEvent


class BaseScene(Scene):
    """Base scene only used in testing"""

    def __init__(self, start_tile_x=13, start_tile_y=10):  # warning ignored because everything has to be redefined
        self.bgm_name = None
        self.background_image = assets.get_asset("textures/map/basic_background_with_houses.png")
        self.upper_layer_image = assets.get_asset("textures/upper_layer/basic_tree_upper_layer.png")
        self.start_tile_x = start_tile_x
        self.start_tile_y = start_tile_y
        self.npcs = [
            NPC(32, 10, SpriteSheet_Constants.FACING_LEFT, 'textures/spritesheets/demo2.png', [DialogueEvent('뭘 봐?')])]
        self.event_tiles = defaultdict(list)
        # self.event_tiles[(10,1)] = [DialogueEvent('그런데, 그것이 과연 완벽한 진실이라고 장담할 수 있을까? 나는 그렇다고 생각하지 않아.',),DialogueEvent(',,,,,,,,,,,,,,이건빠르고저건느리네요..','textures/characters/test.png',),BasicFunctionEvent(self.function_04),DelayEvent(5),DialogueEvent('일어나세요 용사님!!',),BasicFunctionEvent(self.function_05)]
        # self.event_tiles[(11,1)] = [BasicFunctionEvent(self.function_01),]
        # self.event_tiles[(11,2)] = [BasicFunctionEvent(self.function_02),]
        # self.event_tiles[(11,3)] = [BasicFunctionEvent(self.function_03),]
        # self.event_tiles[(11,4)] = [SceneChangeEvent(Scene()),]
        self.movable_tiles = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.scale_screen = True

    def load(self, screen, main_player):
        super().load(screen, main_player)
        self.event_tiles[(10, 1)] = [(SceneChangeEvent(start_scene.StartScene(32, 10)),
                                      "main_player.facing == SpriteSheet_Constants.FACING_LEFT")]
        self.event_tiles[(8, 1)] = [(SceneChangeEvent(start_scene.StartScene(32, 8)),
                                     "main_player.facing == SpriteSheet_Constants.FACING_LEFT")]
        self.event_tiles[(9, 1)] = [(SceneChangeEvent(start_scene.StartScene(32, 9)),
                                     "main_player.facing == SpriteSheet_Constants.FACING_LEFT")]
        self.event_tiles[(10, 2)] = [DialogueEvent("답장을 기대하지 않는 게 좋을 거야."), BasicFunctionEvent(self.npc01_move),
                                     BasicFunctionEvent(self.npc01_move), BasicFunctionEvent(self.npc01_move),
                                     BasicFunctionEvent(self.npc01_move), BasicFunctionEvent(self.npc01_move),
                                     WaitUntilEvent("not args[0].is_moving", self.npcs[0]), DialogueEvent("왜지?"),
                                     BasicFunctionEvent(self.shake_screen), DelayEvent(2), DialogueEvent("????")]
        self.event_tiles[(8, 2)] = [(SceneChangeEvent(start_scene.StartScene(32, 8)),
                                     "main_player.facing == SpriteSheet_Constants.FACING_LEFT")]
        self.event_tiles[(9, 2)] = [(SceneChangeEvent(start_scene.StartScene(32, 9)),
                                     "main_player.facing == SpriteSheet_Constants.FACING_LEFT")]

    def npc01_move(self, screen, scene, main_player):
        """npc01 move"""
        self.npcs[0].move_one_tile(SpriteSheet_Constants.FACING_LEFT, screen, scene, main_player)

    def shake_screen(self, screen, scene, main_player):
        main_player.shake_screen = True
