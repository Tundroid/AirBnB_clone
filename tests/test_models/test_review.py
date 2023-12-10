#!/usr/bin/python3
"""Contains tests for review.py"""

import unittest
from models.base_model import BaseModel

class Review(BaseModel):
    """Review class implementation"""

    def __init__(self, place_id="", user_id="", text=""):
        super().__init__()
        self.place_id = place_id
        self.user_id = user_id
        self.text = text

if __name__ == '__main__':
    unittest.main()
