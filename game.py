import pygame
from config import *
from sprites2 import *


class Spritessheet:
    # for cutting from sheet
    def __init__(self, file):
        self.sheet = pygame.image.load(file).convert()

    def get_sprite(self, x, y, width, height):
        sprite = pygame.Surface([width, height])
        sprite.blit(self.sheet, (0, 0), (x, y, width, height))  # makes cutout from big image
        sprite.set_colorkey("black")
        return sprite

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((HEIGHT, WIDTH))
        self.clock = pygame.time.Clock()
        self.running = True
        self.playing = True
        # self.dt = self.clock.tick(FPS) / 1000  # time delta
        # self.player_pos = pygame.Vector2(self.screen.get_width() / 2, self.screen.get_height() / 2)
        self.character_spritesheet = Spritessheet("pirate/char.png")
        self.terrain_spritesheet = Spritessheet("img/my/tiles.png")
        self.enemy_spritesheet = Spritessheet("img/enemy.png")
        self.font = pygame.font.Font("img/CookieCrisp-L36ly.ttf", 60)
        self.intro_background = pygame.image.load("img/my/bg.png")
        self.button_bg = pygame.image.load("img/my/butnbg.png")
        self.game_over_bg = pygame.transform.scale2x(pygame.image.load("img/gameover.png"))
        # self.ship = pygame.transform.scale2x(pygame.image.load("img/my/ship.png"))
        self.ship2 = Spritessheet("img/my/ship2.png")
        self.attack_spritesheet = Spritessheet("img/attack.png")
        self.sea = pygame.image.load("img/my/sea.jpg")

        self.target = pygame.image.load("img/my/marker.png")

    def background(self):
        size = pygame.transform.scale(self.intro_background, (1800, 1800))
        self.screen.blit(size, (0, 0))

    def createTileMap(self):
        for i, row in enumerate(tilemap):  # numerating rows
            for j, column in enumerate(row):  # numerating elements inside string
                if column =="S":
                    Ground(self, j, i)
                if column == "B":
                    Block(self, j, i)
                if column == "P":
                    self.player = Player(self, j, i)
                # if column == "E":
                #     Enemy(self, j, i)

    def new(self):
        # new game starts
        self.playing = True
        self.all_sprites = pygame.sprite.LayeredUpdates()  # contains all sprites (walls,enem,allow to update allatonce)
        self.blocks = pygame.sprite.LayeredUpdates()  # contains wallls
        self.enemies = pygame.sprite.LayeredUpdates()  # contains enemies
        self.attacks = pygame.sprite.LayeredUpdates()  # attaks and animations

        self.createTileMap()  # map creation

    def main(self):
        # game loop
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        # game loop events
        attack = Attack(self, self.player.rect.x,self.player.rect.y)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.player.facing == "up":
                    Attack(self, self.player.rect.x, (self.player.rect.y - TILE_SIZE))
                if self.player.facing == "down":
                    Attack(self, self.player.rect.x, (self.player.rect.y + TILE_SIZE))
                if self.player.facing == "left":
                    Attack(self, (self.player.rect.x - TILE_SIZE), self.player.rect.y)
                if self.player.facing == "right":
                    Attack(self, (self.player.rect.x + TILE_SIZE), self.player.rect.y)

    def update(self):
        # game loop updates
        self.all_sprites.update()  # special method that will update all sprites

    def draw(self):
        size = pygame.transform.scale(self.sea, (1800, 1800))
        self.screen.blit(size, (0, 0))
        self.all_sprites.draw(self.screen)  # draw all sprites on the screen
        self.clock.tick(FPS)
        pygame.display.update()

    def game_over(self):

        text = self.font.render("No, no, no i think my story was different ", True, "White")
        text_rect = text.get_rect(center=(WIDTH/2, HEIGHT/2))

        restart_button = Button(20, 710, 430, 135, "white", "black", "Again", 32)
        quit_button = Button(20, 860, 430, 135,"white", "black", "Tired of listening", 32)

        for sprite in self.all_sprites:
            sprite.kill()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False


            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if restart_button.is_pressed(mouse_pos, mouse_pressed):
                self.new()
                self.main()
            if quit_button.is_pressed(mouse_pos, mouse_pressed):
                self.running = False
                self.playing = False

            self.screen.blit(self.game_over_bg, (0, 0))
            self.screen.blit(text, text_rect)
            self.screen.blit(self.button_bg, (20, 680))
            self.screen.blit(self.button_bg, (20, 530))
            self.screen.blit(restart_button.image, restart_button.rect)
            self.screen.blit(quit_button.image, quit_button.rect)


            self.clock.tick(FPS)
            pygame.display.update()

    def intro_screen(self):
        intro = True

        title = self.font.render('Black Whisper', True, "black")
        title_rect = title.get_rect(x=250, y=200)

        play_button = Button(550, 865, 430, 135, "white", "black", content_, 50)

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    intro = False
                    self.running = False
            mouse_pos = pygame.mouse.get_pos()  # gets position of mouse on the screen
            mouse_pressed = pygame.mouse.get_pressed()
            if play_button.is_pressed(mouse_pos, mouse_pressed):
                intro = False
            self.screen.blit(self.intro_background, (0, 0))
            self.screen.blit(title, title_rect)
            self.screen.blit(self.button_bg, (500, 680))
            self.screen.blit(play_button.image, play_button.rect)
            self.clock.tick(FPS)
            pygame.display.update()

g = Game()
g.intro_screen()
g.new()
while g.running:

    g.events()

    g.main()

    g.game_over()
pygame.quit()