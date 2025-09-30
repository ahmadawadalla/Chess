import pygame


class King:
    def __init__(self, color):
        self.color = color
        self.has_moved = False
        self.just_moved = False



    def is_legal(self, curr_row,curr_col,next_row,next_col, grid, do_not_take):
        x_moved = next_col - curr_col
        y_moved = -1 * (next_row - curr_row)

        if not self.has_moved and next_row == curr_row:
            if next_col == 2 and grid[curr_row][0] and not grid[curr_row][0].has_moved:
                for i in range(1,3):
                    if grid[curr_row][curr_col - i]:
                        return False

                if not do_not_take: # move the rook
                    grid[curr_row][3] = grid[curr_row][0]
                    grid[curr_row][0] = None


                self.has_moved = True
                return True

            elif next_col == 6 and grid[curr_row][7] and not grid[curr_row][7].has_moved:
                for i in range(1,3):
                    if grid[curr_row][curr_col + i]:
                        return False

                if not do_not_take: # move the rook
                    grid[curr_row][5] = grid[curr_row][7]
                    grid[curr_row][7] = None

                self.has_moved = True
                return True

        if x_moved > 1 or x_moved < -1 or y_moved > 1 or y_moved < -1:
            return False

        if (grid[curr_row - y_moved][curr_col + x_moved] is None or
                grid[curr_row - y_moved][curr_col + x_moved].color != self.color):
            self.has_moved = True
            return True
        return False

    def get_image(self):
        if self.color == 'b':
            return pygame.image.load('Images/king_b.png')
        return pygame.image.load('Images/king_w.png')