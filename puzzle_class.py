# In the Anaconda prompter use 'conda install numpy' command & confirm with 'y'
import numpy as np
import copy

class Puzzle:
    # constructor
    def __init__(self, puzzle_array):
        self.puzzle_array = puzzle_array

    def print_puzzle(self):
        """ Define a function to print the puzzle to the console

        :param puzzleToPrint: 2D Array """

        puzzleToPrint = self.puzzle_array
        for i in range(3):  # iterate ofer the rows of the puzzle
            print(' +---+---+---+')
            for j in range(3):  # iterate ofer the cols of the puzzle
                if puzzleToPrint[i][j] == 0:  # print the value of the tile
                    print(' |', ' ', end='')
                else:
                    print(' |', puzzleToPrint[i][j], end='')  # print nothing if value is zero (0) -> empty tile
            print(' |')
        print(' +---+---+---+')

    def find_empty(self):
        """ Define a function to find the position of the empty tile

        :param puzzle: 2D Array
        :return: index of empty tile """

        puzzle = copy.deepcopy(self.puzzle_array)
        for i in range(3):  # iterate ofer the rows of the puzzle
            for j in range(3):  # iterate ofer the cols of the puzzle
                if puzzle[i][j] == 0:  # find tile with value zero (0) & remember position in the 2D array
                    return i, j

    def puzzle_unordered(self):
        """ Define a function to check if the puzzle is solved

        :param puzzle: 2D Array
        :return: Boolean """
        puzzleInOrder = np.arange(9)  # Make an array with values in the correct order to compare to
        puzzle = self.puzzle_array.reshape(9)  # Reshape 2D array puzzle to simple array

        for i in puzzleInOrder:  # iterate ofer the hole array
            if puzzle[i] != puzzleInOrder[i]:  # check the values of puzzle match the array with correct order, if not..
                return True
        return False

    def moves_possible(self):
        """ Define a function to find all possible directions to move the empty tile

        :param puzzle: 2D Array
        :return: an array of strings with the directions """
        directions = ['up', 'down', 'left', 'right']  # array with the four possible directions
        empty_row, empty_col = self.find_empty()  # get the position of the empty tile

        if empty_row == 0:
            directions.remove('up')  # if the empty tile is in row 0, it cannot move up
        elif empty_row == 2:
            directions.remove('down')  # if the empty tile is in row 2, it cannot move down

        if empty_col == 0:
            directions.remove('left')  # if the empty tile is in col 0, it cannot move left
        elif empty_col == 2:
            directions.remove('right')  # if the empty tile is in col 0, it cannot move right

        return directions

    def move_tile(self, direction):
        """ Define a function to move a tile in the puzzle

        :param puzzle: 2D Array
        :param direction: up, down, left, right
        :return: Boolean """
        puzzle = copy.deepcopy(self.puzzle_array)
        empty_row, empty_col = self.find_empty()  # Get the position of the empty tile
        possible = self.moves_possible()  # Get possible directions to move the tile

        # Move the empty tile in the specified direction up & down change the row, left & right change the col
        if direction == "up" and direction in possible:
            puzzle[empty_row][empty_col] = puzzle[empty_row - 1][empty_col]
            puzzle[empty_row - 1][empty_col] = 0
            return Puzzle(puzzle)
        elif direction == "down" and direction in possible:
            puzzle[empty_row][empty_col] = puzzle[empty_row + 1][empty_col]
            puzzle[empty_row + 1][empty_col] = 0
            return Puzzle(puzzle)
        elif direction == "left" and direction in possible:
            puzzle[empty_row][empty_col] = puzzle[empty_row][empty_col - 1]
            puzzle[empty_row][empty_col - 1] = 0
            return Puzzle(puzzle)
        elif direction == "right" and direction in possible:
            puzzle[empty_row][empty_col] = puzzle[empty_row][empty_col + 1]
            puzzle[empty_row][empty_col + 1] = 0
            return Puzzle(puzzle)
        else:
            print('Move not possible')

    def manhattan_heuristic(self):
        """ Define a function to calculate the heuristic with "Manhattan"

        :param puzzle: 2D Array
        :return: integer -> heuristic """
        puzzle = copy.deepcopy(self.puzzle_array)
        goalPuzzle = np.arange(9).reshape((3, 3))  # make correct puzzle to compare to
        heuristic = 0
        for i in range(1, 9):
            # Get index of tile with number i for both puzzles
            indexPuzzle, indexGoal = tuple(np.argwhere(puzzle == i)[0]), tuple(np.argwhere(goalPuzzle == i)[0])

            steps = abs(indexGoal[0] - indexPuzzle[0]) + abs(indexGoal[1] - indexPuzzle[1])  # calculate needed steps
            heuristic += steps  # add all steps together
            # print(i, ':', indexPuzzle, '->', indexGoal, '=', steps, '|', heuristic)  # just for now
        return heuristic

    def hamming_heuristic(self):
        """ Define a function that returns the number of incorrect placed digits within the delivered
        array - puzzle - compared to the ideal array - goal_puzzle -

        :param  puzzle: 2D Array
        :return: heuristic """
        puzzle = copy.deepcopy(self.puzzle_array).reshape(9)
        goal_puzzle = np.arange(9)  # Create the ideally ordered puzzle
        heuristic = 0  # Heuristic-Counter

        # Here the goal_puzzle is compared to the passed puzzle and whenever there is a different number
        # in the compared cells, the heuristic is increased by 1
        for i in range(1, 9):
            if goal_puzzle[i] != puzzle[i]:
                heuristic += 1

        return heuristic

def init_puzzle():
    """ Define a function to initialize the puzzle

    :return: 2D Array with random puzzle """
    puzzle = np.arange(9)  # Create a array to represent the puzzle
    np.random.shuffle(puzzle)  # Shuffle the puzzle to create a random starting configuration

    while not puzzle_solvable(puzzle):  # check if the puzzle is solvable
        puzzle = init_puzzle()  # recursive call of init_puzzle to make new puzzle and check if new is solvable

    # Shape the array into a 2D array AFTER it was shuffled to assure rows and cols get mixed
    return puzzle.reshape((3, 3))


def puzzle_solvable(puzzle):
    """ Define a function to find out if the puzzle is solvable

    :param puzzle: 2D Array
    :return: boolean """
    inverseCount = 0
    puzzle = puzzle.reshape(9)  # reshape the 2D Array into a 1D Array
    for i in range(9):
        for j in range(i + 1, 9):  # compare i with number to the right of i
            if puzzle[i] > puzzle[j] and (puzzle[j] != 0 and puzzle[i] != 0):
                inverseCount += 1  # if the 1st number is bigger than the 2nd number, increase counter
    return bool((inverseCount % 2) == 0)  # if the counter is a even the puzzle is solvable

# To test the functions
# if __name__ == '__main__':