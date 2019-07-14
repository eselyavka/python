#!/usr/bin/env python

import unittest


class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        sorted_height, res = sorted(heights), 0
        for i in range(len(sorted_height)):
            if sorted_height[i] != heights[i]:
                res += 1

        return res


class TestSolution(unittest.TestCase):
    def test_heightChecker(self):
        solution = Solution()
        self.assertEqual(solution.heightChecker([1, 1, 4, 2, 1, 3]), 3)


if __name__ == '__main__':
    unittest.main()
