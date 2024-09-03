#!/usr/bin/python3
"""Initialization of AirBnB"""

from .engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
