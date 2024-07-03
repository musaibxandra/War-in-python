class Card:

    suits = [u"\u2660", u"\u2665", u"\u2666", u"\u2663"]
    ranks = ["2", "3", "4", "5", "6", "7", "8",
             "9", "10", "J", "Q", "K", "A"]

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = self.get_value()

    def __repr__(self):
        card = f'{self.rank}{self.suit}'
        return card

    def get_value(self):
        values = {}
        for value, rank in enumerate(self.ranks):
            values.update({rank: value + 2})
        return values[self.rank]
