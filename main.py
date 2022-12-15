# import the puzzle class
import puzzel as p

if __name__ == '__main__':
    puzzle = p.init_puzzle()  # Create puzzle to play & print it to console
    p.print_puzzle(puzzle)

    while p.puzzle_inorder(puzzle) != 1:  # Loop until the puzzle is solved
        direction = input('Make a move (up, down, left, right): ')  # Scan the move of the player
        p.move_tile(puzzle, direction)

    print('The puzzle is solved')
    p.print_puzzle(puzzle)

