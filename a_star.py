import puzzle_class
import copy


# node class for all the different states of the 8-Puzzle
class Node:
    # constructor
    def __init__(self, puzzle, parent=None, action=None):
        self.puzzle = puzzle
        self.parent = parent
        self.action = action

        self.h = 0  # Heuristic
        self.f = 0  # Heuristic + Gewichtung
        self.g = 0  # Gewichtung

# 0 = Manhatten
# 1 = Hamming
def astar_alg(heuristic):
    puzzle = puzzle_class.Puzzle(puzzle_class.init_puzzle())
    start_node = Node(puzzle)
    # start_node.puzzle.print_puzzle()
    open_list = []
    closed_list = []
    directions = ['up', 'down', 'left', 'right']

    open_list.append(start_node)

    while len(open_list) > 0:
        current_node = open_list[0]
        current_index = 0
        for count, node in enumerate(open_list):
            if node.f < current_node.f:
                current_node = node
                current_index = count
        # current_node.puzzle.print_puzzle()
        #print(current_node.h)
        closed_list.append(open_list.pop(current_index))

        if not current_node.puzzle.puzzle_unordered():
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = current_node.parent

            for move in path[::-1]:
                print(move.puzzle.print_puzzle())
            return len(closed_list)

        children = []
        for direction in directions:
            if direction == "up" and current_node.action == "down":
                continue
            elif direction == "down" and current_node.action == "up":
                continue
            elif direction == "right" and current_node.action == "left":
                continue
            elif direction == "left" and current_node.action == "right":
                continue

            if direction in current_node.puzzle.moves_possible():
                new_node = Node(current_node.puzzle.move_tile(direction), current_node, direction)
                children.append(new_node)

        for child in children:
            for child_in_closed_list in closed_list:
                if child.puzzle == child_in_closed_list.puzzle:
                    continue

            child.g = current_node.g + 1
            if heuristic == 0:
                child.h = child.puzzle.manhattan_heuristic()
            elif heuristic == 1:
                child.h = child.puzzle.hamming_heuristic()
            child.f = child.g + child.h

            for node in open_list:
                if child.puzzle == node.puzzle and child.g > node.g:
                    continue

            open_list.append(child)

def average_expanded_nodes():
    nodes_expanded = []
    for count in range(20):
        nodes_expanded.append(astar_alg(0))
        print("done")
        print(count)

    average = sum(nodes_expanded) / len(nodes_expanded)
    print(round(average, 2))
