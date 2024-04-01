import pygame
WIDTH, HEIGHT = 1024, 1024
TILE_SIZE = 32
FPS = 60


PLAYER_LAYER = 4  # player will bi above the block so he can stand on it
ENEMY_LAYER = 3
BLOCK_LAYER = 2
GROUND_LAYER = 1

PLAYER_SPEED = 3
ENEMY_SPEED = 2

content_ = "Start Sailing"


tilemap =[
    "",
    "S",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    ".BBBBBBBBB",
    ".B........BBBBBBB",
    ".B...............BB",
    "..B................BBBBBBBBBBBBBBBBBBBBBB",
    "...BB.......P...B........................B",
    ".....BB.........B........................B",
    ".......B........B........................B",
    "........B................................B",
    ".........B...............................B",
    "..........BBBBBBB.......................B",
    ".................B..................BBBB",
    ".................B................BBB",
    "..................BBBBBBBBBBBBBBBB",
]


