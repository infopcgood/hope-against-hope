from src.characters.character import Character
from src.gui.dialogue import Dialogue


class Player(Character):
    dialogue_active = None
    # event system is added here.
    def update(self, screen, scene, main_player, dt):
        super().update(screen, scene, main_player, dt)

    
    def stop(self, screen, scene, main_player):
        super().stop(screen, scene, main_player)
        if scene.event_tiles[(main_player.tile_y, main_player.tile_x)]:
            scene.event_tiles[(main_player.tile_y, main_player.tile_x)](screen, main_player)
        if scene.dialogue_tiles[(main_player.tile_y, main_player.tile_x)]:
            if Player.dialogue_active:
                Player.dialogue_active.hide(screen, scene, main_player)
                Player.dialogue_active = None
            Player.dialogue_active = Dialogue(*scene.dialogue_tiles[(main_player.tile_y, main_player.tile_x)])
            Player.dialogue_active.show(screen, scene, main_player)
