from days.day import Day
from time import sleep
from pprint import pprint
import numpy as np

class Dir:
    N = np.array([0, 1])
    S = np.array([0, -1])
    W = np.array([-1, 0])
    E = np.array([1, 0])
    NE = N + E
    NW = N + W
    SE = S + E
    SW = S + W

    @classmethod
    def all(cls):
        return [cls.N, cls.S, cls.W, cls.E, cls.NE, cls.NW, cls.SE, cls.SW]

def turn_right(dir):
    dir = dir.tolist()
    if dir == Dir.N.tolist():
        return Dir.E
    elif dir == Dir.E.tolist():
        return Dir.S
    elif dir == Dir.S.tolist():
        return Dir.W
    elif dir == Dir.W.tolist():
        return Dir.N
    else:
        raise Exception('bad direction')

"""
height is height (vertical dimension)
width is width (horizontal dimension)
x is horizontal coordinate
y is vertical coordinate
moving left/right is x +/-
moving up/down is y +/-
indexing in the array is [x, y]

to make this work, the original array is sort of reflected
"""
class Crawler:

    def __init__(self, map_lines):
        self.original_map = np.array(list(zip(*map_lines[::-1])))
        self.map = self.original_map
        self.height = len(map_lines)
        self.width = len(map_lines[0])

    def start_at(self, x, y):
        self.covered = np.zeros_like(self.original_map, dtype=bool)
        self.step_count = 0
        self.direction = Dir.N
        self.pos = np.array([x, y])

    def reset_and_place_box(self, x, y):
        self.map = self.original_map.copy()
        self.map[x, y] = '#'
    
    def turn_right(self):
        self.direction = turn_right(self.direction)
    
    # returns true if you get stuck in a loop
    def walk(self):
        while self.step_count < self.height * self.width:
            x, y = self.pos
            if x < 0 or x >= self.width or y < 0 or y >= self.height:
                return False
            elif self.map[x, y] == '#':
                self.pos -= self.direction
                self.turn_right()
            else:
                self.covered[x, y] = True
            self.pos += self.direction
            self.step_count += 1
        return True

class Day6(Day):

    day = 6
    reuse_a_input_for_b = True

    def setup(self):
        self.crawler = Crawler(self.input_lines)
        self.starting_y = 0
        for i, line in enumerate(self.input_lines[::-1]):
            if '^' in line:
                self.starting_y = i
                self.starting_x = line.index('^')
                break

    def solve_a(self):
        self.crawler.start_at(self.starting_x, self.starting_y)
        self.crawler.walk()
        print(self.crawler.covered.sum())

    def solve_b(self):
        count = 0
        self.crawler.start_at(self.starting_x, self.starting_y)
        self.crawler.walk()
        covered = self.crawler.covered.copy()
        for x in range(self.crawler.width):
            for y in range(self.crawler.height):
                if covered[x, y]:
                    self.crawler.reset_and_place_box(x, y)
                    self.crawler.start_at(self.starting_x, self.starting_y)
                    count += self.crawler.walk()
        print(count)