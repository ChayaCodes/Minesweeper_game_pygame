from Cell import Cell
from Draw import Draw


class MineCell(Cell):
    """
    The MineCell class represents a mine cell in a Minesweeper game.
    It inherits from the Cell class.
    """

    def __init__(self, cell):
        """
        Initialize a new MineCell instance.

        Args:
            cell (Cell): The cell to convert to a MineCell.
        """
        super().__init__(cell.row, cell.col)

    def draw(self, screen):
        """
        Draw the mine cell on the given screen.
        If the game has ended, the mine is revealed.

        Args:
            screen (pygame.Surface): The screen to draw the cell on.
        """
        super().draw(screen)
        # If the game has ended, reveal the mine
        if Draw.game_ended:
            Draw.draw_mine(screen, self)
