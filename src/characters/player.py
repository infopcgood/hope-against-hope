"""Player method containing Player class"""

from src.characters.character import Character
from src.gui.dialogue import Dialogue
from src.events.dialogue_event import DialogueEvent
from src.events.basic_function_event import BasicFunctionEvent
from src.events.delay_event import DelayEvent
from src.events.scene_change_event import SceneChangeEvent
import src.constants.base_constants as Constants
import src.constants.spritesheet_constants as SpriteSheet_Constants

class Player(Character):
    """Player class that inherits Character"""
    event_active = None
    event_needs_to_be_initialized = False
    events_waiting = []
    scene_needs_to_be_changed = False
    scene_waiting = None
    ## event system is added here
    # when stopping, check if tile has designated dialogue
    def stop(self, screen, scene, main_player):
        super().stop(screen, scene, main_player)
        self.update_event_system(screen, scene, main_player)
    def activate_next_event(self, screen, scene, main_player):
        """activate next event"""
        if not Player.events_waiting:
            return
        if isinstance(Player.events_waiting[0], tuple):
            if not eval(Player.events_waiting[0][1]):
                Player.events_waiting = Player.events_waiting[1:]
                if Player.events_waiting:
                    self.activate_next_event(screen, scene, main_player)
                return
            Player.events_waiting[0] = Player.events_waiting[0][0]
        Player.event_active = Player.events_waiting[0]
        Player.events_waiting = Player.events_waiting[1:]
        Player.event_needs_to_be_initialized = True
    def update_event_system(self, screen, scene, main_player):
        """update active & waiting dialogues"""
        # check if tile has event
        if not Player.event_active and not Player.events_waiting:
            Player.events_waiting = Player.events_waiting + scene.event_tiles[(main_player.tile_y, main_player.tile_x)]
        # check if event is finished and another event is waiting
        if Player.event_active and Player.event_active.object.finished:
            if isinstance(Player.event_active, DialogueEvent) and Player.event_active.object.finished:
                Player.event_active.object.hide(screen, scene, main_player)
            if Player.events_waiting:
                self.activate_next_event(screen, scene, main_player)
            else:
                Player.event_active = None
        # check if there is no dialogue at all
        elif not Player.event_active:
            if Player.events_waiting:
                self.activate_next_event(screen, scene, main_player)
            else:
                Player.event_active = None
        if Player.event_needs_to_be_initialized:
            Player.event_needs_to_be_initialized = False
            if isinstance(Player.event_active, DialogueEvent):
                Player.event_active.object = Dialogue(*Player.event_active.args)
                Player.event_active.object.show(screen, scene, main_player)
            elif isinstance(Player.event_active, BasicFunctionEvent):
                Player.event_active.object.run(screen, scene, main_player)
            elif isinstance(Player.event_active, DelayEvent):
                Player.event_active.object.start()
            elif isinstance(Player.event_active, SceneChangeEvent):
                Player.event_active.object.run()
                Player.scene_needs_to_be_changed = True
                Player.scene_waiting = Player.event_active.object.desired_scene
            else:
                raise NotImplementedError
