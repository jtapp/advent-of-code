from days.day import Day

class Pattern:

    # transpose finds horizontal reflection line
    def __init__(self, pattern, transpose = False):
        if (not transpose):
            self.pattern = pattern
        if (transpose):
            self.pattern = [[p[i] for p in pattern] for i in range(len(pattern[0]))]
        self.width = len(self.pattern[0])
        self.height = len(self.pattern)

    # tests vertical reflection lines
    def test_reflection_i(self, i):
        i1 = i
        i2 = i + 1
        while i1 >= 0 and i2 < self.width:
            if any((self.pattern[j][i1] != self.pattern[j][i2] for j in range(self.height))):
                return False
            i1 -= 1
            i2 += 1
        return True
    
    # finds vertical reflection line
    def find_reflection_i(self):
        center = self.width // 2
        if self.test_reflection_i(center):
            return center
        for ii in range(1, self.width // 2 + 1):
            upper = center + ii
            if upper < self.width - 1 and self.test_reflection_i(center + ii):
                return upper
            lower = center - ii
            if lower >= 0 and self.test_reflection_i(lower):
                return lower
        return -1


class PatternB:

    # transpose finds horizontal reflection line
    def __init__(self, pattern, transpose = False):
        if (not transpose):
            self.pattern = pattern
        if (transpose):
            self.pattern = [[p[i] for p in pattern] for i in range(len(pattern[0]))]
        self.width = len(self.pattern[0])
        self.height = len(self.pattern)

    # tests vertical reflection lines
    def test_reflection_i(self, i):
        i1 = i
        i2 = i + 1
        num_smudges = 0
        while i1 >= 0 and i2 < self.width and num_smudges <= 1:
            num_smudges += sum((self.pattern[j][i1] != self.pattern[j][i2] for j in range(self.height)))
            i1 -= 1
            i2 += 1
        return num_smudges == 1
    
    # finds vertical reflection line
    def find_reflection_i(self):
        center = self.width // 2
        if self.test_reflection_i(center):
            return center
        for ii in range(1, self.width // 2 + 1):
            upper = center + ii
            if upper < self.width - 1 and self.test_reflection_i(center + ii):
                return upper
            lower = center - ii
            if lower >= 0 and self.test_reflection_i(lower):
                return lower
        return -1



class Day13(Day):

    day = 13
    reuse_a_input_for_b = True

    def setup(self):
        patterns = self.input_blob.split('\n\n')
        self.patterns = [p.split() for p in patterns]

    def solve_a(self):
        self.setup()
        total = 0
        for pattern in self.patterns:
            i_vertical = Pattern(pattern).find_reflection_i()
            i_horizontal = Pattern(pattern, transpose = True).find_reflection_i()
            # print('\n'.join(pattern))
            # print(i_vertical, i_horizontal)
            if i_vertical == -1 and i_horizontal == -1:
                print('pattern has no reflections')
                print('.\n'.join(pattern))
                continue
            if i_vertical > i_horizontal:
                total += i_vertical + 1
            else:
                total += (i_horizontal + 1) * 100
                
        print(total)


    def solve_b(self):
        self.setup()
        total = 0
        for pattern in self.patterns:
            i_vertical = PatternB(pattern).find_reflection_i()
            i_horizontal = PatternB(pattern, transpose = True).find_reflection_i()
            # print('\n'.join(pattern))
            # print(i_vertical, i_horizontal)
            if i_vertical == -1 and i_horizontal == -1:
                print('pattern has no reflections')
                print('.\n'.join(pattern))
                continue
            if i_vertical > i_horizontal:
                total += i_vertical + 1
            else:
                total += (i_horizontal + 1) * 100
                
        print(total)