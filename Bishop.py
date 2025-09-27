class Bishop:
    def __init__(self, color):
        self.color = color
        self.has_moved = False


    def is_legal(self, curr_row,curr_col,next_row,next_col, grid):
        if abs(next_col - curr_col) != abs(next_row - curr_row):
            return False

        for i in range(1,abs(next_col - curr_col) + 1):
            row = int(curr_row + (i * (next_row - curr_row)/abs(next_row - curr_row)))
            col = int(curr_col + (i * (next_col - curr_col)/abs(next_col - curr_col)))
            if grid[row][col] is not None:
                return False
        self.has_moved = True
        return True