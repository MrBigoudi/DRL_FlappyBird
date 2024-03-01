WINDOW_WIDTH = 1680
WINDOW_HEIGHT = 1024
TARGET_FPS = 60

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

BACKGROUND_COLOR = BLACK

AGENT_SIZE = (100, 100) #(width, height)

PIPE_WIDTH = 150
PIPE_HEIGHT = WINDOW_HEIGHT

PIPE_GAP_HEIGHT = 3 * AGENT_SIZE[1]
FIRST_GAP_TOP = WINDOW_HEIGHT // 2 - PIPE_GAP_HEIGHT // 2
MIN_GAP_TOP = AGENT_SIZE[1]
MAX_GAP_TOP = WINDOW_HEIGHT - PIPE_GAP_HEIGHT - MIN_GAP_TOP

SCROLLING_SPEED = 10
PIPE_APPARITION_SPEED = 2000 # in milliseconds

BIRD_FLY_VEL = 28
BIRD_MASS = 0.25
GRAVITY = 9.81

from enum import Enum

class ActionType(Enum):
    DO_NOTHING = 0,
    JUMP = 1,