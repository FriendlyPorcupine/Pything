# import the puzzle class
import a_star
import puzzle_class as puzzle
import statistics
import pandas as pd


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


def merge_dictionary(dict_1, dict_2):
    new_dictionary = {**dict_1, **dict_2}
    for key, value in new_dictionary.items():
        if key in dict_1 and key in dict_2:
            new_dictionary[key] = [dict_1[key], dict_2[key]]
    return new_dictionary


if __name__ == '__main__':
    # play_game()

    one_hundred_tries_manhattan = a_star.expanded_nodes_time('m')
    one_hundred_tries_hamming = a_star.expanded_nodes_time('h')

    merged_dictionary = merge_dictionary(one_hundred_tries_manhattan, one_hundred_tries_hamming)

    df = pd.DataFrame.from_dict(merged_dictionary).T
    df.columns = ['Manhattan: (Nodes, Time)', 'Hamming: (Nodes, Time)']

    print(df, end='\n\n')

    node_list_manhattan = []
    node_list_hamming = []

    time_list_manhattan = []
    time_list_hamming = []

    for i in one_hundred_tries_manhattan:
        node_list_manhattan.append(list(one_hundred_tries_manhattan.values())[i-1][0])
        node_list_hamming.append(list(one_hundred_tries_hamming.values())[i-1][0])

        time_list_manhattan.append(list(one_hundred_tries_manhattan.values())[i-1][1])
        time_list_hamming.append(list(one_hundred_tries_hamming.values())[i-1][1])

    mean_nodes_manhattan = round(statistics.mean(node_list_manhattan), 2)
    deviation_nodes_manhattan = round(statistics.stdev(node_list_manhattan), 2)

    mean_nodes_hamming = round(statistics.mean(node_list_hamming), 2)
    deviation_nodes_hamming = round(statistics.stdev(node_list_hamming), 2)

    mean_time_manhattan = round(statistics.mean(time_list_manhattan), 2)
    deviation_time_manhattan = round(statistics.stdev(time_list_manhattan), 2)

    mean_time_hamming = round(statistics.mean(time_list_hamming), 2)
    deviation_time_hamming = round(statistics.stdev(time_list_hamming), 2)

    max_manhattan = (max(node_list_manhattan), max(time_list_manhattan))
    max_hamming = (max(node_list_hamming), max(time_list_hamming))

    min_manhattan = (min(node_list_manhattan), min(time_list_manhattan))
    min_hamming = (min(node_list_hamming), min(time_list_hamming))

    print('Manhattan:'
          '\nThe A*-Algorithm using the Manhattan-Heuristic expanded a total of', sum(node_list_manhattan), 'Nodes',
          '\nThe puzzle with the max time and nodes needed:', max_manhattan[0], 'Nodes', 'and', max_manhattan[1], 'sec',
          '\nThe puzzle with the min time and nodes needed:', min_manhattan[0], 'Nodes', 'and', min_manhattan[1], 'sec',
          '\n -> mean Nodes expanded:', mean_nodes_manhattan, 'with standard deviation', deviation_nodes_manhattan,
          '\n -> mean Time needed:', mean_time_manhattan, 'with standard deviation', deviation_time_manhattan,
          end='\n\n')

    print('Hamming:'
          '\nThe A*-Algorithm using the Hamming-Heuristic expanded a total of', sum(node_list_hamming), 'Nodes',
          '\nThe puzzle with the max time and nodes needed:', max_hamming[0], 'Nodes', 'and', max_hamming[1], 'sec',
          '\nThe puzzle with the min time and nodes needed:', min_hamming[0], 'Nodes', 'and', min_hamming[1], 'sec',
          '\n -> mean Nodes expanded:', mean_nodes_hamming, 'with standard deviation', deviation_nodes_hamming,
          '\n -> mean Time needed:', mean_time_hamming, 'with standard deviation', deviation_time_hamming, end='\n\n')
