#!/usr/bin/env python

import unittest


class Solution(object):
    def _fib(self, n):
        a = 0
        b = 1

        if n == 0:
            return a
        if n == 1:
            return b

        for _ in range(2, n+1):
            c = a + b
            a = b
            b = c

        return b

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        return self._fib(n+1)


class Solution2(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return n

        dp = [0] * n
        dp[0], dp[1] = 1, 1

        for i in range(1, n):
            j = 1
            while j <= 2 and j <= i:
                dp[i] += dp[i-j]
                j += 1

        return dp[n-1]


class TestSolution(unittest.TestCase):

    def test_climbStairs(self):
        solution = Solution()

        self.assertEqual(solution.climbStairs(2), 2)
        self.assertEqual(solution.climbStairs(3), 3)

        solution2 = Solution2()
        self.assertEqual(solution2.climbStairs(4), 5)


if __name__ == '__main__':
    unittest.main()
