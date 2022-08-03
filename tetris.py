import pygame as pg
import random
from settings import sq_size as size
from block import Block

class Tetris():
    def __init__(self, grid_leghth_width, grid_length_height):
        self.score = 0
        self.grid_length_width = grid_leghth_width
        self.grid_length_height = grid_length_height
        self.field = self.create()

    def create(self):
        field = []

        for x in range(self.grid_length_width):
            field.append([])
            for y in range(self.grid_length_height):
                tile = self.grid_to_field(x,y)
                field[x].append(tile)

        return field

    def grid_to_field(self, x, y):
        rect = [
            (x * size, y * size),
            (x*size + size,y * size),
            (x*size + size, y * size + size),
            (x*size,y * size + size)
        ]

        out = {
            "grid": [x,y],
            "rect": rect
        }
        return out




