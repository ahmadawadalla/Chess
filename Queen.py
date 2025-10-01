import pygame, os, sys
from Rook import Rook
from Bishop import Bishop

def resource_path(relative_path):
    """Get absolute path to resource, works in dev and when bundled"""
    if hasattr(sys, "_MEIPASS"):
        # PyInstaller stores files here
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

class Queen:
    def __init__(self, color):
        self.color = color
        self.has_moved = False
        self.just_moved = False

    def is_legal(self, curr_row,curr_col,next_row,next_col, grid, do_not_take):
        r = Rook(self.color)
        b = Bishop(self.color)
        return r.is_legal(curr_row,curr_col,next_row,next_col,grid, do_not_take) or b.is_legal(curr_row,curr_col,next_row,next_col,grid, do_not_take)


    def get_image(self):
        if self.color == 'b':
            return pygame.image.load(resource_path('Images/queen_b.png'))
        return pygame.image.load(resource_path('Images/queen_w.png'))