# In the Anaconda prompter use 'conda install numpy' command & confirm with 'y'
import numpy as np


def init_puzzle():
    """ Define a function to initialize the puzzle

    :return: 2D Array with random puzzle """
    puzzle = np.arange(9)  # Create a array to represent the puzzle
    np.random.shuffle(puzzle)  # Shuffle the puzzle to create a random starting configuration

    while not puzzle_solvable(puzzle):  # check if the puzzle is solvable
        puzzle = init_puzzle()  # recursive call of init_puzzle to make new puzzle and check if new is solvable

    # Shape the array into a 2D array AFTER it was shuffled to assure rows and cols get mixed
    return puzzle.reshape((3, 3))


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


def moves_possible(puzzle):
    directions = ['up', 'down', 'left', 'right']  # array with the four possible directions
    empty_row, empty_col = find_empty(puzzle)  # get the position of the empty tile

    if empty_row == 0:
        directions.remove('up')  # if the empty tile is in row 0, it cannot move up
    elif empty_row == 2:
        directions.remove('down')  # if the empty tile is in row 2, it cannot move down

    if empty_col == 0:
        directions.remove('left')  # if the empty tile is in col 0, it cannot move left
    elif empty_col == 2:
        directions.remove('right')  # if the empty tile is in col 0, it cannot move right

    return directions


def move_tile(puzzle, direction):
    """ Define a function to move a tile in the puzzle

    :param puzzle: 2D Array
    :param direction: up, down, left, right
    :return: Boolean """
    empty_row, empty_col = find_empty(puzzle)  # Get the position of the empty tile
    possible = moves_possible(puzzle)  # Get possible directions to move the tile

    # Move the empty tile in the specified direction up & down change the row, left & right change the col
    if direction == "up" and direction in possible:
        puzzle[empty_row][empty_col] = puzzle[empty_row - 1][empty_col]
        puzzle[empty_row - 1][empty_col] = 0
    elif direction == "down" and direction in possible:
        puzzle[empty_row][empty_col] = puzzle[empty_row + 1][empty_col]
        puzzle[empty_row + 1][empty_col] = 0
    elif direction == "left" and direction in possible:
        puzzle[empty_row][empty_col] = puzzle[empty_row][empty_col - 1]
        puzzle[empty_row][empty_col - 1] = 0
    elif direction == "right" and direction in possible:
        puzzle[empty_row][empty_col] = puzzle[empty_row][empty_col + 1]
        puzzle[empty_row][empty_col + 1] = 0
    else:
        print('Move not possible')
        return False
    return True


def manhattan_heuristic(puzzle):
    goalPuzzle = np.arange(9).reshape((3, 3))  # make correct puzzle to compare to
    heuristic = 0
    for i in range(9):
        # Get index of tile with number i for both puzzles
        indexPuzzle, indexGoal = tuple(np.argwhere(puzzle == i)[0]), tuple(np.argwhere(goalPuzzle == i)[0])

        steps = abs(indexGoal[0] - indexPuzzle[0]) + abs(indexGoal[1] - indexPuzzle[1])  # calculate needed steps
        heuristic += steps  # add all steps together
        # print(i, ':', indexPuzzle, '->', indexGoal, '=', steps, '|', heuristic)  # just for now
    return heuristic


def hamming_heuristic(puzzle):
    # already done by Raffael -> problems with git
    return 0


# To test the functions
# if __name__ == '__main__':
