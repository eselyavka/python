#!/usr/bin/env python

import unittest

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """

        i = 0

        while n:
            i += 1
            n -= i
            if i >= n:
                break

        return i

class TestSolution(unittest.TestCase):
    def test_arrangeCoins(self):
        solution = Solution()
        self.assertEqual(solution.arrangeCoins(5), 2)
        self.assertEqual(solution.arrangeCoins(8), 3)

if __name__ == '__main__':
    unittest.main()
