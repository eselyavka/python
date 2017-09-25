#!/usr/bin/env python

import unittest
import math

class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """

        unique = set(candies)

        if len(unique) > len(candies)/2:
            return len(candies)/2

        return len(unique)

class TestSolution(unittest.TestCase):

    def test_distributeCandies(self):
        solution = Solution()
        arr1 = [1,1,2,2,3,3]
        arr2 = [1,1,2,3]
        arr3 = [1000,1000,2,1,2,5,3,1]
        arr4 = [1,1,1,1,2,2,2,3,3,3]
        arr5 = [1000,1,1,1]
        arr6 = [0,0,14,0,10,0,0,0]
        self.assertListEqual([solution.distributeCandies(arr) for arr in [arr1, arr2, arr3, arr4, arr5, arr6]], [3, 2, 4, 3, 2, 3])

if __name__ == '__main__':
    unittest.main()
