import re

import pygame

from Board import Board

class Game:
    def __init__(self):
        self.move_number = 0

    def play(self):
        pygame.init()
        GRID_WIDTH = 800
        GRID_HEIGHT = 800
        CELL_SIZE = (GRID_WIDTH * GRID_HEIGHT) / 64

        screen = pygame.display.set_mode((GRID_WIDTH,GRID_HEIGHT))

        board = Board()
        board.draw(screen,GRID_WIDTH,GRID_HEIGHT,CELL_SIZE)
        while True:
            got_move = False
            while not got_move:
                try:
                    move = re.split(r'[, ]',input('Insert move (eg: f2,f4 or f2 f4): '))
                    curr_position = [move[0][0],int(move[0][1])]
                    next_position = [move[1][0],int(move[1][1])]
                    curr_row,curr_col = board.get_position(curr_position)
                    next_row,next_col = board.get_position(next_position)
                    got_move = True
                except:
                    print('Invalid Move!')

            if board.grid[curr_row][curr_col] is not None and board.grid[curr_row][curr_col].color == ['w', 'b'][self.move_number % 2]:
                if board.move(curr_row,curr_col,next_row,next_col):
                    self.move_number += 1
                    board.draw(screen,GRID_WIDTH,GRID_HEIGHT,CELL_SIZE)


                else: print('Invalid Move!')
            else: print('Wrong Persons Turn')

game = Game()
game.play()