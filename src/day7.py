from utils import *
import itertools
import numpy as np

CardDict = {'2': 2, 2: '2',
            '3': 3, 3: '3',
            '4': 4, 4: '4',
            '5': 5, 5: '5',
            '6': 6, 6: '6',
            '7': 7, 7: '7',
            '8': 8, 8: '8',
            '9': 9, 9: '9',
            'T': 10, 10: 'T',
            'J': 1, 1: 'J',
            'Q': 12, 12: 'Q',
            'K': 13, 13: 'K',
            'A': 14, 14: 'A'}



class Card:
    def __init__(self, value: int | str) -> None:
        if type(value) == str:
            self.value = CardDict[value]
            self.symbol = value
        elif type(value) == int:
            self.value = value
            self.symbol = CardDict[value]
        else:
            print('Error: Card value must be int or str')
    
    def __str__(self) -> str:
        return f'Card({self.symbol})'
    
    def __repr__(self) -> str:
        return self.symbol
    
    def __eq__(self, o: object) -> bool:
        return self.value == o.value
    
    def __lt__(self, o: object) -> bool:
        return self.value < o.value
    
    def __gt__(self, o: object) -> bool:
        return self.value > o.value
    
    def __le__(self, o: object) -> bool:
        return self.value <= o.value
    
    def __ge__(self, o: object) -> bool:
        return self.value >= o.value
    
    def __ne__(self, o: object) -> bool:
        return self.value != o.value
    
    def __hash__(self) -> int:
        return hash(self.value)

class Hand:
    def __init__(self, cards: list[Card], bid) -> None:
        self.cards = cards
        self.bid = bid
        self.count_dict = self.get_count_dict()
    
    def get_count_dict(self) -> dict[Card, int]:
        count_dict = {}
        jokers = 0
        for card in self.cards:
            if card == Card('J'):
                jokers += 1
                continue
            elif card in count_dict:
                count_dict[card] += 1
            else:
                count_dict[card] = 1
        if len(count_dict.keys()) == 0:
            return {Card('A'): jokers}
        else:
            sorted_dict = sorted(count_dict.items(), key=lambda x:x[1], reverse=True)
            count_dict[sorted_dict[0][0]] += jokers
        return count_dict
    
    def is_five_of_a_kind(self) -> bool:
        return 5 in self.count_dict.values()
    
    def is_four_of_a_kind(self) -> bool:
        return 4 in self.count_dict.values()
    
    def is_full_house(self) -> bool:
        return 3 in self.count_dict.values() and 2 in self.count_dict.values()
    
    def is_three_of_a_kind(self) -> bool:
        return 3 in self.count_dict.values()
    
    def is_two_pairs(self) -> bool:
        return list(self.count_dict.values()).count(2) == 2
    
    def is_pair(self) -> bool:
        return 2 in self.count_dict.values()
    
    def get_type(self) -> str:
        if self.is_five_of_a_kind():
            return 6
        elif self.is_four_of_a_kind():
            return 5
        elif self.is_full_house():
            return 4
        elif self.is_three_of_a_kind():
            return 3
        elif self.is_two_pairs():
            return 2
        elif self.is_pair():
            return 1
        else:
            return 0
    
    def __repr__(self) -> str:
        return tuple(self.cards).__repr__()
    
    def __str__(self) -> str:
        return f'Hand{tuple(self.cards).__str__()}'
    
    def __eq__(self, o: object) -> bool:
        return self.cards == o.cards
    
    def __lt__(self, o: object) -> bool:
        type_self = self.get_type()
        type_o = o.get_type()
        if type_self == type_o:
            for i in range(len(self.cards)):
                if self.cards[i] != o.cards[i]:
                    return self.cards[i] < o.cards[i]
            return False
        else:
            return type_self < type_o
    
    def __gt__(self, o: object) -> bool:
        type_self = self.get_type()
        type_o = o.get_type()
        if type_self == type_o:
            for i in range(len(self.cards)):
                if self.cards[i] != o.cards[i]:
                    return self.cards[i] > o.cards[i]
            return False
        else:
            return type_self > type_o
    
    def __le__(self, o: object) -> bool:
        type_self = self.get_type()
        type_o = o.get_type()
        if type_self == type_o:
            for i in range(len(self.cards)):
                if self.cards[i] != o.cards[i]:
                    return self.cards[i] <= o.cards[i]
            return True
        else:
            return type_self <= type_o
    
    def __ge__(self, o: object) -> bool:
        type_self = self.get_type()
        type_o = o.get_type()
        if type_self == type_o:
            for i in range(len(self.cards)):
                if self.cards[i] != o.cards[i]:
                    return self.cards[i] >= o.cards[i]
            return True
        else:
            return type_self >= type_o
    
    def __ne__(self, o: object) -> bool:
        return self.cards != o.cards

data = readlines()

hands = []

for line in data:
    line = line.strip()
    hand, bid = line.split(' ')
    bid = int(bid)
    cards = []
    for card in hand:
        cards.append(Card(card))
    hand = Hand(cards, bid)
    hands.append(hand)

answer = 0
hands = sorted(hands)
for idx, hand in enumerate(hands):
    print(hand)
    answer += hand.bid * (idx + 1)

print(answer)