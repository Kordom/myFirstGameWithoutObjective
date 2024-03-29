import pygame
from config import *
import math
import random

class Spritessheet:
    def __init__(self, file):
        self.sheet = pygame.image.load(file).convert()

    def get_sprite(self,x ,y, width, height):
        sprite = pygame.Surface([width, height])
        sprite.blit(self.sheet, (0,0), (x, y, width, height))  # makes cutout from big image
        sprite.set_colorkey("black")
        return sprite

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

        self.change_x = 0
        self.change_y = 0

        self.facing = "down"

        self.image = self.game.character_spritesheet.get_sprite(3, 2, self.width, self.height)
        # self.image = pygame.Surface([self.width, self.height]) # creating rectangle with 32x32p size
        # self.image.set_colorkey("black")  # the function makes specified color transparent
        # self.image.blit(image_to_load, (0,0))  # draw image on surface
        # self.image.fill("red")  # filling it with red color

        self.rect = self.image.get_rect()  # hitbox will be equal to picture size
        self.rect.x = self.x  # coordinates for rectangle
        self.rect.y = self.y

    def update(self):
        self.movement()

        self.rect.x += self.change_x  # allow to move hitbox with player
        self.colide_blocks("x")  # added collision for x axis
        self.rect.y += self.change_y
        self.colide_blocks("y")  # added collision for x axis

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

    def colide_blocks(self, direction):
        if direction == "x":
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.change_x > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width  # to simplify this character gets on the block and thend
                    #pushed away by minusing it width
                if self.change_x < 0:
                    self.rect.x = hits[0].rect.right

        if direction == "y":
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.change_y > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height  # to simplify this code pushes away from a wall
                if self.change_y < 0:
                    self.rect.y = hits[0].rect.bottom

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

        self.image = self.game.terrain_spritesheet.get_sprite(960, 448, self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Ground(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = GROUND_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.width = TILE_SIZE
        self.height = TILE_SIZE

        self.image = self.game.terrain_spritesheet.get_sprite(64, 352,self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
