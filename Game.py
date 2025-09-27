import pygame
from Board import Board

if __name__ == '__main__':
    pygame.init()
    GRID_WIDTH = 800
    GRID_HEIGHT = 800
    CELL_SIZE = (GRID_WIDTH * GRID_HEIGHT) / 64

    screen = pygame.display.set_mode((GRID_WIDTH,GRID_HEIGHT))

    board = Board(screen,GRID_WIDTH,GRID_HEIGHT,CELL_SIZE)
    board.draw()

