import pygame
import sys
from config import *
from sprites import *


#################################################################################
# creating setup
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((HEIGHT, WIDTH))
        # fscreen = pygame.display.toggle_fullscreen()
        self.clock = pygame.time.Clock()
        # self.font = pygame.font.Font('Arial', 32)
        self.running = True
        # self.dt = 0  # delta time in second since last frame used for independent physics

    def new(self):
        # new game starts
        self.playing = True
        self.all_sprites = pygame.sprite.LayeredUpdates()  # contains all sprites (walls ,enemies, char, allow to update all at once)
        self.blocks = pygame.sprite.LayeredUpdates()  # contains wallls
        self.enemies = pygame.sprite.LayeredUpdates()  # contains enemies
        self.attaks = pygame.sprite.LayeredUpdates()  # attaks and animations

        self.player = Player(self, 1, 2)

    def events(self):
        # game loop events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        # game loop updates
        self.all_sprites.update()  # special method that will update all sprites

    def draw(self):
        self.screen.fill("black")
        self.all_sprites.draw(self.screen)  # draw all sprites on the screen
        self.clock.tick(FPS)
        pygame.display.update()

    def main(self):
        # game loop
        while self.playing:
            self.events()
            self.update()
            self.draw()

        self.running = False

    def game_over(self):
        pass

    def intro_screen(self):
        pass


g = Game()
g.intro_screen()
g.new()
while g.running:
    g.main()
    g.game_over()

pygame.quit()
# sys.exit() # to exit from python


# #################################################################################
# player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
#
#
# while running:
#     # creating situation when user press X, and quiting game
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#     screen.fill("black")
#     # game rendering
# #################################################################################
#     # p.char_movement()  # character an his movement keys
#     # lb.borders(player_pos, height, width)
#     pygame.draw.circle(screen, "red", player_pos, 40)
#
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_w]:
#         player_pos.y -= 300 * dt
#     if keys[pygame.K_s]:
#         player_pos.y += 300 * dt
#     if keys[pygame.K_a]:
#         player_pos.x -= 300 * dt
#     if keys[pygame.K_d]:
#         player_pos.x += 300 * dt
#
# #################################################################################
#     # Screen output
#
#     pygame.display.flip()
#
#     dt = clock.tick(60) / 1000
#
# pygame.quit()
