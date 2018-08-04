#!/usr/bin/env python

import unittest

class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if not n:
            return 0

        if n == 1:
            return k

        dp = [0] * n
        dp[0] = k

        same, diff = 0, k
        for i in range(1, n):
            same = diff
            diff = dp[i-1] * (k-1)
            dp[i] = same + diff

        return dp[n-1]

class TestSolution(unittest.TestCase):
    def test_numWays(self):
        solution = Solution()
        self.assertEqual(solution.numWays(3, 2), 6)
        self.assertEqual(solution.numWays(2, 4), 16)
        self.assertEqual(solution.numWays(0, 0), 0)

if __name__ == '__main__':
    unittest.main()
