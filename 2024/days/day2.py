from days.day import Day
from time import sleep
from pprint import pprint

class Day2(Day):

    day = 2
    reuse_a_input_for_b = True

    def setup(self):
        self.levels = [
            [int(level) for level in line.split()]
            for line in self.input_lines
        ]

    def solve_a(self):
        def correct(levels):
            correct = True
            direction = 1 if levels[1] > levels[0] else -1
            for i in range(len(levels) - 1):
                a = levels[i]
                b = levels[i+1]
                correct = correct and 1 <= (b - a) * direction <= 3
            return correct
        correct_count = sum((correct(levels) for levels in self.levels))
        print(correct_count)
            
    def solve_b(self):
        def correct(levels):
            return correct_impl(levels, 1) or correct_impl(levels, -1)
        def correct_impl(levels, direction, without=None):
            if without is not None:
                levels = levels[:without] + levels[without+1:]
            for i in range(len(levels) - 1):
                a = levels[i]
                b = levels[i+1]
                this_step_correct = 1 <= (b - a) * direction <= 3
                if not this_step_correct:
                    return (without is None) and \
                        (correct_impl(levels, direction, i) or correct_impl(levels, direction, i+1))
            return True
        pprint([(levels, correct(levels)) for levels in self.levels])
        correct_count = sum((correct(levels) for levels in self.levels))
        print(correct_count)