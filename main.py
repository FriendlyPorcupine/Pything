# import the puzzle class
import puzzel as p

if __name__ == '__main__':
    puzzle = p.init_puzzle()
    p.print_puzzle(puzzle)
    if p.puzzle_inorder(puzzle) == 0:
        print('Make a move: ')
        direction = 'up'
        p.move_tile(puzzle, direction)
    else:
        print('The Puzzle is solved')
