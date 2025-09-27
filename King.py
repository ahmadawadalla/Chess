class King:
    def __init__(self, color):
        self.color = color
        self.has_moved = False


    def is_legal(self, curr_row,curr_col,next_row,next_col, grid):
        x_moved = next_col - curr_col
        y_moved = -1 * (next_row - curr_row)

        if x_moved > 1 or x_moved < -1 or y_moved > 1 or y_moved < -1:
            return False

        if grid[curr_row - y_moved][curr_col + x_moved] is None:
            self.has_moved = True
            return True
        return False