#!/usr/bin/python3
"""Review module"""

from .base_model import BaseModel


class Review(BaseModel):
    """Review class implementation"""

    place_id = ""
    user_id = ""
    text = ""
