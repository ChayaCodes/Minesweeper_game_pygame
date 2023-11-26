# Minesweeper Game 💣

Welcome to the Minesweeper game, a Python implementation using Pygame with a fantastic graphical user interface! 🎮

## Features 🌟
- Graphical user interface 🖼️
- Customizable board size and mine density 🔍
- Flagging of suspected mines 🚩
- Game data is saved to a JSON file 💾

## How to Play 🕹️
The game starts with a grid of unrevealed cells. Your goal? Reveal all cells without mines! Click left to reveal a cell. If it's a mine-free cell, it shows the number of adjacent mines. Empty cells reveal their neighbors automatically. Right-click flags suspected mines; left-click won't reveal flagged cells.

## Code Structure 🧩
The code comprises several Python files:
- `main.py`: Runs the game, handling the game loop and user input 🎯
- `Board.py`: Defines the Board class, handling board initialization, mine calculation, cell revealing, and win/loss checks 🧭
- `Cell.py`, `MineCell.py`, `RevealedCell.py`: Define different cell types 📊
- `Draw.py`: Manages all drawing operations 🎨

## Installation and Running 🚀
To dive into the game:
1. Make sure you have Python and Pygame installed.
2. Install the required packages using `pip`: 
```bash
pip install pygame json random datetime
```

Then, you can run the game with:

```bash
python main.py
```