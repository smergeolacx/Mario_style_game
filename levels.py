import pygame
from tiles import Tile
from player import Player
from settings import *

class Level:
    def __init__(self,level_data,surface):
        self.display_surface = surface
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

    def collision(self):
        for sprite in self.tiles.sprites():
            pass

    def run(self):
        self.tiles.draw(self.display_surface)
        self.player.draw(self.display_surface)
        self.player.update()
        self.tiles.update(0)
