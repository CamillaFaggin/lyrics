import unittest
import sys
import os
from main_for_test import get_lyrics


class TestInput(unittest.TestCase):

    # invalid inputs
    def test_wrong_values(self):
        # you should input wrong data
        self.assertEqual(get_lyrics("artist", "song"), None)
    # corner case: empty string

    def test_empty_string(self):
        self.assertEqual(get_lyrics(" ", " "), None)
        self.assertEqual(get_lyrics("Coldplay", " "), None)
        self.assertEqual(get_lyrics(" ", "Yellow"), None)
if __name__ == '__test.py__':
    unittest.get_lyrics()
