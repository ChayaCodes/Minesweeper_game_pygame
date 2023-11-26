from Cell import Cell
from Draw import Draw


class MineCell(Cell):
    def __init__(self, cell):
        super().__init__(cell.row, cell.col)

    def draw(self, screen):
        super().draw(screen)
        # אם המשחק נגמר תציג את המוקש
        if Draw.game_ended:
            Draw.draw_mine(screen, self)

