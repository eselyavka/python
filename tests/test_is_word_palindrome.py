#!/usr/bin/env python3

"""Unit tests for is_word_palindrome.py."""

from pathlib import Path
import unittest

from src.is_word_palindrome import solution, solution_reversed, solution_slice

class TestCountFunctions(unittest.TestCase):
    """Unit tests for palindrome helpers."""

    def setUp(self):
        self.lines = Path(__file__).with_name('palindromes.txt').read_text().splitlines()

    def test_solutions(self):
        for sol in [solution, solution_reversed, solution_slice]:
            self.assertTrue(all(sol(word) for word in self.lines))
            self.assertFalse(sol('notapalindrom'))
            self.assertFalse(sol('definitelynotpalindrome'))
            self.assertFalse(sol("shouldn'tpasseither"))

if __name__ == '__main__':
    unittest.main()
