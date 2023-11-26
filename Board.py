import random

from Cell import Cell
from MineCell import MineCell
from RevealedCell import RevealedCell


class Board:
    """
    The Board class represents the game board in a Minesweeper game.
    """

    def __init__(self, size, precent_mines):
        self.SIZE_CELL = 50

        """
        Initialize a new Board instance.

        Args:
            size (int): The size of the board (number of cells in a row/column).
            precent_mines (int): The percentage of cells that should be mines.
        """
        self.precent_mines = precent_mines
        self.size = size
        self.board = [[0 for x in range(size)] for y in range(size)]
        self.init_board()
        self.hidden_cells = {(i, j): True for i in range(size) for j in range(size)}

    def get_size_of_board(self):
        """
        Get the size of the board in pixels.

        Returns:
            int: The size of the board in pixels.
        """
        return self.size * self.SIZE_CELL

    def calc_num_mines_near_cell(self, cell):
        """
        Calculate the number of mines in the cells adjacent to the given cell.

        Args:
            cell (Cell): The cell to check.

        Returns:
            int: The number of mines in the cells adjacent to the given cell.
        """
        count = 0
        for i in range(cell.row - 1, cell.row + 2):
            for j in range(cell.col - 1, cell.col + 2):
                if 0 <= i < self.size and 0 <= j < self.size:
                    if isinstance(self.board[i][j], MineCell):
                        count += 1
        return count

    def reveal_cell(self, cell):
        """
        Reveal a cell on the board.

        Args:
            cell (Cell): The cell to reveal.
        """
        if isinstance(cell, MineCell):
            return
        if isinstance(cell, RevealedCell):
            return

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

    def init_mines(self, row, col):
        """
        Initialize the mines on the board.

        Args:
            row (int): The row of the first clicked cell.
            col (int): The column of the first clicked cell.
        """
        for i in range(0, self.size):
            for j in range(0, self.size):
                if abs(i - row) <= 1 and abs(j - col) <= 1 or random.randint(0, 100) > self.precent_mines:
                    self.board[i][j] = Cell(i, j)
                else:
                    self.board[i][j] = MineCell(self.board[i][j])
                    self.hidden_cells.pop((i, j))

        for i in range(0, self.size):
            for j in range(0, self.size):
                if not isinstance(self.board[i][j], MineCell):
                    (self.board[i][j]).num_mines = self.calc_num_mines_near_cell(self.board[i][j])

        for i in range(0, self.size):
            for j in range(0, self.size):
                if isinstance(self.board[i][j], MineCell):
                    print("X", end=" ")
                else:
                    print(self.board[i][j].num_mines, end=" ")
            print()

    def init_board(self):
        """
        Initialize the board with Cell instances.
        """
        for i in range(0, self.size):
            for j in range(0, self.size):
                self.board[i][j] = Cell(i, j)

    def has_all_revealed(self):
        """
        Check if all non-mine cells have been revealed.

        Returns:
            bool: True if all non-mine cells have been revealed, False otherwise.
        """
        for row in self.board:
            for cell in row:
                if not isinstance(cell, RevealedCell) and not isinstance(cell, MineCell):
                    return False
        return True
