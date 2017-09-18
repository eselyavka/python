#!/usr/bin/env python
""" Unit test for lcs.py """

import unittest
import sys

sys.path.insert(0, '../')
from lcs import lcs, recursion_lcs

class TestSparseVector(unittest.TestCase):
    """ Unit test for sparse_vector.py """

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
