#!/usr/bin/env python

import unittest

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        nums.sort()
        majority = len(nums) / 3
        k = 1

        idx = len(nums) - 1
        while idx >= 0:
            if idx > 0 and nums[idx - 1] == nums[idx]:
                k += 1
                del nums[idx]
            else:
                if k <= majority:
                    del nums[idx]
                k = 1
            idx -= 1
        return nums

class TestSolution(unittest.TestCase):

    def test_majorityElement(self):
        solution = Solution()
        self.assertEqual(solution.majorityElement([1, 2, 3]), [])
        self.assertEqual(solution.majorityElement([1, 2, 1, 3, 1, 2, 2, 1, 5, 2]), [1, 2])
        self.assertEqual(solution.majorityElement([2, 2]), [2])
        self.assertEqual(solution.majorityElement([5, 5, 5, 6]), [5])
        self.assertEqual(solution.majorityElement([5, 5, 5]), [5])
        self.assertEqual(solution.majorityElement([]), [])

if __name__ == '__main__':
    unittest.main()
