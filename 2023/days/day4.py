from days.day import Day

class Card:

    def __init__(self, line, last_card):
        self.last_card = last_card
        label, nums = line.split(': ')
        self.card_num = int(label.split()[1])
        winning_nums, your_nums = nums.split(' | ')
        self.winning_nums = [int(x) for x in winning_nums.split()]
        self.your_nums = [int(x) for x in your_nums.split()]

    @property
    def your_winning_nums(self):
        return [n for n in self.your_nums if n in self.winning_nums]

    @property
    def winning_num_count(self):
        return len(self.your_winning_nums)

    def child_cards(self):
        # card 1 has index zero, so we don't need to add one
        # to start with the next card after this one
        return list(range(
            self.card_num,
            min(self.card_num + self.winning_num_count, self.last_card)
        ))

    def score(self):
        count_winning_nums = self.winning_num_count
        if count_winning_nums == 0:
            return 0
        return 2**(len(self.your_winning_nums) - 1)

class Day4(Day):

    day = 4
    reuse_a_input_for_b = True

    def solve_a(self):
        cards = [Card(line, len(self.input_lines)) for line in self.input_lines]
        print(sum(card.score() for card in cards))

    def solve_b(self):
        cards = [Card(line, len(self.input_lines)) for line in self.input_lines]
        card_counts = [1 for i in range(len(self.input_lines))]
        for card in cards:
            # we end up with a huge list, so it's slow, but it works
            # could create a dict with counts of each card, but meh
            # cards += [cards[i] for i in card.child_cards()]

            # okay I couldn't resist making it linear time instead of exponential
            for i in card.child_cards():
                card_counts[i] += card_counts[card.card_num - 1]
        print(sum(card_counts))
