"""constants related to gui"""
import pygame

import src.constants.base_constants as Constants
from src.i18n.i18n import i18n

TEXT_ANTI_ALIASING = True

DIALOGUE_HEIGHT = 200
DIALOGUE_Y = Constants.WINDOW_HEIGHT - DIALOGUE_HEIGHT
DIALOGUE_BACKGROUND_ALPHA = 128

DIALOGUE_IMAGE_SIZE = 160
DIALOGUE_TEXT_X_NO_IMAGE = 20
DIALOGUE_TEXT_X_WITH_IMAGE = DIALOGUE_TEXT_X_NO_IMAGE * 2 + DIALOGUE_IMAGE_SIZE
DIALOGUE_TEXT_Y = 16
DIALOGUE_TEXT_COLOR = (239, 239, 239)
DIALOGUE_FONT_FILENAME = "fonts/Galmuri14.ttf"
DIALOGUE_GUI_FONT_SIZE = 22

TESTING_GUI_FONT_FILENAME = "fonts/Galmuri14.ttf"
TESTING_GUI_FONT_SIZE = 22

TYPEWRITER_ANIMATION_INDEX_THRESHOLD_NORMAL = int(2 * (Constants.FPS / 60))
TYPEWRITER_ANIMATION_INDEX_THRESHOLD_EXCEPT = int(0.75 * (Constants.FPS / 60))
TYPEWRITER_EXCEPT_CHARS = ' ,/\'\"[]{}()@#$%^&*<>'

OPTIONS_UI_RECTS = [pygame.Rect(48, 48, 224, Constants.WINDOW_HEIGHT - 96),
                    pygame.Rect(48 + 224 + 16, 48, 688, Constants.WINDOW_HEIGHT - 96)]
OPTIONS_UI_SELECTION_CORNER = (61, 61)
OPTIONS_UI_SELECTION_WIDTH = 198
OPTIONS_UI_SELECTION_COLOR = (42, 42, 42)
OPTIONS_UI_BACKGROUND_ALPHA = 176
OPTIONS_UI_BACKGROUND_COLOR = (84, 84, 84)
OPTIONS_UI_TAB_IDS = ['status', 'items', 'save', 'quit']
OPTIONS_UI_FONT_FILENAME = "fonts/Galmuri14.ttf"
OPTIONS_UI_FONT_SIZE = 22
OPTIONS_UI_TEXT_COLOR = (255, 255, 255)
OPTIONS_UI_DISABLED_TEXT_COLOR = (160, 160, 160)
OPTIONS_UI_MENU_TEXT_START_CORNER = (72, 72)
OPTIONS_UI_MENU_TEXT_LINE_HEIGHT = 42
