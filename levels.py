import pygame
from tiles import Tile
from player import Player
from settings import *

class Level:
    def __init__(self,level_data,surface):
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0

    def setup_level(self,layout):
        self.speed = 8
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        for row_ind,row in enumerate(layout):
            for col_ind,cell in enumerate(row):
                x = col_ind * tile_size
                y = row_ind * tile_size
                if cell == "X":
                    tile = Tile((x,y),tile_size)
                    self.tiles.add(tile)
                if cell == "P":
                    play = Player((x, y),self.speed)
                    self.player.add(play)

    def scroll(self):
        keys = pygame.key.get_pressed()
        player = self.player.sprite

        if player.rect.x < 250 and keys[pygame.K_LEFT]:
            self.speed = 0 ; self.world_shift = -8

        elif player.rect.x > 1000 and keys[pygame.K_RIGHT]:
            self.speed = 0 ; self.world_shift = 8

        else:
            self.speed = 8 ; self.world_shift = 0

    def collision(self):
        player = self.player.sprite
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                print(True)

    def run(self):
        self.tiles.draw(self.display_surface)
        self.player.draw(self.display_surface)
        self.player.update(self.speed)
        # self.collision()
        self.scroll()
        self.tiles.update(self.world_shift)
