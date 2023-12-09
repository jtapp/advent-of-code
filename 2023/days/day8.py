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
        self.turns = tuple((int(turn == 'R') for turn in turns))
        self.turns_len = len(self.turns)
        
        branch_lines = self.input_lines[2:]
        branches = [(bl[0:3], bl[7:10], bl[12:15]) for bl in branch_lines]
        self.nodes = {node: (left, right) for node, left, right in branches}

        starting_nodes = [k for k in self.nodes.keys() if k[2] == 'A']
        print("starting nodes", starting_nodes)
        checks = []
        cycle_lengths = []
        for starting_node in starting_nodes:
            interesting_nodes = self.find_loops(starting_node)
            print(interesting_nodes)
            cycle_start_i = interesting_nodes[-1][0]
            cycle_end_i = interesting_nodes[-2][0]
            z_i = interesting_nodes[-3][0]
            cycle_length = cycle_end_i - cycle_start_i
            print(z_i, cycle_length)
            checks.append((z_i, cycle_length))
            """
                they were clever and they made the first occurance of the Z node exactly
                one cycle length into the sequence. This means the depth of Z is exactly 
                N cycles + 1 times the cycle length. Which means Z recurs at the cycle length
                of each sequence, so we can just take the actual least common factor, we
                don't need to do anything weird for the sake of adding in the nodes that
                come before the cycle
            """
            assert z_i == cycle_length
            cycle_lengths.append(cycle_length)
        
        print('cycle lengths', cycle_lengths)
        print('cycle lengths', ' '.join(str(cl) for cl in cycle_lengths))

        checks = tuple(checks)
        print(checks)
        # LCM calculator online says 12315788159977. Let's check it:
        for x in [12315788159977]: #range(1, 10**11):
            # almost_works = any(((x - z_i) % cycle_length) == 0 for z_i, cycle_length in checks)
            # if (almost_works):
            #     print(x, [((x - z_i) % cycle_length) == 0 for z_i, cycle_length in checks])
            if all(((x - z_i) % cycle_length) == 0 for z_i, cycle_length in checks):
                print('this one works:', x)
                break
        print('done', x)


        # ok, as I eventually suspected, these are looping, and we are essentially counting our
        # up to the least common multiple. Instead, let's find the loop length, and then
        # find the least common multiple directly

        # so it looks like our interesting nodes are just the first time we get the cycle node zero,
        # then a Z node, then the second time we come across the cycle node zero



    def find_loops(self, starting_node):
        visited = {}
        interesting = []
        current = starting_node
        turn_count = 0
        turn_index = 0
        while current not in visited or turn_index not in visited[current][0]:
            # print(current, visited, turn_count, turn_index)
            # sleep(1)
            if current[-1] == 'Z' or current[-1] == 'A':
                interesting.append((turn_count, current))
            if current not in visited:
                visited[current] = ({turn_index}, turn_count) # record the first time we see it
            else:
                visited[current][0].add(turn_index)
            turn = self.turns[turn_index]
            current = self.nodes[current][turn]
            turn_count += 1
            turn_index = turn_count % self.turns_len
        interesting.append((turn_count, current))
        interesting.append((visited[current][1], current))
        return interesting
            


    # def solve_b_1(self):
    #     current_nodes = [k for k in self.nodes.keys() if k[2] == 'A']
    #     turn_count = 0
    #     while any((node[2] != 'Z' for node in current_nodes)):
    #         if (turn_count % 1e8 == 0):
    #             print(f"{turn_count:,} : {current_nodes}")
    #         turn = self.turns[turn_count % len(self.turns)]
    #         current_nodes = [self.nodes[current][turn] for current in current_nodes]
    #         turn_count += 1
    #     print(current_nodes)
    #     print(turn_count)
    #     # got to
    #     # 21,900,000,000 : ['MMR', 'HCG', 'CTN', 'GVC', 'HTK', 'LSX']
    #     # 22,000,000,000 : ['FSP', 'XPQ', 'HQV', 'PVT', 'MLL', 'NBL']


    # def solve_b_2(self):
    #     starting_nodes = [k for k in self.nodes.keys() if k[2] == 'A']
    #     for starting_node in starting_nodes:
    #         print("\n === \n")
    #         visited = set()
    #         print("starting node:", starting_node)
    #         current = starting_node
    #         turn = self.turns[0]
    #         current = self.nodes[current][turn]
    #         turn_count = 1
    #         while not current in visited:
    #         # for _ in range(200):
    #             visited.add(current)
    #             turn = self.turns[turn_count % len(self.turns)]
    #             current = self.nodes[current][turn]
    #             turn_count += 1
    #             # if current[2] == 'Z':
    #             #     print(f"found a Z on turn {turn_count}: {current}")
    #             # visited.add(current)
    #             # print("turn", turn_count, "hit", current)
    #         print(f"found a loop after {turn_count} turns with node {current}")
