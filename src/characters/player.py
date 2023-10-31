"""Player method containing Player class"""

from src.characters.character import Character
from src.gui.dialogue import Dialogue
from src.events.dialogue_event import DialogueEvent
from src.events.basic_function_event import BasicFunctionEvent

class Player(Character):
    """Player class that inherits Character"""
    event_active = None
    event_needs_to_be_initialized = False
    events_waiting = []
    ## event system is added here
    # when stopping, check if tile has designated dialogue
    def stop(self, screen, scene, main_player):
        super().stop(screen, scene, main_player)
        self.update_event_system(screen, scene, main_player)
    def update_event_system(self, screen, scene, main_player):
        """update active & waiting dialogues"""
        # check if tile has event
        if not Player.event_active and not Player.events_waiting:
            Player.events_waiting = Player.events_waiting + scene.event_tiles[(main_player.tile_y, main_player.tile_x)]
        # check if event is finished and another event is waiting
        if Player.event_active:
            if isinstance(Player.event_active, DialogueEvent) and Player.event_active.object.finished:
                Player.event_active.object.hide(screen, scene, main_player)
            if Player.events_waiting:
                Player.event_active = Player.events_waiting[0]
                Player.events_waiting = Player.events_waiting[1:]
                Player.event_needs_to_be_initialized = True
            else:
                Player.event_active = None
        # check if there is no dialogue at all
        elif not Player.event_active:
            if Player.events_waiting:
                Player.event_active = Player.events_waiting[0]
                Player.events_waiting = Player.events_waiting[1:]
                Player.event_needs_to_be_initialized = True
            else:
                Player.event_active = None
        if Player.event_needs_to_be_initialized:
            Player.event_needs_to_be_initialized = False
            if isinstance(Player.event_active, DialogueEvent):
                Player.event_active.object = Dialogue(*Player.event_active.args)
                Player.event_active.object.show(screen, scene, main_player)
            elif isinstance(Player.event_active, BasicFunctionEvent):
                Player.event_active.object(screen, scene, main_player)
            else:
                raise NotImplementedError
