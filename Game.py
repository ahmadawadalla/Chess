import pygame
from Board import Board

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Chess Game")

    GRID_WIDTH = 800
    GRID_HEIGHT = 800
    CELL_SIZE = (GRID_WIDTH * GRID_HEIGHT) / 64

    screen = pygame.display.set_mode((GRID_WIDTH,GRID_HEIGHT))
    start_noise = pygame.mixer.Sound("Sounds/notify.mp3")
    pygame.mixer.Sound.play(start_noise)
    board = Board(screen,GRID_WIDTH,GRID_HEIGHT,CELL_SIZE)
    board.draw()