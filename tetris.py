import pygame as pg
import random
from settings import sq_size as size,colors
from block import Block
from collections import deque
from queue import Queue


class Tetris():
    def __init__(self, grid_leghth_width, grid_length_height):
        self.score = 0
        self.grid_length_width = grid_leghth_width
        self.grid_length_height = grid_length_height
        self.block_queue = deque(maxlen=2) #blockqueue.pop
        self.current_block = None   #Remember to add the initial block
        self.field = self.create()
        self.game_state = "playing"
        # self.next_field = self.create_next()

    def create(self):
        field = []
        block1 = Block()
        block2 = Block()

        for x in range(self.grid_length_width):
            field.append([])
            for y in range(self.grid_length_height):
                tile = self.grid_to_field(x,y)
                field[x].append(tile)

        self.block_queue.append(block1)
        self.block_queue.append(block2)

        return field
    # def create_next(self):
    #     field = []
    #     # block = self.get_next()
    #     next_block = self.block_queue[1]
    #     for x in range(4):
    #         field.append([])
    #         for y in range(4):
    #             tile = self.grid_to_field(x, y)
    #             field[x].append(tile)
    #     for i1 in range(4):
    #         for j1 in range(4):
    #             if i1+j1*4 in next_block.image():
    #                 field[i1][j1]['color'] = 7 #GRAY
    #     out = {
    #         "field": field,
    #         "type": next_block.type,
    #         "block": next_block
    #     }
    #     return out

    def grid_to_field(self, x, y):
        rect = [
            (x * size, y * size),
            (x * size + size,y * size),
            (x * size + size, y * size + size),
            (x * size,y * size + size)
        ]
        color = None
        out = {
            "grid": [x,y],
            "rect": rect,
            "color": color
        }
        return out

    def add_block(self):
        print("adding")
        self.current_block = self.block_queue.pop()
        new_block = Block()
        self.block_queue.append(new_block)

    def collide(self):
        collided = False
        for i in range(4):
            for j in range(4):
                if i + j*4 in self.current_block.image():
                    if j + self.current_block.y > self.grid_length_height - 1 or \
                            i + self.current_block.x > self.grid_length_width - 1 or \
                            i + self.current_block.x < 0 or \
                            self.field[i + self.current_block.x][j + self.current_block.y]["color"] is not None: #might have logic error here, attention
                        collided = True
        return collided

    def anchor(self):
        ''' Fix the position of the current block'''
        for i in range(4):
            for j in range(4):
                if i + j*4 in self.current_block.image():
                    self.field[i + self.current_block.x][j + self.current_block.y]["color"] = self.current_block.color
        self.break_line()
        self.add_block()
        if self.collide():
            self.game_state = "gameover"

    def side_step(self, value):
        old = self.current_block.x
        self.current_block.x += value
        if self.collide():
            self.current_block.x = old

    def break_line(self):
        lines_count = 0
        for y in range(1,self.grid_length_height):
            valid = True
            for x in range(self.grid_length_width):
                if self.field[x][y]["color"] == None:
                    valid = False
            if valid:
                lines_count += 1
                for i in range(y, 1, -1):
                    for j in range(self.grid_length_width):
                        self.field[j][i]["color"] = self.field[j][i-1]["color"]
        self.score += lines_count

    def rotate(self):
        old = self.current_block.rotation
        self.current_block.rotate()
        if self.collide():
            self.current_block.rotation = old

    def go_down(self):
        self.current_block.y += 1
        if self.collide():
            self.current_block.y -= 1
            self.anchor()

    def rush(self):
        while not self.collide():
            self.current_block.y += 1
        self.current_block.y -= 1
        self.anchor()

    # def get_next(self):
    #     next_block = self.block_queue[1]
    #     return next_block






