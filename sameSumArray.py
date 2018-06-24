"""
Given two integer arrays, find a pair of values (one from each array) that
you can swap to give the two arrays the same sum.
"""

import unittest

class Solution(object):
    """
    Class which implements algorithm
    """
    def sameSumArray(self, array1, array2, fast=True):
        """
        Time complexity:
        O(n) - sum(array1)
        O(n) - sum(array2)
        O(n^2) - finding pair
        O(n^2) + O(2n)
        """
        if fast:
            return self.sameSumArrayFast(array1, array2)

        _sum_array1 = sum(array1)
        _sum_array2 = sum(array2)

        for i in array1:
            for j in array2:
                if (_sum_array1 - i) + j == (_sum_array2 - j) + i:
                    return i, j
        return -1

    def sameSumArrayFast(self, array1, array2):
        """
        Time complexity:
        O(n) - sum(array1)
        O(n) - sum(array2)
        O(n) - finding pair
        O(3n)
        """
        _sum_array1 = sum(array1)
        _sum_array2 = sum(array2)

        target = (_sum_array1 - _sum_array2)//2

        _set_array2 = set(array2)

        for num in array1:
            if num - target in _set_array2:
                return num, num - target

            if num + target in _set_array2:
                return num, num + target

        return -1

class TestSolutionMethods(unittest.TestCase):
    """
    Test for Solution
    """

    def setUp(self):
        self.solution = Solution()

    def test_sameSumArray(self):
        """
        Find a pair of values (one from each array) that
        you can swap to give the two arrays the same sum.
        """
        self.assertEqual(self.solution.sameSumArray([8, 7, 13, -1, 3, -6, 4],
                                                    [-3, 1, 9, 10, -1, 5, 1]), (8, 5))
        self.assertEqual(self.solution.sameSumArray([1, 1, 1, 1],
                                                    [1, 1, 1, 1, 1, 1]), -1)

if __name__ == '__main__':
    unittest.main()
