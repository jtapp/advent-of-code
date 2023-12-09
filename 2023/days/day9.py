from days.day import Day

class Seq:

    def __self__(self, line):
        self.seq = [int(n) for n in line.split()]
        

class Day9(Day):

    day = 9
    reuse_a_input_for_b = True

    def solve_a(self):
        seqs = tuple([[int(n) for n in line.split()] for line in self.input_lines])
        total = 0
        for seq in seqs:
            these = [seq]
            current = seq
            while any(current):
                current = tuple((current[i] - current[i-1] for i in range(1, len(current))))
                these.append(current)
            next_num_in_seq = sum((d[-1] for d in these))
            total += next_num_in_seq
            print(seq, ' -> ', next_num_in_seq)        
        print(total)

    def solve_b(self):
        seqs = tuple([[int(n) for n in line.split()] for line in self.input_lines])
        total = 0
        for seq in seqs:
            these = [seq]
            current = seq
            while any(current):
                current = tuple((current[i] - current[i-1] for i in range(1, len(current))))
                these.append(current)
                
            prev_num_in_seq = 0
            for d in reversed(these):
                prev_num_in_seq = d[0] - prev_num_in_seq
            total += prev_num_in_seq
            print(prev_num_in_seq, '<- ', seq)
        print(total)