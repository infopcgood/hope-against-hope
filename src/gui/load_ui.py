import json

import pygame

import src.constants.base_constants as Constants
import src.constants.gui_constants as GUIConstants
from src.base.assets import assets
from src.base.save import save
from src.i18n.i18n import i18n


# UI class for loading scenes, slightly modified version of src/gui/option.py
class LoadUI:
    def __init__(self):
        # set variables
        self.background_surface = pygame.Surface((Constants.WINDOW_WIDTH, Constants.WINDOW_HEIGHT), pygame.SRCALPHA)
        self.background_surface.set_alpha(GUIConstants.OPTIONS_UI_BACKGROUND_ALPHA)
        self.selection_level = 1
        self.selected_tab = 1
        self.sub_selection = 0

    # draw transparent background
    def draw_background(self, screen, scene, main_player):
        for rect in GUIConstants.OPTIONS_UI_RECTS:
            self.background_surface.fill(GUIConstants.OPTIONS_UI_BACKGROUND_COLOR, rect)

    # change selection with amount of delta
    def change_selection(self, delta):
        self.sub_selection += delta
        self.sub_selection %= GUIConstants.OPTIONS_UI_TAB_OPTIONS[1]

    # trigger event from selection
    def trigger_event(self, screen, scene, main_player):
        save.load_data = save.load_data_from_file(f'save_{self.sub_selection + 1:02}.gsvf')
        save.load_needed = True

    # draw menu texts
    def draw_menu_texts(self, screen, scene, main_player):
        # load save files and then draw titles of it
        for idx, tab_id in enumerate(['load']):
            label = assets.get_asset(GUIConstants.OPTIONS_UI_FONT_FILENAME, GUIConstants.OPTIONS_UI_FONT_SIZE).render(
                i18n.get_string_from_id('cannot_save' if not scene.can_save and tab_id == 'save' else tab_id),
                GUIConstants.TEXT_ANTI_ALIASING,
                GUIConstants.OPTIONS_UI_DISABLED_TEXT_COLOR if not scene.can_save and tab_id == 'save' else GUIConstants.OPTIONS_UI_TEXT_COLOR)
            screen.blit(label, (
                GUIConstants.OPTIONS_UI_MENU_TEXT_START_CORNER[0],
                GUIConstants.OPTIONS_UI_MENU_TEXT_START_CORNER[
                    1] + GUIConstants.OPTIONS_UI_MENU_TEXT_LINE_HEIGHT * idx))

    # draw submenus but fixed to draw load menu
    def draw_submenus(self, screen, scene, main_player):
        # open save datas data
        save_time_file = open('save_datas.json', 'r')
        save_time_json = dict(json.load(save_time_file))
        save_time_file.close()
        if self.selection_level == 1:  # always true
            # draw selection rect
            screen.fill(GUIConstants.OPTIONS_UI_SELECTION_COLOR,
                        pygame.Rect((GUIConstants.OPTIONS_UI_CONTENT_START_CORNER[0] - 10,
                                     GUIConstants.OPTIONS_UI_CONTENT_START_CORNER[1] - 10 + (
                                         self.sub_selection) * GUIConstants.OPTIONS_UI_SAVE_MENU_HEIGHT,
                                     GUIConstants.OPTIONS_UI_CONTENT_SELECTION_WIDTH,
                                     GUIConstants.OPTIONS_UI_SAVE_MENU_HEIGHT)))
        # draw label for each save
        for idx in range(Constants.SAVE_COUNT):
            save_title_label = assets.get_asset(GUIConstants.OPTIONS_UI_FONT_FILENAME,
                                                GUIConstants.OPTIONS_UI_FONT_SIZE).render(
                i18n.get_string_from_id('save_file_preposition') + f'{idx + 1:02}',
                GUIConstants.TEXT_ANTI_ALIASING, GUIConstants.OPTIONS_UI_TEXT_COLOR)
            screen.blit(save_title_label, (GUIConstants.OPTIONS_UI_CONTENT_START_CORNER[0],
                                           GUIConstants.OPTIONS_UI_CONTENT_START_CORNER[
                                               1] + GUIConstants.OPTIONS_UI_SAVE_MENU_HEIGHT * idx))
            save_time_label = assets.get_asset(GUIConstants.OPTIONS_UI_FONT_FILENAME,
                                               GUIConstants.OPTIONS_UI_FONT_SIZE - 2).render(
                '  ' + save_time_json[f'save_{idx + 1:02}.gsvf'],
                GUIConstants.TEXT_ANTI_ALIASING, GUIConstants.OPTIONS_UI_TEXT_COLOR)
            screen.blit(save_time_label, (GUIConstants.OPTIONS_UI_CONTENT_START_CORNER[0],
                                          GUIConstants.OPTIONS_UI_CONTENT_START_CORNER[
                                              1] + GUIConstants.OPTIONS_UI_SAVE_MENU_HEIGHT * (idx + 0.5)))

    # update and blit the contents
    def update(self, screen, scene, main_player):
        # draw background
        self.background_surface.fill((0, 0, 0, 0))
        self.draw_background(screen, scene, main_player)
        screen.blit(self.background_surface, (0, 0))
        # draw menu selection
        screen.fill(
            GUIConstants.OPTIONS_UI_SELECTION_COLOR if self.selection_level == 0 else GUIConstants.OPTIONS_UI_LIGHT_SELECTION_COLOR,
            pygame.Rect((GUIConstants.OPTIONS_UI_SELECTION_CORNER[0],
                         GUIConstants.OPTIONS_UI_SELECTION_CORNER[
                             1] + 0 * GUIConstants.OPTIONS_UI_MENU_TEXT_LINE_HEIGHT,
                         GUIConstants.OPTIONS_UI_SELECTION_WIDTH,
                         GUIConstants.OPTIONS_UI_MENU_TEXT_LINE_HEIGHT)))
        # draw menu
        self.draw_menu_texts(screen, scene, main_player)
        self.draw_submenus(screen, scene, main_player)
