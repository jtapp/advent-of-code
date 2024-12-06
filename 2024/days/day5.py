from days.day import Day
from time import sleep
from pprint import pprint

class Day5(Day):

    day = 5
    reuse_a_input_for_b = True

    def setup(self):
        rule_lines, update_lines = self.input_blob.split('\n\n')
        self.rules = [line.split('|') for line in rule_lines.split()]
        self.rules = [(int(x), int(y)) for x, y in self.rules]
        self.updates = [[int(p) for p in line.split(',')] for line in update_lines.split()]
        self.must_come_after = {}
        for x, y in self.rules:
            if y not in self.must_come_after:
                self.must_come_after[y] = {x}
            else:
                self.must_come_after[y].add(x)

        self.valid_updates = []
        self.invalid_updates = []
        for update in self.updates:
            valid = True
            for i, y in enumerate(update):
                does_come_before = set(update[i+1:])
                valid = valid and does_come_before.isdisjoint(self.must_come_after.get(y, []))
            if valid:
                self.valid_updates.append(update)
            else:
                self.invalid_updates.append(update)

    def solve_a(self):
        total = 0
        for update in self.valid_updates:
            middle = update[len(update) // 2]
            total += middle
        print(total)
                
    def solve_b(self):
        corrected_updates = []
        for update in self.invalid_updates:
            # print(update)
            relevant_must_come_after = {}
            count_of_must_come_after = {}
            pages = set(update)
            for y in update:
                relevant_must_come_after[y] = self.must_come_after.get(y, set()).intersection(pages)
                count_of_must_come_after[y] = len(relevant_must_come_after[y])
            # print(relevant_must_come_after)
            def keyfunc(p):
                nonlocal count_of_must_come_after
                return count_of_must_come_after[p]
            corrected_update = sorted(update, key=keyfunc)
            # print(corrected_update)
            corrected_updates.append(corrected_update)
            # print()
        total = 0
        for update in corrected_updates:
            middle = update[len(update) // 2]
            total += middle
        print(total)
