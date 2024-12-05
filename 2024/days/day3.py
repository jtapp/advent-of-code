from days.day import Day
from time import sleep
from pprint import pprint
import re

class Day3(Day):

    day = 3
    reuse_a_input_for_b = True

    def setup(self):
        pass

    def solve_a(self):
        pattern = r'mul\((?P<a>\d{1,3}),(?P<b>\d{1,3})\)'
        total = 0
        for line in self.input_lines:
            matches = re.finditer(pattern, line)
            for match in matches:
                a = int(match.group('a'))
                b = int(match.group('b'))
                total += a * b
        print(total)

    def solve_b(self):
        pattern = re.compile(r'(mul\((?P<a>\d{1,3}),(?P<b>\d{1,3})\))|do\(\)|don\'t\(\)')
        total = 0
        # self.input_lines = ["xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"]
        enabled = True
        for line in self.input_lines:
            matches = pattern.finditer(line)
            for match in matches:
                whole = match.group(0)
                if whole == "do()":
                    enabled = True
                elif whole == "don't()":
                    enabled = False
                elif enabled:
                    a = int(match.group('a'))
                    b = int(match.group('b'))
                    total += a * b
        print(total)