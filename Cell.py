from abc import abstractmethod

import pygame
from Draw import Draw


class Cell:
    SIZE_CELL = 50
    COLOR_HIDDEN_CELL = (0, 255, 0)

    @abstractmethod
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.x = col * self.SIZE_CELL
        self.y = row * self.SIZE_CELL
        self.isFlagged = False

    @abstractmethod
    def draw(self, screen):
        # ציור הריבוע
        pygame.draw.rect(screen, self.COLOR_HIDDEN_CELL,
                         pygame.Rect(self.x, self.y, self.SIZE_CELL, self.SIZE_CELL))
        #ציור המסגרת
        pygame.draw.rect(screen, Draw.BLACK,
                         pygame.Rect(self.x, self.y, self.SIZE_CELL, self.SIZE_CELL), 2)

        if self.isFlagged:
            # ציור הדגל
            pygame.draw.rect(screen, Draw.BLACK,
                             pygame.Rect(self.x + self.SIZE_CELL / 4, self.y + self.SIZE_CELL / 4,
                                         self.SIZE_CELL / 2, self.SIZE_CELL / 2))
            pygame.draw.rect(screen, Draw.RED,
                             pygame.Rect(self.x + self.SIZE_CELL / 4 + 2, self.y + self.SIZE_CELL / 4 + 2,
                                         self.SIZE_CELL / 2 - 4, self.SIZE_CELL / 2 - 4))
            pygame.draw.rect(screen, Draw.BLACK,
                             pygame.Rect(self.x + self.SIZE_CELL / 4 + 2, self.y + self.SIZE_CELL / 4 + 2,
                                         self.SIZE_CELL / 2 - 4, self.SIZE_CELL / 2 - 4), 2)




