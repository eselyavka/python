#!/usr/bin/env python

import unittest

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        _max = 0

        while left <= right:
            if height[right] >= height[left]:
                _max = max(_max, min(height[left], height[right]) * (right - left))
                left += 1
            else:
                _max = max(_max, min(height[left], height[right]) * (right - left))
                right -= 1

        return _max

class TestSolution(unittest.TestCase):

    def test_maxArea(self):
        solution = Solution()

        self.assertEqual(solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)
        self.assertEqual(solution.maxArea([1, 5, 4, 3]), 6)
        self.assertEqual(solution.maxArea([3, 1, 2, 4, 5]), 12)

if __name__ == '__main__':
    unittest.main()
