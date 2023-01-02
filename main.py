# import the puzzle class
import a_star
import puzzle_class as puzzle
import time


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

    print('Manhattan: ')
    start_time = time.time()
    print('average_Nodes:', a_star.average_expanded_nodes('m'))
    end_time = time.time()
    Manhattan_time = end_time - start_time
    print('average_Time:', round(Manhattan_time, 2))

    '''
    print('-----------------------\n')

    print('Hamming:')
    start_time = time.time()
    print('average_Nodes:', a_star.average_expanded_nodes('h'))
    end_time = time.time()
    Hamming_time = end_time - start_time
    print('average_Time:', round(Hamming_time, 2))
    '''

