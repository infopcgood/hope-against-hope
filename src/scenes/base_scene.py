"""Base Scene only used in testing"""
from collections import defaultdict
import pygame
from src.scenes.scene import Scene
import src.scenes.start_scene as start_scene
from src.events.scene_change_event import SceneChangeEvent
import src.constants.spritesheet_constants as SpriteSheet_Constants

class BaseScene(Scene):
    """Base scene only used in testing"""
    def __init__(self, start_tile_x = 13, start_tile_y = 10): # warning ignored because everything has to be redefined
        self.background_image = pygame.image.load("textures/map/basic_background_with_houses.png").convert_alpha()
        self.upper_layer_image = pygame.image.load("textures/upper_layer/basic_tree_upper_layer.png").convert_alpha()
        self.start_tile_x = start_tile_x
        self.start_tile_y = start_tile_y
        self.event_tiles = defaultdict(list)
        # self.event_tiles[(10,1)] = [DialogueEvent('그런데, 그것이 과연 완벽한 진실이라고 장담할 수 있을까? 나는 그렇다고 생각하지 않아.',),DialogueEvent(',,,,,,,,,,,,,,이건빠르고저건느리네요..','textures/characters/test.png',),BasicFunctionEvent(self.function_04),DelayEvent(5),DialogueEvent('일어나세요 용사님!!',),BasicFunctionEvent(self.function_05)]
        # self.event_tiles[(11,1)] = [BasicFunctionEvent(self.function_01),]
        # self.event_tiles[(11,2)] = [BasicFunctionEvent(self.function_02),]
        # self.event_tiles[(11,3)] = [BasicFunctionEvent(self.function_03),]
        # self.event_tiles[(11,4)] = [SceneChangeEvent(Scene()),]
        self.movable_tiles = [  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                [1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]  ]
    def load(self, screen, main_player):
        super().load(screen,main_player)
        self.event_tiles[(10,1)] = [(SceneChangeEvent(start_scene.StartScene(32,10)), "main_player.facing == SpriteSheet_Constants.FACING_LEFT")]
        self.event_tiles[(8,1)] = [(SceneChangeEvent(start_scene.StartScene(32,8)), "main_player.facing == SpriteSheet_Constants.FACING_LEFT")]
        self.event_tiles[(9,1)] = [(SceneChangeEvent(start_scene.StartScene(32,9)), "main_player.facing == SpriteSheet_Constants.FACING_LEFT")] 
    def function_01(self, screen, scene, main_player):
        """sample function 01"""
        main_player.anim = SpriteSheet_Constants.ACTION_SHOOTING
        main_player.playing_anim = True
    def function_02(self, screen, scene, main_player):
        """sample function 02"""
        main_player.anim = SpriteSheet_Constants.ACTION_SLASHING
        main_player.playing_anim = True
    def function_03(self, screen, scene, main_player):
        """sample function 03"""
        main_player.anim = SpriteSheet_Constants.ACTION_THRUSTING
        main_player.playing_anim = True
    def function_04(self, screen, scene, main_player):
        """sample function 04"""
        main_player.anim = SpriteSheet_Constants.ACTION_DEAD
        main_player.playing_anim = True
        main_player.is_paralyzed = True
    def function_05(self, screen, scene, main_player):
        """sample function 05"""
        main_player.anim = SpriteSheet_Constants.ACTION_WALKING
        main_player.playing_anim = False
        main_player.is_paralyzed = False
