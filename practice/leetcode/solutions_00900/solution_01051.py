#!/usr/bin/env python3

"""LeetCode solution 01051."""

import unittest


class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        sorted_height, res = sorted(heights), 0
        for i, height in enumerate(sorted_height):
            if height != heights[i]:
                res += 1

        return res


class TestSolution(unittest.TestCase):
    def test_heightChecker(self):
        solution = Solution()
        self.assertEqual(solution.heightChecker([1, 1, 4, 2, 1, 3]), 3)


if __name__ == '__main__':
    unittest.main()
