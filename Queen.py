import pygame

from Rook import Rook
from Bishop import Bishop

class Queen:
    def __init__(self, color):
        self.color = color
        self.has_moved = False


    def is_legal(self, curr_row,curr_col,next_row,next_col, grid):
        r = Rook(self.color)
        b = Bishop(self.color)
        return r.is_legal(curr_row,curr_col,next_row,next_col,grid) or b.is_legal(curr_row,curr_col,next_row,next_col,grid)


    def get_image(self):
        if self.color == 'b':
            return pygame.image.load('Images/queen_b.png')
        return pygame.image.load('Images/queen_w.png')