import pygame

import src.constants.gui_constants as GUIConstants
import src.constants.base_constants as Constants
from src.base.assets import assets
from src.i18n.i18n import i18n


class Option:
    def __init__(self):
        self.background_surface = pygame.Surface((Constants.WINDOW_WIDTH, Constants.WINDOW_HEIGHT), pygame.SRCALPHA)
        self.background_surface.set_alpha(GUIConstants.OPTIONS_UI_BACKGROUND_ALPHA)
        self.selection_level = 0
        self.selected_tab = 0

    def draw_background(self, screen, scene, main_player):
        for rect in GUIConstants.OPTIONS_UI_RECTS:
            self.background_surface.fill(GUIConstants.OPTIONS_UI_BACKGROUND_COLOR, rect)

    def change_selected_tab(self, scene, delta):
        self.selected_tab += delta
        self.selected_tab %= len(GUIConstants.OPTIONS_UI_TAB_IDS)
        if GUIConstants.OPTIONS_UI_TAB_IDS[self.selected_tab] == 'save' and not scene.can_save:
            self.selected_tab += delta // abs(delta)
            self.selected_tab %= len(GUIConstants.OPTIONS_UI_TAB_IDS)

    def draw_menu_texts(self, screen, scene, main_player):
        for idx, tab_id in enumerate(GUIConstants.OPTIONS_UI_TAB_IDS):
            label = assets.get_asset(GUIConstants.OPTIONS_UI_FONT_FILENAME, GUIConstants.OPTIONS_UI_FONT_SIZE).render(
                i18n.get_string_from_id(tab_id), GUIConstants.TEXT_ANTI_ALIASING,
                GUIConstants.OPTIONS_UI_DISABLED_TEXT_COLOR if not scene.can_save and tab_id == 'save' else GUIConstants.OPTIONS_UI_TEXT_COLOR)
            screen.blit(label, (
                GUIConstants.OPTIONS_UI_MENU_TEXT_START_CORNER[0],
                GUIConstants.OPTIONS_UI_MENU_TEXT_START_CORNER[
                    1] + GUIConstants.OPTIONS_UI_MENU_TEXT_LINE_HEIGHT * idx))

    def update(self, screen, scene, main_player):
        self.background_surface.fill((0, 0, 0, 0))
        self.draw_background(screen, scene, main_player)
        self.background_surface.fill(GUIConstants.OPTIONS_UI_SELECTION_COLOR,
                                     pygame.Rect((GUIConstants.OPTIONS_UI_SELECTION_CORNER[0],
                                                  GUIConstants.OPTIONS_UI_SELECTION_CORNER[
                                                      1] + self.selected_tab * GUIConstants.OPTIONS_UI_MENU_TEXT_LINE_HEIGHT,
                                                  GUIConstants.OPTIONS_UI_SELECTION_WIDTH,
                                                  GUIConstants.OPTIONS_UI_MENU_TEXT_LINE_HEIGHT)))
        screen.blit(self.background_surface, (0, 0))
        self.draw_menu_texts(screen, scene, main_player)
