#!/usr/bin/env python

import unittest


class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        if rec1[0] >= rec2[2] or rec2[0] >= rec1[2]:
            return False
        if rec1[1] >= rec2[3] or rec2[1] >= rec1[3]:
            return False

        return True


class TestSolution(unittest.TestCase):
    def test_isRectangleOverlap(self):
        solution = Solution()
        self.assertTrue(solution.isRectangleOverlap([0, 0, 2, 2], [1, 1, 3, 3]))
        self.assertFalse(solution.isRectangleOverlap([0, 0, 1, 1], [1, 0, 2, 1]))


if __name__ == '__main__':
    unittest.main()
