from days.day import Day

def build_a_row(broken, runs):
    ways = 0
    gaps = []


class Row:

    def __init__(self, line):
        record, runs = line.split()
        self.broken = [True if c == '#' else None if c == '?' else False for c in self.record]
        self.runs = [int(run) for run in runs.split(',')]
        self.known_broken_count = sum(self.broken)
        self.missing_broken_count = sum(self.runs) - self.known_broken_count
        self.available_gaps = len(self.broken) - known_broken_count

    def build_a_row(self):
        ways = 0
        gaps = []

    def recurse(self, record, in_a_run, remaining_runs):
        assert len(remaining_runs) == 0 or remaining_runs[0] > 0
        if len(record) == 0:
            return len(remaining_runs) == 0
        elif len(record) == 1:
            c = record[0]
            if c == '#':
                return in_a_run and len(remaining_runs) == 1 and remaining_runs[0] == 1
            else c == '.':
                return not in_a_run and len(remaining_runs) == 0
            elif c == '?':
                return (in_a_run and len(remaining_runs) == 1 and remaining_runs[0] == 1) or \
                    (not in_a_run and len(remaining_runs) == 0)
        else:
            remaining_runs = remaining_runs.copy()
            c, rest = record[0], record[1:]
            if c == '#':
                if in_a_run:
                    remaining_in_this_run = remaining_runs[0] - 1
                    if remaining_in_this_run == 0:
                        return self.recurse(rest, False, remaining_runs[1:])
                    else:
                        return self.recurse(rest, True, [remaining_in_this_run] + remaining_runs[1:])
                else:
                    # TODO need some of that other logic in here to decrememnt, and handle the case where there is only a run of 1
                    # oh and I'm missing logic for making sure there is a gap between runs :(
                    return self.recurse(rest, True, remaining_runs)
            elif c == '.':
                if in_a_run:
                    return 0
                else:
                    return self.recurse(rest, False, remaining_runs[1:])
            elif c == '?':
                if in_a_run:
                    # has to be broken, copy from above
                    remaining_in_this_run = remaining_runs[0] - 1
                    if remaining_in_this_run == 0:
                        return self.recurse(rest, False, remaining_runs[1:])
                    else:
                        return self.recurse(rest, True, [remaining_in_this_run] + remaining_runs[1:])
                else:
                    if len(remaining_runs) == 0:
                        return self.recurse(rest, False, remaining_runs[1:])
                    else:
                        remaining_in_this_run = remaining_runs[0] - 1
                        count_if_broken = self.recurse(rest, True, remaining_runs[])

            else:
                raise Exception("Unexpected charater " + c)



.
#
?



class Day12(Day):

    day = 12
    reuse_a_input_for_b = True

    def solve_a(self):


    # def solve_b(self):
