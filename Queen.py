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