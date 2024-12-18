import src.constants.spritesheet_constants as SpriteSheet_Constants
from src.battles.battle import Battle
from src.characters.character import Character
from src.events.basic_function_event import BasicFunctionEvent
from src.events.delay_event import DelayEvent
from src.events.dialogue_event import DialogueEvent
from src.events.emote_event import PlayerEmoteEvent, NPCEmoteEvent
from src.events.scene_change_event import SceneChangeEvent
from src.events.void_event import VoidEvent
from src.events.wait_until_event import WaitUntilEvent
from src.gui.dialogue import Dialogue


# player class that adds event system and stuff.
class Player(Character):

    def __init__(self, tile_x=16, tile_y=9, facing=SpriteSheet_Constants.FACING_RIGHT,
                 spritesheet_path='textures/spritesheets/demo.png', max_hp=20):
        super().__init__(tile_x, tile_y, facing, spritesheet_path, max_hp)
        # initialize event system parameters
        self.event_active = None
        self.event_needs_to_be_initialized = False
        self.events_waiting = []
        self.scene_needs_to_be_changed = True
        self.scene_waiting = None
        # set etc parameters
        self.shake_screen = False
        self.power = 8

    # event system is added here
    # when stopping, check if tile has designated dialogue. only in Scene types of space, not battles (not tile based)
    def stop(self, screen, scene, main_player):
        super().stop(screen, scene, main_player)
        if not isinstance(scene, Battle):
            self.update_event_system(screen, scene, main_player)

    # activate next event that is queued
    def activate_next_event(self, screen, scene, main_player):
        if not self.events_waiting:
            return
        # check if event has a condition
        if isinstance(self.events_waiting[0][0], tuple):
            # check if there are arguments
            if len(self.events_waiting[0]) >= 3:
                args = self.events_waiting[0][2]
            else:
                args = None
            # check for condition
            if not eval(self.events_waiting[0][1]):
                self.events_waiting = self.events_waiting[1:]
                if self.events_waiting:
                    self.activate_next_event(screen, scene, main_player)
                return
            self.events_waiting[0] = self.events_waiting[0][0]
        # update variables
        self.event_active = self.events_waiting[0][0](*self.events_waiting[0][1:])
        self.events_waiting = self.events_waiting[1:]
        self.event_needs_to_be_initialized = True

    # add events to event queue
    def add_event_queue(self, screen, scene, main_player, events=None):
        if events is None:
            events = []
        # add event to queue except VoidEvent
        self.events_waiting = [event for event in self.events_waiting if not isinstance(event[0], VoidEvent)]
        events_unprocessed = events[:]
        # validate condition for each event
        for event in events_unprocessed:
            if isinstance(event[0], tuple) and len(event) >= 3:
                args = event[2]
            else:
                args = None
            if isinstance(event[0], tuple) and not eval(event[1]):
                events_unprocessed.remove(event)
            else:
                break
        events_stripped = events_unprocessed[:]
        # add VoidEvent for extra keypress
        self.events_waiting += events_stripped + [(VoidEvent,)] if events_stripped else []

    # update whole event system
    def update_event_system(self, screen, scene, main_player):
        # check if tile has event
        if not self.event_active and not self.events_waiting:
            self.add_event_queue(screen, scene, main_player,
                                 scene.event_tiles[(main_player.tile_y, main_player.tile_x)])
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
        # initialize events
        if self.event_needs_to_be_initialized:
            self.event_needs_to_be_initialized = False
            if isinstance(self.event_active, DialogueEvent):
                self.event_active.object = Dialogue(*self.event_active.args)
                self.event_active.object.show(screen, scene, main_player)
            elif isinstance(self.event_active, BasicFunctionEvent):
                self.event_active.object.run(screen, scene, main_player, self.event_active.args)
            elif isinstance(self.event_active, DelayEvent):
                self.event_active.object.start()
            elif isinstance(self.event_active, SceneChangeEvent):
                self.event_active.object.run()
                self.scene_needs_to_be_changed = True
                self.scene_waiting = self.event_active.object.desired_scene
            elif isinstance(self.event_active, PlayerEmoteEvent):
                self.event_active.object.run(main_player)
            elif isinstance(self.event_active, NPCEmoteEvent):
                self.event_active.object.run(scene.npcs[self.event_active.object.args[1]])
            elif isinstance(self.event_active, WaitUntilEvent):
                pass
            elif isinstance(self.event_active, VoidEvent):
                pass
            else:
                raise NotImplementedError
