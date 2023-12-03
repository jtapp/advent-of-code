from days.day import Day

class Day3(Day):

    day = 3
    reuse_a_input_for_b = True

    def solve_a(self):
        parts = self.get_parts()
        total = sum([num_info[0] * num_info[2] for num_info in parts])
        print(total)

    def solve_b(self):
        parts = self.get_parts()
        gears = {}
        print(parts[0])
        for part_num, _, is_part, (touches_gear, gear_line, gear_i) in parts:
            if is_part and touches_gear:
                k = (gear_line, gear_i)
                gears[k] = gears.get(k, []) + [part_num]
        total = 0
        for (gear_line, gear_i), part_nums in gears.items():
            if len(part_nums) == 2:
                total += part_nums[0] * part_nums[1]
        print(total)


    def get_parts(self):
        nums = []
        in_a_num = False
        for j, line in enumerate(self.input_lines):
            for i, c in enumerate(line):
                if in_a_num:
                    if c.isdigit():
                        end_of_num += 1
                    else:
                        in_a_num = False
                        nums += [[int(line[start_of_num : end_of_num + 1]), (j, start_of_num, end_of_num)]]
                elif c.isdigit():
                    in_a_num = True
                    start_of_num = i
                    end_of_num = i
            if in_a_num: # num at end of line
                in_a_num = False
                nums += [[int(line[start_of_num : end_of_num + 1]), (j, start_of_num, end_of_num)]]
        return [self.part_info(num_info) for num_info in nums]

    # arg: num_info is [part_num, (line, begin_i, end_i)]
    # ret: part_info is [part_num, (line, begin_i, end_i), is_part, (touches_gear, gear_line, gear_i)]
    def part_info(self, num_info):
        num, (line, start_of_num, end_of_num) = num_info
        lines_to_check = []
        if line != 0:
            lines_to_check += [line - 1]
        if line != self.height - 1:
            lines_to_check += [line + 1]

        if start_of_num == 0:
            first_i = 0
        else:
            first_i = start_of_num - 1
            c = self.input_lines[line][start_of_num - 1]
            if self.is_symbol(c):
                return num_info + [True, self.gear_info(c, line, start_of_num - 1)]

        if end_of_num == self.width - 1:
            last_i = end_of_num
        else:
            last_i = end_of_num + 1
            c = self.input_lines[line][end_of_num + 1]
            if (self.is_symbol(c)):
                return num_info + [True, self.gear_info(c, line, end_of_num + 1)]

        for j in lines_to_check:
            for i in range(first_i, last_i + 1):
                c = self.input_lines[j][i]
                if (self.is_symbol(c)):
                    return num_info + [True, self.gear_info(c, j, i)]
        return num_info + [False, (False, None, None)]
    
    def is_symbol(self, c):
        return not (c.isdigit() or c == '.')

    def gear_info(self, symbol, line, i):
        if (symbol != '*'): # not a gear
            return (False, None, None)
        return (True, line, i)
