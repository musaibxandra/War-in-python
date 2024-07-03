from card import Card
from deck import Deck
from player import Player
from dealer import Dealer
# from hand import Hand



class GamePlay:
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player('You')
        print('Weclome to War.')
        print('\n')

        # play = input("Enter P to play or Q to Quit.")
        # if play.lower() == 'q':
        #     return
        # elif play.lower() != 'p':
        #     print('Invalid key! ')
        
    def cards_drawn(self, card_1, card_2):
        print(f'The dealer is dealt: {card_1}\nYou are dealt: {card_2}')
    
    def value_of_cards(self, value_1, value_2):
        print(f"Value of the dealer's card is {value_1}\nValue of your card is {value_2}")

    def start(self):
        print('Lets begin the War.')
        self.dealer.deal_cards()
        self.player.deal_cards()
        print('The Cards have been dealt, you can start the game. ')
        while True:
            if len(self.dealer.hand) == 0:
                print('Dealer No Cards left.')
                break
            elif len(self.player.hand) == 0:
                print('Player No Cards left.')
                break
            user_input = input('Enter D to Draw a card from hand or Q to quit: ')
            if user_input.lower() == 'q':
                break 
            if user_input.lower() != 'd':
                print('Invalid key!')
                continue

            dealer_card = self.dealer.draw_card_from_dealer_hand()
            player_card = self.player.draw_card_from_player_hand()
            dealer_card_rank = Card(dealer_card.suit, dealer_card.rank)
            player_card_rank = Card(player_card.suit, player_card.rank)
            dealer_card_value = dealer_card_rank.get_value()
            player_card_value = player_card_rank.get_value()
            self.cards_drawn(dealer_card, player_card)
            self.value_of_cards(dealer_card_value, player_card_value)
            if dealer_card_value > player_card_value:
                self.dealer.hand.append(dealer_card)
                self.dealer.hand.append(player_card)
                print('Dealer wins the round.')
                print(f'length of Dealer hand {len(self.dealer.hand)}\nlength of your hand {len(self.player.hand)}')
                if len(self.player.hand) == 0:
                    print('Player has no Cards left')
                    break
            elif player_card_value > dealer_card_value:
                self.player.hand.append(dealer_card)
                self.player.hand.append(player_card)
                print(f'{self.player.name} win the round.')
                print(f'length of Dealer hand {len(self.dealer.hand)}\nlength of your hand {len(self.player.hand)}')
                if len(self.dealer.hand) == 0:
                    print('Dealer has no Cards left')
                    break
            elif dealer_card_value == player_card_value:
                print()
                print('Its a tie! we go to war.')
                print()
                while True:
                    if len(self.dealer.hand) == 0:
                        print('Dealer No Cards left.')
                        break
                    elif len(self.player.hand) == 0:
                        print('Player No Cards left.')
                        break
                    print()
                    print(" - -  WAR  - - ")
                    print()
                    print('Draw three cards..')
                    self.tie_list = []
                    self.tie_list.append(dealer_card)
                    self.tie_list.append(player_card)
                    response = input('Enter D to draw cards or Q to quit: ')
                    if response.lower() == 'q':
                        break
                    elif response.lower() != 'd':
                        print('Invalid key! ')
                        continue
                    for i in range(1,4):
                        dealer_card = self.dealer.draw_card_from_dealer_hand()
                        print(f'Dealer card face down {i}')
                        player_card = self.player.draw_card_from_player_hand()
                        print(f'player card face down {i}')
                        self.tie_list.append(dealer_card)
                        self.tie_list.append(player_card)
                    print('The three hidden cards:\nXXX\nXXX')
                    print('')
                    print('Fourth Cards:')
                    dealer_card = self.dealer.draw_card_from_dealer_hand()
                    player_card = self.player.draw_card_from_player_hand()
                    dealer_card_rank = Card(dealer_card.suit, dealer_card.rank)
                    player_card_rank = Card(player_card.suit, player_card.rank)
                    dealer_card_value = dealer_card_rank.get_value()
                    player_card_value = player_card_rank.get_value()
                    self.cards_drawn(dealer_card, player_card)
                    self.value_of_cards(dealer_card_value, player_card_value)
                    if dealer_card_value > player_card_value:
                        self.dealer.hand.append(dealer_card)
                        self.dealer.hand.append(player_card)
                        self.dealer.hand.extend(self.tie_list)
                        print('Dealer wins the round.')
                        print(f'length of Dealer hand {len(self.dealer.hand)}\nlength of your hand {len(self.player.hand)}')
                        break
                    elif player_card_value > dealer_card_value:
                        self.player.hand.append(dealer_card)
                        self.player.hand.append(player_card)
                        self.player.hand.extend(self.tie_list)
                        print(f'{self.player.name} win the round.')
                        print(f'length of Dealer hand {len(self.dealer.hand)}\nlength of your hand {len(self.player.hand)}')
                        break
                    elif dealer_card_value == player_card_value:
                        continue
                if response.lower() == 'q':
                     break

        self.winner()

    def winner(self):
        if len(self.dealer.hand) > len(self.player.hand):
            print("DEALER WINS")
        if len(self.dealer.hand) < len(self.player.hand):
            print('YOU WIN')
            
game = GamePlay()
game.start()
