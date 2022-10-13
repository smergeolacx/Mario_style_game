import pygame
from tiles import Tile
from settings import *

class Level:
    def __init__(self,level_data,surface):
        self.display_surface = surface
        self.setup_level(level_data)

    def setup_level(self,layout):
        self.tiles = pygame.sprite.Group()
        for row_ind,row in enumerate(layout):
            for col_ind,cell in enumerate(row):
                if cell == "X":
                    x = col_ind * tile_size
                    y = row_ind * tile_size
                    tile = Tile((x,y),tile_size)
                    self.tiles.add(tile)
                    # print(tile)
    def run(self):
        self.tiles.draw(self.display_surface)