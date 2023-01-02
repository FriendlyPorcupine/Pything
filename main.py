# import the puzzle class
import a_star
import puzzle_class as puzzle


def play_game():
    """ To play the 8-Puzzle as a User on the Console """
    game = puzzle.init_puzzle()  # Create puzzle to play & print it to console
    game.print_puzzle()

    while game.puzzle_unordered():  # Loop until the puzzle is solved
        print('Possible Moves are: ', game.moves_possible())
        direction = input('Make a move :')  # Scan the move of the player
        game.move_tile(direction)
        game.print_puzzle()

    print('The puzzle is solved')
    game.print_puzzle()


if __name__ == '__main__':
    #  play_game()
    print(a_star.average_expanded_nodes("h"))

    # for i in range(5):
    #   p = puzzle.Puzzle(puzzle.init_puzzle())
    #  print(p.manhattan_heuristic())
