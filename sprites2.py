import pygame
from config import *
import math
import random

bullets = []
class Player(pygame.sprite.Sprite):  # pygame lib. class which helps with creating sprites
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
        self.animation_loop = 1
        self.animation_loop_idle = 3
        self.animation_loop_left = 6
        self.animation_loop_right = 9

        self.image = self.game.character_spritesheet.get_sprite(3, 2, self.width, self.height)

        self.rect = self.image.get_rect()  # hitbox will be equal to picture size
        self.rect.x = self.x  # coordinates for rectangle
        self.rect.y = self.y

        self.down_animations = [self.game.character_spritesheet.get_sprite(0, 131, self.width, self.height),
                                self.game.character_spritesheet.get_sprite(32, 133, self.width, self.height),
                                self.game.character_spritesheet.get_sprite(65, 131, self.width, self.height)]

        self.up_animations = [self.game.character_spritesheet.get_sprite(0, 163, self.width, self.height),
                              self.game.character_spritesheet.get_sprite(32, 165, self.width, self.height),
                              self.game.character_spritesheet.get_sprite(65, 163, self.width, self.height)]

        self.left_animations = [self.game.character_spritesheet.get_sprite(1, 230, self.width, self.height),
                                self.game.character_spritesheet.get_sprite(37, 231, self.width, self.height),
                                self.game.character_spritesheet.get_sprite(70, 230, self.width, self.height)]

        self.right_animations = [self.game.character_spritesheet.get_sprite(1, 196, self.width, self.height),
                                 self.game.character_spritesheet.get_sprite(34, 198, self.width, self.height),
                                 self.game.character_spritesheet.get_sprite(67, 196, self.width, self.height)]

        self.idle_animation = [self.game.character_spritesheet.get_sprite(0, 0, self.width, self.height),
                               self.game.character_spritesheet.get_sprite(32, 1, self.width, self.height),
                               self.game.character_spritesheet.get_sprite(65, 1, self.width, self.height),
                               self.game.character_spritesheet.get_sprite(0, 32, self.width, self.height),
                               self.game.character_spritesheet.get_sprite(32, 34, self.width, self.height),
                               self.game.character_spritesheet.get_sprite(65, 34, self.width, self.height),
                               self.game.character_spritesheet.get_sprite(5, 98, self.width, self.height),
                               self.game.character_spritesheet.get_sprite(38, 100, self.width, self.height),
                               self.game.character_spritesheet.get_sprite(71, 100, self.width, self.height),
                               self.game.character_spritesheet.get_sprite(1, 65, self.width, self.height),
                               self.game.character_spritesheet.get_sprite(34, 67, self.width, self.height),
                               self.game.character_spritesheet.get_sprite(67, 67, self.width, self.height),

                               ]

    def update(self):
        self.movement()
        self.animate()
        self.collide_enemy()

        self.rect.x += self.change_x  # allow to move hitbox with player
        self.colide_blocks("x")  # added collision for x axis
        self.rect.y += self.change_y
        self.colide_blocks("y")  # added collision for x axis

        self.change_x = 0  # temp
        self.change_y = 0

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            for sprite in self.game.all_sprites:
                sprite.rect.y += PLAYER_SPEED
            self.change_y -= PLAYER_SPEED  # y axis starts from top 0
            self.facing = "up"
        elif keys[pygame.K_s]:
            for sprite in self.game.all_sprites:
                sprite.rect.y -= PLAYER_SPEED
            self.change_y += PLAYER_SPEED
            self.facing = "down"
        elif keys[pygame.K_a]:
            for sprite in self.game.all_sprites:
                sprite.rect.x += PLAYER_SPEED
            self.change_x -= PLAYER_SPEED  # x axis starts from left 0
            self.facing = "left"
        elif keys[pygame.K_d]:
            for sprite in self.game.all_sprites:
                sprite.rect.x -= PLAYER_SPEED
            self.change_x += PLAYER_SPEED
            self.facing = "right"

    def colide_blocks(self, direction):
        if direction == "x":
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.change_x > 0:
                    self.rect.x = hits[
                                      0].rect.left - self.rect.width  # to simplify this character gets on the block and thend
                    # pushed away by minusing it width
                    for sprites in self.game.all_sprites:
                        sprites.rect.x += PLAYER_SPEED
                if self.change_x < 0:
                    self.rect.x = hits[0].rect.right
                    for sprites in self.game.all_sprites:
                        sprites.rect.x -= PLAYER_SPEED
        if direction == "y":
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.change_y > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height  # to simplify this code pushes away from a wall
                    for sprites in self.game.all_sprites:
                        sprites.rect.y += PLAYER_SPEED
                if self.change_y < 0:
                    self.rect.y = hits[0].rect.bottom
                    for sprites in self.game.all_sprites:
                        sprites.rect.y -= PLAYER_SPEED

    def collide_enemy(self):
        hits = pygame.sprite.spritecollide(self, self.game.enemies, False)
        if hits:
            self.kill()
            self.game.playing = False

    def animate(self):
        if self.facing == "down":
            if self.change_y == 0:
                self.image = self.idle_animation[math.floor(self.animation_loop_idle)]
                self.animation_loop_idle += 0.1
                if self.animation_loop_idle >= 3:
                    self.animation_loop_idle = 1
            else:
                self.image = self.down_animations[
                    math.floor(self.animation_loop)]  # when key is pressed index will grow + 0.1
                self.animation_loop += 0.1
                if self.animation_loop >= 3:  # what affects in changing the pictures
                    self.animation_loop = 1

        if self.facing == "up":
            if self.change_y == 0:
                self.image = self.idle_animation[math.floor(self.animation_loop_idle)]
                self.animation_loop_idle += 0.1
                if self.animation_loop_idle >= 6:
                    self.animation_loop_idle = 3
            else:
                self.image = self.up_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1

        if self.facing == "left":
            if self.change_x == 0:
                self.image = self.idle_animation[math.floor(self.animation_loop_left)]
                self.animation_loop_left += 0.1
                if self.animation_loop_left >= 9:
                    self.animation_loop_left = 6
            else:
                self.image = self.left_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1

        if self.facing == "right":
            if self.change_x == 0:
                self.image = self.idle_animation[math.floor(self.animation_loop_right)]
                self.animation_loop_right += 0.1
                if self.animation_loop_right >= 12:
                    self.animation_loop_right = 9
            else:
                self.image = self.right_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1


class Block(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = BLOCK_LAYER
        self.groups = self.game.all_sprites, self.game.blocks
        pygame.sprite.Sprite.__init__(self, *self.groups)

        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.width = TILE_SIZE
        self.height = TILE_SIZE

        self.image = self.game.terrain_spritesheet.get_sprite(190, 3031, self.width, self.height)
        self.image.set_colorkey("white")
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

        self.image = self.game.ship2.get_sprite(130, 467, 1800, 1800)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


class Attack(pygame.sprite.Sprite):
    def __init__(self, game, x, y):

        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites, self.game.attacks
        pygame.sprite.Sprite.__init__(self, *self.groups)

        self.x = x
        self.y = y
        self.width = TILE_SIZE
        self.height = TILE_SIZE

        self.animation_loop = 0
        # self.attack_animation_loop_up = 9
        # self.attack_animation_loop_down = 3
        # self.attack_animation_loop_left = 6
        # self.attack_animation_loop_right = 1

        self.image = self.game.attack_spritesheet.get_sprite(0, 0, self.width, self.height)

        self.rect = self.image.get_rect()

        self.rect.x = self.x
        self.rect.y = self.y

        # self.attack_animations = [self.game.attack_spritesheet.get_sprite(336, 65, self.width, self.height),  # right
        #                           self.game.attack_spritesheet.get_sprite(367, 67, self.width, self.height),
        #                           self.game.attack_spritesheet.get_sprite(402, 65, self.width, self.height),
        #                           self.game.attack_spritesheet.get_sprite(335, 0, self.width, self.height),  # down
        #                           self.game.attack_spritesheet.get_sprite(367, 0, self.width, self.height),
        #                           self.game.attack_spritesheet.get_sprite(400, 0, self.width, self.height),
        #                           self.game.attack_spritesheet.get_sprite(334, 98, self.width, self.height),  # left
        #                           self.game.attack_spritesheet.get_sprite(367, 100, self.width, self.height),
        #                           self.game.attack_spritesheet.get_sprite(406, 98, self.width, self.height),
        #                           self.game.attack_spritesheet.get_sprite(335, 33, self.width, self.height),  # up
        #                           self.game.attack_spritesheet.get_sprite(367, 33, self.width, self.height),
        #                           self.game.attack_spritesheet.get_sprite(400, 33, self.width, self.height)]

        self.right_animations = [
            self.game.attack_spritesheet.get_sprite(0, 64, self.width, self.height),
            self.game.attack_spritesheet.get_sprite(32, 64, self.width, self.height),
            self.game.attack_spritesheet.get_sprite(64, 64, self.width, self.height),
            self.game.attack_spritesheet.get_sprite(96, 64, self.width, self.height),
            self.game.attack_spritesheet.get_sprite(128, 64, self.width, self.height)]

        self.down_animations = [self.game.attack_spritesheet.get_sprite(0, 32, self.width, self.height),
                                self.game.attack_spritesheet.get_sprite(32, 32, self.width, self.height),
                                self.game.attack_spritesheet.get_sprite(64, 32, self.width, self.height),
                                self.game.attack_spritesheet.get_sprite(96, 32, self.width, self.height),
                                self.game.attack_spritesheet.get_sprite(128, 32, self.width, self.height)]

        self.left_animations = [self.game.attack_spritesheet.get_sprite(0, 96, self.width, self.height),
                                self.game.attack_spritesheet.get_sprite(32, 96, self.width, self.height),
                                self.game.attack_spritesheet.get_sprite(64, 96, self.width, self.height),
                                self.game.attack_spritesheet.get_sprite(96, 96, self.width, self.height),
                                self.game.attack_spritesheet.get_sprite(128, 96, self.width, self.height)]

        self.up_animations = [self.game.attack_spritesheet.get_sprite(0, 0, self.width, self.height),
                              self.game.attack_spritesheet.get_sprite(32, 0, self.width, self.height),
                              self.game.attack_spritesheet.get_sprite(64, 0, self.width, self.height),
                              self.game.attack_spritesheet.get_sprite(96, 0, self.width, self.height),
                              self.game.attack_spritesheet.get_sprite(128, 0, self.width, self.height)]

    def update(self):
        self.animate()
        self.collide()

    def collide(self):
        hits = pygame.sprite.spritecollide(self, self.game.enemies, True)  # checking collision betwen hero and enemies

    def animate(self):
        direction = self.game.player.facing
        if direction == "up":
            self.image = self.up_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.5
            if self.animation_loop >= 5:
                self.kill()
        if direction == "down":
            self.image = self.down_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.5
            if self.animation_loop >= 5:
                self.kill()
        if direction == "left":
            self.image = self.left_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.5
            if self.animation_loop >= 5:
                self.kill()
        if direction == "right":
            self.image = self.right_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.5
            if self.animation_loop >= 5:
                self.kill()

    # def animate_att(self):
    #     direction = self.game.player.facing
    #     if direction == "up":
    #         self.image = self.up_animations[math.floor(self.animation_loop)]
    #         self.animation_loop += 0.5
    #         if self.animation_loop >= 5:
    #             self.kill()
    #     if direction == "down":
    #         self.image = self.down_animations[math.floor(self.animation_loop)]
    #         self.animation_loop += 0.5
    #         if self.animation_loop >= 5:
    #             self.kill()
    #     if direction == "left":
    #         self.image = self.left_animations[math.floor(self.animation_loop)]
    #         self.animation_loop += 0.5
    #         if self.animation_loop >= 5:
    #             self.kill()
    #     if direction == "right":
    #         self.image = self.attack_animations[math.floor(self.attack_animation_loop_right)]
    #         self.animation_loop += 0.5
    #         if self.animation_loop >= 3:
    #             self.attack_animation_loop_right = 1


class Button:
    def __init__(self, x, y, width, height, fg, bg, content, fontsize):
        self.font = pygame.font.Font("img/CookieCrisp-L36ly.ttf", fontsize)
        self.content = content

        self.x = x
        self.y = y

        self.width = width
        self.heigt = height

        self.fg = fg
        self.bg = bg

        self.image = pygame.Surface((self.width, self.heigt))

        self.image.fill(self.bg)
        self.rect = self.image.get_rect()

        self.rect.x = self.x
        self.rect.y = self.y

        self.text = self.font.render(self.content, True, self.fg)
        self.text_rect = self.text.get_rect(center=(self.width / 2, self.heigt / 2))
        self.image.blit(self.text, self.text_rect)
        self.image.set_colorkey("black")

    def is_pressed(self, pos, pressed):
        if self.rect.collidepoint(pos):
            if pressed[0]:
                return True
            return False
        return False


class Bullet(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = PLAYER_LAYER
        self.groups1 = self.game.all_sprites, self.game.bullets
        pygame.sprite.Sprite.__init__(self, *self.groups1)

        self.image = self.game.bullet_spritesheet.get_sprite(570, 475, 9, 9)
        self.rect = self.image.get_rect()

        self.x = x
        self.y = y
        self.rect.x = self.x
        self.rect.y = self.y

        # self.shooting = False
        self.facing = "down"
        self.shoot_cooldown = 0
        self.speed = BULLET_SPEED

    def update(self):
        if self.game.player.facing == "up":
            self.rect.y -= BULLET_SPEED

        if self.game.player.facing == "down":
            self.rect.y += BULLET_SPEED

        if self.game.player.facing == "right":
            self.rect.x += BULLET_SPEED

        if self.game.player.facing == "left":
            self.rect.x -= BULLET_SPEED

        self.is_shooting()
        self.collide()

    def is_shooting(self):
        if self.shoot_cooldown > 0:
            self.shoot_cooldown = SHOOT_COOLDOWN
        else:
            self.shoot_cooldown -= 1

    def collide(self):
        hits = pygame.sprite.spritecollide(self, self.game.enemies, True)
        hits2 = pygame.sprite.spritecollide(self, self.game.blocks, False)
        if hits:
            pygame.sprite.Sprite.kill(self)
        if hits2:
            pygame.sprite.Sprite.kill(self)


class Enemy(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = ENEMY_LAYER  # to put correctly player on the grass
        self.groups = self.game.all_sprites, self.game.enemies
        pygame.sprite.Sprite.__init__(self, *self.groups)  # with this move we are adding our self.groups
        # to already existing Sprite class

        self.x = x * TILE_SIZE  # because its tile based game we need tile size
        self.y = y * TILE_SIZE
        self.width = TILE_SIZE
        self.height = TILE_SIZE

        self.temp_left = 0
        self.change_x = 0
        self.change_y = 0
        self.facing = random.choice(["left", "right"])

        self.animation_loop = 1
        self.movement_loop = 0
        self.max_travel_x = random.randint(20, 25)
        self.max_travel_y = random.randint(10, 20)

        self.image = self.game.enemy_spritesheet.get_sprite(3, 2, self.width, self.height)
        self.image.set_colorkey("black")

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.down_animations = [self.game.enemy_spritesheet.get_sprite(3, 2, self.width, self.height),
                                self.game.enemy_spritesheet.get_sprite(35, 2, self.width, self.height),
                                self.game.enemy_spritesheet.get_sprite(68, 2, self.width, self.height)]

        self.up_animations = [self.game.enemy_spritesheet.get_sprite(3, 34, self.width, self.height),
                              self.game.enemy_spritesheet.get_sprite(35, 34, self.width, self.height),
                              self.game.enemy_spritesheet.get_sprite(68, 34, self.width, self.height)]

        self.left_animations = [self.game.enemy_spritesheet.get_sprite(3, 98, self.width, self.height),
                                self.game.enemy_spritesheet.get_sprite(35, 98, self.width, self.height),
                                self.game.enemy_spritesheet.get_sprite(68, 98, self.width, self.height)]

        self.right_animations = [self.game.enemy_spritesheet.get_sprite(3, 66, self.width, self.height),
                                 self.game.enemy_spritesheet.get_sprite(35, 66, self.width, self.height),
                                 self.game.enemy_spritesheet.get_sprite(68, 66, self.width, self.height)]

    def update(self):
        self.movement()
        self.animate()

        self.rect.x += self.change_x
        self.rect.y += self.change_y

        self.change_x = 0
        self.change_y = 0

    def movement(self):
        if self.facing == "left":
            self.change_x -= ENEMY_SPEED
            self.movement_loop -= 1
            if self.temp_left == 2:
                self.facing = "up"
            if self.movement_loop <= -self.max_travel_x:
                self.facing = "right"

        if self.facing == "right":
            self.change_x += ENEMY_SPEED
            self.movement_loop += 1
            if self.movement_loop >= self.max_travel_x:
                self.facing = "left"

    def animate(self):
        if self.facing == "down":
            if self.change_y == 0:
                self.game.enemy_spritesheet.get_sprite(3, 2, self.width, self.height)
            else:
                self.image = self.down_animations[
                    math.floor(self.animation_loop)]  # when key is pressed index will grow + 0.1
                self.animation_loop += 0.1
                if self.animation_loop >= 3:  # what affects in changing the pictures
                    self.animation_loop = 1
        if self.facing == "up":
            if self.change_y == 0:
                self.game.enemy_spritesheet.get_sprite(3, 2, self.width, self.height)
            else:
                self.image = self.up_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1
        if self.facing == "left":
            if self.change_x == 0:
                self.game.enemy_spritesheet.get_sprite(3, 2, self.width, self.height)
            else:
                self.image = self.left_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1
        if self.facing == "right":
            if self.change_x == 0:
                self.game.enemy_spritesheet.get_sprite(3, 2, self.width, self.height)
            else:
                self.image = self.right_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1
