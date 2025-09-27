class Rook:
    def __init__(self, color):
        self.color = color
        self.has_moved = False

    def is_legal(self,curr_row,curr_col,next_row,next_col, grid):
        if curr_col == next_col and curr_row != next_row:
            # y-direction
            for i in range(1,abs(curr_row - next_row)):
                row = int(curr_row + (i * (next_row - curr_row)/abs(next_row - curr_row)))
                if grid[row][curr_col] is not None:
                    return False
            self.has_moved = True
            return True
        elif curr_row == next_row and curr_col != next_col:
            # x-direction
            for i in range(1,abs(curr_col - next_col)):
                col = int(curr_col + (i * (next_col - curr_col)/abs(next_col - curr_col)))
                if grid[curr_row][col] is not None:
                    return False
            self.has_moved = True
            return True
        else: return False