#!/usr/bin/env python

import unittest

class Solution(object):
    def findBuildings(self, heights):
        """
        :type heights: List[int]
        :rtype: List[int]
        """
        if len(heights) == 1:
            return [0]

        r = len(heights) - 2
        res = [r+1]
        max_so_far = heights[-1]

        while r >= 0:
            if heights[r] > heights[r+1] and heights[r] > max_so_far:
                max_so_far = max(max_so_far, heights[r])
                res.append(r)
            r -= 1

        res.sort()

        return res

class TestSolution(unittest.TestCase):
    def test_findBuildings(self):
        solution = Solution()
        self.assertListEqual(solution.findBuildings([4, 2, 3, 1]), [0, 2, 3])


if __name__ == '__main__':
    unittest.main()
