class Knight:
    def __init__(self, color):
        self.color = color
        self.has_moved = False

    def is_legal(self,curr_row,curr_col,next_row,next_col, grid):
        legal_moves = [[1,2],[-1,2],[1,-2],[-1,-2], [2,-1], [2,1], [-2,-1], [-2,1]] # x,y

        col_moved = next_col - curr_col
        row_moved = next_row - curr_row
        if [col_moved,row_moved] in legal_moves and grid[curr_row + row_moved][curr_col + col_moved] is None:
            self.has_moved = True
            return True
        return False