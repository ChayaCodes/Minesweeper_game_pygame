import math
from random import random
import pygame
import random
from Board import Board
from Cell import Cell
from Draw import Draw
from MineCell import MineCell
from RevealedCell import RevealedCell




def not_all_revealed_or_flagged():
    for row in board.board:
        for cell in row:
            if not isinstance(cell, MineCell) and not isinstance(cell, RevealedCell):
                return True
    return False


def game_over():
    draw.game_ended = True
    # תציג את כל המוקשים
    for row in board.board:
        for cell in row:
            if isinstance(cell, MineCell):
                draw.draw_mine(draw.screen, cell)

    # תעבור על הלוח מהאצע לפינות בצורה רנדומלית
    # ותחשוף את התאים
    while len(board.hidden_cells) > 0:
        i, j = random.choice(list(board.hidden_cells.keys()))
        board.reveal_cell(board.board[i][j])

        draw.draw_grid(board)
    # תציג הודעה "הפסדת"
    font = pygame.font.SysFont("Arial", 50)
    text_surface = font.render("You Lost", True, Draw.RED)
    text_rect = text_surface.get_rect()
    text_rect.center = (250, 250)
    draw.screen.blit(text_surface, text_rect)
    pygame.display.flip()


def handle_click_cell(cell):
    if isinstance(cell, RevealedCell):
        return
    if cell.is_flagged:
        return
    if isinstance(cell, MineCell):
        game_over()

    else:
        board.reveal_cell(cell)
        draw.draw_grid(board)



def handle_right_click_cell(cell):
    cell.is_flagged = not cell.is_flagged
    draw.draw_grid(board)


def game_win():
    draw.game_ended = True
    # תציג הודעה "ניצחת"
    if not not_all_revealed_or_flagged():
        return
    font = pygame.font.SysFont("Arial", 50)
    text_surface = font.render("You Won", True, Draw.GREEN)
    text_rect = text_surface.get_rect()
    text_rect.center = (250, 250)
    draw.screen.blit(text_surface, text_rect)
    pygame.display.flip()


def handle_click(mouse_x, mouse_y, left_click=True):
    for row in board.board:
        for cell in row:
            if cell.x < mouse_x < cell.x + Cell.SIZE_CELL and cell.y < mouse_y < cell.y + cell.SIZE_CELL:
                if left_click:
                    handle_click_cell(cell)
                else:
                    handle_right_click_cell(cell)
                    if board.has_all_revealed():
                        game_win()
                return


def handle_first_click(x, y):
    # תמצא את התא שנלחץ
    row = int(y / Cell.SIZE_CELL)
    col = int(x / Cell.SIZE_CELL)
    # תעבור על 7 תאים סמוכים לתא שנלחץ ותהפוך טותם לתאים שאינם מוקשים
    board.initMines(row, col)
    board.reveal_cell(board.board[row][col])
    draw.draw_grid(board)


def draw_grid(self):
    draw.draw_grid(self.board)

is_first_click = True
board = Board(10, 20)
draw = Draw(500, 500, board)
draw.draw_grid(board)

finish = False
draw.game_ended = False
while not finish:
    if board.has_all_revealed() and not draw.game_ended:
        game_win()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True
        elif event.type == pygame.MOUSEBUTTONDOWN and not draw.game_ended:
            # Get the position of the mouse
            x, y = pygame.mouse.get_pos()
            # Check if the left or right mouse button was clicked
            if is_first_click:
                board = Board(10, 20)
                draw = Draw(500, 500, board)
                handle_first_click(x, y)
                is_first_click = False
            if event.button == pygame.BUTTON_LEFT:
                handle_click(x, y)
            elif event.button == pygame.BUTTON_RIGHT:
                handle_click(x, y, False)
