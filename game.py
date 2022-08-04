import pygame as pg
import sys
from tetris import Tetris
from settings import sq_size as size, colors, draw_text

class Game:
    def __init__(self,screen, clock):
        self.screen = screen
        self.clock = clock
        self.width, self.height = self.screen.get_size()

        self.Tetris = Tetris(10,20)

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(5)
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()
                if event.key == pg.K_UP:
                    self.Tetris.rotate()
                if event.key == pg.K_LEFT:
                    self.Tetris.side_step(-1)
                if event.key == pg.K_RIGHT:
                    self.Tetris.side_step(1)
                if event.key == pg.K_DOWN:
                    self.Tetris.rush()


    def update(self):
        if self.Tetris.current_block is None:
            self.Tetris.add_block()
        self.Tetris.go_down()
        print(self.Tetris.current_block.x, self.Tetris.current_block.y)




    def draw(self):
        self.screen.fill((255,255,255))

        #Draw field, and anchored blocks
        for x in range(self.Tetris.grid_length_width):
            for y in range(self.Tetris.grid_length_height):
                coor = self.Tetris.field[x][y]["rect"]
                block_color = self.Tetris.field[x][y]["color"]
                sq = pg.Rect(coor[0][0] + 800, coor[0][1] + 250 ,size,size)
                if block_color is not None:
                    pg.draw.rect(self.screen, colors[block_color], sq, 0)
                else:
                    pg.draw.rect(self.screen, (0,0,0), sq, 1)

        #Draw current block
        if self.Tetris.current_block is not None:
            for i in range(4):
                for j in range(4):
                    pointer = i*4 + j
                    if pointer in self.Tetris.current_block.image():
                        pg.draw.rect(self.screen, colors[self.Tetris.current_block.color],
                                         [ (j + self.Tetris.current_block.x)*size + 800 ,
                                           (i + self.Tetris.current_block.y)*size + 250 ,
                                          size-2, size-2],0)

        #Draw FPS
        draw_text(self.screen,'fps={}'.format(round(self.clock.get_fps())),20,(255,0,0),(5,55))
        pg.display.flip()

