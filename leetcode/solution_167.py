#!/usr/bin/env python

import unittest

class Solution(object):
    def binary_search(self, arr, number):
        i = 0
        j = len(arr) - 1

        while i <= j:
            mid = (i+j)//2
            if arr[mid] == number:
                return mid
            elif number > arr[mid]:
                i = mid + 1
            else:
                j = mid - 1

        return -1

    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = set()

        for i, number in enumerate(numbers):
            diff = target - number
            idx = self.binary_search(numbers, diff)
            if idx != -1 and idx != i:
                res.add(i+1)
                res.add(idx+1)

        return sorted(list(res))

class TestSolution(unittest.TestCase):

    def test_twoSum(self):
        solution = Solution()
        self.assertEqual(solution.twoSum([2, 7, 11, 15], 9), [1, 2])
        self.assertEqual(solution.twoSum([2, 3, 4], 6), [1, 3])

if __name__ == '__main__':
    unittest.main()
