from days.day import Day
from time import sleep
from pprint import pprint

def hash(s):
    val = 0
    for c in s:
        val = ((val + ord(c)) * 17) % 256
    return val

class Day15(Day):

    day = 15
    reuse_a_input_for_b = True

    def solve_a(self):
        assert hash('HASH') == 52
        seqs = self.input_blob.strip().split(',')
        verification_number = sum((hash(seq) for seq in seqs))
        print(verification_number)

    # This is a hashmap
    # the labels are keys
    # the focal lengths are values
    # the boxes are buckets.
    def solve_b(self):
        assert hash('HASH') == 52
        seqs = self.input_blob.strip().split(',')
        boxes = [[] for i in range(256)]
        for instruction in seqs:
            if instruction[-1] == '-':
                label = instruction[:-1]
                box_i = hash(label)
                boxes[box_i] = [lens for lens in boxes[box_i] if lens[0] != label]
            else:
                label, focal_length = instruction.split('=')
                focal_length = int(focal_length)
                box_i = hash(label)
                if not any((lens[0] == label for lens in boxes[box_i])):
                    boxes[box_i].append((label, focal_length))
                else:
                    for i, lens in enumerate(boxes[box_i]):
                        if lens[0] == label:
                            boxes[box_i][i] = (label, focal_length)
                            break
        # pprint(boxes[:5])
        total = 0
        for box_num, box in enumerate(boxes):
            for lens_num, (_label, focal_length) in enumerate(box):
                total += (1 + box_num) * (1 + lens_num) * focal_length
        print(total)

