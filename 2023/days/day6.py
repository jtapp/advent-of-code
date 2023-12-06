from days.day import Day

class Day6(Day):

    day = 6
    reuse_a_input_for_b = True

    def solve_a(self):
        times = [int(t) for t in self.input_lines[0].split()[1:]]
        distances = [int(d) for d in self.input_lines[1].split()[1:]]
        races = list(zip(times, distances))
        winning_options_counts = []
        for i, (total_time, record_distance) in enumerate(races):
            winning_options_counts += [0]
            for t in range(total_time):
                distance = t * (total_time - t)
                if distance > record_distance:
                    winning_options_counts[i] += 1
        answer = 1
        for w in winning_options_counts:
            answer *= w
        print(answer)

    def solve_b(self):
        # you could solve this by finding the solutions to x(59688274 - x) = 543102016641022
        # and subtracting them and subtracting 1 (for the reverse fencepost problem)
        # but it was easier to just copy and paste the code above and let it run for a little while

        total_time = int(''.join(self.input_lines[0].split()[1:]))
        record_distance = int(''.join(self.input_lines[1].split()[1:]))
        # winning_options_count = 0
        # for t in range(total_time):
        #     distance = t * (total_time - t)
        #     if distance > record_distance:
        #         winning_options_count += 1
        # print(winning_options_count)

        # okay let's try to the quadratic way for fun
        a = -1
        b = total_time # 59688274
        c = -record_distance # -543102016641022
        bsq_4ac = b**2 - 4 * a * c
        import math
        sqrt = math.sqrt(bsq_4ac)
        pos_numerator = -b + sqrt
        neg_numerator = -b - sqrt
        pos_solution = math.ceil(pos_numerator / (2 * a))
        neg_solution = math.ceil(neg_numerator / (2 * a))
        diff = abs(pos_solution - neg_solution)
        print(diff) # actually don't need to subtract one because I ceil'ed both numbers before diffing, so one is in the range and the other isn't
