import pygame


class Pawn:
    def __init__(self, color,):
        self.color = color
        self.has_moved = False


    def is_legal(self, curr_row,curr_col,next_row,next_col, grid):
        if self.color == 'w':
            return self.is_legal_w(curr_row,curr_col,next_row,next_col, grid)
        else:
            return self.is_legal_b(curr_row,curr_col,next_row,next_col, grid)


    def is_legal_w(self, curr_row,curr_col,next_row,next_col, grid):
        col_moved = next_col - curr_col
        row_moved = -1 * (next_row - curr_row)

        if col_moved > 1 or row_moved > 2 or col_moved < -1 or row_moved <= 0:
            return False

        elif col_moved == 1 or col_moved == -1:
            if row_moved == 1 and grid[curr_row - 1][curr_col + col_moved] is not None:
                return True # captures
            # check for en croissant
            return False

        elif row_moved == 2:
            if self.has_moved:
                return False
            for i in range(1,3):
                if grid[curr_row - i][curr_col] is not None:
                    return False
            self.has_moved = True
            return True

        else: #it moved up 1
            if grid[curr_row - 1][curr_col] is not None:
                return False
            self.has_moved = True
            return True

    def is_legal_b(self, curr_row,curr_col,next_row,next_col, grid):
        col_moved = next_col - curr_col
        row_moved = -1 * (next_row - curr_row)

        if col_moved > 1 or row_moved < -2 or col_moved < -1 or row_moved >= 0:
            return False

        elif col_moved == 1 or col_moved == -1:
            if row_moved == -1 and grid[curr_row + 1][curr_col + col_moved] is not None:
                return True # captures
            # check for en croissant
            return False

        elif row_moved == -2:
            if self.has_moved:
                return False
            for i in range(1,3):
                if grid[curr_row + i][curr_col] is not None:
                    return False
            self.has_moved = True
            return True

        else: #it moved down 1
            if grid[curr_row + 1][curr_col] is not None:
                return False
            self.has_moved = True
            return True

    def get_image(self):
        if self.color == 'b':
            return pygame.image.load('Images/pawn_b.png')
        return pygame.image.load('Images/pawn_w.png')
