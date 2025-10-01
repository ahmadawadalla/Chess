import copy
import time

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
        self.possible_moves = []
        self.all_moves = []
        self.all_move_positions = []
        self.all_selected_positions = []
        self.all_selected_pieces = []

        self.WHITE = (255,255,255)
        self.GREEN = (78,170,45)
        self.BLUE = (72,209,204)
        self.LIGHT_BLUE = (8,232,222)
        self.YELLOW = (200,220,10)
        self.LIGHT_YELLOW = (255,255,50)
        self.BLACK = (30,30,30)
        self.LIGHT_BLACK = (150,150,150)
        self.GRAY = (211,211,211)
        self.RED = (255,0,0)

        self.screen = screen
        self.GRID_WIDTH = GRID_WIDTH
        self.GRID_HEIGHT = GRID_HEIGHT
        self.CELL_SIZE = CELL_SIZE

        self.font = pygame.font.Font(None,50)
        self.time_moved = time.time() - 2

    def get_position(self,position): # will output [row,col]
        # position will look like ['f',2]

        row = 8 - position[1]
        col = ['a','b','c','d','e','f','g','h'].index(position[0])

        return [row,col]


    def move(self, curr_row,curr_col,next_row,next_col, do_not_move):
        piece = self.grid[curr_row][curr_col]
        piece_moved = piece.has_moved

        piece_before_move = self.grid[next_row][next_col]
        adj_piece_1 = None
        adj_piece_2 = None
        if curr_col < 7:
            adj_piece_1 = self.grid[curr_row][curr_col + 1]
        if curr_col > 0:
            adj_piece_2 = self.grid[curr_row][curr_col - 1]
        moved = False

        can_castle = False
        if isinstance(piece, King) and not piece_moved:
            can_castle = True
            castle_row = (self.grid[curr_row])[:]

        if piece.is_legal(curr_row,curr_col,next_row,next_col, self.grid, False or (isinstance(self.grid[curr_row][curr_col],King) and do_not_move)):
            self.grid[next_row][next_col] = piece
            self.grid[curr_row][curr_col] = None
            if not do_not_move:
                self.possible_moves = []

                #change every piece just_moved to false except for the piece you just moved
                for row in range(8):
                    for col in range(8):
                        if self.grid[row][col]:
                            self.grid[row][col].just_moved = False
                piece.just_moved = True

            moved = True
        elif not do_not_move:
            self.selected_piece = None
            self.possible_moves = []


        available_piece_pos = []
        available_enemy_piece_pos = []
        for row in range(8):
            for col in range(8):
                enemy_piece = self.grid[row][col]
                if enemy_piece and enemy_piece.color != piece.color:
                    enemy_piece_moved = enemy_piece.has_moved
                    if isinstance(enemy_piece,Pawn):
                        enemy_moved_two = enemy_piece.moved_up_two
                    # all available enemy positions
                    # if it is of type pawn, then change moved_up_two back to original

                    for final_row in range(8):
                        for final_col in range(8):
                            next_position = self.grid[final_row][final_col]
                            if (not next_position or next_position.color != enemy_piece.color) and enemy_piece.is_legal(row,col,final_row,final_col,self.grid, True):
                                available_enemy_piece_pos.append((final_row,final_col))
                                enemy_piece.has_moved = enemy_piece_moved
                                if isinstance(enemy_piece,Pawn):
                                    enemy_piece.moved_up_two = enemy_moved_two

                    # position of enemy king
                    if isinstance(self.grid[row][col],King):
                        king_enemy_pos = (row,col)
                # position of ally king
                if isinstance(self.grid[row][col],King) and self.grid[row][col].color == piece.color:
                    king_ally_pos = (row,col)

                # available positions for the piece that you just moved
                if piece.is_legal(next_row,next_col,row,col,self.grid, True):
                    available_piece_pos.append((row,col))

        piece.has_moved = piece_moved
        if can_castle and not piece_moved and (next_col == 2 or next_col == 6) :
            col_dir = int((next_col - curr_col)/abs(next_col - curr_col))
            if (curr_row,curr_col + col_dir * 2) in available_enemy_piece_pos or (curr_row,curr_col) in available_enemy_piece_pos or (curr_row,curr_col + col_dir) in available_enemy_piece_pos:
                moved = False
            if not moved:
                self.grid[curr_row] = castle_row

        if king_ally_pos in available_enemy_piece_pos:
            self.grid[next_row][next_col] = piece_before_move
            self.grid[curr_row][curr_col] = piece
            if isinstance(piece,Pawn):
                if adj_piece_1:
                    self.grid[curr_row][curr_col + 1] = adj_piece_1
                if adj_piece_2:
                    self.grid[curr_row][curr_col - 1] = adj_piece_2
            moved = False

        elif piece.is_legal(curr_row,curr_col,next_row,next_col, self.grid, True) and not do_not_move:
            #change every piece just_moved to false except for the piece you just moved
            for row in range(8):
                for col in range(8):
                    if self.grid[row][col]:
                        self.grid[row][col].just_moved = False

            if isinstance(piece,Pawn) and (next_row == 0 or next_row == 7):
                self.draw_pawn_options(next_row, next_col, piece.color)

        if moved and not do_not_move:
            piece.has_moved = True
            piece.just_moved = True

        if do_not_move:
            self.grid[next_row][next_col] = piece_before_move
            self.grid[curr_row][curr_col] = piece
            if isinstance(piece,Pawn):
                if adj_piece_1:
                    self.grid[curr_row][curr_col + 1] = adj_piece_1
                if adj_piece_2:
                    self.grid[curr_row][curr_col - 1] = adj_piece_2
            piece.has_moved = piece_moved

        return moved

    def draw(self):
        # Game loop
        running = True
        self.all_moves.append(self.get_grid_by_value(self.grid,8,8))
        self.all_move_positions.append(None)
        while running:
            flip = self.move_number % 2 == 1
            self.draw_board_cells(flip)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                # Check for mouse button down event
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1: # left mouse click
                        x,y = event.pos
                        if flip:
                            new_col = 7 - int(x // (self.CELL_SIZE ** 0.5))
                            new_row = 7 - int(y // (self.CELL_SIZE ** 0.5))
                        else:
                            new_col = int(x // (self.CELL_SIZE ** 0.5))
                            new_row = int(y // (self.CELL_SIZE ** 0.5))
                        old_piece = self.selected_piece
                        new_piece = self.grid[new_row][new_col]

                        # selecting a piece
                        if old_piece != new_piece and new_piece and new_piece.color == ['w','b'][self.move_number % 2]:
                            self.selected_position = new_row,new_col
                            self.selected_piece = new_piece
                            self.possible_moves = []

                            moved = self.selected_piece.has_moved
                            if isinstance(new_piece,Pawn):
                                moved_two = new_piece.moved_up_two

                            # get all possible moves that that piece can move
                            for i in range(8):
                                for j in range(8):
                                    self.selected_piece.has_moved = moved

                                    if new_piece.is_legal(new_row,new_col,i,j,self.grid,True) and ((self.grid[i][j] and self.grid[i][j].color != new_piece.color) or not self.grid[i][j]):
                                        self.possible_moves.append((i,j))
                                        if isinstance(new_piece,Pawn):
                                            new_piece.moved_up_two = moved_two

                            self.selected_piece.has_moved = moved

                        # Unselecting
                        elif old_piece == new_piece:
                            self.selected_piece = None
                            self.selected_position = None

                        # selecting where to move
                        elif new_piece is None or old_piece and new_piece.color != old_piece.color:
                            old_row, old_col = self.selected_position[0], self.selected_position[1]
                            check_if_captured = self.grid[new_row][new_col]

                            if self.move(old_row,old_col,new_row,new_col, False):
                                if check_if_captured:
                                    move_noise = pygame.mixer.Sound("Sounds/capture.mp3")
                                else:
                                    move_noise = pygame.mixer.Sound("Sounds/move-self.mp3")

                                pygame.mixer.Sound.play(move_noise)

                                self.grid[old_row][old_col] = None
                                self.move_number += 1
                                self.all_moves.insert(self.move_number,self.get_grid_by_value(self.grid,8,8))
                                self.all_moves = self.all_moves[:self.move_number + 1]

                                self.move_positions = [[old_row,old_col],[new_row,new_col]]
                                self.all_move_positions.insert(self.move_number,[[old_row,old_col],[new_row,new_col]])
                                self.all_move_positions = self.all_move_positions[:self.move_number + 1]

                                self.all_selected_positions.insert(self.move_number,self.selected_position)
                                self.all_selected_positions = self.all_selected_positions[:self.move_number + 1]

                                self.all_selected_pieces.insert(self.move_number,self.selected_piece)
                                self.all_selected_pieces = self.all_selected_pieces[:self.move_number + 1]

                            self.selected_piece = None
                            self.selected_position = None

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    if event.key == pygame.K_LEFT: # go back a move
                        if self.move_number >= 1:
                            self.move_number -= 1
                            self.grid = self.get_grid_by_value(self.all_moves[self.move_number],8,8)
                            if self.all_move_positions[self.move_number] is None:
                                self.move_positions = None
                            else:
                                self.move_positions = self.get_grid_by_value(self.all_move_positions[self.move_number],2,2)
                            self.selected_position = None
                            self.selected_piece = None

                    if event.key == pygame.K_RIGHT: # go forward a move
                        if self.move_number + 1 < len(self.all_moves):
                            self.move_number += 1
                            self.grid = self.get_grid_by_value(self.all_moves[self.move_number],8,8)
                            self.move_positions = self.get_grid_by_value(self.all_move_positions[self.move_number],2,2)
                            self.selected_position = None
                            self.selected_piece = None




            # adding blue marker for selected position
            if self.selected_position:
                row, col = self.selected_position

                # Flip the coordinates if needed
                draw_row = 7 - row if flip else row
                draw_col = 7 - col if flip else col

                blue_color = self.LIGHT_BLUE if self.get_cell_color(col, row) == 'g' else self.BLUE
                self.draw_cell_color(draw_row,draw_col, blue_color)

            else:
                self.draw_board_cells(flip)

            # adding a yellow marker for the previous move
            if self.move_positions and self.move_number > 0:
                flip = (self.move_number % 2 == 1)  # black’s turn → flipped

                old_row, old_col = self.move_positions[0]
                new_row, new_col = self.move_positions[1]

                # Flip coords if needed
                draw_old_row = 7 - old_row if flip else old_row
                draw_old_col = 7 - old_col if flip else old_col
                draw_new_row = 7 - new_row if flip else new_row
                draw_new_col = 7 - new_col if flip else new_col

                # Draw old square
                yellow_color = self.LIGHT_YELLOW if self.get_cell_color(new_row, new_col) == 'g' else self.YELLOW
                self.draw_cell_color(draw_old_row, draw_old_col, yellow_color)

                # Draw new square
                yellow_color = self.LIGHT_YELLOW if self.get_cell_color(new_row, new_col) == 'g' else self.YELLOW
                self.draw_cell_color(draw_new_row, draw_new_col, yellow_color)


            self.draw_board_imgs(flip)

            if self.selected_position:
                flip = (self.move_number % 2 == 1)  # flip when black’s turn
                sel_row, sel_col = self.selected_position

                for i in self.possible_moves:
                    row, col = i

                    if self.move(sel_row, sel_col, row, col, True):
                        # Flip coords for drawing
                        draw_row = 7 - row if flip else row
                        draw_col = 7 - col if flip else col

                        x = int(self.CELL_SIZE ** 0.5 * draw_col + 50)
                        y = int(self.CELL_SIZE ** 0.5 * draw_row + 50)

                        if self.grid[row][col] and self.grid[row][col].color != self.selected_piece.color:
                            # Enemy piece → red circle
                            pygame.draw.circle(self.screen, self.RED, (x, y), int(self.CELL_SIZE ** 0.5 // 3), 6)
                        elif not self.grid[row][col]:
                            # Empty square → gray circle
                            pygame.draw.circle(self.screen, self.GRAY, (x, y), int(self.CELL_SIZE ** 0.5 // 6))


            pygame.display.flip()

    def draw_pawn_options(self, pawn_row, pawn_col, color):
        running = True
        while running:
            flip = self.move_number % 2 == 1
            self.draw_board_cells(flip)

            self.draw_board_imgs(flip)

            queen = Queen(color).get_image()
            rook = Rook(color).get_image()
            bishop = Bishop(color).get_image()
            knight = Knight(color).get_image()

            pygame.draw.rect(self.screen, self.BLACK,
                             pygame.Rect(self.CELL_SIZE ** 0.5 * 1.9, self.CELL_SIZE ** 0.5 * 2.9, self.CELL_SIZE ** 0.5 * 4.2, self.CELL_SIZE ** 0.5 * 1.2)
                             )

            for col in range(4):
                self.draw_cell_color(3,col + 2,self.WHITE)

            for col in range(3):
                pygame.draw.rect(self.screen, self.BLACK,
                                 pygame.Rect(self.CELL_SIZE ** 0.5 * (col + 2.95), self.CELL_SIZE ** 0.5 * 3, self.CELL_SIZE ** 0.5 * .1, self.CELL_SIZE ** 0.5)
                                 )

            self.screen.blit(queen,(self.CELL_SIZE ** 0.5 * 2, self.CELL_SIZE ** 0.5 * 3))
            self.screen.blit(rook,(self.CELL_SIZE ** 0.5 * 3, self.CELL_SIZE ** 0.5 * 3))
            self.screen.blit(bishop,(self.CELL_SIZE ** 0.5 * 4, self.CELL_SIZE ** 0.5 * 3))
            self.screen.blit(knight,(self.CELL_SIZE ** 0.5 * 5, self.CELL_SIZE ** 0.5 * 3))
            pygame.display.flip()


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                # Check for mouse button down event
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1: # left mouse click
                        x,y = event.pos
                        col = int(x // (self.CELL_SIZE ** 0.5))
                        row = int(y // (self.CELL_SIZE ** 0.5))

                        if row == 3:
                            if col == 2: # queen
                                self.grid[pawn_row][pawn_col] = Queen(color)
                                running = False
                            if col == 3: # rook
                                self.grid[pawn_row][pawn_col] = Rook(color)
                                running = False
                            if col == 4: # bishop
                                self.grid[pawn_row][pawn_col] = Bishop(color)
                                running = False
                            if col == 5: # knight
                                self.grid[pawn_row][pawn_col] = Knight(color)
                                running = False

    def get_cell_color(self,row,col):
        return 'w' if (row + col) % 2 == 0 else 'g'


    def get_grid_by_value(self,grid, num_row, num_col):
        array = []
        for row in range(num_row):
            line = []
            for col in range(num_col):
                line.append(copy.deepcopy(grid[row][col]))
            array.append(line)

        return array

    def draw_board_cells(self,flip=False):
        self.screen.fill(self.WHITE)
        for i in range(4*8):
            row = i // 4
            row += 0 if flip else 1
            x = ((self.CELL_SIZE **0.5) * 2 * i) % self.GRID_WIDTH + (row % 2) * self.CELL_SIZE ** 0.5
            y = (self.CELL_SIZE **0.5) * (i//4)
            pygame.draw.rect(self.screen,self.GREEN,
                             pygame.Rect(x, y, self.CELL_SIZE **0.5, self.CELL_SIZE ** 0.5)
                             )

    def draw_cell_color(self, row, col, color):
        pygame.draw.rect(self.screen, color,
                         pygame.Rect(self.CELL_SIZE ** 0.5 * col, self.CELL_SIZE ** 0.5 * row, self.CELL_SIZE ** 0.5, self.CELL_SIZE ** 0.5)
                         )

    def draw_board_imgs(self, flip=False):
        for row in range(8):
            row_number = row + 1if flip else 8 - row
            draw_row_number = self.font.render(str(row_number),True,self.BLACK)
            self.screen.blit(draw_row_number,(0.05 * self.CELL_SIZE ** 0.5, (row + .03) * self.CELL_SIZE ** 0.5))

            for col in range(8):
                piece = self.grid[row][col]

                # If flipping, invert row/col
                draw_row = 7 - row if flip else row
                draw_col = 7 - col if flip else col

                x = (self.CELL_SIZE ** 0.5) * draw_col
                y = (self.CELL_SIZE ** 0.5) * draw_row

                if piece:
                    img = piece.get_image()
                    self.screen.blit(img, (x, y))


            # put the column letters
        for i in range(8):
            col_letter = self.font.render(['a','b','c','d','e','f','g','h'][i],True,self.BLACK)
            self.screen.blit(col_letter,((i + 0.75) * self.CELL_SIZE ** 0.5, 7.65 * self.CELL_SIZE ** 0.5))