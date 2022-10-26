import pygame
import pymunk

class Player(pygame. sprite. Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = pygame.Surface((32,64))
        self.image.fill('red')
        self.rect = self. image.get_rect(topleft =pos)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.y -=10
        if keys[pygame.K_DOWN]:
            self.rect.y +=10
        if keys[pygame.K_RIGHT]:
            self.rect.x +=10
        if keys[pygame.K_LEFT]:
            self.rect.x -=10

    def update(self):
        self.move()