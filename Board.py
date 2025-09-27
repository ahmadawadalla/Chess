from Pawn import Pawn
from Knight import Knight
from Bishop import Bishop
from Rook import Rook
from Queen import Queen
from King import King
from Piece import Piece

import pygame

class Board:
    def __init__(self, screen,GRID_WIDTH,GRID_HEIGHT,CELL_SIZE):
        self.pieces = Piece()
        self.grid = self.pieces.list_of_pieces
        self.selected_piece = None
        self.selected_position = None
        self.move_positions = None
        self.move_number = 0

        self.WHITE = (255,255,255)
        self.GREEN = (78,170,45)
        self.BLUE = (0,0,250)
        self.YELLOW = (255,255,0)
        self.BLACK = (0,0,0)

        self.screen = screen
        self.GRID_WIDTH = GRID_WIDTH
        self.GRID_HEIGHT = GRID_HEIGHT
        self.CELL_SIZE = CELL_SIZE

        self.font = pygame.font.Font(None,50)

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
        else:
            self.selected_piece = None
            return False

    def draw(self):
        # Game loop
        running = True
        while running:
            self.screen.fill(self.WHITE)
            for i in range(4*8):
                row = i // 4
                x = ((self.CELL_SIZE **0.5) * 2 * i) % self.GRID_WIDTH + ((row + 1) % 2) * self.CELL_SIZE ** 0.5
                y = (self.CELL_SIZE **0.5) * (i//4)
                pygame.draw.rect(self.screen,self.GREEN,
                                 pygame.Rect(x, y, self.CELL_SIZE **0.5, self.CELL_SIZE ** 0.5)
                                 )

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                # Check for mouse button down event
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1: # left mouse click
                        x,y = event.pos
                        new_col = int(x // (self.CELL_SIZE ** 0.5))
                        new_row = int(y // (self.CELL_SIZE ** 0.5))
                        old_piece = self.selected_piece
                        new_piece = self.grid[new_row][new_col]

                        # selecting a piece
                        if old_piece != new_piece and new_piece is not None and new_piece.color == ['w','b'][self.move_number % 2]:
                            self.selected_position = new_row,new_col
                            self.selected_piece = new_piece

                        # Unselecting
                        elif old_piece == new_piece:
                            self.selected_piece = None
                            self.selected_position = None

                        # selecting where to move
                        elif new_piece is None or old_piece and new_piece.color != old_piece.color:
                            old_row, old_col = self.selected_position[0], self.selected_position[1]
                            old_x = self.selected_position[1] * self.CELL_SIZE ** 0.5
                            old_y = self.selected_position[0] * self.CELL_SIZE ** 0.5
                            new_x = new_col * self.CELL_SIZE ** 0.5
                            new_y = new_row * self.CELL_SIZE ** 0.5

                            if self.move(old_row,old_col,new_row,new_col):
                                self.draw_movement(self.screen,self.selected_piece, old_x, old_y, new_x, new_y)
                                self.grid[old_row][old_col] = None
                                self.move_number += 1
                                self.move_positions = [[old_row,old_col],[new_row,new_col]]
                            self.selected_piece = None
                            self.selected_position = None


            # adding blue marker for selected position
            if self.selected_position:
                pygame.draw.rect(self.screen,self.BLUE,
                                 pygame.Rect(self.CELL_SIZE ** 0.5 * self.selected_position[1], self.CELL_SIZE ** 0.5 * self.selected_position[0], self.CELL_SIZE **0.5, self.CELL_SIZE ** 0.5)
                                 )
            else:
                self.screen.fill(self.WHITE)
                for i in range(4*8):
                    row = i // 4
                    x = ((self.CELL_SIZE **0.5) * 2 * i) % self.GRID_WIDTH + ((row + 1) % 2) * self.CELL_SIZE ** 0.5
                    y = (self.CELL_SIZE **0.5) * (i//4)
                    pygame.draw.rect(self.screen,self.GREEN,
                                     pygame.Rect(x, y, self.CELL_SIZE **0.5, self.CELL_SIZE ** 0.5)
                                     )

            # adding a yellow marker for the previous move
            if self.move_positions:
                old_row,old_col = self.move_positions[0]
                new_row,new_col = self.move_positions[1]
                pygame.draw.rect(self.screen,self.YELLOW,
                                 pygame.Rect(self.CELL_SIZE ** 0.5 * old_col, self.CELL_SIZE ** 0.5 * old_row, self.CELL_SIZE **0.5, self.CELL_SIZE ** 0.5)
                                 )
                pygame.draw.rect(self.screen,self.YELLOW,
                                 pygame.Rect(self.CELL_SIZE ** 0.5 * new_col, self.CELL_SIZE ** 0.5 * new_row, self.CELL_SIZE **0.5, self.CELL_SIZE ** 0.5)
                                 )

            row = 0
            for line in self.grid:
                # start of the row, put the row numbers
                row_number = self.font.render(str(8-row),True,self.BLACK)
                self.screen.blit(row_number,(0.05 * self.CELL_SIZE ** 0.5,(row + 0.05) * self.CELL_SIZE ** 0.5))
                col = 0
                for piece in line:
                    x = (self.CELL_SIZE **0.5) * col
                    y = (self.CELL_SIZE **0.5) * row

                    if piece:
                        img = piece.get_image()
                        self.screen.blit(img,(x,y))

                    col += 1
                row += 1

            # put the column letters
            for i in range(8):
                col_letter = self.font.render(['a','b','c','d','e','f','g','h'][i],True,self.BLACK)
                self.screen.blit(col_letter,((i + 0.75) * self.CELL_SIZE ** 0.5, 7.65 * self.CELL_SIZE ** 0.5))

            pygame.display.flip()

    def draw_movement(self, screen, piece, curr_x, curr_y, next_x, next_y):
        x_direction = 0
        y_direction = 0

        x_moved = next_x - curr_x
        y_moved = next_y - curr_y

        if next_x - curr_x != 0:
            x_direction = x_moved / abs(x_moved)
        if next_y - curr_y != 0:
            y_direction = y_moved / abs(y_moved)


        while (curr_x,curr_y) != (next_x,next_y):
            pygame.time.delay(1)

            screen.fill(self.WHITE)
            for i in range(4*8):
                row = i // 4
                x = ((self.CELL_SIZE **0.5) * 2 * i) % self.GRID_WIDTH + ((row + 1) % 2) * self.CELL_SIZE ** 0.5
                y = (self.CELL_SIZE **0.5) * (i//4)
                pygame.draw.rect(screen,self.GREEN,
                                 pygame.Rect(x, y, self.CELL_SIZE **0.5, self.CELL_SIZE ** 0.5)
                                 )


            row = 0
            for line in self.grid:
                # start of the row, put the row numbers
                row_number = self.font.render(str(8-row),True,self.BLACK)
                self.screen.blit(row_number,(0.05 * self.CELL_SIZE ** 0.5,(row + 0.05) * self.CELL_SIZE ** 0.5))
                col = 0
                for piece_img in line:
                    x = (self.CELL_SIZE **0.5) * col
                    y = (self.CELL_SIZE **0.5) * row

                    # move piece
                    if piece_img == piece:
                        img = piece.get_image()
                        screen.blit(img,(curr_x,curr_y))

                    # not moving peices
                    elif piece_img:
                        img = piece_img.get_image()
                        self.screen.blit(img,(x,y))

                    col += 1
                row += 1

            if not isinstance(piece,Knight):
                curr_x += 2*x_direction
                curr_y += 2*y_direction
            else:
                if abs(x_moved) > abs(y_moved): # moves in x direction more
                    curr_x += 4*x_direction
                    curr_y += 2*y_direction
                else: # moves in y direction more
                    curr_x += 2*x_direction
                    curr_y += 4*y_direction

            pygame.display.flip()

        # put the column letters
        for i in range(8):
            col_letter = self.font.render(['a','b','c','d','e','f','g','h'][i],True,self.BLACK)
            self.screen.blit(col_letter,((i + 0.75) * self.CELL_SIZE ** 0.5, 7.65 * self.CELL_SIZE ** 0.5))

        pygame.display.flip()





