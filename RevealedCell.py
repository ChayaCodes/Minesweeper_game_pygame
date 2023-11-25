import pygame

from Cell import Cell
from Draw import Draw


class RevealedCell(Cell):
    COLOR = Draw.WHITE
    def __init__(self, cell, num_mines):
        super().__init__(cell.row, cell.col)
        self.num_mines = num_mines


    def draw(self, screen):
        # ציור הריבוע
        pygame.draw.rect(screen, self.COLOR,
                         pygame.Rect(self.x, self.y, self.SIZE_CELL, self.SIZE_CELL))
        if self.num_mines > 0:
            # ציור הטקסט
            font = pygame.font.SysFont("Arial", 30)
            text_surface = font.render(str(self.num_mines), True, Draw.BLACK)
            text_rect = text_surface.get_rect()
            text_rect.center = (self.x + self.SIZE_CELL / 2, self.y + self.SIZE_CELL / 2)
            screen.blit(text_surface, text_rect)
        # ציור המסגרת
        pygame.draw.rect(screen, Draw.BLACK,
                         pygame.Rect(self.x, self.y, self.SIZE_CELL, self.SIZE_CELL), 2)