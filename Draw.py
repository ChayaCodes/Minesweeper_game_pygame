import pygame



class Draw:
    screen = None
    WHITE = (255, 255, 255)
    COLOR_HIDDEN_CELL = (255, 0,0)
    COLOR_BORDER = (0,0,0)
    COLOR_REVEAL_COLOR = (255,255,255)
    BLACK = (0,0,0)
    RED = (255,0,0)

    def __init__(self, width, height,board):
        WINDOW_WIDTH = width
        WINDOW_HEIGHT = height
        pygame.init()
        size = (WINDOW_WIDTH, WINDOW_HEIGHT)
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Minesweeper")
        self.screen.fill(self.WHITE)
        self.drawGrid(board)

    def drawGrid(self, board):
        for i in range(board.size):
            for j in range(board.size):
               (board.board[i][j]).draw(self.screen)
        pygame.display.flip()






