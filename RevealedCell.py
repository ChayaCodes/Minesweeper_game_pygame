import pygame
from Cell import Cell
from Draw import Draw

class RevealedCell(Cell):
    """
    The RevealedCell class represents a cell that has been revealed in a Minesweeper game.
    It inherits from the Cell class.
    """

    COLOR = Draw.WHITE

    def __init__(self, cell):
        """
        Initialize a new RevealedCell instance.

        Args:
            cell (Cell): The cell to convert to a RevealedCell.
        """
        super().__init__(cell.row, cell.col, cell.num_mines)

    def draw(self, screen):
        """
        Draw the revealed cell on the given screen.
        If the cell is adjacent to mines, the number of adjacent mines is also drawn.

        Args:
            screen (pygame.Surface): The screen to draw the cell on.
        """
        # Draw the cell
        pygame.draw.rect(screen, self.COLOR,
                         pygame.Rect(self.x, self.y, self.SIZE_CELL, self.SIZE_CELL))
        if self.num_mines > 0:
            # Draw the number of adjacent mines
            font = pygame.font.SysFont("Arial", 30)
            text_surface = font.render(str(self.num_mines), True, Draw.BLACK)
            text_rect = text_surface.get_rect()
            text_rect.center = (self.x + self.SIZE_CELL / 2, self.y + self.SIZE_CELL / 2)
            screen.blit(text_surface, text_rect)
        # Draw the cell border
        pygame.draw.rect(screen, Draw.BLACK,
                         pygame.Rect(self.x, self.y, self.SIZE_CELL, self.SIZE_CELL), 2)