from pprint import pprint
from time import sleep
from days.day import Day
from itertools import permutations
from time import time

class Options:

    def __init__(self, options):
        middle = len(options) // 2
        self.value = options[middle]
        if middle > 0:
            self.left = Options(options[:middle])
        else:
            self.left = None
        if middle < len(options) - 1:
            self.right = Options(options[1+middle:])
        else:
            self.right = None

class Day7(Day):

    day = 7
    reuse_a_input_for_b = True

    def setup(self):
        self.lines = [
            (int(line_pair[0]), [int(x) for x in line_pair[1].strip().split()])
            for line_pair in [line.split(":") for line in self.input_lines]
        ]

    # rest should be pairs of (0, x) for addition and (1, x) for multiplication
    def eval(self, x1, rest):
        total = x1
        rest = list(rest)
        for op, x in rest:
            total = total + (total * (op * (x - 1))) + ((1 - op) * x)
        # print(x1, rest, total)
        return total

    # concat is 2
    def eval_with_concat(self, value, x1, rest):
        total = x1
        rest = list(rest)
        for op, x in rest:
            if op == 2:
                shift = ((x < 10) * 10) + ((10 <= x < 100) * 100) + ((100 <= x < 1000) * 1000)
                total = (total * shift) + x
            else:
                total = total + (total * (op * (x - 1))) + ((1 - op) * x)
            if (total > value):
                return total
        # print(x1, rest, total)
        return total

    def try_with_n_multiplies(self, value, xs, n):
        base_ops = [1] * n + [0] * (len(xs) - 1 - n)
        results = []
        for ops in list(set(permutations(base_ops)))[::-1]:
            result = self.eval(xs[0], zip(ops, xs[1:]))
            results.append(result)
            if result == value:
                return results
        return results

    def try_with_n1_multiplies_n2_concats(self, value, xs, n1, n2):
        base_ops = [1] * n1 + [2] * n2 + [0] * (len(xs) - 1 - n1 - n2)
        # results = []
        for ops in set(permutations(base_ops)):
            result = self.eval_with_concat(value, xs[0], zip(ops, xs[1:]))
            # results.append(result)
            if result == value:
                return True
                # return results
        return False
        # return results


    def possible_without_concat(self, value, xs):
        stack = [None, Options(range(len(xs)))]
        while len(stack) > 0:
            options = stack.pop()
            if options is None:
                continue
            num_multiplication = options.value
            results = self.try_with_n_multiplies(value, xs, num_multiplication)
            if value in results:
                return True
            if max(results) < value:
                # more multiplication, so push right second
                stack.append(options.left)
                stack.append(options.right)
            elif min(results) > value:
                # less multiplication, so push left second
                stack.append(options.right)
                stack.append(options.left)
            else:
                avg = sum(results) / len(results)
                if avg < value:
                    # more multiplication, so push right second
                    stack.append(options.left)
                    stack.append(options.right)
                else:
                    # less multiplication, so push left second
                    stack.append(options.right)
                    stack.append(options.left)
        return False

    def possible_with_concat(self, value, xs, big=False):
        for n2 in range(1, len(xs)): # must use at least 1 concat or it wouldnt need it
            for n1 in range(0, len(xs) - n2):
                if big and (n2 >= 1 + big*2) and (n1 >= big*3):
                    continue
                if self.try_with_n1_multiplies_n2_concats(value, xs, n1, n2):
                    return True
        return False

    def solve_a(self):
        total = 0
        for i, (value, xs) in enumerate(self.lines):
            if self.possible_without_concat(value, xs):
                total += value
            if not i % 25:
                print(i)
        print(total)

    def solve_b(self):
        works_without_concat = []
        # for i, (value, xs) in enumerate(self.lines):
        #     if self.possible_without_concat(value, xs):
        #         works_without_concat.append(i)
        #     if not i % 25:
        #         print("progress:", i)
        # print("works without concat:", works_without_concat, "\n")
        works_without_concat = [1, 4, 5, 7, 8, 11, 18, 19, 22, 25, 30, 34, 38, 43, 46, 49, 50, 55, 57, 60, 62, 67, 69, 74, 75, 76, 77, 78, 80, 83, 85, 88, 92, 94, 96, 97, 98, 104, 108, 112, 113, 115, 117, 119, 120, 124, 126, 127, 128, 131, 132, 133, 135, 137, 140, 141, 142, 144, 145, 148, 149, 151, 154, 156, 157, 161, 162, 164, 166, 168, 172, 173, 182, 185, 186, 187, 190, 191, 192, 195, 201, 204, 207, 208, 209, 210, 213, 214, 215, 216, 217, 220, 222, 224, 225, 228, 229, 232, 233, 234, 238, 241, 242, 245, 248, 251, 254, 256, 258, 263, 264, 266, 268, 271, 273, 279, 283, 284, 287, 290, 295, 297, 299, 300, 301, 303, 307, 310, 311, 313, 317, 323, 326, 327, 330, 332, 333, 335, 336, 337, 339, 340, 341, 342, 343, 344, 349, 353, 357, 360, 364, 368, 370, 371, 373, 375, 376, 380, 381, 382, 385, 387, 392, 395, 399, 400, 402, 404, 408, 409, 412, 414, 415, 418, 422, 424, 425, 426, 427, 429, 432, 434, 435, 437, 438, 442, 443, 444, 447, 449, 451, 453, 454, 455, 461, 464, 465, 466, 467, 468, 476, 478, 480, 481, 483, 484, 487, 492, 494, 496, 497, 498, 500, 501, 502, 509, 512, 515, 516, 519, 523, 524, 528, 529, 530, 533, 539, 541, 546, 550, 553, 554, 555, 563, 570, 572, 574, 575, 576, 578, 579, 580, 584, 588, 590, 591, 592, 593, 595, 598, 600, 602, 604, 606, 609, 610, 612, 613, 615, 616, 617, 619, 620, 623, 624, 628, 634, 637, 638, 646, 648, 649, 650, 652, 653, 655, 657, 659, 661, 662, 666, 667, 672, 676, 678, 680, 682, 685, 686, 687, 688, 689, 692, 694, 699, 700, 701, 705, 707, 711, 713, 717, 718, 719, 720, 724, 727, 728, 729, 730, 734, 740, 743, 745, 746, 747, 749, 750, 753, 756, 760, 761, 762, 767, 768, 769, 771, 772, 776, 780, 782, 786, 789, 794, 795, 800, 807, 808, 814, 815, 818, 820, 822, 826, 828, 830, 838, 841, 844, 846]
        print("there are", len(works_without_concat), "that work without concat")
        total = 0
        check_with_concat = []
        start = time()
        for i, line in enumerate(self.lines):
            if i in works_without_concat:
                total += line[0]
            else:
                check_with_concat.append(line)
        skipped = []
        # FEASIBLE_LENGTH = 11
        # for i, (value, xs) in enumerate(check_with_concat):
        #     if (len(xs) > FEASIBLE_LENGTH):
        #         skipped.append((value, xs))
        #         continue
        #     if self.possible_with_concat(value, xs):
        #         total += value
        #     if not i % 25:
        #         print(f"progress: {i} / {len(check_with_concat)} after {time() - start:.2f} seconds")
        skipped = [(34951709, [7, 6, 7, 2, 8, 765, 9, 97, 1, 9, 1, 7]), (320286213, [5, 6, 99, 75, 95, 5, 3, 3, 1, 6, 2, 7]), (5078158, [5, 6, 6, 92, 83, 1, 4, 1, 8, 4, 60, 1]), (2536267308, [9, 54, 7, 9, 5, 2, 53, 3, 1, 6, 5, 5]), (5309045, [1, 6, 9, 9, 2, 5, 203, 2, 2, 1, 54, 4]), (84131040, [8, 16, 4, 3, 7, 2, 552, 6, 8, 7, 4, 1]), (49303083, [2, 4, 453, 3, 7, 8, 8, 2, 7, 76, 6, 3]), (203668202, [1, 4, 449, 9, 18, 2, 2, 3, 2, 5, 1, 4]), (1097770009, [6, 8, 6, 6, 82, 9, 7, 372, 2, 3, 7, 7]), (12444030231, [85, 5, 4, 8, 2, 6, 3, 86, 7, 4, 2, 29]), (295200671, [3, 1, 7, 6, 6, 492, 2, 3, 3, 3, 4, 2]), (63001440, [9, 7, 71, 3, 4, 1, 4, 9, 141, 2, 3, 6]), (16205356271, [2, 45, 9, 1, 1, 6, 781, 4, 9, 1, 4, 5]), (75032493, [6, 5, 3, 4, 4, 3, 4, 2, 231, 4, 6, 1]), (12690529743, [6, 1, 2, 3, 576, 8, 14, 3, 9, 6, 4, 6]), (7257802, [5, 8, 192, 2, 3, 6, 1, 8, 2, 3, 30, 9]), (3494721190, [8, 32, 5, 8, 4, 6, 174, 6, 7, 3, 8, 8]), (99124639, [9, 1, 6, 4, 8, 6, 30, 8, 4, 463, 6, 3]), (14139025531, [2, 7, 8, 3, 585, 58, 4, 3, 3, 5, 6, 7]), (383283459, [9, 2, 6, 1, 813, 2, 1, 2, 2, 2, 24, 8]), (380801339, [50, 8, 238, 2, 1, 1, 7, 4, 4, 1, 6, 1]), (4039457351, [738, 9, 9, 3, 8, 2, 2, 91, 6, 4, 4, 8]), (162731016, [7, 9, 1, 3, 56, 233, 7, 6, 7, 6, 4, 9]), (4654432831942, [5, 96, 8, 4, 4, 9, 8, 4, 9, 3, 194, 1]), (206338833295, [9, 2, 1, 34, 2, 6, 7, 5, 781, 4, 4, 1]), (153441694949, [7, 1, 4, 3, 7, 7, 208, 2, 9, 4, 9, 49]), (191964843181, [74, 2, 6, 9, 7, 8, 9, 15, 14, 6, 3, 1]), (350312763, [405, 8, 3, 8, 8, 9, 5, 9, 7, 4, 2, 7]), (16479828637, [5, 6, 51, 8, 6, 1, 9, 99, 57, 6, 4, 5]), (6129304, [8, 8, 86, 53, 3, 6, 2, 1, 1, 1, 3, 35]), (261741896, [2, 3, 7, 3, 1, 49, 9, 7, 418, 3, 6, 9]), (20416347, [9, 9, 3, 4, 8, 5, 3, 139, 6, 3, 8, 1]), (908336037, [9, 801, 9, 7, 90, 5, 6, 1, 5, 4, 1, 2]), (9530549257, [4, 8, 6, 4, 8, 79, 8, 103, 6, 4, 5, 6]), (2699428486, [3, 6, 8, 7, 8, 3, 6, 7, 51, 4, 47, 8]), (10235870, [2, 2, 9, 5, 3, 7, 9, 9, 4, 73, 1, 195]), (6758911, [29, 1, 1, 9, 463, 3, 7, 4, 5, 9, 7, 8]), (372902, [5, 8, 3, 2, 8, 44, 2, 8, 9, 80, 81, 3])]
        total = 144844108814807
        print("total so far:", total)
        print("skipped:", len(skipped))
        # print(skipped)
        for i, (value, xs) in enumerate(skipped):
            if value in [320286213, 1097770009, 7257802, 162731016, 206338833295, 191964843181, 49303083, 99124639, 20416347]:
                result = True # already worked with the special Big setting
            else:
                result = self.possible_with_concat(value, xs, True)
                print(value, result)
            if result:
                total += value
            print(f"progress: {i} / {len(skipped)} after {time() - start:.2f} seconds")
        print("final total:", total)
