from days.day import Day

class Day11(Day):

    day = 11
    reuse_a_input_for_b = True

    def solve_a(self):
        star_map = self.input_lines
        empty_rows = [j for j in range(self.height) if star_map[j] == ('.' * self.width)]
        empty_columns = [i for i in range(self.width) if all((row[i] == '.' for row in star_map))]
        for i in reversed(empty_columns):
            star_map = [row[:i] + '.' + row[i:] for row in star_map]
        width = len(star_map[0])
        for i in reversed(empty_rows):
            star_map.insert(i, '.' * width)
        height = len(star_map)
        # print('\n'.join(star_map))
        stars = [(x, y) for x in range(width) for y in range(height) if star_map[y][x] == '#']
        # print(stars)
        total_distance = 0
        for a, (x_a, y_a) in enumerate(stars):
            for (x_b, y_b) in stars[a+1:]:
                total_distance += abs(x_b - x_a) + abs(y_b - y_a)
        print(total_distance)

    def solve_b(self):
        expansion_factor = 1000000
        # expansion_factor = 100
        star_map = self.input_lines
        empty_rows = [j for j in range(self.height) if star_map[j] == ('.' * self.width)]
        empty_columns = [i for i in range(self.width) if all((row[i] == '.' for row in star_map))]
        def x_distance(x_a, x_b):
            x1 = min(x_a, x_b)
            x2 = max(x_a, x_b)
            distance = 0
            for x in range(x1, x2):
                if x in empty_columns:
                    distance += expansion_factor
                else:
                    distance += 1
            return distance
        def y_distance(y_a, y_b):
            y1 = min(y_a, y_b)
            y2 = max(y_a, y_b)
            distance = 0
            for y in range(y1, y2):
                if y in empty_rows:
                    distance += expansion_factor
                else:
                    distance += 1
            return distance
        stars = [(x, y) for x in range(self.width) for y in range(self.height) if star_map[y][x] == '#']
        total_distance = 0
        for a, (x_a, y_a) in enumerate(stars):
            for (x_b, y_b) in stars[a+1:]:
                total_distance += x_distance(x_a, x_b) + y_distance(y_a, y_b)
        print(total_distance)
