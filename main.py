# import the puzzle class
import numpy as np
import a_star
import puzzle_class as puzzle


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
    #  play_game()
    print(a_star.astar_alg("m"))

    # for i in range(5):
    #   p = puzzle.Puzzle(puzzle.init_puzzle())
    #  print(p.manhattan_heuristic())
