import pygame

class TestingGUI:
    def __init__(self, main_font):
        self.main_font = main_font
    
    def update(self, screen, main_player, movable_tiles):
        tile_pos_label = self.main_font.render(f'Tile Pos: ({main_player.tile_x}, {main_player.tile_y})', False, (0, 0, 0))
        real_pos_label = self.main_font.render(f'Real Pos: ({main_player.x:.2f}, {main_player.y:.2f})', False, (0, 0, 0))
        movable_tiles_label = self.main_font.render(f'Tile Info: movable[{main_player.tile_x}][{main_player.tile_y}] = {movable_tiles[main_player.tile_y][main_player.tile_x]}', False, (0, 0, 0))
        screen.blit(tile_pos_label, (16,8))
        screen.blit(real_pos_label, (16,40))
        screen.blit(movable_tiles_label, (16,72))