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
            while self.Tetris.game_state != "gameover":
                self.clock.tick(5)
                self.events()
                self.update()
                self.draw()
            self.gameover()

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


    def gameover(self):
        self.clock.tick(0)
        draw_text(self.screen, "Game over", 20, (255, 0, 0), (20, 200))

    def draw(self):
        self.screen.fill((255,255,255))
        #Draw field, and anchored blocks
        for x in range(self.Tetris.grid_length_width):
            for y in range(self.Tetris.grid_length_height):
                coor = self.Tetris.field[x][y]["rect"]
                block_color = self.Tetris.field[x][y]["color"]
                sq = pg.Rect(coor[0][0] + 800, coor[0][1] + 250 ,size -1,size -1)
                if block_color is not None:
                    pg.draw.rect(self.screen, colors[block_color], sq, 0)
                else:
                    pg.draw.rect(self.screen, (0,0,0), sq, 1)

        #Draw next block field
        # next_field = self.Tetris.create_next()
        # for i_next in range(4):
        #     for j_next in range(4):
        #         rect = next_field["field"][i_next][j_next]["rect"]
        #         color_next = next_field["block"][i_next][j_next]["color"]
        #         next_grid = pg.Rect(rect[0][0] + 1200, rect[0][1] + 250, size -1, size -1)
        #         if block_color is not None:
        #             pg.draw.rect(self.screen, colors[color_next], sq, 0)
        #         else:
        #             pg.draw.rect(self.screen, (0,0,0), next_grid, 1)


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
        #Draw score
        draw_text(self.screen,"Score: " + str(self.Tetris.score),20,(255,0,0),(800,55))
        #Draw FPS
        draw_text(self.screen,'fps={}'.format(round(self.clock.get_fps())),20,(255,0,0),(5,55))
        pg.display.flip()

