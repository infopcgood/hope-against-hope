"""Testing GUI module that contains TestingGUI class"""

import pygame
import src.constants.gui_constants as GUIConstants
from src.base.assets import assets


class TestingGUI:
    """gui for testing. it's honestly a show-off."""

    def __init__(self):
        pass

    def update(self, screen, main_player, movable_tiles, fps):
        """updates the GUI every frame"""
        tile_pos_label = assets.get_asset(GUIConstants.TESTING_GUI_FONT_FILENAME,
                                          GUIConstants.TESTING_GUI_FONT_SIZE).render(
            f'Tile Pos: ({main_player.tile_x}, {main_player.tile_y})', GUIConstants.TEXT_ANTI_ALIASING, (255, 255, 255))
        real_pos_label = assets.get_asset(GUIConstants.TESTING_GUI_FONT_FILENAME,
                                          GUIConstants.TESTING_GUI_FONT_SIZE).render(
            f'Real Pos: ({main_player.x:.2f}, {main_player.y:.2f})', GUIConstants.TEXT_ANTI_ALIASING, (255, 255, 255))
        movable_tiles_label = assets.get_asset(GUIConstants.TESTING_GUI_FONT_FILENAME,
                                               GUIConstants.TESTING_GUI_FONT_SIZE).render(
            f'Speed: ({main_player.vx:.2f}, {main_player.vy:.2f})',
            GUIConstants.TEXT_ANTI_ALIASING, (255, 255, 255))
        fps_label = assets.get_asset(GUIConstants.TESTING_GUI_FONT_FILENAME, GUIConstants.TESTING_GUI_FONT_SIZE).render(
            f'FPS: {fps:.0f}', GUIConstants.TEXT_ANTI_ALIASING, (255, 255, 255))
        screen.blit(tile_pos_label, (16, 8))
        screen.blit(real_pos_label, (16, 40))
        screen.blit(movable_tiles_label, (16, 72))
        screen.blit(fps_label, (16, 104))
