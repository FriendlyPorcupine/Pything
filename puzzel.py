# In the Anaconda prompter use 'conda install numpy' command & confirm with 'y'
import numpy as np


# Define a function to initialize the puzzle
def init_puzzle():
    # Create a array to represent the puzzle
    puzzle = np.arange(9)
    # Shuffle the puzzle to create a random starting configuration
    np.random.shuffle(puzzle)
    # Shape the array into a 2D array after it was shuffled to to assure rows and cols get mixed
    shuffledPuzzle = puzzle.reshape((3, 3))

    return shuffledPuzzle


# To print the 8-puzzel to the console
def print_puzzle(puzzleToPrint):
    for i in range(3):
        print(' +--------------+ ')
        for j in range(3):
            if puzzleToPrint[i][j] == 0:
                print(' | ', ' ', end='')
            else:
                print(' | ', puzzleToPrint[i][j], end='')
        print(' | ')
    print(' +--------------+ ')


"""
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
"""

# To test the functions
if __name__ == '__main__':
    p = init_puzzle()
    print_puzzle(p)
