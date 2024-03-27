import pygame
import library as lb
#################################################################################
# creating setup
pygame.init()
height, width = 1980, 1080
screen = pygame.display.set_mode((height, width))
# fscreen = pygame.display.toggle_fullscreen()
clock = pygame.time.Clock()
dt = 0  #  delta time in second since last frame used for independent physics

#################################################################################
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

running = True
while running:
    # creating situation when user press X, and quiting game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")
    # game rendering
#################################################################################
    # p.char_movement()  # character an his movement keys
    # lb.borders(player_pos, height, width)
    pygame.draw.circle(screen, "red", player_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

#################################################################################
    # Screen output

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()






