import pygame

class Player(pygame. sprite. Sprite):
    def __init__(self,pos,speed):
        super().__init__()
        self.image = pygame.Surface((32,64))
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft =pos)
        self.direction = pygame.math.Vector2(0,0)
        self.speed = speed

    def move(self,spd):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]: self.direction.y = -1
        elif keys[pygame.K_DOWN]: self.direction.y = 1
        else: self.direction.y = 0

        if keys[pygame.K_RIGHT]: self.direction.x = 1
        elif keys[pygame.K_LEFT]: self.direction.x = -1
        else: self.direction.x = 0

        self.rect.x += self.direction.x * spd
        self.rect.y += self.direction.y * spd
        print(f"{self.speed}")

    def update(self,spd):
        self.move(spd)
