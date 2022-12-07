from card_sintax import valid_cards as cards
from random import shuffle

class Deck:
    def __init__(self):
        self.cards = cards()[:]

    def shuffle_deck(self):
        shuffle(self.cards)

    def deal_cards(self, value):
        dealt_cards = []
        for _ in range(value):
            dealt_cards.append(self.cards.pop())
        
        return dealt_cards


