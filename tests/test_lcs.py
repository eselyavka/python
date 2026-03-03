#!/usr/bin/env python3

"""Unit tests for lcs.py."""

import unittest

from src.lcs import lcs, recursion_lcs

class TestSparseVector(unittest.TestCase):
    """Unit tests for lcs.py."""

    def setUp(self):
        self.seq1 = 'ABCDGH'
        self.seq2 = 'AEDFHR'
        self.seq3 = 'AGGTAB'
        self.seq4 = 'GXTXAYB'

    def test_lcs(self):
        self.assertEqual(lcs(self.seq1, self.seq2), 3)
        self.assertEqual(lcs(self.seq3, self.seq4), 4)

    def test_recursion_lcs(self):
        self.assertEqual(recursion_lcs(self.seq1, self.seq2, len(self.seq1), len(self.seq2)), 3)
        self.assertEqual(recursion_lcs(self.seq3, self.seq4, len(self.seq3), len(self.seq4)), 4)

if __name__ == '__main__':
    unittest.main()
