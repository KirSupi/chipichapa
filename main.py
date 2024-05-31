import sys
import pygame

from game import game

if __name__ == '__main__':
    pygame.init()

    game.run()

    pygame.quit()
    sys.exit()
