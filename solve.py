# import necessary classes
import numpy as np
import puzzle as p

directions = ['up', 'down', 'left', 'right']  # array with the four possible directions


def random_solve(unsolvedPuzzle):
    countMoves = 0  # variable to count how many moves where necessary to solve the puzzle
    while not p.puzzle_solvable(unsolvedPuzzle):  # check if the puzzle is solvable
        unsolvedPuzzle = p.init_puzzle()  # make new puzzle and check if new puzzle is solvable

    while p.puzzle_unordered(unsolvedPuzzle):  # Loop until the puzzle is solved
        direction = np.random.choice(directions)  # Choose random direction to move the empty tile
        if p.move_tile(unsolvedPuzzle, direction):  # if move is True count, increment countMoves
            countMoves += 1
        if countMoves >= 100:  # stop the while loop if the puzzle is not solved after 200 valid moves
            countMoves = 0
            return countMoves
    return countMoves


# To test the functions
"""
if __name__ == '__main__':
    puzzle = p.init_puzzle()  # init_puzzle function must not shuffle
    p.move_tile(puzzle, 'down')  # Make puzzle with just one wrong tile

    movesToSolve = random_solve(puzzle)

    print(movesToSolve, 'moves were necessary to solve the puzzle')
    p.print_puzzle(puzzle)
"""

