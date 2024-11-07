#!/usr/bin/env python

import unittest

class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        #TODO (eseliavka), improve time complexity from O(logN) to O(N)
        res = [a*x**2 + b*x +c for x in nums]
        res.sort()

        return res

class TestSolution(unittest.TestCase):
    def test_sortTransformedArray(self):
        solution = Solution()
        self.assertListEqual(solution.sortTransformedArray([-4, -2, 2, 4],
                                                           *(1, 3, 5)),
                             [3, 9, 15, 33])
        self.assertListEqual(solution.sortTransformedArray([-4, -2, 2, 4],
                                                           *(-1, 3, 5)),
                             [-23, -5, 1, 7])

if __name__ == '__main__':
    unittest.main()
