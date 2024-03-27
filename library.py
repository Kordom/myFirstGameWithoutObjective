import pygame


class Character:
    def __init__(self, player_pos, dt, screen):
        self.player_pos = player_pos
        self.dt = dt
        self.screen = screen

    def char_movement(self):
        keys = pygame.key.get_pressed()
        pygame.draw.circle(self.screen, "white", self.player_pos, 40)
        if keys[pygame.K_w]:
            self.player_pos.y -= 300 * self.dt
        if keys[pygame.K_s]:
            self.player_pos.y += 300 * self.dt
        if keys[pygame.K_a]:
            self.player_pos.x -= 300 * self.dt
        if keys[pygame.K_d]:
            self.player_pos.x += 300 * self.dt

# def borders(player_pos,height, width):
#     if player_pos.y > height:
#         player_pos.y = height
