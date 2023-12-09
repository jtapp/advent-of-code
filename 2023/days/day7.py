from days.day import Day

from functools import total_ordering

## hand types ##
# 5 = five of a kind
# 4 = four of a kind
# 3.5 = full house
# 3 = three of a kind
# 2 = two pair
# 1 = one pair
# 0 = high card

card_values_a = {c: (13 - i) for i, c in enumerate('AKQJT98765432')}
card_values_b = {c: (13 - i) for i, c in enumerate('AKQT98765432J')}

class Hand:

    def __init__(self, hand, bid, b = False):
        self.hand = hand
        self.bid = int(bid)
        self.hand_type = self.get_hand_type_b() if b else self.get_hand_type()
        self.card_values = self.get_card_values(card_values_b if b else card_values_a)

    def get_hand_type(self):
        card_counts = {}
        for c in self.hand:
            card_counts[c] = card_counts.get(c, 0) + 1
        card_counts = list(reversed(sorted(card_counts.values())))
        if card_counts[0] == 5:
            return 5
        elif card_counts[0] == 4:
            return 4
        elif card_counts[0] == 3 and card_counts[1] == 2:
            return 3.5
        elif card_counts[0] == 3:
            return 3
        elif card_counts[0] == 2 and card_counts[1] == 2:
            return 2
        elif card_counts[0] == 2:
            return 1
        return 0

    def get_hand_type_b(self):
        hand_without_jokers = self.hand.replace('J', '')
        joker_count = len(self.hand) - len(hand_without_jokers)
        if joker_count == 5:
            card_counts = [5]
        else:
            card_counts = {}
            for c in hand_without_jokers:
                card_counts[c] = card_counts.get(c, 0) + 1
            card_counts = list(reversed(sorted(card_counts.values())))
            card_counts[0] += joker_count
            
        if card_counts[0] == 5:
            return 5
        elif card_counts[0] == 4:
            return 4
        elif card_counts[0] == 3 and card_counts[1] == 2:
            return 3.5
        elif card_counts[0] == 3:
            return 3
        elif card_counts[0] == 2 and card_counts[1] == 2:
            return 2
        elif card_counts[0] == 2:
            return 1
        return 0

    def get_card_values(self, card_value_key):
        return [card_value_key[c] for c in self.hand]

    def __lt__(self, other):
        return self.hand_type < other.hand_type or (self.hand_type == other.hand_type and self.card_values < other.card_values)
    
    def __eq__(self, other):
        return self.hand_type == other.hand_type and self.card_values == other.card_values


class Day7(Day):

    day = 7
    reuse_a_input_for_b = True

    def solve_a(self):
        hands = [Hand(*line.split()) for line in self.input_lines]
        ranked_hands = sorted(hands)
        winnings = sum([hand.bid * (i + 1) for i, hand in enumerate(ranked_hands)])
        print(winnings)

    def solve_b(self):
        hands = [Hand(*line.split(), True) for line in self.input_lines]
        ranked_hands = sorted(hands)
        winnings = sum([hand.bid * (i + 1) for i, hand in enumerate(ranked_hands)])
        print(winnings)