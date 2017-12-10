#!/usr/bin/env python

import unittest

class Solution(object):

    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """

        res = float('+inf')
        length = 0
        ss = 0

        for i, num in enumerate(nums):
            ss += num
            while ss >= s:
                res = min(res, i+1 - length)
                ss -= nums[length]
                length += 1

        return res if res != float('+inf') else 0

class TestSolution(unittest.TestCase):

    def test_minSubArrayLen(self):
        nums = [2, 3, 1, 2, 4, 3]
        nums1 = [4, 5, 8]
        nums2 = [1, 0, 1]
        nums3 = [1, 2, 3, 4, 5]
        nums4 = [12, 28, 83, 4, 25, 26, 25, 2, 25, 25, 25, 12]

        solution = Solution()
        self.assertEqual(solution.minSubArrayLen(7, nums), 2)
        self.assertEqual(solution.minSubArrayLen(8, nums1), 1)
        self.assertEqual(solution.minSubArrayLen(3, nums2), 0)
        self.assertEqual(solution.minSubArrayLen(11, nums3), 3)
        self.assertEqual(solution.minSubArrayLen(213, nums4), 8)

if __name__ == '__main__':
    unittest.main()
