import random

from Cell import Cell
from MineCell import MineCell
from RevealedCell import RevealedCell


class Board:
    SIZE_CELL = 50

    def __init__(self, size, precent_mines):
        self.precent_mines = precent_mines
        self.size = size
        self.board = [[0 for x in range(size)] for y in range(size)]
        self.init_board()
        self.hidden_cells = {(i, j): True for i in range(size) for j in range(size)}



    def calc_num_mines_near_cell(self, cell):
        count = 0
        for i in range(cell.row - 1, cell.row + 2):
            for j in range(cell.col - 1, cell.col + 2):
                if 0 <= i < self.size and 0 <= j < self.size:
                    if isinstance(self.board[i][j], MineCell):
                        count += 1
        return count

    def reveal_cell(self, cell):
        if isinstance(cell, MineCell):
            return
        if isinstance(cell, RevealedCell):
            return
        # אם לתא יש 0 שכנים מוקשים תחשוף את כל השכנים שלו
        # אחרת תחשוף רק את התא עצמו


        col = cell.col
        row = cell.row
        self.board[row][col] = RevealedCell(cell)
        self.hidden_cells.pop((row, col))

        if self.calc_num_mines_near_cell(cell) != 0:
            return




        for i in range(cell.row - 1, cell.row + 2):
            for j in range(cell.col - 1, cell.col + 2):
                if 0 <= i < self.size and 0 <= j < self.size:
                    self.reveal_cell(self.board[i][j])




    def initMines(self, row, col):
        # התא שנלחץ והתאים הסמוכים אליו לא יהיו מוקשים
        for i in range(0, self.size):
            for j in range(0, self.size):
                if abs(i - row) <= 1 and abs(j - col) <= 1 or random.randint(0, 100) > self.precent_mines:
                    self.board[i][j] = Cell(i, j)
                else:
                    self.board[i][j] = MineCell(self.board[i][j])
                    self.hidden_cells.pop((i, j))
        # תחשב את התאים הסמוכים של כל תא
        for i in range(0, self.size):
            for j in range(0, self.size):
                if not isinstance(self.board[i][j], MineCell):
                    (self.board[i][j]).num_mines = self.calc_num_mines_near_cell(self.board[i][j])
        # תדפיס את הלוח
        for i in range(0, self.size):
            for j in range(0, self.size):
                if isinstance(self.board[i][j], MineCell):
                    print("X", end=" ")
                else:
                    print(self.board[i][j].num_mines, end=" ")
            print()


    def init_board(self):
        for i in range(0, self.size):
            for j in range(0, self.size):
                self.board[i][j] = Cell(i, j)

    def has_all_revealed(self):
        for row in self.board:
            for cell in row:
                if not isinstance(cell, RevealedCell) and not isinstance(cell, MineCell):
                    return False
        return True







