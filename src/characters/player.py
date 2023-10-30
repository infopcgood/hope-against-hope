from src.characters.character import Character

class Player(Character):
    def stop(self, screen, scene, main_player):
        super().stop(screen, scene, main_player)
        if scene.event_tiles[(main_player.tile_y, main_player.tile_x)]:
            scene.event_tiles[(main_player.tile_y, main_player.tile_x)](screen)