from days.day import Day
from time import sleep
from pprint import pprint

class Day1(Day):

    day = 1
    reuse_a_input_for_b = True

    def setup(self):
        lines = [line.split() for line in self.input_lines]
        (ones, twos) = zip(*lines)
        self.ones = [int(n) for n in sorted(ones)]
        self.twos = [int(n) for n in sorted(twos)]

    def solve_a(self):
        total = 0
        for (a, b) in zip(self.ones, self.twos):
            total += abs(b - a)
        print(total)

    def solve_b(self):
        counts = {}
        for n in self.twos:
            counts[n] = counts.get(n, 0) + 1
        total = 0
        for n in self.ones:
            total += n * counts.get(n, 0)
        print(total)
