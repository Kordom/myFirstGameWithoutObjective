import pygame
from config import *
import math
import random

class Player(pygame.sprite.Sprite): # pygame lib. class which helps with creating sprites
    def __init__(self,game, x, y):

        self.game = game
        self._layer = PLAYER_LAYER # to put correctly player on the grass
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILE_SIZE # because its tile based game we need tile size
        self.y = y * TILE_SIZE
        self.width = TILE_SIZE
        self.height = TILE_SIZE

        self.image = pygame.Surface([self.width, self.height]) # creating rectangle with 32x32p size
        self.image.fill("red") # filling it with red color

        self.rect = self.image.get_rect() # hitbox will be equal to picture size
        self.rect.x = self.x # coordinates for rectangle
        self.rect.y = self.y

    def update(self):
        pass




    # def char_movement(self):
    #     keys = pygame.key.get_pressed()
    #     pygame.draw.circle(self.screen, "white", self.player_pos, 40)
    #     if keys[pygame.K_w]:
    #         self.player_pos.y -= 300 * self.dt
    #     if keys[pygame.K_s]:
    #         self.player_pos.y += 300 * self.dt
    #     if keys[pygame.K_a]:
    #         self.player_pos.x -= 300 * self.dt
    #     if keys[pygame.K_d]:
    #         self.player_pos.x += 300 * self.dt

# def borders(player_pos,height, width):
#     if player_pos.y > height:
#         player_pos.y = height
