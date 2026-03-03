#!/usr/bin/env python3

"""LeetCode solution 00531."""

import unittest

class Solution(object):
    def findLonelyPixel(self, picture):
        """
        :type picture: List[List[str]]
        :rtype: int
        """
        cnt = 0
        for i, row in enumerate(picture):
            for j, element in enumerate(row):
                if element == 'B':
                    if (all(value == 'W' for x, value in enumerate(row) if x != j) and
                            all(row[j] == 'W' for x, row in enumerate(picture) if x != i)):
                        cnt += 1
        return cnt

class TestSolution(unittest.TestCase):

    def test_findLonelyPixel(self):
        picture = [['W', 'W', 'B'],
                   ['W', 'B', 'W'],
                   ['B', 'W', 'W']]
        picture2 = [['B', 'W', 'B'],
                    ['W', 'B', 'W'],
                    ['B', 'W', 'W']]
        solution = Solution()
        self.assertEqual(solution.findLonelyPixel(picture), 3)
        self.assertEqual(solution.findLonelyPixel(picture2), 1)

if __name__ == '__main__':
    unittest.main()
