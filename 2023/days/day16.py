from days.day import Day
from time import sleep
from pprint import pprint

REFLECTIONS = {
    ('R', '-'): ('R',),
    ('L', '-'): ('L',),
    ('U', '-'): ('L', 'R'),
    ('D', '-'): ('L', 'R'),
    ('U', '|'): ('U',),
    ('D', '|'): ('D',),
    ('R', '|'): ('U', 'D'),
    ('L', '|'): ('U', 'D'),

    ('R', '/'): ('U',),
    ('L', '/'): ('D',),
    ('U', '/'): ('R',),
    ('D', '/'): ('L',),
    ('R', '\\'): ('D',),
    ('L', '\\'): ('U',),
    ('U', '\\'): ('L',),
    ('D', '\\'): ('R',),
}

class Day16(Day):

    day = 16
    reuse_a_input_for_b = True

    def count_energized(self, initial_beam):
        grid = self.input_lines
        beams = [initial_beam]
        max_beams = 0
        energized = {} # (0, 0): {'R'}
        while beams:
            # pprint(beams)
            # pprint(energized)
            max_beams = max(max_beams, len(beams))
            x, y, dir = beam = beams.pop()
            if dir in energized.get((x, y), []):
                # print('hit a loop: ', beam)
                continue
            energized[(x, y)] = energized.get((x, y), []) + [dir]
            if dir == 'R':
                x += 1
            elif dir == 'L':
                x -= 1
            elif dir == 'U':
                y -= 1
            elif dir == 'D':
                y += 1
            else:
                assert False

            if x < 0 or x >= self.width or y < 0 or y >= self.height:
                continue

            tile = grid[y][x]
            if tile == '.':
                beams.append((x, y, dir))
            else:
                new_dirs = REFLECTIONS[(dir, tile)]
                beams += [(x, y, new_dir) for new_dir in new_dirs]
            # print()
        # print('max length of beams', max_beams)
        # del energized[(-1, 0)]
        return len(energized) - 1

    def solve_a(self):
        print(self.count_energized((-1, 0, 'R')))

    def solve_b(self):
        beams_to_test = \
            [(-1, j, 'R') for j in range(self.height)] + \
            [(self.width, j, 'L') for j in range(self.height)] + \
            [(i, -1, 'D') for i in range(self.width)] + \
            [(i, self.height, 'U') for i in range(self.width)]
        print(max((self.count_energized(initial_beam) for initial_beam in beams_to_test)))