#!/usr/bin/env python

import unittest

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        i = len(nums) - 1
        while len(nums) != 2:
            if nums[i-1] == nums[i]:
                del nums[i - 1]
                del nums[i - 1]
                i -= 2
            else:
                i -= 1
        return nums

class TestSolution(unittest.TestCase):

    def test_singleNumber(self):
        nums = [1, 2, 1, 3, 2, 5]
        solution = Solution()
        self.assertEqual(solution.singleNumber(nums), [3, 5])

if __name__ == '__main__':
    unittest.main()
