from days.day import Day
from time import sleep

class Board:

    def __init__(self, rows):
        self.rows = [[None if c == '.' else c == '#' for c in row] for row in rows]
        self.width = len(rows[0])
        self.height = len(rows)
        self.cols = [[row[i] for row in self.rows] for i in range(self.width)]

    # tilts the board "north"
    def tilt(self):
        runs = []
        for i, col in enumerate(self.cols):
            run_start = 0
            run_len = 0
            for j, c in enumerate(col):
                if c is None:
                    pass
                elif c: # is rock
                    if run_len > 0:
                        runs.append((i, run_start, run_len))
                    run_start = j + 1 # run starts on the next row
                    run_len = 0
                else:
                    run_len += 1
            if run_len > 0:
                runs.append((i, run_start, run_len))
        self.runs = runs

    # rotates the board 90 degrees so that west becomes north
    # uses self.runs as input and writes to self.rows
    def rotate_current_runs(self):
        # empty the rocks
        for i in range(self.width):
            for j in range(self.height):
                self.cols[i][j] = self.cols[i][j] or None
        # add the rocks back in
        for col, run_start, run_len in self.runs:
            for j in range(run_start, run_start + run_len):
                self.cols[col][j] = False
        self.rows = [tuple(reversed(col)) for col in self.cols]
        self.cols = [[row[i] for row in self.rows] for i in range(self.width)]
        w, h = self.width, self.height
        self.width, self.height = h, w

    def cycle(self):
        for _ in range(4):
            self.tilt()
            self.rotate_current_runs()

    def __str__(self):
        return '\n'.join((''.join(('.' if c is None else '#' if c else 'O' for c in row)) for row in self.rows))

    def __eq__(self, other):
        return self.rows == other.rows
    
    def north_load(self):
        total = 0
        # for _, run_start, run_len in self.runs:
        #     for j in range(run_start, run_start + run_len):
        #         total += self.height - j
        for j, row in enumerate(self.rows):
            for c in row:
                if c == False:
                    total += self.height - j
        return total


class Day14(Day):

    day = 14
    reuse_a_input_for_b = True

    def solve_a(self):
        board = Board(self.input_lines)
        board.tilt()
        total = 0
        for _, run_start, run_len in board.runs:
            for j in range(run_start, run_start + run_len):
                total += self.height - j
        print(total)


    def solve_b(self):
        target_cycles = 1000000000
        board = Board(self.input_lines)
        seen = {}
        for i in range(10000):
            if i % 1000 == 0:
                # print(f" == {i} == ")
                # print(board)
                # print()
                print("i = ", i)
            board.cycle()
            new_board = str(board)
            if new_board in seen:
                print(f"repeat seen on i = {i}")
                print(f"it matched a board from i = {seen[new_board]}")
                first_seen = seen[new_board]
                cycle_length = i - first_seen
                break
            seen[new_board] = i
        equivalent_cycles = first_seen + ((target_cycles - first_seen) % cycle_length)
        print(f"equivalent cycles = ", equivalent_cycles)
        
        board = Board(self.input_lines)
        for i in range(equivalent_cycles):
            board.cycle()
        print(board.north_load())
        
