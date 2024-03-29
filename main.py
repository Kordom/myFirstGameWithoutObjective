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

    def createTileMap(self):
        for i, row in enumerate(tilemap):  # numerating rows
            for j, column in enumerate(row):  # numerating elements inside string
                if column == "B":
                    Block(self, j, i)
                if column == "P":
                    Player(self, j, i)


    def new(self):

        # new game starts
        self.playing = True
        self.all_sprites = pygame.sprite.LayeredUpdates()  # contains all sprites (walls,enem,allow to update allatonce)
        self.blocks = pygame.sprite.LayeredUpdates()  # contains wallls
        self.enemies = pygame.sprite.LayeredUpdates()  # contains enemies
        self.attaks = pygame.sprite.LayeredUpdates()  # attaks and animations

        self.createTileMap()



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

