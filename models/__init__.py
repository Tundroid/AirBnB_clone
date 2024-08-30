#!/usr/bin/python3
"""Initialization of AirBnB console"""

from .engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
