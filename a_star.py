import queue as q
import puzzle_class
import time


# node class for all the different states of the 8-Puzzle
class Node:
    # constructor
    def __init__(self, puzzle, parent=None, action=None):
        # the state of the puzzle
        self.puzzle = puzzle
        # the parent of the node (how the puzzle looked like before the last move was made)
        self.parent = parent
        # the last move that was made to archive this state
        self.action = action

        # heuristic
        self.h = 0
        # cost
        self.g = 0
        # heuristic + cost
        self.f = 0

    # to make it possible to compare the f values in the priority queue
    def __lt__(self, other):
        return self.f < other.f


# a star algorithm that takes the parameters "m" and "h" for the two different heuristics - m = Manhattan, h = Hamming
def a_star_alg(heuristic):
    # initializing a random puzzle
    puzzle = puzzle_class.Puzzle(puzzle_class.init_puzzle())
    # creating the first node with the randomly created puzzle
    start_node = Node(puzzle)
    # creating a priority queue where all the children nodes will be added to
    open_list = q.PriorityQueue()
    # a list where all the expanded nodes will be added
    closed_list = set()
    # the possible directions the empty tile can move to
    directions = ['up', 'down', 'left', 'right']
    # the start node is added to the priority queue, with the priority f
    open_list.put((start_node.f, start_node))

    # while the priority queue is not empty
    while not open_list.empty():
        # the element with the highest priority is saved in current_node
        current_node = open_list.get()[1]
        # since the current not will be expanded, it is added to the closed list
        closed_list.add(current_node)

        # when a node is reached that is in the solved state a new list is created where all the parent nodes of the
        # node is saved until the start node is reached in reverse order
        if not current_node.puzzle.puzzle_unordered():
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = current_node.parent

            # for move in path[::-1]:
            # print(move.puzzle.print_puzzle())
            return len(closed_list)

        # in this part the children nodes of the current_node are created
        children = []
        # makes sure that the move that led to the current node is not reversed
        for direction in directions:
            if direction == "up" and current_node.action == "down":
                continue
            elif direction == "down" and current_node.action == "up":
                continue
            elif direction == "right" and current_node.action == "left":
                continue
            elif direction == "left" and current_node.action == "right":
                continue
            # if the move is possible, a new child node is created and added to the children list
            if direction in current_node.puzzle.moves_possible():
                new_node = Node(current_node.puzzle.move_tile(direction), current_node, direction)
                children.append(new_node)

        for child in children:
            # g, h and f values for the created node values are set
            # depending on what parameter was used, either Manhattan or Hamming was used as the heuristic
            child.g = current_node.g + 1
            if heuristic == "m":
                child.h = child.puzzle.manhattan_heuristic()
            elif heuristic == "h":
                child.h = child.puzzle.hamming_heuristic()
            child.f = child.g + child.h

            # the children nodes that were created are added into the priority queue with the f value as their priority
            open_list.put((child.f, child))


def expanded_nodes_time(heuristic):
    # dictionary is created where expanded nodes and run time is saved
    nodes_expanded_time = {}
    # loop that goes through 100 iterations with different 8-Puzzles that are solved, run time and expanded nodes are
    # saved in nodes_expanded_time dictionary
    for count in range(100):
        start_time = time.time()
        steps = a_star_alg(heuristic)
        end_time = time.time()

        runTime = round(end_time - start_time, 2)
        nodes_expanded_time.update({count: (steps, runTime)})
        # print(count, ':', steps, runTime)
    return nodes_expanded_time
