"""Player method containing Player class"""

from src.characters.character import Character
from src.gui.dialogue import Dialogue
from src.events.dialogue_event import DialogueEvent
from src.events.basic_function_event import BasicFunctionEvent
from src.events.delay_event import DelayEvent
from src.events.scene_change_event import SceneChangeEvent
from src.events.wait_until_event import WaitUntilEvent
import src.constants.base_constants as Constants
import src.constants.tilemap_constants as TileMap_Constants
import src.constants.spritesheet_constants as SpriteSheet_Constants


class Player(Character):
    """Player class that inherits Character"""

    def __init__(self, tile_x=TileMap_Constants.TILEMAP_WIDTH // 2, tile_y=TileMap_Constants.TILEMAP_HEIGHT // 2,
                 facing=SpriteSheet_Constants.FACING_RIGHT, spritesheet_path='textures/spritesheets/demo.png'):
        self.event_active = None
        self.event_needs_to_be_initialized = False
        self.events_waiting = []
        self.scene_needs_to_be_changed = False
        self.scene_waiting = None
        self.shake_screen = False
        super().__init__(tile_x, tile_y, facing, spritesheet_path)

    ## event system is added here
    # when stopping, check if tile has designated dialogue
    def stop(self, screen, scene, main_player):
        super().stop(screen, scene, main_player)
        self.update_event_system(screen, scene, main_player)

    def activate_next_event(self, screen, scene, main_player):
        """activate next event"""
        if not self.events_waiting:
            return
        if isinstance(self.events_waiting[0], tuple):
            if not eval(self.events_waiting[0][1]):
                self.events_waiting = self.events_waiting[1:]
                if self.events_waiting:
                    self.activate_next_event(screen, scene, main_player)
                return
            self.events_waiting[0] = self.events_waiting[0][0]
        self.event_active = self.events_waiting[0]
        self.events_waiting = self.events_waiting[1:]
        self.event_needs_to_be_initialized = True

    def add_event_queue(self, events):
        """add events to event queue"""
        self.events_waiting = self.events_waiting + events

    def update_event_system(self, screen, scene, main_player):
        """update active & waiting dialogues"""
        # check if tile has event
        if not self.event_active and not self.events_waiting:
            self.add_event_queue(scene.event_tiles[(main_player.tile_y, main_player.tile_x)])
        # check if event is finished and another event is waiting
        if self.event_active and self.event_active.object.finished:
            if isinstance(self.event_active, DialogueEvent) and self.event_active.object.finished:
                self.event_active.object.hide(screen, scene, main_player)
            if self.events_waiting:
                self.activate_next_event(screen, scene, main_player)
            else:
                self.event_active = None
        # check if there is no dialogue at all
        elif not self.event_active:
            if self.events_waiting:
                self.activate_next_event(screen, scene, main_player)
            else:
                self.event_active = None
        if self.event_needs_to_be_initialized:
            self.event_needs_to_be_initialized = False
            if isinstance(self.event_active, DialogueEvent):
                self.event_active.object = Dialogue(*self.event_active.args)
                self.event_active.object.show(screen, scene, main_player)
            elif isinstance(self.event_active, BasicFunctionEvent):
                self.event_active.object.run(screen, scene, main_player)
            elif isinstance(self.event_active, DelayEvent):
                self.event_active.object.start()
            elif isinstance(self.event_active, SceneChangeEvent):
                self.event_active.object.run()
                self.scene_needs_to_be_changed = True
                self.scene_waiting = self.event_active.object.desired_scene
            elif isinstance(self.event_active, WaitUntilEvent):
                pass
            else:
                raise NotImplementedError
