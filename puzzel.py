# Import necessary modules
import random

# Define a function to initialize the puzzle
def initialize_puzzle():
  # Create a 2D array to represent the puzzle
  puzzle = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 0]]

  # Shuffle the puzzle to create a random starting configuration
  random.shuffle(puzzle)

  return puzzle

# Define a function to move a tile in the puzzle
def move_tile(puzzle, direction):
  # Get the position of the empty tile
  for i in range(3):
    for j in range(3):
      if puzzle[i][j] == 0:
        empty_row = i
        empty_col = j
        break

  # Move the empty tile in the specified direction
  if direction == "up" and empty_row > 0:
    puzzle[empty_row][empty_col] = puzzle[empty_row - 1][empty_col]
    puzzle[empty_row - 1][empty_col]

