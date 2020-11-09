#!/usr/bin/env python

import unittest


class Solution(object):
    def dieSimulator(self, n, rollMax):
        """
        :type n: int
        :type rollMax: List[int]
        :rtype: int
        """
        m = len(rollMax)

        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

        dp[0][m] = 1

        for j in range(m):
            dp[1][j] = 1
        dp[1][m] = 6

        for i in range(2, n+1):
            for j in range(m):
                for k in range(1, rollMax[j]+1):
                    if i - k < 0:
                        break
                    dp[i][j] += dp[i-k][m] - dp[i-k][j]
            dp[i][m] = sum(dp[i])

        return dp[n][m] % (10**9 + 7)


class TestSolution(unittest.TestCase):
    def test_dieSimulator(self):
        solution = Solution()
        self.assertEqual(solution.dieSimulator(2, [1, 1, 2, 2, 2, 3]), 34)


if __name__ == '__main__':
    unittest.main()
