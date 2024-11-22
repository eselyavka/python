#!/usr/bin/env python

import unittest
from collections import defaultdict


class Solution(object):
    def maxEqualRowsAfterFlips(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        ans = 0
        rows_hash = defaultdict(int)
        for row in matrix:
            if len(set(row)) == 1:
                ans += 1
            rows_hash[tuple(row)] += 1

        for row in matrix:
            xor = tuple([0 if x == 1 else 1 for x in row])
            ans = max(ans, rows_hash[tuple(row)] + rows_hash[xor])
        return ans


class TestSolution(unittest.TestCase):
    def test_maxEqualRowsAfterFlips(self):
        solution = Solution()
        self.assertEqual(solution.maxEqualRowsAfterFlips([[0, 0, 0], [0, 0, 1], [1, 1, 0]]), 2)


if __name__ == '__main__':
    unittest.main()
