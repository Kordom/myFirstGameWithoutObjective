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

SHOOT_COOLDOWN = 300
BULLET_SPEED = 3
BULLET_DISTANCE = 10
content_ = "Start Sailing"

tilemap = [
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
    "...BB.......P...B....E...................B",
    ".....BB.........B............E...........B",
    ".......B........B........................B",
    "........B........................E.......B",
    ".........B............E..................B",
    "..........BBBBBBB...........E...........B",
    ".................B..................BBBB",
    ".................B................BBB",
    "..................BBBBBBBBBBBBBBBB",
]
