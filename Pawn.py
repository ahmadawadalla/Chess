import pygame, os, sys

def resource_path(relative_path):
    """Get absolute path to resource, works in dev and when bundled"""
    if hasattr(sys, "_MEIPASS"):
        # PyInstaller stores files here
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

class Pawn:
    def __init__(self, color):
        self.color = color
        self.has_moved = False
        self.moved_up_two = False
        self.just_moved = False

    def is_legal(self, curr_row,curr_col,next_row,next_col, grid, do_not_take):
        if self.color == 'w':
            return self.is_legal_w(curr_row,curr_col,next_row,next_col, grid,do_not_take)
        else:
            return self.is_legal_b(curr_row,curr_col,next_row,next_col, grid, do_not_take)


    def is_legal_w(self, curr_row,curr_col,next_row,next_col, grid, do_not_take):
        col_moved = next_col - curr_col
        row_moved = -1 * (next_row - curr_row)

        if col_moved > 1 or row_moved > 2 or col_moved < -1 or row_moved <= 0:
            return False

        elif col_moved == 1 or col_moved == -1:
            if row_moved == 1 and grid[curr_row - 1][curr_col + col_moved] is not None:
                return True # captures
            # check for en croissant
            if curr_row == 3 and row_moved == 1: # if we are on row 3
                if col_moved == 1:
                    adj_piece = grid[3][curr_col + 1]
                    if isinstance(adj_piece, Pawn): # if the piece next to you is a pawn
                        if adj_piece.moved_up_two and adj_piece.color != self.color and adj_piece.just_moved: # if it moved up twice and is black and it just moved
                            if do_not_take:
                                return True
                            grid[3][curr_col + 1] = None
                            return grid

                elif col_moved == -1:
                    adj_piece = grid[3][curr_col - 1]
                    if isinstance(adj_piece, Pawn): # if the piece next to you is a pawn
                        if adj_piece.moved_up_two and adj_piece.color != self.color and adj_piece.just_moved: # if it moved up twice and is black and it just moved
                            if do_not_take:
                                return True
                            grid[3][curr_col - 1] = None
                            return grid

            return False

        elif row_moved == 2:
            if self.has_moved:
                return False
            for i in range(1,3):
                if grid[curr_row - i][curr_col] is not None:
                    return False
            self.has_moved = True
            self.moved_up_two = True
            return True

        else: #it moved up 1
            if grid[curr_row - 1][curr_col] is not None:
                return False
            self.has_moved = True
            return True

    def is_legal_b(self, curr_row,curr_col,next_row,next_col, grid, do_not_take):
        col_moved = next_col - curr_col
        row_moved = -1 * (next_row - curr_row)

        if col_moved > 1 or row_moved < -2 or col_moved < -1 or row_moved >= 0:
            return False

        elif col_moved == 1 or col_moved == -1:
            if row_moved == -1 and grid[curr_row + 1][curr_col + col_moved] is not None:
                return True # captures
            # check for en croissant
            if curr_row == 4 and row_moved == -1: # if we are on row 3
                if col_moved == 1:
                    adj_piece = grid[4][curr_col + 1]
                    if isinstance(adj_piece, Pawn): # if the piece next to you is a pawn
                        if adj_piece.moved_up_two and adj_piece.color != self.color and adj_piece.just_moved: # if it moved up twice and is black and it just moved
                            if do_not_take:
                                return True
                            grid[4][curr_col + 1] = None
                            return grid

                elif col_moved == -1:
                    adj_piece = grid[4][curr_col - 1]
                    if isinstance(adj_piece, Pawn): # if the piece next to you is a pawn
                        if adj_piece.moved_up_two and adj_piece.color != self.color and adj_piece.just_moved: # if it moved up twice and is black and it just moved
                            if do_not_take:
                                return True
                            grid[4][curr_col - 1] = None
                            return grid

            return False

        elif row_moved == -2:
            if self.has_moved:
                return False
            for i in range(1,3):
                if grid[curr_row + i][curr_col] is not None:
                    return False
            self.has_moved = True
            self.moved_up_two = True
            return True

        else: #it moved down 1
            if grid[curr_row + 1][curr_col] is not None:
                return False
            self.has_moved = True
            return True

    def get_image(self):
        if self.color == 'b':
            return pygame.image.load(resource_path('Images/pawn_b.png'))
        return pygame.image.load(resource_path('Images/pawn_w.png'))
