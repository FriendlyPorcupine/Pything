# import the puzzle class
import numpy as np
import puzzle
import solve

oneHundredTries = np.arange(100)


def one_hundred(arrayWithMoves):
    for i in arrayWithMoves:
        game = puzzle.init_puzzle()  # Create puzzle to play & print it to console
        puzzle.move_tile(game, 'down')  # Make puzzle with just one wrong tile
        moves = solve.random_solve(game)  # use the random solve method with simple puzzle
        arrayWithMoves[i] = moves  # save the number of moves necessary to solve the puzzle
    return arrayWithMoves


def average(arrayToCalculate):
    allMovesTogether = 0
    for i in arrayToCalculate:
        allMovesTogether += i  # add the moves needed to solve the puzzle
    averageMovesNeeded = allMovesTogether / len(arrayToCalculate)
    return averageMovesNeeded


def play_game():
    """ To play the 8-Puzzle as a User on the Console """
    game = puzzle.init_puzzle()  # Create puzzle to play & print it to console
    puzzle.print_puzzle(game)

    while puzzle.puzzle_unordered(game):  # Loop until the puzzle is solved
        print('Possible Moves are: ', puzzle.moves_possible(game))
        direction = input('Make a move :')  # Scan the move of the player
        puzzle.move_tile(game, direction)
        puzzle.print_puzzle(game)

    print('The puzzle is solved')
    puzzle.print_puzzle(game)


if __name__ == '__main__':
    play_game()
