import unittest

from .blackjack import Hand

#! TEST CASES
#! A, 8 --> 11 + 8 == 19
#! A, 8, A --> 11 + 8 + 1 == 20
#! A, 8, A, A --> 11 + 8 + 1 + 1 == 21
#! A, 8, A, 5 --> 1 + 8 + 1 + 5 == 15


class TestBlackJack(unittest.TestCase):
    def test_initial_hand_value(self):
        hand1 = Hand(["A", "8"])
        hand2 = Hand(["A", "J"])
        hand3 = Hand(["A", "10"])
        hand4 = Hand(["2", "7"])

        self.assertEqual(hand1.value(), 19)
        self.assertEqual(hand2.value(), "BLACKJACK")
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


#! Really gotta learn to use pytest library
# * seems less verbose and the use of fixture and mark.parameterize sounds noice!
# import pytest
# from .blackjack import Hand

# # @pytest.fixture
# ...
#
# @pytest.mark.parametrize(
#     "hand",
#     "value",
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
