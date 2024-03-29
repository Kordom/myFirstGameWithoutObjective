import pygame
from config import *
import math
import random

class Player(pygame.sprite.Sprite): # pygame lib. class which helps with creating sprites
    def __init__(self, game, x, y):

        self.game = game
        self._layer = PLAYER_LAYER  # to put correctly player on the grass
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)  # with this move we are adding our self.groups
        # to already existing Sprite class

        self.x = x * TILE_SIZE  # because its tile based game we need tile size
        self.y = y * TILE_SIZE
        self.width = TILE_SIZE
        self.height = TILE_SIZE

        self.image = pygame.Surface([self.width, self.height]) # creating rectangle with 32x32p size
        self.image.fill("red")  # filling it with red color

        self.change_x = 0
        self.change_y = 0

        self.facing = "down"

        self.rect = self.image.get_rect()  # hitbox will be equal to picture size
        self.rect.x = self.x  # coordinates for rectangle
        self.rect.y = self.y

    def update(self):
        self.movement()

        self.rect.x += self.change_x # allow to move hitbox with player
        self.rect.y += self.change_y

        self.change_x = 0  # temp
        self.change_y = 0

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.change_y -= PLAYER_SPEED  # y axis starts from top 0
            self.facing = "up"
        if keys[pygame.K_s]:
            self.change_y += PLAYER_SPEED
            self.facing = "down"
        if keys[pygame.K_a]:
            self.change_x -= PLAYER_SPEED   # x axis starts from left 0
            self.facing = "left"
        if keys[pygame.K_d]:
            self.change_x += PLAYER_SPEED
            self.facing = "right"


class Block(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = BLOCK_LAYER
        self.groups = self.game.all_sprites, self.game.blocks
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.width = TILE_SIZE
        self.height = TILE_SIZE

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill("blue")

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

