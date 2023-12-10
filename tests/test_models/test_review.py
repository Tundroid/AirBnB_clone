#!/usr/bin/python3
"""Contains tests for review.py"""

import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    """Review class implementation"""

    def __init__(self, place_id="", user_id="", text=""):
        super().__init__()
        self.place_id = place_id
        self.user_id = user_id
        self.text = text

if __name__ == '__main__':
    unittest.main()
