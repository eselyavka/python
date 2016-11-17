#!/usr/bin/env python

import sys
import unittest
import mock

sys.path.insert(0, '../')
import decorator_examples as de


def noop(func):
    return func

class TestSpam(unittest.TestCase):
    @mock.patch("decorator_examples.my_dec", return_value=noop)
    @mock.patch("decorator_examples.my_dec2", return_value=noop)
    def test_spam(self, mock_my_dec, mock_my_dec2):
        actual = [de.spam(1,2,3), de.spam('a','b','c')]
        expected = [6, 'abc']
        self.assertListEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
