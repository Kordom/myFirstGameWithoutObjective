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

        self.character_spritesheet = Spritessheet("img/character.png")
        self.terrain_spritesheet = Spritessheet("img/terrain.png")
        self.enemy_spritesheet = Spritessheet("img/enemy.png")
        self.font = pygame.font.Font("img/CookieCrisp-L36ly.ttf",60)
        self.intro_background = pygame.image.load("img/my/bg.png")
        # self.button_bg = pygame.image.load("img/my/butnbg.png")

    def createTileMap(self):
        for i, row in enumerate(tilemap):  # numerating rows
            for j, column in enumerate(row):  # numerating elements inside string
                Ground(self, j, i)
                if column == "B":
                    Block(self, j, i)
                if column == "P":
                    Player(self, j, i)
                if column == "E":
                    Enemy(self, j, i)


    def new(self):

        # new game starts
        self.playing = True
        self.all_sprites = pygame.sprite.LayeredUpdates()  # contains all sprites (walls,enem,allow to update allatonce)
        self.blocks = pygame.sprite.LayeredUpdates()  # contains wallls
        self.enemies = pygame.sprite.LayeredUpdates()  # contains enemies
        self.attacks = pygame.sprite.LayeredUpdates()  # attaks and animations

        self.createTileMap()  #map creation



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
        intro = True

        title = self.font.render('Black Whisper',True, "black")
        title_rect = title.get_rect(x=250, y=200)

        play_button = Button(350,800,400,60,"white","black" , content_,50)


        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    intro = False
                    self.running = False
            mouse_pos = pygame.mouse.get_pos()  # gets position of mouse on the screen
            mouse_pressed = pygame.mouse.get_pressed()
            if play_button.is_pressed(mouse_pos, mouse_pressed):
                intro = False
            self.screen.blit(self.intro_background, (0,0))
            self.screen.blit(title, title_rect)
            self.screen.blit(play_button.image, play_button.rect)
            self.clock.tick(FPS)
            pygame.display.update()

g = Game()
g.intro_screen()
g.new()
while g.running:
    g.main()
    g.game_over()

pygame.quit()

