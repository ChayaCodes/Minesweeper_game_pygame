from abc import abstractmethod
import pygame
from Draw import Draw

class Cell:
    """
    The Cell class represents a cell in a Minesweeper game.
    """

    SIZE_CELL = 50
    COLOR_HIDDEN_CELL = (0, 255, 0)

    @abstractmethod
    def __init__(self, row, col, num_mines=0):
        """
        Initialize a new Cell instance.

        Args:
            row (int): The row of the cell on the board.
            col (int): The column of the cell on the board.
            num_mines (int, optional): The number of mines adjacent to the cell. Defaults to 0.
        """
        self.row = row
        self.col = col
        self.x = col * self.SIZE_CELL
        self.y = row * self.SIZE_CELL
        self.is_flagged = False
        self.num_mines = num_mines
        if self.num_mines == 0:
            print(f"cell {self.row},{self.col} has 0 mines")

    @abstractmethod
    def draw(self, screen):
        """
        Draw the cell on the given screen.

        Args:
            screen (pygame.Surface): The screen to draw the cell on.
        """
        # Draw the cell
        pygame.draw.rect(screen, self.COLOR_HIDDEN_CELL,
                         pygame.Rect(self.x, self.y, self.SIZE_CELL, self.SIZE_CELL))
        # Draw the cell border
        pygame.draw.rect(screen, Draw.BLACK,
                         pygame.Rect(self.x, self.y, self.SIZE_CELL, self.SIZE_CELL), 2)

        if self.is_flagged:
            Draw.draw_flag(screen, self)