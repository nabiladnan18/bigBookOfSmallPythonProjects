import unittest

from .blackjack import BLACKJACK, Hand, get_does_dealer_win, get_is_hand_bust

#! TEST CASES
#! A, 8 --> 11 + 8 == 19
#! A, 8, A --> 11 + 8 + 1 == 20
#! A, 8, A, A --> 11 + 8 + 1 + 1 == 21
#! A, 8, A, 5 --> 1 + 8 + 1 + 5 == 15


class TestBlackJack(unittest.TestCase):
    def test_initial_hand_value(self):
        hand1 = Hand(["A", "8"])
        hand2 = Hand(["A", "Q"])
        hand3 = Hand(["A", "10"])
        hand4 = Hand(["2", "7"])

        self.assertEqual(hand1.value(), 19)
        self.assertEqual(hand2.value(), BLACKJACK)
        self.assertEqual(hand3.value(), 21)
        self.assertEqual(hand4.value(), 9)

    def test_ace_is_1(self):
        hand = Hand(["A", "8"])
        hand.add_specific_cards(["A"])
        self.assertEqual(hand.value(), 20)

        hand.add_specific_cards(["A"])
        self.assertEqual(hand.value(), 21)

    def test_all_aces_are_1(self):
        hand = Hand(["A", "8"])
        hand.add_specific_cards(["A", "5"])
        self.assertEqual(hand.value(), 15)

    def test_all_aces_are_1_with_face_card(self):
        hand = Hand(["A", "8"])
        hand.add_specific_cards(["A", "K"])
        self.assertEqual(hand.value(), 20)

    def test_bust_or_not(self):
        hand1 = Hand(["A", "8", "5", "10"])
        hand2 = Hand(["10", "9", "A", "A"])

        self.assertEqual(hand1.value(), 24)
        self.assertEqual(get_is_hand_bust(hand1.value()), True)

        self.assertEqual(hand2.value(), 21)
        self.assertEqual(get_is_hand_bust(hand2.value()), False)

    def test_dealer_wins(self):
        player_losing_hands = [
            Hand(["5", "5", "5", "A"]),
            Hand(["5", "5", "7"]),
            Hand(["A", "9"]),
        ]
        dealer_winning_hands = [
            Hand(["10", "8"]),
            Hand(["5", "5", "A", "7"]),
            Hand(["10", "3", "5", "3"]),
        ]
        test_set = list(zip(player_losing_hands, dealer_winning_hands))

        for player_hand, dealer_hand in test_set:
            self.assertGreater(dealer_hand.value(), player_hand.value())
            self.assertTrue(
                get_does_dealer_win(dealer_hand.value(), player_hand.value())
            )

    def test_player_wins(self): ...

    def test_tie(self): ...


#! Really gotta learn to use pytest library
# * seems less verbose and the use of fixture and mark.parameterize sounds noice!
# import pytest
# from .blackjack import Hand

# # @pytest.fixture
# ...
#
# @pytest.mark.parametrize(
#     "hand",
#     "value()",
#     [
#         (Hand(["A", "8"]), 19),
#         (Hand(["A", "J"]), "BLACKJACK"),
#         (Hand(["A", "10"]), 21),
#         (Hand(["2", "7"]), 9),
#     ],
# )
# def test_dealt_hand_values(hand, value):
#     assert hand.value() == value

# @pytest.mark.parametrize(
#     "num1, num2, expected", [(3, 2, 5), (4, 10, 14), (100, -1, 99)]
# )
# def test_add(num1, num2, expected):
#     assert add(num1, num2) == expected
