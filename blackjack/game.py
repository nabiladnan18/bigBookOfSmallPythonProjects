import random
from card import Card, CARDS, SUITS
from hand import Hand, BLACKJACK
from money import Money


class Game:
    def __init__(self, buy_in: int) -> None:
        self.money = Money(buy_in)
        self.deck = self.create_deck()

    def create_deck(self):
        # 4 decks to draw from
        deck = [
            Card(card, suit) for card in CARDS for suit in SUITS for _ in range(0, 4)
        ]
        random.shuffle(deck)
        return deck

    def deal_card(self):
        return self.deck.pop()

    def determine_winner(
        self, player_hand: Hand, dealer_hand: Hand, bet: int, doubled_down=False
    ):
        if player_hand.is_bust():
            return "Dealer wins!", 0
        if dealer_hand.is_bust():
            winnings = bet * 2
            if doubled_down:
                winnings *= 2
            self.money.win(winnings)
            return "Player wins!", winnings
        if player_hand.value() == dealer_hand.value():
            return "Push", 0

        return "Dealer wins!", 0

    def play(self, bet):
        player_hand = Hand()
        dealer_hand = Hand()
        doubled_down = False
        first_move = True

        for _ in range(0, 2):
            player_hand.add_card(self.deal_card())
            dealer_hand.add_card(self.deal_card())

        while not player_hand.is_bust():
            print("Dealer: ???")
            print(f"Dealer: *** {dealer_hand.cards[0]}\n")
            # show cards here
            print(f"Player: {player_hand.value()}")
            print(f"Player: {player_hand}")

            if first_move and not player_hand.is_blackjack():
                move = input("(H)it, (S)tand or (D)ouble Down?: ").lower()
            else:
                move = input("(H)it or (S)tand?: ").lower()

            if move == "h":
                player_hand.add_card(self.deal_card())
                first_move = False
            elif move == "s":
                break
            elif move == "d" and first_move and len(player_hand.cards) == 2:
                doubled_down = True
                self.money.bet(bet)
                bet *= 2
                player_hand.add_card(self.deal_card())
                break
            else:
                print("Invalid move; please choose again.")

        while dealer_hand.value() <= 17:
            dealer_hand.add_card(self.deal_card())

        result, winnings = self.determine_winner(
            player_hand, dealer_hand, bet, doubled_down
        )
        print(f"Dealer: {dealer_hand.value()}")
        print(f"Dealer: {dealer_hand.cards}\n")
        print(f"Player: {player_hand.value()}")
        print(f"Player: {player_hand.cards}\n")
        print(result)

        return winnings
