#!/usr/bin/env python

import unittest


class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        i = len(arr) - 1
        while i >= 0:
            if arr[i] == 0:
                arr.pop()
                arr.insert(i, 0)
            i -= 1


class TestSolution(unittest.TestCase):
    def test_duplicateZeros(self):
        arr = [1, 0, 2, 3, 0, 4, 5, 0]
        solution = Solution()
        solution.duplicateZeros(arr)
        self.assertListEqual(arr, [1, 0, 0, 2, 3, 0, 0, 4])
        arr = [0]
        solution.duplicateZeros(arr)
        self.assertListEqual(arr, [0])
        arr = [1, 2, 3]
        solution.duplicateZeros(arr)
        self.assertListEqual(arr, [1, 2, 3])
        arr = [0, 1]
        solution.duplicateZeros(arr)
        self.assertListEqual(arr, [0, 0])
        arr = [1, 0]
        solution.duplicateZeros(arr)
        self.assertListEqual(arr, [1, 0])

if __name__ == '__main__':
    unittest.main()
