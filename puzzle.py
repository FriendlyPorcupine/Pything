# In the Anaconda prompter use 'conda install numpy' command & confirm with 'y'
import numpy as np


# Define a function to initialize the puzzle
def init_puzzle():
    puzzle = np.arange(9)  # Create a array to represent the puzzle
    np.random.shuffle(puzzle)  # Shuffle the puzzle to create a random starting configuration

    # Shape the array into a 2D array AFTER it was shuffled to assure rows and cols get mixed
    shuffledPuzzle = puzzle.reshape((3, 3))
    return shuffledPuzzle


# Define a function to print the puzzle to the console
def print_puzzle(puzzleToPrint):
    for i in range(3):  # iterate ofer the rows of the puzzle
        print(' +---+---+---+')
        for j in range(3):  # iterate ofer the cols of the puzzle
            if puzzleToPrint[i][j] == 0:  # print the value of the tile
                print(' |', ' ', end='')
            else:
                print(' |', puzzleToPrint[i][j], end='')  # print nothing if value is zero (0) -> empty tile
        print(' |')
    print(' +---+---+---+')


# Define a function to find the position of the empty tile
def find_empty(puzzle):
    empty_row, empty_col = 0, 0

    for i in range(3):  # iterate ofer the rows of the puzzle
        for j in range(3):  # iterate ofer the cols of the puzzle
            if puzzle[i][j] == 0:  # find tile with value zero (0) & remember position in the 2D array
                empty_row, empty_col = i, j
    return empty_row, empty_col


# Define a function to check if the puzzle is solved
def puzzle_inorder(puzzle):
    puzzleInOrder = np.arange(9)  # Make an array with values in the correct order to compare to
    puzzle = puzzle.reshape(9)  # Reshape 2D array puzzle to simple array

    for i in puzzleInOrder:  # iterate ofer the hole array
        if puzzle[i] != puzzleInOrder[i]:  # check the values of puzzle match the array with correct order, if not ...
            return False
    return True


# Define a function to move a tile in the puzzle
def move_tile(puzzle, direction):
    empty_row, empty_col = find_empty(puzzle)  # Get the position of the empty tile

    # Move the empty tile in the specified direction up & down change the row, left & right change the col
    if direction == "up" and empty_row > 0:
        puzzle[empty_row][empty_col] = puzzle[empty_row - 1][empty_col]
        puzzle[empty_row - 1][empty_col] = 0

    elif direction == "down" and empty_row < 2:
        puzzle[empty_row][empty_col] = puzzle[empty_row + 1][empty_col]
        puzzle[empty_row + 1][empty_col] = 0

    elif direction == "left" and empty_col > 0:
        puzzle[empty_row][empty_col] = puzzle[empty_row][empty_col - 1]
        puzzle[empty_row][empty_col - 1] = 0

    elif direction == "right" and empty_col < 2:
        puzzle[empty_row][empty_col] = puzzle[empty_row][empty_col + 1]
        puzzle[empty_row][empty_col + 1] = 0
    else:
        return False
    return True


# maybe add function to count how many tiles are already at a correct position?
# To test the functions
"""
if __name__ == '__main__':
    p = init_puzzle()
    print_puzzle(p)
    print(puzzle_inorder(p))
    print(find_empty(p))
    move_tile(p, "right")
"""


