import json
import math
from random import random
from sqlite3 import Date

import pygame
import random
from Board import Board
from Cell import Cell
from Draw import Draw
from MineCell import MineCell
from RevealedCell import RevealedCell
from datetime import datetime

def not_all_revealed_or_flagged():
    return any(
        not isinstance(cell, MineCell) and not isinstance(cell, RevealedCell) for row in board.board for cell in row)


def add_game_data(data_file, game_data):
        try:
            # Open the file in read mode.
            f = open(data_file, "r+")
        except FileNotFoundError:
            # If the file does not exist, create a new one.
            f = open(data_file, "w")
            # תוסיף לדף מערך ריק
            json.dump([], f)
            f.close()
            f = open(data_file, "r+")
        try:
            data = json.load(f)
        except json.decoder.JSONDecodeError:
            # If the file is empty, initialize it with an empty list.
            data = []

        # Check if the existing data structure is compatible.
        if not isinstance(data, list):
            raise ValueError("The existing data is not in a list format.")

        # Try to convert the 'date' field to a JSON-compatible format
        try:
            game_data["date"] = game_data["date"].strftime("%Y-%m-%d %H:%M:%S")
        except TypeError:
            # If the conversion fails, log an error and skip the game data
            print(f"Failed to convert date to JSON format: {game_data['date']}")
            return

        # Update the existing data.
        data.append(game_data)

        # Write the updated data back to the file.
        f.seek(0)
        json.dump(data, f)

        # Close the file
        f.close()


def game_over():
    draw.game_ended = True
    # תציג את כל המוקשים
    for row in board.board:
        for cell in row:
            if isinstance(cell, MineCell):
                draw.draw_mine(draw.screen, cell)
                pygame.display.flip()

    # תעבור על הלוח מהאצע לפינות בצורה רנדומלית
    # ותחשוף את התאים
    while len(board.hidden_cells) > 0:
        i, j = random.choice(list(board.hidden_cells.keys()))
        board.reveal_cell(board.board[i][j])

        draw.draw_grid(board)
    # תציג הודעה "הפסדת"

    # תוסיף תאריך כולל שעות ודקות לקובץ data.json
    game_data = {"date": datetime.now(), "win": False}

    add_game_data("data.json", game_data)
    draw.draw_grid(board)

    # Draw the results.
    draw.draw_results("data.json")


def handle_click_cell(cell):
    if isinstance(cell, RevealedCell):
        return
    if cell.is_flagged:
        return
    if isinstance(cell, MineCell):
        game_over()

    else:
        board.reveal_cell(cell)
        draw.draw_grid(board)
        if board.has_all_revealed():
            game_win()


def handle_right_click_cell(cell):
    cell.is_flagged = not cell.is_flagged
    draw.draw_grid(board)


def game_win():
    print("game win")
    game_data = {"date": datetime.now(), "win": True}
    add_game_data("data.json", game_data)
    draw.draw_grid(board)
    draw.draw_results("data.json")


def handle_click(mouse_x, mouse_y, left_click=True):
    for row in board.board:
        for cell in row:
            if cell.x < mouse_x < cell.x + Cell.SIZE_CELL and cell.y < mouse_y < cell.y + cell.SIZE_CELL:
                if left_click:
                    handle_click_cell(cell)
                else:
                    handle_right_click_cell(cell)
                    if board.has_all_revealed():
                        game_win()
                return


def handle_first_click(x, y):
    # תמצא את התא שנלחץ
    row = int(y / Cell.SIZE_CELL)
    col = int(x / Cell.SIZE_CELL)
    # תעבור על 7 תאים סמוכים לתא שנלחץ ותהפוך טותם לתאים שאינם מוקשים
    board.initMines(row, col)
    board.reveal_cell(board.board[row][col])
    draw.draw_grid(board)


def draw_grid(self):
    draw.draw_grid(self.board)


is_first_click = True
board = Board(10, 20)
draw = Draw(500, 500, board)
draw.draw_grid(board)

finish = False
draw.game_ended = False
while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True
        elif event.type == pygame.MOUSEBUTTONDOWN and not draw.game_ended:
            # Get the position of the mouse
            x, y = pygame.mouse.get_pos()
            # Check if the left or right mouse button was clicked
            if is_first_click:
                board = Board(10, 20)
                draw = Draw(500, 500, board)
                handle_first_click(x, y)
                is_first_click = False
            if event.button == pygame.BUTTON_LEFT:
                handle_click(x, y)
            elif event.button == pygame.BUTTON_RIGHT:
                handle_click(x, y, False)
