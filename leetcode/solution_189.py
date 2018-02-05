#!/usr/bin/env python

import unittest

class Solution(object):
    def rotate_temp_arr(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        arr = [None for _ in nums]
        for i in range(len(nums)):
            arr[(i+k)%len(nums)] = nums[i]

        for i in range(len(nums)):
            nums[i] = arr[i]

    def _reverse(self, nums, start, end):
        while start < end:
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp
            start += 1
            end -= 1

    def rotate_reverse(self, nums, k):
        n = len(nums)
        k %= n
        self._reverse(nums, 0, n - 1)
        self._reverse(nums, 0, k - 1)
        self._reverse(nums, k, n - 1)

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        self.rotate_reverse(nums, k)

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_rotate(self):
        arr = [1, 2, 3, 4, 5, 6, 7]
        self.solution.rotate(arr, 3)
        self.assertEqual(arr, [5, 6, 7, 1, 2, 3, 4])
        arr2 = [1, 2]
        self.solution.rotate(arr2, 0)
        self.assertEqual(arr2, [1, 2])
        self.solution.rotate(arr2, 1)
        self.assertEqual(arr2, [2, 1])
        arr3 = [1, 2]
        self.solution.rotate(arr3, 3)
        self.assertEqual(arr3, [2, 1])

    def test_rotate_temp_arr(self):
        arr = [1, 2, 3, 4, 5, 6, 7]
        self.solution.rotate_temp_arr(arr, 3)
        self.assertEqual(arr, [5, 6, 7, 1, 2, 3, 4])
        arr2 = [1, 2]
        self.solution.rotate_temp_arr(arr2, 0)
        self.assertEqual(arr2, [1, 2])
        self.solution.rotate_temp_arr(arr2, 1)
        self.assertEqual(arr2, [2, 1])
        arr3 = [1, 2]
        self.solution.rotate_temp_arr(arr3, 3)
        self.assertEqual(arr3, [2, 1])

    def test_rotate_reverse(self):
        arr = [1, 2, 3, 4, 5, 6, 7]
        self.solution.rotate_temp_arr(arr, 3)
        self.assertEqual(arr, [5, 6, 7, 1, 2, 3, 4])
        arr2 = [1, 2]
        self.solution.rotate_temp_arr(arr2, 0)
        self.assertEqual(arr2, [1, 2])
        self.solution.rotate_temp_arr(arr2, 1)
        self.assertEqual(arr2, [2, 1])
        arr3 = [1, 2]
        self.solution.rotate_temp_arr(arr3, 3)
        self.assertEqual(arr3, [2, 1])

if __name__ == '__main__':
    unittest.main()
