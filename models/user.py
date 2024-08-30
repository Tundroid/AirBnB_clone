#!/usr/bin/python3
"""User module"""

from .base_model import BaseModel


class User(BaseModel):
    """User class implementation"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
