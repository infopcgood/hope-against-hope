from src.characters.character import Character
from src.gui.dialogue import Dialogue


class Player(Character):
    dialogue_active = None
    dialogues_waiting = []
    dialogue_was_just_cancelled = False
    # event system is added here.
    def update(self, screen, scene, main_player, dt):
        super().update(screen, scene, main_player, dt)

    
    def stop(self, screen, scene, main_player):
        super().stop(screen, scene, main_player)
        self.update_dialogues(screen, scene, main_player)
    
    def update_dialogues(self, screen, scene, main_player):
        if scene.event_tiles[(main_player.tile_y, main_player.tile_x)]:
            scene.event_tiles[(main_player.tile_y, main_player.tile_x)](screen, main_player)
        if scene.dialogue_tiles[(main_player.tile_y, main_player.tile_x)] and not Player.dialogue_active:
            Player.dialogues_waiting = Player.dialogues_waiting + scene.dialogue_tiles[(main_player.tile_y, main_player.tile_x)]
        if Player.dialogue_active and Player.dialogue_active.animation_finished:
            Player.dialogue_active.hide(screen, scene, main_player)
            Player.dialogue_was_just_cancelled = True
            if len(Player.dialogues_waiting):
                Player.dialogue_active = Dialogue(*Player.dialogues_waiting[0])
                Player.dialogue_active.show(screen, scene, main_player)
                Player.dialogues_waiting = Player.dialogues_waiting[1:]
            else:
                Player.dialogue_active = None
        elif not Player.dialogue_active:
            if len(Player.dialogues_waiting):
                Player.dialogue_active = Dialogue(*Player.dialogues_waiting[0])
                Player.dialogue_active.show(screen, scene, main_player)
                Player.dialogues_waiting = Player.dialogues_waiting[1:]
            else:
                Player.dialogue_active = None