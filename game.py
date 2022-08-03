import pygame as pg
import sys
from tetris import Tetris
from settings import sq_size as size, colors

class Game:
    def __init__(self,screen, clock):
        self.screen = screen
        self.clock = clock
        self.width, self.height = self.screen.get_size()

        self.Tetris = Tetris(10,20)

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(60)
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

    def update(self):
        pass

    def draw(self):
        self.screen.fill((255,255,255))

        #Draw field
        for x in range(self.Tetris.grid_length_width):
            for y in range(self.Tetris.grid_length_height):
                coor = self.Tetris.field[x][y]["rect"]
                sq = pg.Rect(coor[0][0] + 800, coor[0][1] + 250 ,size,size)
                pg.draw.rect(self.screen, (0,0,0), sq, 1)

        pg.display.flip()

