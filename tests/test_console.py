#!/usr/bin/python3
"""Console Test Module"""

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """Console test class implementation"""

    def setUp(self):
        self.console_stdout = StringIO()

    def tearDown(self):
        self.console_stdout.close()

    def test_help_show(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("help show")
            self.assertEqual(mock_stdout.getvalue().strip(),
                             "Shows the string representation of an instance")

    # Add more test cases as needed


if __name__ == '__main__':
    unittest.main()
