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
        self.map = np.array(list(zip(*map_lines[::-1])))
        self.height = len(map_lines)
        self.width = len(map_lines[0])
        self.verbose = False

    def look_everywhere(self, pattern, allowed_directions, callback):
        for x in range(self.width):
            for y in range(self.height):
                self.goto(x, y)
                self.look_for(pattern, allowed_directions, callback)

    def goto(self, x, y):
        self.pos = np.array([x, y])
    
    def look_for(self, pattern, allowed_directions, callback):
        starting_pos = self.pos
        for direction in allowed_directions:
            self.goto(*starting_pos)
            self.look_for_in_direction(pattern, direction, callback)
    
    def look_for_in_direction(self, pattern, direction, callback):
        # print(f'looking for {pattern} at {self.pos.tolist()} in direction {direction.tolist()}')
        if len(pattern) == 0:
            callback(self.pos, direction) # found the pattern!
            return
        x, y = self.pos
        if x < 0 or x >= self.width or y < 0 or y >= self.height or (self.map[x, y] != pattern[0]):
            return
        self.pos += direction
        self.look_for_in_direction(pattern[1:], direction, callback)


class Day4(Day):

    day = 4
    reuse_a_input_for_b = True

    def setup(self):
        pass

    def solve_a(self):
        count = 0
        def callback(*args):
            nonlocal count
            count += 1
        crawler = Crawler(self.input_lines)
        crawler.look_everywhere('XMAS', Dir.all(), callback)
        print(count)

    def solve_b(self):
        centers = []
        def callback(pos, direction):
            nonlocal centers
            center = pos + (-2 * direction)
            centers += [center.tolist()]
        crawler = Crawler(self.input_lines)
        crawler.look_everywhere('MAS', [Dir.NE, Dir.SW], callback)
        # pprint(centers)

        allowed_crossing_dirs = [Dir.SE, Dir.NW]
        count = 0
        def count_callback(*args):
            nonlocal count
            count += 1
        for center in centers:
            crawler.goto(*(Dir.NW + center))
            crawler.look_for_in_direction('MAS', Dir.SE, count_callback)
            crawler.goto(*(Dir.SE + center))
            crawler.look_for_in_direction('MAS', Dir.NW, count_callback)
        print(count)
