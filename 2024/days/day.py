import os

class Day():

    day = 0
    reuse_a_input_for_b = False

    def __init__(self, ab, test, test_case):
        self.ab = ab
        self.test = test
        self.test_case = test_case
        self.input_lines = self._read_input()
        self.input_blob = '\n'.join(self.input_lines)
        self.setup()

    def _read_input(self):
        ab = 'a' if self.reuse_a_input_for_b else self.ab
        path = f"{'test_' if self.test else ''}inputs/{self.test_case or (str(self.day) + ab)}.txt"
        if (not os.path.exists(path)):
            print(f"No file found at {path}")
            exit(1)
        try:
            with open(path, 'r') as input_file:
                # return input_file.readlines()
                return [line.strip() for line in input_file.readlines()]
        except FileNotFoundError as e:
            print(e)

    def setup(self):
        pass

    @property
    def height(self):
        return len(self.input_lines)

    @property
    def width(self):
        return len(self.input_lines[0])

    def solve(self):
        getattr(self, f"solve_{self.ab}")()

    def solve_a(self):
        print(f"You haven't implemented {self.day}{self.ab} yet")

    def solve_b(self):
        print(f"You haven't implemented {self.day}{self.ab} yet")
