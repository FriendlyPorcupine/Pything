# import the puzzle class
import numpy as np
import puzzle as p
import solve as s

oneHundredTries = np.arange(100)

if __name__ == '__main__':
    """
    # First try's of playing the game 
    puzzle = p.init_puzzle()  # Create puzzle to play & print it to console
    p.print_puzzle(puzzle)

    while p.puzzle_inorder(puzzle) != 1:  # Loop until the puzzle is solved
        direction = input('Make a move (up, down, left, right): ')  # Scan the move of the player
        p.move_tile(puzzle, direction)

    print('The puzzle is solved')
    p.print_puzzle(puzzle)
    """

    for i in oneHundredTries:
        puzzle = p.init_puzzle()  # Create puzzle to play & print it to console
        p.move_tile(puzzle, 'down')  # Make puzzle with just one wrong tile
        moves = s.random_solve(puzzle)  # use the random solve method with simple puzzle
        oneHundredTries[i] = moves  # save the number of moves necessary to solve the puzzle
    print(oneHundredTries)

    # average of all tries
    allMovesTogether = 0
    for i in oneHundredTries:
        allMovesTogether += i
    print(allMovesTogether / 100)


