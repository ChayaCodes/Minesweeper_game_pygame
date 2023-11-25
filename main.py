from datetime import time
from random import random

import pygame

from Board import Board
from Cell import Cell
from Draw import Draw
from MineCell import MineCell
from RevealedCell import RevealedCell

board = Board(10,20)

draw = Draw(500,500, board)
pygame.display.flip()
finish = False


def notAllRevealedOrFlagged():
    for row in board.board:
        for cell in row:
            if not isinstance(cell, MineCell) and not isinstance(cell, RevealedCell):
                return True
    return False


def gameOver():

    # תעבור על הלוח מהאצע לפינות בצורה רנדומלית
    #ותחשוף את התאים
    while notAllRevealedOrFlagged():
        i = int(random() * board.size)
        j = int(random() * board.size)
        if not isinstance(board.board[i][j], MineCell):
            board.revealCell(board.board[i][j])
            draw.drawGrid(board)
        else:
            board.board[i][j].isFlagged = True
            draw.drawGrid(board)
    # תציג הודעה "הפסדת"
    font = pygame.font.SysFont("Arial", 50)
    text_surface = font.render("You Lost", True, Draw.RED)
    text_rect = text_surface.get_rect()
    text_rect.center = (250, 250)
    draw.screen.blit(text_surface, text_rect)
    pygame.display.flip()





def handleClickCell(cell):
    if isinstance(cell, MineCell):
        gameOver()
    else:
        board.revealCell(cell)
        draw.drawGrid(board)


def handleRightClickCell(cell):
    cell.isFlagged = True
    draw.drawGrid(board)


def handleClick(x,y, leftClick = True):
    for row in board.board:
        for cell in row:
            if x > cell.x and x < cell.x + Cell.SIZE_CELL and y > cell.y and y < cell.y + cell.SIZE_CELL:
                if leftClick:
                    handleClickCell(cell)
                else:
                    handleRightClickCell(cell)
                return





while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get the position of the mouse
            x, y = pygame.mouse.get_pos()
            # Check if the left or right mouse button was clicked
            if event.button == pygame.BUTTON_LEFT:
                handleClick(x, y)
            elif event.button == pygame.BUTTON_RIGHT:
                handleClick(x, y, False)


def drawGrid(self):
    draw.drawGrid(self.board)


