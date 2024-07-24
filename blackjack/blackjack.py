import random
import sys

# CARDS
CARDS = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")

# SUITS
HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)

# OTHER CONSTANTS
BLACKJACK = "BLACKJACK"
EXITS = ("n", "no", "quit", "q", "exit", "out")
OPTIONS = ("h", "s", "d")

# CARD GRAPHIC
BASE_CARD = """
     ___ 
    |*  | 
    | * | 
    |__*| 

    """


def main():
    print(
        """
Rules:
    Try to get as close to 21 without going over.
    Kings, Queens, and Jacks are worth 10 points.
    Aces are worth 1 or 11 points.
    Cards 2 through 10 are worth their face value.
    (H)it to take another card.
    (S)tand to stop taking cards.
    On your first play, you can (D)ouble down to increase your bet
    but must hit exactly one more time before standing.
    In case of a tie, the bet is returned to the player.
    The dealer stops hitting at 17.
        """
    )

    money = 5000
    while money >= 0:
        print(f"Money: {money}")
        if money == 0:
            print("Sorry, you ran out of money!")
            play_again = input("Would you like to play again? [y]/n:\n")
            if play_again not in EXITS:
                money = 5000
                continue
            else:
                sys.exit()
        bet_user_input = input("How much would you like to bet?: ")
        bet = get_bet(bet_user_input, money)
        if bet:
            money -= bet
        else:
            continue

        # * Deal cards
        betting = True
        player_hand = Hand([deal_a_card() for i in range(0, 2)])
        dealer_hand = Hand([deal_a_card() for i in range(0, 2)])
        player_value = player_hand.value()
        dealer_value = "???" if betting else dealer_hand.value()

        # * Hit, Stand, or Double Down
        while betting:
            dealer_hand.show()
            player_hand.show()
            choice = input("(H)it, (S)tand or (D)ouble Down?: ")
            hit, betting = get_decision(choice)
            if hit:
                player_hand.add_card()
                print(f"Player: {player_value}")
                player_hand.show()

                # TODO: implement function
                can_player_continue = get_can_continue(player_hand)

            if betting:
                continue
            else:
                break

        # * Reveal dealer cards
        while dealer_value <= 17:
            dealer_hand.show(player=False)
            dealer_hand.add_card()

        # TODO: determine who wins
        # * Who wins - player or dealer?
        if player_value > 21 or dealer_value > player_value:
            if player_value > 21:
                print("Bust")
            else:
                print("Dealer wins.")
            money -= bet
        elif player_value > dealer_value:
            money += bet * 2
        elif player_value == dealer_value:
            money += bet
        elif player_value == "blackjack":
            money += bet * 2.5


# TODO: Implement function
def get_can_continue(hand_value: int) -> bool: ...


class Hand:
    def __init__(self, cards: list):
        self.cards = cards
        # self.value = self._value() Running into a circular-reference problem

    def __repr__(self) -> str:
        return "A hand of cards."

    def _list_cards(self):
        return self.cards

    def show(self, all=True):
        if all:
            return " ".join(self.cards)
        return f"*** {self._list_cards()[1]}"

    def add_card(self):
        self.cards.append(deal_a_card())

    def add_specific_cards(self, cards: list):
        for card in cards:
            self.cards.append(card)

    def value(self):
        face = False
        ace = False
        cards = self._list_cards()
        cards = cards.copy()
        for index, card in enumerate(cards):
            try:
                card = int(card)
            except ValueError:
                if card != "A":
                    face = True
                    cards[index] = 10
                else:
                    ace = True
                    cards[index] = 11
            else:
                cards[index] = card

        if face and ace and len(cards) == 2:
            return BLACKJACK

        # Check if Aces need to be high ace or low ace.
        for index, card in enumerate(cards):
            while sum(cards) > 21:
                if card == 11:
                    cards[index] = 1
                break

        return sum(cards)


# TODO: implement this; P3
def get_winnings(value1, value2): ...


def print_dealer_cards(betting_complete, dealer_cards):
    if betting_complete:
        return " ".join(dealer_cards)
    return f"*** {dealer_cards[1]}"


def get_decision(choice: str):
    choice = choice.lower()
    if choice in OPTIONS:
        if choice == "h":
            return True, True
        if choice == "s":
            return False, False
        if choice == "d":
            return True, False
    else:
        get_decision(
            input("Please choose to either: (H)it, (S)tand or (D)ouble Down: ")
        )


def deal_a_card():
    return random.choice(CARDS)


def get_bet(bet: str, max_bet: int):
    if bet in EXITS:
        print("Thank you for playing.")
        return sys.exit()
    try:
        bet = int(bet)
    except ValueError:
        print("Enter an integer value. Type quit to quit playing.")
        return
    if bet > max_bet:
        print("Cannot bet more than you have.")
        return
    elif bet == max_bet:
        print("Warning: This is your last bet.")
    return bet


if __name__ == "__main__":
    main()
