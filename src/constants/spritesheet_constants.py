"""Constants related to spritesheet and animations"""

import src.constants.base_constants as Constants

FACING_LEFT = 1
FACING_UP = 0
FACING_DOWN = 2
FACING_RIGHT = 3

ACTION_SPELLCASTING = 0
ACTION_THRUSTING = 4
ACTION_WALKING = 8
ACTION_IDLE = 8
ACTION_SLASHING = 12
ACTION_SHOOTING = 16
ACTION_DEAD = 20

EMOTE_LIKE = 0
EMOTE_THINK = 1
EMOTE_EXCLAIM = 2
EMOTE_QUESTION = 3

ACTION_START_CNT = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
ACTION_INDEX_CNT = [7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 6, 6, 6, 6, 13, 13, 13, 13, 6]
EMOTE_START_CNT = [0, 0, 0, 0]
EMOTE_INDEX_CNT = [10, 10, 10, 10]
ACTION_LOOP = [False, False, False, False, False, False, False, False, True, True, True, True, False, False, False,
               False, False, False, False, False, False]
ACTION_STOP = [True, True, True, True, True, True, True, True, None, None, None, None, True, True, True, True, True,
               True, True, True, False]
ACTUALLY_MOVES = [False, False, False, False, False, False, False, False, True, True, True, True, False, False, False,
                  False, False, False, False, False, False]

SPEED_X = [0, -0.11, 0, 0.11]
SPEED_Y = [-0.11, 0, 0.11, 0]

ANIM_UPDATE_THRESHOLD = int(5 * (Constants.FPS / 60))
EMOTE_UPDATE_THRESHOLD = int(6 * (Constants.FPS / 60))
