from Pawn import Pawn
from Knight import Knight
from Bishop import Bishop
from Rook import Rook
from Queen import Queen
from King import King
from Piece import Piece

import pygame

class Board:
    def __init__(self):
        self.pieces = Piece()
        self.grid = self.pieces.list_of_pieces
        self.selected_piece = None

    def get_position(self,position): # will output [row,col]
        # position will look like ['f',2]

        row = 8 - position[1]
        col = ['a','b','c','d','e','f','g','h'].index(position[0])

        return [row,col]


    def move(self, curr_row,curr_col,next_row,next_col):
        piece = self.grid[curr_row][curr_col]
        if piece.is_legal(curr_row,curr_col,next_row,next_col, self.grid):
            self.grid[next_row][next_col] = piece
            self.grid[curr_row][curr_col] = None
            return True
        else: return False

    def draw(self, screen, GRID_WIDTH, GRID_HEIGHT, CELL_SIZE):
        WHITE = (255,255,255)
        GREEN = (78,170,45)

        # Game loop
        running = True
        while running:
            screen.fill(WHITE)
            for i in range(4*8):
                row = i // 4
                x = ((CELL_SIZE **0.5) * 2 * i) % GRID_WIDTH + ((row + 1) % 2) * CELL_SIZE ** 0.5
                y = (CELL_SIZE **0.5) * (i//4)
                pygame.draw.rect(screen,GREEN,
                                 pygame.Rect(x, y, CELL_SIZE **0.5, CELL_SIZE ** 0.5)
                                 )

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                # Check for mouse button down event
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1: # left mouse click
                        x,y = event.pos
                        new_col = int(x // (CELL_SIZE ** 0.5))
                        new_row = int(y // (CELL_SIZE ** 0.5))
                        old_piece = self.selected_piece
                        new_piece = self.grid[new_row][new_col]

                        # selecting a piece
                        if old_piece != new_piece and new_piece is not None:
                            selected_position = new_row,new_col
                            self.selected_piece = new_piece

                        # selecting where to move
                        elif new_piece is None or new_piece.color != old_piece.color:
                            old_row, old_col = selected_position[0], selected_position[1]
                            if self.move(old_row,old_col,new_row,new_col):
                                self.grid[old_row][old_col] = None
                                self.selected_piece = None

                        else:
                            print('error')







            row = 0
            for line in self.grid:
                col = 0
                for piece in line:
                    x = (CELL_SIZE **0.5) * col
                    y = (CELL_SIZE **0.5) * row
                    if isinstance(piece,Pawn):
                        if piece.color == 'b':
                            img = pygame.image.load('Images/pawn_b.png')
                            screen.blit(img,(x,y))
                        else:
                            img = pygame.image.load('Images/pawn_w.png')
                            screen.blit(img,(x,y))

                    elif isinstance(piece,Bishop):
                        if piece.color == 'b':
                            img = pygame.image.load('Images/bishop_b.png')
                            screen.blit(img,(x,y))
                        else:
                            img = pygame.image.load('Images/bishop_w.png')
                            screen.blit(img,(x,y))

                    elif isinstance(piece,Knight):
                        if piece.color == 'b':
                            img = pygame.image.load('Images/knight_b.png')
                            screen.blit(img,(x,y))
                        else:
                            img = pygame.image.load('Images/knight_w.png')
                            screen.blit(img,(x,y))

                    elif isinstance(piece,Rook):
                        if piece.color == 'b':
                            img = pygame.image.load('Images/rook_b.png')
                            screen.blit(img,(x,y))
                        else:
                            img = pygame.image.load('Images/rook_w.png')
                            screen.blit(img,(x,y))

                    elif isinstance(piece,Queen):
                        if piece.color == 'b':
                            img = pygame.image.load('Images/queen_b.png')
                            screen.blit(img,(x,y))
                        else:
                            img = pygame.image.load('Images/queen_w.png')
                            screen.blit(img,(x,y))

                    elif isinstance(piece,King):
                        if piece.color == 'b':
                            img = pygame.image.load('Images/king_b.png')
                            screen.blit(img,(x,y))
                        else:
                            img = pygame.image.load('Images/king_w.png')
                            screen.blit(img,(x,y))

                    col += 1
                row += 1

            pygame.display.flip()






