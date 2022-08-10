import pygame as pg
from tetris import Tetris as tr
from game import Game as g

def main():
    running = True
    playing = True

    #initiate the game
    pg.init()
    clock = pg.time.Clock()
    screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)


    #Title and Icon
    pg.display.set_caption("Tetris: Homemade Edition")
    # icon = pygame.image.load(os.path.join(path,'icon.png'))
    # pygame.display.set_icon(icon)

    #Implement game
    game = g(screen,clock)

    while running:
        #add game menu
        while playing:
            game.run()

if __name__ == "__main__":
    main()

