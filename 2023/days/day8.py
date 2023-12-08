from days.day import Day
from time import sleep

class Day8(Day):

    day = 8
    reuse_a_input_for_b = True

    def solve_a(self):
        turns = self.input_lines[0]
        branch_lines = self.input_lines[2:]
        branches = [(bl[0:3], bl[7:10], bl[12:15]) for bl in branch_lines]
        nodes = {node: (left, right) for node, left, right in branches}
        current = 'AAA'
        turn_count = 0
        while current != 'ZZZ':
            turn = turns[turn_count % len(turns)]
            current = nodes[current][turn == 'R'] # == 'L' -> True -> 1 -> right child
            turn_count += 1
        print(turn_count)

    def solve_b(self):
        turns = self.input_lines[0]
        branch_lines = self.input_lines[2:]
        branches = [(bl[0:3], bl[7:10], bl[12:15]) for bl in branch_lines]
        nodes = {node: (left, right) for node, left, right in branches}

        turns = tuple([int(turn == 'R') for turn in turns])

        current_nodes = [k for k in nodes.keys() if k[2] == 'A']
        turn_count = 0
        while any((node[2] != 'Z' for node in current_nodes)):
            if (turn_count % 1e8 == 0):
                print(f"{turn_count:,} : {current_nodes}")
            turn = turns[turn_count % len(turns)]
            current_nodes = [nodes[current][turn] for current in current_nodes]
            turn_count += 1
        print(current_nodes)
        print(turn_count)


    def solve_b_2(self):
        turns = self.input_lines[0]
        branch_lines = self.input_lines[2:]
        branches = [(bl[0:3], bl[7:10], bl[12:15]) for bl in branch_lines]
        nodes = {node: (left, right) for node, left, right in branches}

        turns = tuple([int(turn == 'R') for turn in turns])

        starting_nodes = [k for k in nodes.keys() if k[2] == 'A']
        for starting_node in starting_nodes:
            print("\n === \n")
            visited = set()
            print("starting node:", starting_node)
            current = starting_node
            turn = turns[0]
            current = nodes[current][turn]
            turn_count = 1
            while not current in visited:
            # for _ in range(200):
                visited.add(current)
                turn = turns[turn_count % len(turns)]
                current = nodes[current][turn]
                turn_count += 1
                # if current[2] == 'Z':
                #     print(f"found a Z on turn {turn_count}: {current}")
                # visited.add(current)
                # print("turn", turn_count, "hit", current)
            print(f"found a loop after {turn_count} turns with node {current}")
