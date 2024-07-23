import unittest
import datetime

from birthday_paradox import (
    matching_birthday,
    readable_birthdays,
    make_readable,
)


class TestBirthdayParadox(unittest.TestCase):
    def test_no_matching_birthdays(self):
        birthdays = [
            datetime.date(1991, 10, 16),
            datetime.date(1990, 11, 16),
            datetime.date(1992, 12, 16),
        ]
        readable = make_readable(birthdays)
        self.assertEqual(matching_birthday(readable), False)

    def test_birthdays_match(self):
        birthdays = [
            datetime.date(1991, 10, 16),
            datetime.date(1990, 10, 16),
            datetime.date(1992, 12, 16),
            datetime.date(1993, 12, 16),
        ]
        readable = make_readable(birthdays)
        self.assertEqual(
            matching_birthday(readable), readable_birthdays(datetime.date(1990, 10, 16))
        )
