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


# To print the puzzle to the console
def print_puzzle(puzzleToPrint):
    for i in range(3):
        print(' +---+---+---+')
        for j in range(3):
            if puzzleToPrint[i][j] == 0:
                print(' |', ' ', end='')
            else:
                print(' |', puzzleToPrint[i][j], end='')
        print(' |')
    print(' +---+---+---+')


def find_empty(puzzle):
    empty_row = 0
    empty_col = 0

    for i in range(3):
        for j in range(3):
            if puzzle[i][j] == 0:
                empty_row = i
                empty_col = j
    return empty_row, empty_col


def puzzle_inorder(puzzle):
    # Make array to compare to
    puzzleInOrder = np.arange(9)
    # reshape puzzle to array
    puzzle = puzzle.reshape(9)
    # make boolean value for return statement & set to true (1) as a start value
    inOrder = 1

    # print(puzzle, '==', puzzleInOrder)  # only for now to check the function

    for i in puzzleInOrder:
        if puzzle[i] != puzzleInOrder[i]:
            inOrder = 0
            break
    return bool(inOrder == 1)


# Define a function to move a tile in the puzzle
def move_tile(puzzle, direction):
    # Get the position of the empty tile
    empty_row = find_empty(puzzle)[0]
    empty_col = find_empty(puzzle)[1]

    print('empty_tile: ', empty_row, empty_col)

    # Move the empty tile in the specified direction up & down change the row, left & right change the col
    if direction == "up" and empty_row > 0:
        puzzle[empty_row][empty_col] = puzzle[empty_row - 1][empty_col]
        puzzle[empty_row - 1][empty_col] = 0
        print_puzzle(puzzle)

    elif direction == "down" and empty_row < 2:
        puzzle[empty_row][empty_col] = puzzle[empty_row + 1][empty_col]
        puzzle[empty_row + 1][empty_col] = 0
        print_puzzle(puzzle)

    elif direction == "left" and empty_col > 0:
        puzzle[empty_row][empty_col] = puzzle[empty_row][empty_col - 1]
        puzzle[empty_row][empty_col - 1] = 0
        print_puzzle(puzzle)

    elif direction == "right" and empty_col < 2:
        puzzle[empty_row][empty_col] = puzzle[empty_row][empty_col + 1]
        puzzle[empty_row][empty_col + 1] = 0
        print_puzzle(puzzle)
    else:
        print('move not possible')


# To test the functions
if __name__ == '__main__':
    p = init_puzzle()
    print_puzzle(p)
    #print(puzzle_inorder(p))
    #print(find_empty(p))
    #move_tile(p, "right")
