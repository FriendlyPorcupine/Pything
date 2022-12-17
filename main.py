# import the puzzle class
import numpy as np
import puzzle as p
import solve as s

oneHundredTries = np.arange(100)


def one_hundred(arrayWithMoves):
    for i in arrayWithMoves:
        puzzle = p.init_puzzle()  # Create puzzle to play & print it to console
        p.move_tile(puzzle, 'down')  # Make puzzle with just one wrong tile
        moves = s.random_solve(puzzle)  # use the random solve method with simple puzzle
        arrayWithMoves[i] = moves  # save the number of moves necessary to solve the puzzle
    return arrayWithMoves


def average(arrayToCalculate):
    allMovesTogether = 0
    for i in arrayToCalculate:
        allMovesTogether += i  # add the moves needed to solve the puzzle
    averageMovesNeeded = allMovesTogether / 100
    return averageMovesNeeded


def play_puzzle_game():
    puzzle = p.init_puzzle()  # Create puzzle to play & print it to console
    p.print_puzzle(puzzle)

    while p.puzzle_inorder(puzzle) != 1:  # Loop until the puzzle is solved
        direction = input('Make a move (up, down, left, right): ')  # Scan the move of the player
        p.move_tile(puzzle, direction)
        p.print_puzzle(puzzle)

    print('The puzzle is solved')
    p.print_puzzle(puzzle)


if __name__ == '__main__':
    # print(average(one_hundred(oneHundredTries)))
    play_puzzle_game()
