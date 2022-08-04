import pygame as pg
from settings import colors
from random import randint
"""
    4x4 matrix of block
    *---*---*---*---*
    * 0 * 1 * 2 * 3 *
    *---*---*---*---*
    * 4 * 5 * 6 * 7 *
    *---*---*---*---*
    * 8 * 9 * 10*11*
    *---*---*---*---*
    * 12* 13 *14* 15*
    
"""
class Block():
    blocks = [
        [[1, 5, 9, 13], [4, 5, 6, 7]],
        [[4, 5, 9, 10], [2, 6, 5, 9]],
        [[6, 7, 9, 10], [1, 5, 6, 10]],
        [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
        [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],
        [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],
        [[1, 2, 5, 6]],
    ]

    def __init__(self):
        #starting position
        self.x = 3
        self.y = 0
        self.type = randint(0, len(self.blocks) - 1)
        self.color = randint(1, len(colors) - 1)
        self.rotation = 0


    def image(self):
        return self.blocks[self.type][self.rotation]

    def rotate(self):
        self.rotation = (self.rotation + 1) % len(self.blocks[self.type])