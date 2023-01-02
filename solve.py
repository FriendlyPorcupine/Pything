# import necessary classes
from typing import Any

import numpy as np
from queue import PriorityQueue
from dataclasses import dataclass

directions = ['up', 'down', 'left', 'right']  # array with the four possible directions


def random_solve(unsolvedPuzzle):
    countMoves = 0  # variable to count how many moves where necessary to solve the puzzle

    while puzzle.puzzle_unordered(unsolvedPuzzle):  # Loop until the puzzle is solved
        direction = np.random.choice(directions)  # Choose random direction to move the empty tile
        if puzzle.move_tile(unsolvedPuzzle, direction):  # if move is True count, increment countMoves
            countMoves += 1
        if countMoves >= 100:  # stop the while loop if the puzzle is not solved after 200 valid moves
            countMoves = 0
            return countMoves
    return countMoves


class Node:
    puzzle_state: Any
    steps: int

    def __init__(self, puzzle_state, steps):
        self.puzzle_state = puzzle_state
        self.steps = steps

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False

        return self.puzzle_state == other.puzzle_state

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.puzzle_state)


def a_star_solve(unsolved_puzzle, h):
    open_list = PriorityQueue()
    closed_list = set()

    open_list.put((0, Node(unsolved_puzzle, 0)))

    while not open_list.empty():
        current_node = open_list.get()

        if not p.puzzle_unordered(current_node.puzzle_state):
            return 0

        closed_list.add(current_node)
        expand(open_list, closed_list, h, current_node)

    raise Exception("no solution found")


def expand(open_list, closed_list, h, current_node):
    moves = p.moves_possible(current_node.puzzle_state)

    for successor_move in moves:
        new_puzzle_state = current_node.puzzle_state.copy()
        p.move_tile(new_puzzle_state, successor_move)
        successor_node = Node(new_puzzle_state, current_node.steps + 1)

        if successor_node in closed_list:
            continue

        tentative_g = current_node.steps + 1

        if open_list.get() and (tentative_g >= successor_node.steps):
            continue

        open_list.put((tentative_g + h(successor_node.puzzle_state), successor_node))


# To test the functions
if __name__ == '__main__':
    puzzle = p.init_puzzle()  # init_puzzle function must not shuffle
    p.move_tile(puzzle, 'down')  # Make puzzle with just one wrong tile

    # movesToSolve = random_solve(puzzle)
    movesToSolve = a_star_solve(puzzle, p.hamming_heuristic)

    print(movesToSolve, 'moves were necessary to solve the puzzle')
    p.print_puzzle(puzzle)


