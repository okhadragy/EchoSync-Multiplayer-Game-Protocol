"""
Grid Clash - Configuration
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ESP_config import *

# Window settings
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
FPS = 60

# Grid settings
GRID_SIZE = GRID_N
CELL_SIZE = 24
MARGIN = 4

# UI Colors
WHITE = (255, 255, 255)
BLACK = (12, 12, 12)
GREY = (230, 230, 235)
DARK_GREY = (40, 40, 50)
LIGHT_GREY = (245, 245, 250)
ACCENT_COLOR = (60, 180, 180)
BTN_BG = (30, 30, 40)
BTN_HOVER = (60, 180, 180)
BTN_TEXT = (230, 230, 230)
PANEL_BG = (245, 245, 250)
TEXT_ACCENT = (40, 40, 60)

# Room settings
MAX_ROOMS = 16
MIN_PLAYERS = REQUIRED_ROOM_PLAYERS
MAX_PLAYERS = REQUIRED_ROOM_PLAYERS