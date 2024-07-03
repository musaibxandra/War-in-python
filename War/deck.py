import random
from card import Card

class Deck:
    def __init__(self):
        self.cards = []
        for suit in Card.suits:
            for rank in Card.ranks:
                self.cards.append(Card(suit, rank))
        
        random.shuffle(self.cards)
