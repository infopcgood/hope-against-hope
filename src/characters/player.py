"""Player method containing Player class"""

from src.characters.character import Character
from src.gui.dialogue import Dialogue

class Player(Character):
    """Player class that inherits Character"""
    dialogue_active = None
    dialogues_waiting = []
    ## event system is added here
    # when stopping, check if tile has designated dialogue
    def stop(self, screen, scene, main_player):
        super().stop(screen, scene, main_player)
        self.update_dialogues(screen, scene, main_player)
    def update_dialogues(self, screen, scene, main_player):
        """update active & waiting dialogues"""
        # check if tile has event
        if scene.event_tiles[(main_player.tile_y, main_player.tile_x)]:
            scene.event_tiles[(main_player.tile_y, main_player.tile_x)](screen, main_player)
        # check if tile has dialogue
        if scene.dialogue_tiles[(main_player.tile_y, main_player.tile_x)] and not Player.dialogue_active:
            Player.dialogues_waiting = Player.dialogues_waiting + scene.dialogue_tiles[(main_player.tile_y, main_player.tile_x)]
        # check if dialogue is finished and another dialogue is waiting
        if Player.dialogue_active and Player.dialogue_active.animation_finished:
            Player.dialogue_active.hide(screen, scene, main_player)
            if Player.dialogues_waiting:
                Player.dialogue_active = Dialogue(*Player.dialogues_waiting[0])
                Player.dialogue_active.show(screen, scene, main_player)
                Player.dialogues_waiting = Player.dialogues_waiting[1:]
            else:
                Player.dialogue_active = None
        # check if there is no dialogue at all
        elif not Player.dialogue_active:
            if Player.dialogues_waiting:
                Player.dialogue_active = Dialogue(*Player.dialogues_waiting[0])
                Player.dialogue_active.show(screen, scene, main_player)
                Player.dialogues_waiting = Player.dialogues_waiting[1:]
            else:
                Player.dialogue_active = None
