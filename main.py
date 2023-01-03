# import the puzzle class
import a_star
import puzzle_class as puzzle
import statistics


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

    one_hundred_tries_manhattan = a_star.expanded_nodes_time('m')
    one_hundred_tries_hamming = a_star.expanded_nodes_time('h')

    node_list_manhattan = []
    node_list_hamming = []

    time_list_manhattan = []
    time_list_hamming = []

    for i in one_hundred_tries_manhattan:
        node_list_manhattan.append(list(one_hundred_tries_manhattan.values())[i][0])
        node_list_hamming.append(list(one_hundred_tries_hamming.values())[i][0])

        time_list_manhattan.append(list(one_hundred_tries_manhattan.values())[i][1])
        time_list_hamming.append(list(one_hundred_tries_hamming.values())[i][1])

    mean_nodes_manhattan = round(statistics.mean(node_list_manhattan), 2)
    deviation_nodes_manhattan = round(statistics.stdev(node_list_manhattan), 2)

    mean_nodes_hamming = round(statistics.mean(node_list_hamming), 2)
    deviation_nodes_hamming = round(statistics.stdev(node_list_hamming), 2)

    mean_time_manhattan = round(statistics.mean(time_list_manhattan), 2)
    deviation_time_manhattan = round(statistics.stdev(time_list_manhattan), 2)

    mean_time_hamming = round(statistics.mean(time_list_hamming), 2)
    deviation_time_hamming = round(statistics.stdev(time_list_hamming), 2)

    print('Manhattan:\nNodes:', mean_nodes_manhattan, 'with standard deviation', deviation_nodes_manhattan)
    print('Time:', mean_time_manhattan, 'with standard deviation', deviation_time_manhattan, end='\n')

    print('Hamming:\nNodes:', mean_nodes_hamming, 'with standard deviation', deviation_nodes_hamming)
    print('Time:', mean_time_hamming, 'with standard deviation', deviation_time_hamming)





