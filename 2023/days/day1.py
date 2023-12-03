from days.day import Day

class Day1(Day):

    day = 1
    reuse_a_input_for_b = True

    def solve_a(self):
        total = sum([self.cal_from_line(line) for line in self.input_lines])
        print(total)

    def cal_from_line(self, line):
        first = None
        last = None
        for c in line:
            if c.isdigit():
                first = first or c
                last = c
        return int(f"{first}{last}")
    
    def solve_b(self):
        total = sum([self.cal_from_line_b(line) for line in self.input_lines])
        print(total)
    
    def cal_from_line_b(self, line):
        numbers = [
            "one",
            "two",
            "three",
            "four",
            "five",
            "six",
            "seven",
            "eight",
            "nine",
        ]

        first = None
        last = None
        for i, c in enumerate(line):
            if c.isdigit():
                first = first or c
                last = c
            else:
                for j, num in enumerate(numbers):
                    if (line[i : i + len(num)] == num):
                        first = first or (j + 1)
                        last = j + 1
        return int(f"{first}{last}")
    