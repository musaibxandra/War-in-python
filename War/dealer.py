from deck import Deck

class Dealer:
    def __init__(self):
        self.deck = Deck()
        self.hand = []

    def draw_card_from_dealer_hand(self):
        if len(self.hand) == 0:
            return None
        return self.hand.pop()

    def deal_cards(self):
        for i in range(26):
            if len(self.deck.cards) == 0:
                return None
            self.hand.append(self.deck.cards.pop())
