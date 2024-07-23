import unittest

from bagels import secret_number, get_hint


class BagelsTestCases(unittest.TestCase):
    def test_no_repeating_digits(self):
        """
        Secret number has no repeating digits
        """
        n = 0
        nums = []
        while n != 10:
            nums.append(secret_number())
            n += 1
        for num in nums:
            self.assertEqual(len(set(str(num))), 3)

    def test_three_digits(self):
        """
        Secret number has three digits
        """
        self.assertEqual(len(str(secret_number())), 3)

    def test_get_hint(self):
        secret = 701
        guesses = [123, 456, 178, 791, 701]
        result = []
        for guess in guesses:
            result.append(get_hint(secret, guess))

        self.assertListEqual(
            result, ["Pico", "Bagels", "Pico Pico", "Fermi Fermi", "You got it!"]
        )
