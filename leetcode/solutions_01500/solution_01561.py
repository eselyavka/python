#!/usr/bin/env python

import unittest


class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        piles.sort()
        left, right = 0, len(piles) - 1

        res = 0
        while left <= right:
            _, me, _ = piles[right], piles[right-1], piles[left]
            left += 1
            right -= 2
            res += me

        return res


class TestSolution(unittest.TestCase):
    def test_maxCoins(self):
        solution = Solution()
        self.assertEqual(solution.maxCoins([9, 8, 7, 6, 5, 1, 2, 3, 4]), 18)


if __name__ == '__main__':
    unittest.main()
