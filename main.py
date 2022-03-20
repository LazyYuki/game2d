import pygame, settings
from game import *

pygame.init()

screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
clock = pygame.time.Clock()

g = game(screen)

while True:
    dt = clock.tick(settings.FPS)
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill(settings.BLACK)

    g.update(dt, keys)
    g.draw()

    pygame.display.update()