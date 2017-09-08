#!/usr/bin/env python
""" Unit test for is_word_polindrome.py """

import unittest
import sys

sys.path.insert(0, '../')
from is_word_palindrome import solution, solution_reversed, solution_slice

class TestCountFunctions(unittest.TestCase):
    """ Unit test for is_word_polindrome.py """

    def setUp(self):
        self.lines = open('palindromes.txt', 'r').readlines()

    def test_solutions(self):
        for sol in [solution, solution_reversed, solution_slice]:
            self.assertTrue(all([sol(word) for word in self.lines]))
            self.assertFalse(sol('notapalindrom'))
            self.assertFalse(sol('definitelynotpalindrome'))
            self.assertFalse(sol("shouldn'tpasseither"))

if __name__ == '__main__':
    unittest.main()
