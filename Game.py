import pygame
from Board import Board
import os, sys

def resource_path(relative_path):
    """Get absolute path to resource, works in dev and when bundled"""
    if hasattr(sys, "_MEIPASS"):
        # PyInstaller stores files here
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Chess Game")

    GRID_WIDTH = 800
    GRID_HEIGHT = 800
    CELL_SIZE = (GRID_WIDTH * GRID_HEIGHT) / 64

    screen = pygame.display.set_mode((GRID_WIDTH,GRID_HEIGHT))
    start_noise = pygame.mixer.Sound(resource_path("Sounds/notify.mp3"))
    pygame.mixer.Sound.play(start_noise)
    board = Board(screen,GRID_WIDTH,GRID_HEIGHT,CELL_SIZE)
    board.draw()