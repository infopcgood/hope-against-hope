import pygame
import src.constants.gui_constants as GUIConstants

# gui for testing. it's honestly a show-off.
class TestingGUI:
    def __init__(self):
        pass
    
    def update(self, screen, main_player, movable_tiles):
        tile_pos_label = GUIConstants.TESTING_GUI_FONT.render(f'Tile Pos: ({main_player.tile_x}, {main_player.tile_y})', GUIConstants.TEXT_ANTI_ALIASING, (0, 0, 0))
        real_pos_label = GUIConstants.TESTING_GUI_FONT.render(f'Real Pos: ({main_player.x:.2f}, {main_player.y:.2f})', GUIConstants.TEXT_ANTI_ALIASING, (0, 0, 0))
        movable_tiles_label = GUIConstants.TESTING_GUI_FONT.render(f'Tile Info: movable[{main_player.tile_y}][{main_player.tile_x}] = {movable_tiles[main_player.tile_y][main_player.tile_x]}', GUIConstants.TEXT_ANTI_ALIASING, (0, 0, 0))
        screen.blit(tile_pos_label, (16,8))
        screen.blit(real_pos_label, (16,40))
        screen.blit(movable_tiles_label, (16,72))