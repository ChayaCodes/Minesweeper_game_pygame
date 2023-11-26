import json
import pygame

class Draw:
    """
    The Draw class is responsible for all the drawing operations in the Minesweeper game.
    """

    game_ended = False
    GREEN = (0, 255, 0)
    screen = None
    WHITE = (255, 255, 255)
    COLOR_HIDDEN_CELL = (255, 0, 0)
    COLOR_BORDER = (0, 0, 0)
    COLOR_REVEAL_COLOR = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)

    def __init__(self, board, width = None, height = None):
        """
        Initialize a new Draw instance.

        Args:
            width (int): The width of the game window.
            height (int): The height of the game window.
            board (Board): The game board.
        """
        if width is None or height is None:
            self.width = board.get_size_of_board()
            self.height = board.get_size_of_board()
        else:
            self.width = width
            self.height = height

        pygame.init()
        size = (self.width, self.height)
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Minesweeper")
        self.screen.fill(self.WHITE)

    def draw_grid(self, board):
        """
        Draw the game grid on the screen.

        Args:
            board (Board): The game board.
        """
        for i in range(board.size):
            for j in range(board.size):
                (board.board[i][j]).draw(self.screen)
        pygame.display.flip()

    @classmethod
    def draw_flag(cls, screen, cell):
        """
        Draw a flag on a cell.

        Args:
            screen (pygame.Surface): The screen to draw the flag on.
            cell (Cell): The cell to draw the flag on.
        """
        # Draw the triangle
        pygame.draw.polygon(screen, cls.RED, [(cell.x + cell.SIZE_CELL * 2 / 3, cell.y + cell.SIZE_CELL / 4),
                                              (cell.x + cell.SIZE_CELL / 4, cell.y + cell.SIZE_CELL / 2),
                                              (cell.x + cell.SIZE_CELL * 2 / 3, cell.y + cell.SIZE_CELL * 3 / 5)])
        # Draw the line
        pygame.draw.line(screen, cls.BLACK, (cell.x + cell.SIZE_CELL * 2 / 3, cell.y + cell.SIZE_CELL / 4),
                         (cell.x + cell.SIZE_CELL * 2 / 3, cell.y + cell.SIZE_CELL * 4 / 5), 5)

    @classmethod
    def draw_mine(cls, screen, self):
        """
        Draw a mine on a cell.

        Args:
            screen (pygame.Surface): The screen to draw the mine on.
            self (Cell): The cell to draw the mine on.
        """
        # Draw the circle
        pygame.draw.circle(screen, cls.BLACK,
                           (self.x + self.SIZE_CELL / 2, self.y + self.SIZE_CELL / 2), self.SIZE_CELL / 3)
        # Draw the cross
        pygame.draw.line(screen, cls.BLACK, (self.x + self.SIZE_CELL / 3, self.y + self.SIZE_CELL / 2),
                         (self.x + self.SIZE_CELL * 2 / 3, self.y + self.SIZE_CELL / 2), 5)
        pygame.draw.line(screen, cls.BLACK, (self.x + self.SIZE_CELL / 2, self.y + self.SIZE_CELL / 3),
                         (self.x + self.SIZE_CELL / 2, self.y + self.SIZE_CELL * 2 / 3), 5)

    def draw_results(self, data_file):
        """
        Draw the results of the game on the screen.

        Args:
            data_file (str): The path to the file containing the game data.
        """
        with open(data_file, "r") as f:
            data = json.load(f)

        # Get the last game data.
        last_game = data[-1]

        # Check if the last game was a win or a loss.
        if last_game["win"]:
            win_text = "you win!"
        else:
            win_text = "you lose!"

        # Create a transparent rectangle surface
        surface = pygame.Surface((400, 400))
        surface.set_alpha(190)  # Set the alpha value (0-255) for transparency

        # Fill the surface with white color
        surface.fill((255, 255, 255))

        # Blit the surface onto the screen
        self.screen.blit(surface, (self.width // 2 - 200, self.height // 2 - 200))

        # Draw the text "ניצחת!" or "נכשלת!" in the center of the rectangle.
        font = pygame.font.Font(None, 100)
        text = font.render(win_text, True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (self.width // 2, self.height * 1 / 4)
        self.screen.blit(text, text_rect)

        # draw the text "previous games" in the center of the rectangle.
        font = pygame.font.Font(None, 35)
        text = font.render("previous games:", True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (self.width // 2, self.height * 2/5)
        self.screen.blit(text, text_rect)

        # Draw the three previous games.
        for i in range(-1, -6, -1):
            try:
                game = data[i]
            except IndexError:
                break
            date = game["date"]
            win = "win" if game["win"] else "lose"
            font = pygame.font.Font(None, 20)
            text = font.render(f"{date}: {win}", True, (0, 0, 0))
            text_rect = text.get_rect()
            text_rect.center = (self.width / 2, self.height * (i + 15) / 20)
            self.screen.blit(text, text_rect)

        # add a button to play again
        self.game_ended = True
        font = pygame.font.Font(None, 30)
        text = font.render("play again", True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (self.width / 2, self.height * 4 / 5)
        self.screen.blit(text, text_rect)
        pygame.draw.rect(self.screen, self.RED, pygame.Rect(self.width / 2 - 100, self.height * 4 / 5 - 25, 200, 50),
                         0)
        self.play_again_button = {"x": self.width / 2 - 100, "y": self.height * 4 / 5 - 25, "width": 200, "height": 50}
        self.screen.blit(text, text_rect)
        pygame.draw.rect(self.screen, self.BLACK, pygame.Rect(self.width / 2 - 100, self.height * 4 / 5 - 25, 200, 50), 2)
        self.play_again_button = {"x": self.width / 2 - 100, "y": self.height * 4 / 5 - 25, "width": 200, "height": 50}

        # add event to the button


        # Flip the screen.
        pygame.display.flip()