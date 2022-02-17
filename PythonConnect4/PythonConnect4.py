# Source https://www.youtube.com/watch?v=XGf2GcyHPhc&t=9767s
# Ownership: https://github.com/KeithGalli/Connect4-Python
#
#   Purpose: python syntax of matrices practice with numpy and pygame library
#
import numpy as np
import pygame
import sys
import math

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
WHITE = (255,255,255)

ROW_COUNT = 6
COLUMN_COUNT = 7

def create_matrix():
    board = np.zeros((ROW_COUNT,COLUMN_COUNT))
    return board

def drop_piece(board, row, col, piece):
    board[row][col] = piece

#checks if the column has an empty slot
def is_valid_move(board, col):
    return board[ROW_COUNT - 1][col] == 0

def next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

def print_board(board):
    print(np.flip(board,0))

def winning_move(board, piece):
    #winning horizontal move check
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    #winning vertical move check
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True
    #winning pos diaganol move check
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True
    #winning neg diaganol move check
    for c in range(COLUMN_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True

def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (c*squareSize, r*squareSize + squareSize, squareSize, squareSize))
                          #  border_top_right_radius=5, border_top_left_radius=5, border_bottom_right_radius=5, border_bottom_left_radius=5)
            pygame.draw.circle(screen, BLACK, (int(c*squareSize + squareSize/2), int(r*squareSize + squareSize + squareSize/2)), radius)
   
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT): 
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (int(c*squareSize + squareSize/2), height - int(r*squareSize  + squareSize/2)), radius)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, GREEN, (int(c*squareSize + squareSize/2), height - int(r*squareSize  + squareSize/2)), radius)

    pygame.display.update()

board = create_matrix()
print_board(board)
game_over = False
turn = 0

pygame.init()

squareSize = 100

width = COLUMN_COUNT * squareSize
height = (ROW_COUNT + 1) * squareSize
radius = int(squareSize/2 - 5)

size = (width, height)

screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

myfont = pygame.font.SysFont("monospace", 75, True)

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0,0,width, squareSize))
            posx = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, RED, (posx, int(squareSize/2)), radius)
            else:
                pygame.draw.circle(screen, GREEN, (posx, int(squareSize/2)), radius)
        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            #print(event.pos)

            if turn == 0:
                posx = event.pos[0]
                col = int(math.floor(posx/squareSize))

                if is_valid_move(board, col):
                    row = next_open_row(board, col)
                    drop_piece(board, row, col, 1)

                    if winning_move(board, 1):
                        label = myfont.render("PLayer 1 WINS!", 1, WHITE)
                        screen.blit(label, (40,10))
                        game_over = True
        
            else:
                posx = event.pos[0]
                col = int(math.floor(posx/squareSize))

                if is_valid_move(board, col):
                    row = next_open_row(board, col)
                    drop_piece(board, row, col, 2)

                    if winning_move(board, 2):
                        label = myfont.render("PLayer 2 WINS!", 1, WHITE)
                        screen.blit(label, (40,10))
                        game_over = True

            print_board(board)
            draw_board(board)
            turn += 1
            turn = turn % 2

            if game_over:
                pygame.time.wait(3000)
