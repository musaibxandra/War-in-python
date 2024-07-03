from deck import Deck

class Player:
    def __init__(self, name):
        self.name = name
        self.deck = Deck()
        self.hand = []

    def draw_card_from_player_hand(self):
        if len(self.hand) == 0:
            return None
        return self.hand.pop()
    
    def deal_cards(self):
        for i in self.deck.cards:
            if len(self.deck.cards) == 0:
                return None
            self.hand.append(self.deck.cards.pop())
