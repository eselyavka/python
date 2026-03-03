#!/usr/bin/env python3

"""Tests for decorator examples."""

import unittest
from unittest import mock

from src import decorator_examples as de

class TestSpam(unittest.TestCase):
    @mock.patch("builtins.print")
    def test_spam(self, mock_print):
        actual = [de.spam(1, 2, 3), de.spam('a', 'b', 'c')]
        expected = [6, 'abc']
        self.assertListEqual(actual, expected)
        self.assertEqual(mock_print.call_count, 4)

if __name__ == '__main__':
    unittest.main()
