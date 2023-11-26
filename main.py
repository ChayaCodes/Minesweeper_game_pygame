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
    """
    Check if all cells on the board that are not mines have been revealed or flagged.

    Returns:
        bool: True if all non-mine cells have been revealed or flagged, False otherwise.
    """
    return any(
        not isinstance(cell, MineCell) and not isinstance(cell, RevealedCell) for row in board.board for cell in row)


def add_game_data(data_file, game_data):
    """
    Add game data to a JSON file.

    Args:
        data_file (str): The path to the JSON file.
        game_data (dict): The game data to add.
    """
    try:
        # Open the file in read mode.
        f = open(data_file, "r+")
    except FileNotFoundError:
        # If the file does not exist, create a new one.
        f = open(data_file, "w")
        # Add an empty list to the file.
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
    """
    End the game as a loss.
    """
    draw.game_ended = True
    # Reveal all mines.
    for row in board.board:
        for cell in row:
            if isinstance(cell, MineCell):
                draw.draw_mine(draw.screen, cell)
                pygame.display.flip()

    # Randomly reveal the remaining hidden cells.
    while len(board.hidden_cells) > 0:
        i, j = random.choice(list(board.hidden_cells.keys()))
        board.reveal_cell(board.board[i][j])

        draw.draw_grid(board)
    # Display a loss message.

    # Add the game data to the data file.
    game_data = {"date": datetime.now(), "win": False}

    add_game_data("data.json", game_data)
    draw.draw_grid(board)

    # Draw the results.
    draw.draw_results("data.json")


def handle_click_cell(cell):
    """
    Handle a left click on a cell.

    Args:
        cell (Cell): The cell that was clicked.
    """
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
    """
    Handle a right click on a cell.

    Args:
        cell (Cell): The cell that was clicked.
    """
    cell.is_flagged = not cell.is_flagged
    draw.draw_grid(board)


def game_win():
    """
    End the game as a win.
    """
    print("game win")
    game_data = {"date": datetime.now(), "win": True}
    add_game_data("data.json", game_data)
    draw.draw_grid(board)
    draw.draw_results("data.json")


def handle_click(mouse_x, mouse_y, left_click=True):
    """
    Handle a mouse click.

    Args:
        mouse_x (int): The x-coordinate of the mouse click.
        mouse_y (int): The y-coordinate of the mouse click.
        left_click (bool, optional): Whether the click was a left click. Defaults to True.
    """
    for row in board.board:
        for cell in row:
            if cell.x < mouse_x < cell.x + Cell.SIZE_CELL and cell.y < mouse_y < cell.y + Cell.SIZE_CELL:
                if left_click:
                    handle_click_cell(cell)
                else:
                    handle_right_click_cell(cell)
                    if board.has_all_revealed():
                        game_win()
                return


def handle_first_click(x, y):
    """
    Handle the first click of the game.

    Args:
        x (int): The x-coordinate of the click.
        y (int): The y-coordinate of the click.
    """
    # Find the cell that was clicked.
    row = int(y / Cell.SIZE_CELL)
    col = int(x / Cell.SIZE_CELL)
    # Initialize the mines on the board, avoiding the clicked cell and its neighbors.
    board.init_mines(row, col)
    board.reveal_cell(board.board[row][col])
    draw.draw_grid(board)


def draw_grid(self):
    """
    Draw the game grid on the screen.
    """
    draw.draw_grid(self.board)


is_first_click = True
board = Board(10, 20)
draw = Draw(board)
draw.draw_grid(board)

finish = False
draw.game_ended = False
while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True


        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not draw.game_ended:
                # Get the position of the mouse
                x, y = pygame.mouse.get_pos()
                # Check if the left or right mouse button was clicked
                if is_first_click:
                    handle_first_click(x, y)
                    is_first_click = False
                if event.button == pygame.BUTTON_LEFT:
                    handle_click(x, y)
                elif event.button == pygame.BUTTON_RIGHT:
                    handle_click(x, y, False)
            else:
                # If the game has ended, check if the user clicked in th play again button
                x, y = pygame.mouse.get_pos()
                if draw.play_again_button['x'] < x < draw.play_again_button['x'] + draw.play_again_button['width'] and \
                        draw.play_again_button['y'] < y < draw.play_again_button['y'] + draw.play_again_button[
                    'height']:
                    # If the user clicked the play again button, restart the game
                    board = Board(10, 20)
                    draw = Draw(board)
                    draw.draw_grid(board)
                    is_first_click = True
                    draw.game_ended = False
                    continue