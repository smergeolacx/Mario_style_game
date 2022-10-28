import pygame
from sys import exit
from settings import *
from levels import *

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
level = Level(level_map, screen)

while True:
    key = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or key[pygame.K_q]:
            pygame.quit()
            exit()

    screen.fill('black')
    level.run()

    pygame.display.update()
    clock.tick(60)