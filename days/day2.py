from days.day import Day

class Day2(Day):

    day = 2
    reuse_a_input_for_b = True

    def solve_a(self):
        total = 0
        for line in self.input_lines:
            game, handlfuls = line.split(':')
            game = int(game.split()[1])
            total += game * all([
                all([
                    self.possible_once(*once.strip().split()) 
                    for once in handful.split(',')
                ])
                for handful in handlfuls.split(';')
            ])
        print(total)

    def possible_once(self, count, color):
        count = int(count)
        return (color == "red" and count <= 12) or \
            (color == "green" and count <= 13) or \
            (color == "blue" and count <= 14)

    def solve_b(self):
        total = 0
        for line in self.input_lines:
            game, handfuls = line.split(':')
            game = int(game.split()[1])
            mins = {}
            for handful in handfuls.split(';'):
                for once in handful.split(','):
                    count, color = once.strip().split()
                    count = int(count)
                    mins[color] = max(mins.get(color, 0), count)
            power = mins["red"] * mins["green"] * mins["blue"]
            total += power
        print(total)