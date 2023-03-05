import pygame
from tiles import Tile
from player import Player
from settings import *

class Level:
    def __init__(self,level_data,surface):
        self.display_surface = surface
        self.world_shift = 0
        self.setup_level(level_data)

    def setup_level(self,layout):
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
                    play = Player((x, y))
                    self.player.add(play)

    def scroll(self):
        player = self.player.sprite

        if player.rect.centerx < 200 and player.direction.x < 0:
            self.world_shift = 8
            player.speed = 0
        elif player.rect.centerx > 1000 and player.direction.x > 0:
            self.world_shift = -8
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 8

    def horizontal_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                if player.direction.x > 0:
                    player.rect.right = sprite.rect.left
    
    def vertical_collision(self):
        player = self.player.sprite
        
        player.grav()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                if player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0

    def run(self):
        self.tiles.draw(self.display_surface)
        self.tiles.update(self.world_shift)

        self.player.update()
        self.player.draw(self.display_surface)
        self.horizontal_collision()
        self.vertical_collision()
        self.scroll()

        