# Tic-Tac-Toe Game

This is a simple command-line implementation of the classic Tic-Tac-Toe game, where a human player can compete against an AI opponent. The AI can either make random moves or use an optimal strategy based on the Minimax algorithm.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Game Rules](#game-rules)
- [Code Breakdown](#code-breakdown)
- [License](#license)

## Features

- Play against a computer opponent.
- Option for the computer to make random moves or optimal moves using the Minimax algorithm.
- Simple command-line interface to input moves.
- Displays the current state of the board after each move.

## Requirements

- Python 3.x

## Installation

1. Clone the repository or download the code.
2. Ensure you have Python 3 installed on your machine.
3. Navigate to the directory containing the code.

## Usage

1. Run the game by executing the following command in your terminal:

   ```bash
   python tic_tac_toe.py
   ```

2. Follow the on-screen prompts to enter your moves. Input your move as two numbers separated by a comma, representing the row and column (0-indexed).

3. The game will alternate turns between you (X) and the computer (O).

4. The game ends when either player wins or if there is a tie.

## Game Rules

- The game is played on a 3x3 grid.
- Players take turns placing their symbol (X or O) in an empty cell.
- The first player to align three of their symbols horizontally, vertically, or diagonally wins the game.
- If all cells are filled and no player has won, the game is a tie.

## Code Breakdown

### Functions

- `print_board(board)`: Displays the current state of the Tic-Tac-Toe board.
  
- `get_empty_cells(board)`: Returns a list of tuples representing the indices of empty cells on the board.

- `check_winner(board)`: Checks the board for a winner and returns the winning symbol ('X' or 'O') or `None` if there is no winner.

- `computer_move(board)`: Makes a random move for the computer.

- `optimal_computer_move(board, player)`: Determines the optimal move for the computer using the Minimax algorithm.

- `minimax(board, depth, is_maximizing)`: Implements the Minimax algorithm to evaluate the best possible move for the computer.

- `main()`: The main function that runs the game loop, handles player input, and checks for game status.

### Game Flow

1. The game initializes a 3x3 board.
2. The current player is set to 'X' (the human player).
3. The game enters a loop where it:
   - Displays the board.
   - Prompts the human player for their move.
   - Executes the computer's move (either random or optimal).
   - Checks for a winner or a tie.
   - Switches the current player.
4. The loop continues until there is a winner or a tie.

## License

This project is licensed under the MIT License. Feel free to modify and distribute the code as you wish.
