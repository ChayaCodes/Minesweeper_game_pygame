import pygame


class Draw:
    game_ended = False
    GREEN = (0, 255, 0)
    screen = None
    WHITE = (255, 255, 255)
    COLOR_HIDDEN_CELL = (255, 0, 0)
    COLOR_BORDER = (0, 0, 0)
    COLOR_REVEAL_COLOR = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)

    def __init__(self, width, height, board):

        pygame.init()
        size = (width, height)
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Minesweeper")
        self.screen.fill(self.WHITE)

    def draw_grid(self, board):
        for i in range(board.size):
            for j in range(board.size):
                (board.board[i][j]).draw(self.screen)
        pygame.display.flip()

    @classmethod
    def draw_flag(cls, screen, cell):
        # ציור משולש
        pygame.draw.polygon(screen, cls.RED, [(cell.x + cell.SIZE_CELL * 2 / 3, cell.y + cell.SIZE_CELL / 4),
                                              (cell.x + cell.SIZE_CELL / 4, cell.y + cell.SIZE_CELL / 2),
                                              (cell.x + cell.SIZE_CELL * 2 / 3, cell.y + cell.SIZE_CELL * 3 / 5)])
        # ציור קו
        pygame.draw.line(screen, cls.BLACK, (cell.x + cell.SIZE_CELL * 2 / 3, cell.y + cell.SIZE_CELL / 4),
                         (cell.x + cell.SIZE_CELL * 2 / 3, cell.y + cell.SIZE_CELL * 4 / 5), 5)

    @classmethod
    def draw_mine(cls, screen, self):
        print("drow mine 2")
        # ציור העיגול
        pygame.draw.circle(screen, cls.BLACK,
                           (self.x + self.SIZE_CELL / 2, self.y + self.SIZE_CELL / 2), self.SIZE_CELL / 3)
        # ציור הקרס
        pygame.draw.line(screen, cls.BLACK, (self.x + self.SIZE_CELL / 3, self.y + self.SIZE_CELL / 2),
                         (self.x + self.SIZE_CELL * 2 / 3, self.y + self.SIZE_CELL / 2), 5)
        pygame.draw.line(screen, cls.BLACK, (self.x + self.SIZE_CELL / 2, self.y + self.SIZE_CELL / 3),
                         (self.x + self.SIZE_CELL / 2, self.y + self.SIZE_CELL * 2 / 3), 5)
