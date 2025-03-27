import random

def print_board(board):
  """Prints the current state of the tic-tac-toe board."""
  print("-------------")
  for row in board:
    print("|", end="")
    for cell in row:
      print(f" {cell} ", end="|")
    print("\n-------------")

def get_empty_cells(board):
  """Returns a list of tuples representing the indices of empty cells."""
  empty_cells = []
  for row_index, row in enumerate(board):
    for col_index, cell in enumerate(row):
      if cell == " ":
        empty_cells.append((row_index, col_index))
  return empty_cells

def check_winner(board):
  """Checks if there is a winner and returns their symbol ('X' or 'O'),
  otherwise returns None.
  """
  # Check rows
  for row in board:
    if row[0] == row[1] == row[2] and row[0] != " ":
      return row[0]

  # Check columns
  for col in range(3):
    if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
      return board[0][col]

  # Check diagonals
  if (board[0][0] == board[1][1] == board[2][2] or
      board[0][2] == board[1][1] == board[2][0]) and board[1][1] != " ":
    return board[1][1]

  return None

def computer_move(board):
  """Makes a random move for the computer."""
  empty_cells = get_empty_cells(board)
  if empty_cells:
    row, col = random.choice(empty_cells)
    board[row][col] = "O"

def optimal_computer_move(board, player):
  """Makes an optimal move for the computer using recursion and Minimax."""
  best_score = float('-inf')
  best_move = None

  for row, col in get_empty_cells(board):
    board[row][col] = player
    score = minimax(board, 0, False)
    board[row][col] = " "  # Undo the move

    if score > best_score:
      best_score = score
      best_move = (row, col)

  if best_move:
    board[best_move[0]][best_move[1]] = player

def minimax(board, depth, is_maximizing):
  """Minimax algorithm to determine the optimal move."""
  winner = check_winner(board)
  if winner == "O":
    return 10 - depth
  elif winner == "X":
    return depth - 10
  elif not get_empty_cells(board):
    return 0

  if is_maximizing:
    best_score = float('-inf')
    for row, col in get_empty_cells(board):
      board[row][col] = "O"
      score = minimax(board, depth + 1, False)
      board[row][col] = " "
      best_score = max(score, best_score)
    return best_score
  else:
    best_score = float('inf')
    for row, col in get_empty_cells(board):
      board[row][col] = "X"
      score = minimax(board, depth + 1, True)
      board[row][col] = " "
      best_score = min(score, best_score)
    return best_score


def main():
  """Main function to run the tic-tac-toe game."""
  board = [[" " for _ in range(3)] for _ in range(3)]
  current_player = "X"

  while True:
    print_board(board)

    if current_player == "X":
      # Human player's turn
      while True:
        try:
          row, col = map(int, input("Enter your move (row, col) separated by comma: ").split(","))
          if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == " ":
            board[row][col] = current_player
            break
          else:
            print("Invalid move. Try again.")
        except (ValueError, IndexError):
          print("Invalid input. Enter two numbers between 0 and 2 separated by a comma.")
    else:
      # Computer's turn
      print("Computer's turn:")
      # Choose between random move or optimal move
      # computer_move(board)  # Uncomment for random move
      optimal_computer_move(board, current_player)  # Uncomment for optimal move

    winner = check_winner(board)
    if winner:
      print_board(board)
      print(f"{winner} wins!")
      break

    if not get_empty_cells(board):
      print_board(board)
      print("It's a tie!")
      break

    # Switch player
    current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
  main()
