# In the Anaconda prompter use 'conda install numpy' command & confirm with 'y'
import numpy as np


def init_puzzle():
    """ Define a function to initialize the puzzle

    :return: 2D Array with random puzzle """
    puzzle = np.arange(9)  # Create a array to represent the puzzle
    np.random.shuffle(puzzle)  # Shuffle the puzzle to create a random starting configuration

    # Shape the array into a 2D array AFTER it was shuffled to assure rows and cols get mixed
    return puzzle.reshape((3, 3))


def print_puzzle(puzzleToPrint):
    """ Define a function to print the puzzle to the console

    :param puzzleToPrint: 2D Array """
    for i in range(3):  # iterate ofer the rows of the puzzle
        print(' +---+---+---+')
        for j in range(3):  # iterate ofer the cols of the puzzle
            if puzzleToPrint[i][j] == 0:  # print the value of the tile
                print(' |', ' ', end='')
            else:
                print(' |', puzzleToPrint[i][j], end='')  # print nothing if value is zero (0) -> empty tile
        print(' |')
    print(' +---+---+---+')


def find_empty(puzzle):
    """ Define a function to find the position of the empty tile

    :param puzzle: 2D Array
    :return: index of empty tile """
    for i in range(3):  # iterate ofer the rows of the puzzle
        for j in range(3):  # iterate ofer the cols of the puzzle
            if puzzle[i][j] == 0:  # find tile with value zero (0) & remember position in the 2D array
                return i, j


def puzzle_unordered(puzzle):
    """ Define a function to check if the puzzle is solved

    :param puzzle: 2D Array
    :return: Boolean """
    puzzleInOrder = np.arange(9)  # Make an array with values in the correct order to compare to
    puzzle = puzzle.reshape(9)  # Reshape 2D array puzzle to simple array

    for i in puzzleInOrder:  # iterate ofer the hole array
        if puzzle[i] != puzzleInOrder[i]:  # check the values of puzzle match the array with correct order, if not ...
            return True
    return False


def move_tile(puzzle, direction):
    """ Define a function to move a tile in the puzzle

    :param puzzle: 2D Array
    :param direction: up, down, left, right
    :return: Boolean """
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


def puzzle_solvable(puzzle):
    """ Define a function to find out if the puzzle is solvable

    :param puzzle: 2D Array
    :return: boolean """
    inverseCount = 0
    puzzle = puzzle.reshape(9)  # reshape the 2D Array into a 1D Array
    for i in range(9):
        for j in range(i + 1, 9):  # compare i with number to the right of i
            if puzzle[i] > puzzle[j] and (puzzle[j] != 0 and puzzle[i] != 0):
                inverseCount += 1  # if the 1st number is bigger than the 2nd number, increase counter
    return bool((inverseCount % 2) == 0)  # if the counter is a even the puzzle is solvable

# maybe add function to count how many tiles are already at a correct position?
# To test the functions


# if __name__ == '__main__':
