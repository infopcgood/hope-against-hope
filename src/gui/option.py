import json

import pygame

import src.constants.base_constants as Constants
import src.constants.gui_constants as GUIConstants
from src.base.assets import assets
from src.base.save import save
from src.i18n.i18n import i18n


# class that controls UI of option window system
class Option:
    def __init__(self):
        # set basic variables
        self.background_surface = pygame.Surface((Constants.WINDOW_WIDTH, Constants.WINDOW_HEIGHT), pygame.SRCALPHA)
        self.background_surface.set_alpha(GUIConstants.OPTIONS_UI_BACKGROUND_ALPHA)
        self.selection_level = 0
        self.selected_tab = 0
        self.sub_selection = 0
        self.last_saved_save_file_index = -1

    # draw transparent background
    def draw_background(self, screen, scene, main_player):
        for rect in GUIConstants.OPTIONS_UI_RECTS:
            self.background_surface.fill(GUIConstants.OPTIONS_UI_BACKGROUND_COLOR, rect)

    # change selected tab by delta
    def change_selected_tab(self, scene, delta):
        self.last_saved_save_file_index = -1
        self.selected_tab += delta
        self.selected_tab %= len(GUIConstants.OPTIONS_UI_TAB_IDS)
        # check if selected data is save tab and scene is not allowed to save
        if GUIConstants.OPTIONS_UI_TAB_IDS[self.selected_tab] == 'save' and not scene.can_save:
            self.selected_tab += delta // abs(delta)
            self.selected_tab %= len(GUIConstants.OPTIONS_UI_TAB_IDS)

    # change selection level by delta
    def change_selection_level(self, delta):
        self.selection_level += delta
        self.selection_level = max(0, self.selection_level)
        self.selection_level = min(GUIConstants.OPTIONS_UI_TAB_DEPTH[self.selected_tab] - 1, self.selection_level)
        self.sub_selection = min(GUIConstants.OPTIONS_UI_TAB_OPTIONS[self.selected_tab] - 1, self.sub_selection)

    # change selection by delta
    def change_selection(self, delta):
        self.sub_selection += delta
        self.sub_selection %= GUIConstants.OPTIONS_UI_TAB_OPTIONS[self.selected_tab]

    # trigger event based on selection
    def trigger_event(self, screen, scene, main_player):
        match GUIConstants.OPTIONS_UI_TAB_IDS[self.selected_tab]:
            case 'status':
                pass
            case 'save':
                save.save_data_to_file(f'save_{self.sub_selection + 1:02}.gsvf', scene, main_player)
                self.last_saved_save_file_index = self.sub_selection
            case 'quit':
                if self.sub_selection == 0:
                    exit(0)
                else:
                    self.change_selection_level(-1)
            case other:
                raise NotImplementedError

    # draw menu texts
    def draw_menu_texts(self, screen, scene, main_player):
        for idx, tab_id in enumerate(GUIConstants.OPTIONS_UI_TAB_IDS):
            label = assets.get_asset(GUIConstants.OPTIONS_UI_FONT_FILENAME, GUIConstants.OPTIONS_UI_FONT_SIZE).render(
                i18n.get_string_from_id('cannot_save' if not scene.can_save and tab_id == 'save' else tab_id),
                GUIConstants.TEXT_ANTI_ALIASING,
                GUIConstants.OPTIONS_UI_DISABLED_TEXT_COLOR if not scene.can_save and tab_id == 'save' else GUIConstants.OPTIONS_UI_TEXT_COLOR)
            screen.blit(label, (
                GUIConstants.OPTIONS_UI_MENU_TEXT_START_CORNER[0],
                GUIConstants.OPTIONS_UI_MENU_TEXT_START_CORNER[
                    1] + GUIConstants.OPTIONS_UI_MENU_TEXT_LINE_HEIGHT * idx))

    # draw submenus depending on selection
    def draw_submenus(self, screen, scene, main_player):
        match GUIConstants.OPTIONS_UI_TAB_IDS[self.selected_tab]:
            # if selected menu is status menu
            case 'status':
                # draw character profile pic
                screen.blit(assets.get_asset('textures/characters/main_player_idle.png'),
                            GUIConstants.OPTIONS_UI_CONTENT_START_CORNER)
                # draw data labels
                name_label = (assets.get_asset(GUIConstants.OPTIONS_UI_FONT_FILENAME, GUIConstants.OPTIONS_UI_FONT_SIZE)
                              .render(i18n.get_string_from_id('player_name'), GUIConstants.TEXT_ANTI_ALIASING,
                                      GUIConstants.OPTIONS_UI_TEXT_COLOR))
                screen.blit(name_label, (
                    GUIConstants.OPTIONS_UI_CONTENT_START_CORNER[0] + 176,
                    GUIConstants.OPTIONS_UI_CONTENT_START_CORNER[1]))
                hp_label = (assets.get_asset(GUIConstants.OPTIONS_UI_FONT_FILENAME, GUIConstants.OPTIONS_UI_FONT_SIZE)
                            .render(f' HP: {main_player.hp}/{main_player.max_hp}', GUIConstants.TEXT_ANTI_ALIASING,
                                    GUIConstants.OPTIONS_UI_TEXT_COLOR))
                screen.blit(hp_label, (GUIConstants.OPTIONS_UI_CONTENT_START_CORNER[0] + 176,
                                       GUIConstants.OPTIONS_UI_CONTENT_START_CORNER[
                                           1] + GUIConstants.OPTIONS_UI_MENU_TEXT_LINE_HEIGHT * 0.8))
            # if selected menu is save menu
            case 'save':
                save_time_file = open('save_datas.json', 'r')
                save_time_json = dict(json.load(save_time_file))
                save_time_file.close()
                if self.selection_level == 1:
                    # fill backgrounds
                    screen.fill(GUIConstants.OPTIONS_UI_SELECTION_COLOR,
                                pygame.Rect((GUIConstants.OPTIONS_UI_CONTENT_START_CORNER[0] - 10,
                                             GUIConstants.OPTIONS_UI_CONTENT_START_CORNER[1] - 10 + (
                                                 self.sub_selection) * GUIConstants.OPTIONS_UI_SAVE_MENU_HEIGHT,
                                             GUIConstants.OPTIONS_UI_CONTENT_SELECTION_WIDTH,
                                             GUIConstants.OPTIONS_UI_SAVE_MENU_HEIGHT)))
                for idx in range(Constants.SAVE_COUNT):
                    # draw save and datas
                    save_title_label = assets.get_asset(GUIConstants.OPTIONS_UI_FONT_FILENAME,
                                                        GUIConstants.OPTIONS_UI_FONT_SIZE).render(
                        i18n.get_string_from_id('save_file_preposition') + f'{idx + 1:02}',
                        GUIConstants.TEXT_ANTI_ALIASING, GUIConstants.OPTIONS_UI_TEXT_COLOR)
                    screen.blit(save_title_label, (GUIConstants.OPTIONS_UI_CONTENT_START_CORNER[0],
                                                   GUIConstants.OPTIONS_UI_CONTENT_START_CORNER[
                                                       1] + GUIConstants.OPTIONS_UI_SAVE_MENU_HEIGHT * idx))
                    save_time_label = assets.get_asset(GUIConstants.OPTIONS_UI_FONT_FILENAME,
                                                       GUIConstants.OPTIONS_UI_FONT_SIZE - 2).render(
                        '  ' + i18n.get_string_from_id('saved') if self.last_saved_save_file_index == idx else '  ' +
                                                                                                               save_time_json[
                                                                                                                   f'save_{idx + 1:02}.gsvf'],
                        GUIConstants.TEXT_ANTI_ALIASING, GUIConstants.OPTIONS_UI_TEXT_COLOR)
                    screen.blit(save_time_label, (GUIConstants.OPTIONS_UI_CONTENT_START_CORNER[0],
                                                  GUIConstants.OPTIONS_UI_CONTENT_START_CORNER[
                                                      1] + GUIConstants.OPTIONS_UI_SAVE_MENU_HEIGHT * (idx + 0.5)))

            # if quit menu is selected
            case 'quit':
                # draw selection rect
                if self.selection_level == 1:
                    screen.fill(GUIConstants.OPTIONS_UI_SELECTION_COLOR,
                                pygame.Rect((GUIConstants.OPTIONS_UI_CONTENT_START_CORNER[0] - 10,
                                             GUIConstants.OPTIONS_UI_CONTENT_START_CORNER[1] - 10 + (
                                                     self.sub_selection + 1) * GUIConstants.OPTIONS_UI_MENU_TEXT_LINE_HEIGHT,
                                             GUIConstants.OPTIONS_UI_CONTENT_SELECTION_WIDTH,
                                             GUIConstants.OPTIONS_UI_MENU_TEXT_LINE_HEIGHT)))
                # draw labels
                confirmation_label = assets.get_asset(GUIConstants.OPTIONS_UI_FONT_FILENAME,
                                                      GUIConstants.OPTIONS_UI_FONT_SIZE).render(
                    i18n.get_string_from_id('quit_confirmation_prompt'), GUIConstants.TEXT_ANTI_ALIASING,
                    GUIConstants.OPTIONS_UI_TEXT_COLOR)
                screen.blit(confirmation_label, GUIConstants.OPTIONS_UI_CONTENT_START_CORNER)
                yes_label = assets.get_asset(GUIConstants.OPTIONS_UI_FONT_FILENAME,
                                             GUIConstants.OPTIONS_UI_FONT_SIZE).render(
                    i18n.get_string_from_id('yes'), GUIConstants.TEXT_ANTI_ALIASING,
                    GUIConstants.OPTIONS_UI_TEXT_COLOR)
                screen.blit(yes_label, (GUIConstants.OPTIONS_UI_CONTENT_START_CORNER[0],
                                        GUIConstants.OPTIONS_UI_CONTENT_START_CORNER[
                                            1] + GUIConstants.OPTIONS_UI_MENU_TEXT_LINE_HEIGHT))
                no_label = assets.get_asset(GUIConstants.OPTIONS_UI_FONT_FILENAME,
                                            GUIConstants.OPTIONS_UI_FONT_SIZE).render(
                    i18n.get_string_from_id('no'), GUIConstants.TEXT_ANTI_ALIASING,
                    GUIConstants.OPTIONS_UI_TEXT_COLOR)
                screen.blit(no_label, (GUIConstants.OPTIONS_UI_CONTENT_START_CORNER[0],
                                       GUIConstants.OPTIONS_UI_CONTENT_START_CORNER[
                                           1] + 2 * GUIConstants.OPTIONS_UI_MENU_TEXT_LINE_HEIGHT))
            case other:
                raise NotImplementedError

    # draw menu to screen
    def update(self, screen, scene, main_player):
        self.background_surface.fill((0, 0, 0, 0))
        self.draw_background(screen, scene, main_player)
        screen.blit(self.background_surface, (0, 0))
        screen.fill(
            GUIConstants.OPTIONS_UI_SELECTION_COLOR if self.selection_level == 0 else GUIConstants.OPTIONS_UI_LIGHT_SELECTION_COLOR,
            pygame.Rect((GUIConstants.OPTIONS_UI_SELECTION_CORNER[0],
                         GUIConstants.OPTIONS_UI_SELECTION_CORNER[
                             1] + self.selected_tab * GUIConstants.OPTIONS_UI_MENU_TEXT_LINE_HEIGHT,
                         GUIConstants.OPTIONS_UI_SELECTION_WIDTH,
                         GUIConstants.OPTIONS_UI_MENU_TEXT_LINE_HEIGHT)))
        self.draw_menu_texts(screen, scene, main_player)
        self.draw_submenus(screen, scene, main_player)
