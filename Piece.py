from Pawn import Pawn
from Knight import Knight
from Bishop import Bishop
from Rook import Rook
from Queen import Queen
from King import King

class Piece:
    def __init__(self):
        self.list_of_pieces = self.initial_position_b() + self.initial_position_w()

    def initial_position_b(self):
        grid = [[None for i in range(8)] for j in range(4)]
        color = 'b'
        # Rooks
        grid[0][0] = Rook(color)
        grid[0][7] = Rook(color)
        # Knights
        grid[0][1] = Knight(color)
        grid[0][6] = Knight(color)
        # Bishops
        grid[0][2] = Bishop(color)
        grid[0][5] = Bishop(color)
        #Queen
        grid[0][3] = Queen(color)
        #King
        grid[0][4] = King(color)
        #Pawns
        grid[1] = [Pawn(color) for i in range(8)]

        return grid


    def initial_position_w(self):
        grid = [[None for i in range(8)] for j in range(4)]
        color = 'w'
        #Pawns
        grid[2] = [Pawn(color) for i in range(8)]
        # Rooks
        grid[3][0] = Rook(color)
        grid[3][7] = Rook(color)
        # Knights
        grid[3][1] = Knight(color)
        grid[3][6] = Knight(color)
        # Bishops
        grid[3][2] = Bishop(color)
        grid[3][5] = Bishop(color)
        #Queen
        grid[3][3] = Queen(color)
        #King
        grid[3][4] = King(color)

        return grid
