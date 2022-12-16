# import necessary classes
import numpy as np
import puzzle as p

directions = ['up', 'down', 'left', 'right']  # array with the four possible directions


def random_solve(unsolvedPuzzle):
    countMoves = 0  # variable to count how many moves where necessary to solve the puzzle

    while p.puzzle_inorder(unsolvedPuzzle) != 1:  # Loop until the puzzle is solved
        direction = np.random.choice(directions)  # Choose random direction to move the empty tile
        if p.move_tile(unsolvedPuzzle, direction) == 1:  # if move is valid count, increment countMoves
            countMoves += 1
        if countMoves >= 100:  # stop the while loop if the puzzle is not solved after 200 valid moves
            countMoves = 0
            return countMoves

    return countMoves


if __name__ == '__main__':
    puzzle = p.init_puzzle()  # init_puzzle function must not shuffle
    p.move_tile(puzzle, 'down')  # Make puzzle with just one wrong tile

    movesToSolve = random_solve(puzzle)

    print(movesToSolve, 'moves were necessary to solve the puzzle')
    p.print_puzzle(puzzle)
