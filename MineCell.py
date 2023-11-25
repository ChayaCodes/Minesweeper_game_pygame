from Cell import Cell


class MineCell(Cell):
    def __init__(self, cell):
        super().__init__(cell.row, cell.col)

    def draw(self, screen):
        super().draw(screen)
