#!/usr/bin/env python

import unittest

class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        snums = sorted(nums)
        s, e = 0, len(nums) - 1

        while s < len(nums) - 1:
            if nums[s] != snums[s]:
                break
            s += 1

        if s == len(nums) - 1:
            return 0

        while e > 0:
            if nums[e] != snums[e]:
                break
            e -= 1

        return (e - s) + 1

class TestSolution(unittest.TestCase):

    def test_findUnsortedSubarray(self):
        solution = Solution()

        self.assertEqual(solution.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]), 5)
        self.assertEqual(solution.findUnsortedSubarray([1, 2, 3, 4]), 0)
        self.assertEqual(solution.findUnsortedSubarray([1, 3, 2, 2, 2]), 4)
        self.assertEqual(solution.findUnsortedSubarray([1, 2, 3, 3, 3]), 0)
        self.assertEqual(solution.findUnsortedSubarray([1, 3, 2, 3, 3]), 2)

if __name__ == '__main__':
    unittest.main()
