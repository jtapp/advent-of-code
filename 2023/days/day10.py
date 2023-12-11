from days.day import Day
from time import sleep

next_dir = {
    ('north', '|'): 'south',
    ('south', '|'): 'north',
    ('east', '-'): 'west',
    ('west', '-'): 'east',
    ('north', 'L'): 'east',
    ('east', 'L'): 'north',
    ('north', 'J'): 'west',
    ('west', 'J'): 'north',
    ('south', '7'): 'west',
    ('west', '7'): 'south',
    ('south', 'F'): 'east',
    ('east', 'F'): 'south',
}

flip_dir = {
    'north': 'south',
    'south': 'north',
    'east' : 'west',
    'west': 'east',
}

class Day10(Day):

    day = 10
    reuse_a_input_for_b = True

    def find_start(self):
        for i in range(self.width):
            for j in range(self.height):
                if self.input_lines[j][i] =='S':
                     return i, j

    def solve_a(self):
        mapp = self.input_lines
        x, y = self.find_start()
        leaving_dir = 'west' # manual inspection
        next = 'L' # manual inspection
        step_count = 0
        while next != 'S' and step_count < 1e6:
            entering_dir = flip_dir[leaving_dir]
            leaving_dir = next_dir[(entering_dir, next)]
            # print(next, x, y, entering_dir, leaving_dir)
            # sleep(1)
            if leaving_dir == 'north':
                y -= 1
            elif leaving_dir == 'south':
                y += 1
            elif leaving_dir == 'east':
                x += 1
            else:
                assert leaving_dir == 'west'
                x -= 1
            next = mapp[y][x]
            step_count += 1
        print(step_count / 2)

    def solve_b(self):
        mapp = self.input_lines
        x, y = self.find_start()
        S_x, S_y = x, y
        leaving_dir = 'west' # manual inspection
        next = 'L' # manual inspection
        step_count = 0
        loop_spots = []
        while next != 'S' and step_count < 1e6:
            loop_spots.append((x, y))
            entering_dir = flip_dir[leaving_dir]
            leaving_dir = next_dir[(entering_dir, next)]
            # print(next, x, y, entering_dir, leaving_dir)
            # sleep(1)
            if leaving_dir == 'north':
                y -= 1
            elif leaving_dir == 'south':
                y += 1
            elif leaving_dir == 'east':
                x += 1
            else:
                assert leaving_dir == 'west'
                x -= 1
            next = mapp[y][x]
            step_count += 1

        loop_spots = set(loop_spots)
        clean_map = []
        for y in range(self.height):
            clean_map.append([])
            for x in range(self.width):
                clean_map[y].append(mapp[y][x] if (x, y) in loop_spots else None)
        printable_clean_map = '\n'.join([''.join([spot if spot else ' ' for spot in row]) for row in clean_map])
        print(printable_clean_map)
        print()

        clean_map[S_y][S_x] = 'L' # manual inspection
        inside_count = 0
        for y, row in enumerate(clean_map):
            inside = False
            entered_horizontal_from_above = False
            entered_horizontal_from_below = False
            for x, spot in enumerate(row):
                if spot == None:
                    inside_count += inside
                elif spot == '|':
                    inside = not inside
                elif spot == 'F':
                    entered_horizontal_from_below = True
                elif spot == 'L':
                    entered_horizontal_from_above = True
                elif entered_horizontal_from_below:
                    if spot == 'J':
                        inside = not inside
                        entered_horizontal_from_below = False
                    elif spot == '7':
                        entered_horizontal_from_below = False
                    else:
                        assert spot == '-'
                elif entered_horizontal_from_above:
                    if spot == '7':
                        inside = not inside
                        entered_horizontal_from_above = False
                    elif spot == 'J':
                        entered_horizontal_from_above = False
                    else:
                        assert spot == '-'
                else:
                    print("that's weird", x, y, spot, inside, entered_horizontal_from_above, entered_horizontal_from_below)
                    assert False
            # print(y, row)
            assert not inside # we should finish each row outside again
            assert not entered_horizontal_from_above # we should finish each row outside of a pipe
            assert not entered_horizontal_from_below # we should finish each row outside of a pipe
        print('answer:', inside_count)
                



# verticals = {
#     'F': 'J',
#     'L': '7',
# }

# not_verticals = {
#     'F': '7',
#     'L': 'J',
# }
