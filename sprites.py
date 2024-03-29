import pygame
from config import *
import math
import random


class Player(pygame.sprite.Sprite):  # pygame lib. class which helps with creating sprites
    def __init__(self, game, x, y):
        self.game = game
        self._layer = PLAYER_LAYER  # to put correctly player on the grass
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILE_SIZE  # because its tile based game we need tile size
        self.y = y * TILE_SIZE
        self.width = TILE_SIZE
        self.height = TILE_SIZE

        self.x_change = 0  # temp for variables to store movement changes
        self.y_change = 0

        self.facing = "down"  # for animations to know where the character is facing

        self.image = pygame.Surface([self.width, self.height])  # creating rectangle with 32x32p size
        self.image.fill("red")  # filling it with red color

        self.rect = self.image.get_rect()  # hitbox will be equal to picture size
        self.rect.x = self.x  # coordinates for rectangle
        self.rect.y = self.y

    def update(self):
        self.movement()

        self.rect.x += self.x_change  # its for the hitbox to move around with char
        self.rect.y += self.y_change

        self.x_change = 0  # temp for variables to store movement changes
        self.y_change = 0

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.y_change -= PLAYER_SPEED  # it starts from top 0 y axis increses going down
            self.facing = "up"
        if keys[pygame.K_s]:
            self.y_change += PLAYER_SPEED
            self.facing = "down"
        if keys[pygame.K_a]:
            self.x_change -= PLAYER_SPEED
            self.facing = "left"
        if keys[pygame.K_d]:
            self.x_change += PLAYER_SPEED
            self.facing = "right"

# def borders(player_pos,height, width):
#     if player_pos.y > height:
#         player_pos.y = height
