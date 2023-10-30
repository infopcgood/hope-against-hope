import src.constants.base_constants as Constants

SPRITE_WIDTH = 64
SPRITE_HEIGHT = 64

FACING_LEFT = 1
FACING_UP = 0
FACING_DOWN = 2
FACING_RIGHT = 3

ACTION_SPELLCASTING = 0
ACTION_THRUSTING = 4
ACTION_WALKING = 8
ACTION_IDLE = 8

ACTION_START_CNT = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
ACTION_INDEX_CNT = [7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 6, 6, 6, 6, 13, 13, 13, 13, 6]

SPEED_X = [0, -0.1, 0, 0.1]
SPEED_Y = [-0.1, 0, 0.1, 0]

ANIM_UPDATE_THRESHOLD = int(4 * (Constants.FPS / 60) )