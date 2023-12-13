from days.day import Day

import re
from time import sleep

# def build_a_row(broken, runs):
#     ways = 0
#     gaps = []


# class Row:

#     def __init__(self, line):
#         record, runs = line.split()
#         self.broken = [True if c == '#' else None if c == '?' else False for c in self.record]
#         self.runs = [int(run) for run in runs.split(',')]
#         self.known_broken_count = sum(self.broken)
#         self.missing_broken_count = sum(self.runs) - self.known_broken_count
#         self.available_gaps = len(self.broken) - self.known_broken_count
#         self.regex = re.compile()

#     def row_matches_pattern(self, row):
#         pass

#     def recurse(self, record, in_a_run, remaining_runs):
#         assert len(remaining_runs) == 0 or remaining_runs[0] > 0
#         if len(record) == 0:
#             return len(remaining_runs) == 0
#         elif len(record) == 1:
#             c = record[0]
#             if c == '#':
#                 return in_a_run and len(remaining_runs) == 1 and remaining_runs[0] == 1
#             elif c == '.':
#                 return not in_a_run and len(remaining_runs) == 0
#             elif c == '?':
#                 return (in_a_run and len(remaining_runs) == 1 and remaining_runs[0] == 1) or \
#                     (not in_a_run and len(remaining_runs) == 0)
#         else:
#             remaining_runs = remaining_runs.copy()
#             c, rest = record[0], record[1:]
#             if c == '#':
#                 if in_a_run:
#                     remaining_in_this_run = remaining_runs[0] - 1
#                     if remaining_in_this_run == 0:
#                         return self.recurse(rest, False, remaining_runs[1:])
#                     else:
#                         return self.recurse(rest, True, [remaining_in_this_run] + remaining_runs[1:])
#                 else:
#                     # TODO need some of that other logic in here to decrememnt, and handle the case where there is only a run of 1
#                     # oh and I'm missing logic for making sure there is a gap between runs :(
#                     return self.recurse(rest, True, remaining_runs)
#             elif c == '.':
#                 if in_a_run:
#                     return 0
#                 else:
#                     return self.recurse(rest, False, remaining_runs[1:])
#             elif c == '?':
#                 if in_a_run:
#                     # has to be broken, copy from above
#                     remaining_in_this_run = remaining_runs[0] - 1
#                     if remaining_in_this_run == 0:
#                         return self.recurse(rest, False, remaining_runs[1:])
#                     else:
#                         return self.recurse(rest, True, [remaining_in_this_run] + remaining_runs[1:])
#                 else:
#                     if len(remaining_runs) == 0:
#                         return self.recurse(rest, False, remaining_runs[1:])
#                     else:
#                         remaining_in_this_run = remaining_runs[0] - 1
#                         count_if_broken = self.recurse(rest, True, remaining_runs[])

#             else:
#                 raise Exception("Unexpected charater " + c)


class Day12(Day):

    day = 12
    reuse_a_input_for_b = True

    def solve_a(self):
        total_option_count = 0
        for i, line in enumerate(self.input_lines):
            # print(i, line)
            record, runs = line.split()
            broken = [True if c == '#' else None if c == '?' else False for c in record]
            runs = [int(run) for run in runs.split(',')]
            known_broken_count = sum([borked == True for borked in broken])
            missing_broken_count = sum(runs) - known_broken_count
            available_gaps = len(broken) - known_broken_count
            # regex_for_record = re.compile(r'^' + record.replace('?', r"(.|#)").replace('.', r"\.") + '$')
            regex_for_runs = re.compile(r"^\.*" + r"\.+".join(("#" * run for run in runs)) + r"\.*$")
            
            def construct(acc, rest):
                if len(rest) == 0:
                    return acc
                this = rest[0]
                if this == '?':
                    acc = [up_to_now + '.' for up_to_now in acc] + [up_to_now + '#' for up_to_now in acc]
                else:
                    acc = [up_to_now + this for up_to_now in acc]
                return construct(acc, rest[1:])

            options = construct([''], record)
            option_count = 0
            for option in options:
                valid_option = regex_for_runs.fullmatch(option) is not None
                # print(option, valid_option)
                option_count += valid_option
            total_option_count += option_count

        print(total_option_count)
                        
    def solve_b(self):
        total_option_count = 0
        for ii, line in enumerate(self.input_lines):
            # print(ii, line)
            record, runs = line.split()
            record = '?'.join([record] * 5)
            # print(record)
            runs = [int(run) for run in runs.split(',')]
            runs = runs * 5
            num_runs = len(runs)
            regex_for_runs = re.compile(r"^\.*" + r"\.+".join(("#" * run for run in runs)) + r"\.*$")
            
            def valid_runs_so_far(partial_option):
                partial_runs = [len(run) for run in partial_option.split('.') if run]
                num_partial_runs = len(partial_runs)
                if num_partial_runs == 0:
                    return True
                valid = num_partial_runs <= num_runs and \
                    ((partial_option[-1] == '.' and partial_runs == runs[:num_partial_runs]) or \
                    (partial_option[-1] == '#' and partial_runs[:-1] == runs[:num_partial_runs-1] and partial_runs[-1] <= runs[num_partial_runs - 1]))
                # print(partial_option, '\t', num_partial_runs, partial_runs[:-1], runs[:num_partial_runs - 1], partial_runs[:-1] == runs[:num_partial_runs - 1], valid)
                return valid
            
            def valid_partial_runs(partial_runs, last_char):
                num_partial_runs = len(partial_runs)
                if num_partial_runs == 0:
                    return True
                valid = num_partial_runs <= num_runs and \
                    ((last_char == '.' and partial_runs == runs[:num_partial_runs]) or \
                    (last_char == '#' and partial_runs[:-1] == runs[:num_partial_runs-1] and partial_runs[-1] <= runs[num_partial_runs - 1]))
                return valid

            def valid_final_runs(final_option):
                final_runs = [len(run) for run in final_option.split('.') if run]
                return final_runs == runs

            # def construct_options(count, acc, rest):
            #     if len(rest) == 0:
            #         return count + len(acc)
            #     this = rest[0]
            #     if this == '?':
            #         acc = [up_to_now + '.' for up_to_now in acc] + [up_to_now + '#' for up_to_now in acc]
            #     else:
            #         acc = [up_to_now + this for up_to_now in acc]
            #     acc = [partial_option for partial_option in acc if valid_runs_so_far(partial_option)]
            #     return construct_options(count, acc, rest[1:])
            # options = construct_options(0, [''], record)
            # option_count = 0
            # for option in options:
            #     valid_option = regex_for_runs.fullmatch(option) is not None
            #     # print(option, valid_option)
            #     option_count += valid_option
            
            # def count_options(count, up_to_now, rest):
            #     # print(up_to_now)
            #     # sleep(0.1)
            #     if not valid_runs_so_far(up_to_now):
            #         return count
            #     if len(rest) == 0:
            #         # return count + (regex_for_runs.fullmatch(up_to_now) is not None)
            #         return count + valid_final_runs(up_to_now)
            #     if rest[0] == '?':
            #         count = count_options(count, up_to_now + '.', rest[1:])
            #         count = count_options(count, up_to_now + '#', rest[1:])
            #     else:
            #         count = count_options(count, up_to_now + rest[0], rest[1:])
            #     return count
            # option_count = count_options(0, '', record)
            # print(i, line, '\t\t', option_count)

            
            # let's try doing it iteratively instead of recursively
            option_count = 0
            i = 0
            up_to_now = ""
            partial_runs = []
            state = [0] * len(record)
            # 0 is not visited
            # 1 is trying broken
            # 2 is trying working
            while i > -1:
                # print(''.join((str(s) for s in state)))
                # print()
                # print(record)
                # print(up_to_now, '\t', i)
                # print(partial_runs)
                # sleep(0.1)
                assert i == len(up_to_now)
                if i == len(record):
                    option_count += valid_final_runs(up_to_now)
                    if up_to_now[-1] == '#':
                        partial_runs[-1] -= 1
                        if partial_runs[-1] == 0:
                            partial_runs = partial_runs[:-1]
                    up_to_now = up_to_now[:-1]
                    i -= 1
                    # continue
                # elif not valid_runs_so_far(up_to_now):
                elif len(up_to_now) > 1 and not valid_partial_runs(partial_runs, up_to_now[-1]):
                    if up_to_now[-1] == '#':
                        partial_runs[-1] -= 1
                        if partial_runs[-1] == 0:
                            partial_runs = partial_runs[:-1]
                    up_to_now = up_to_now[:-1]
                    i -= 1
                    # continue

                # prev = record[i - 1]
                this = record[i]
                if state[i] == 0 and (this == '?' or this == '#'):
                    up_to_now += '#'
                    state[i] = 1
                    if len(partial_runs) == 0 or up_to_now[i-1] == '.':
                        partial_runs.append(1)
                    else: # up_to_now[i-1] == '#':
                        partial_runs[-1] += 1
                    i += 1
                elif state[i] == 0 or (state[i] == 1 and this == '?'):
                    up_to_now += '.'
                    state[i] = 2
                    i += 1
                else:
                    if i > 0 and up_to_now[i-1] == '#':
                        partial_runs[-1] -= 1
                        if partial_runs[-1] == 0:
                            partial_runs = partial_runs[:-1]
                    up_to_now = up_to_now[:-1]
                    state[i] = 0
                    i -= 1


            print(ii, line, '\t\t', option_count)
            total_option_count += option_count


        print(total_option_count)