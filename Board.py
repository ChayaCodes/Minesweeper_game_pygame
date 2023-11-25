import random


from Cell import Cell
from MineCell import MineCell
from RevealedCell import RevealedCell


class Board:
    SIZE_CELL = 50
    def __init__(self, size, precentMines):
        self.size = size
        self.board = [[0 for x in range(size)] for y in range(size)]
        for i in range(0,self.size):
            for j in range(0, self.size):
                self.board[i][j] = Cell(i,j)
                r = random.random()*100
                if r < precentMines:
                    self.board[i][j] = MineCell(self.board[i][j])
                else:
                    self.board[i][j] = Cell(i,j)

    def revealCell(self, cell):
        if cell.isFlagged:
            return
        num_mines = 0
        for i in range(cell.row-1, cell.row+2):
            for j in range(cell.col-1, cell.col+2):
                if i >= 0 and i < self.size and j >= 0 and j < self.size  and not (i == cell.row and j == cell.col):
                    if isinstance(self.board[i][j], MineCell):
                        num_mines += 1
        self.board[cell.row][cell.col] = RevealedCell(cell, num_mines)







