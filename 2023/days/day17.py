from days.day import Day
from time import sleep
from pprint import pprint
from random import random

SIZE = 13

class Step:

    def from_len_dir(cls, length, direction):
        pass

    def __init__(self, dx, dy):
        self.dx = dx
        self.dy = dy
    
    # True is Right, False is Left, None is Straight
    def next(self, turn):
        if turn is None:
            return self
        elif turn: # right
            return Step(-self.dy, self.dx)
        else: # left
            return Step(self.dy, -self.dx)


    def __add__(self, other):
        return Step(self.dx + other.dx, self.dy + other.dy)
    
class Pos:

    def __init__(self, x, y):
        self.x, self.y = x, y

    def step(self, step):
        self.x += step.dx
        self.y += step.dy

    def check_and_step(self, step):
        if not (0 <= self.x + step.dx < SIZE) or not (0 <= self.y + step.dy < SIZE):
            return False
        self.step(step)
        return True

def random_turn(preferred):
    r = random()
    if r < 0.67:
        return preferred
    return not preferred

class Day17(Day):

    day = 17
    reuse_a_input_for_b = True

    # True is Right, False is Left, None is Straight
    def random_path(start_x, start_y, end_x, end_y, first_step):
        pos = Pos(start_x, start_y)
        straight_count = 0
        path = [first_step]
        while x != end_x and y != end_y:
            if random() < straight_count * 0.34:
                path.append(None)
            else:
                path.append(random() < 0.5)
        

    # def solve_a(self):

    # def solve_b(self):