#!/usr/bin/env python

import unittest


class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return 1

        cnt = 1
        buf = 1
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                buf += 1
            else:
                cnt = max(cnt, buf)
                buf = 1

        return max(cnt, buf)

    def findLengthOfLCIS2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0

        if nums == 1:
            return 1

        n = len(nums)
        i, length_so_far = 1, 1
        max_ = 0
        while i < n:
            if nums[i-1] < nums[i]:
                length_so_far += 1
            else:
                max_ = max(max_, length_so_far)
                length_so_far = 1
            i += 1

        return max(max_, length_so_far)


class TestSolution(unittest.TestCase):
    def test_findLengthOfLCIS(self):
        solution = Solution()
        self.assertEqual(solution.findLengthOfLCIS([1, 3, 5, 4, 7]), 3)
        self.assertEqual(solution.findLengthOfLCIS([2, 2, 2, 2, 2]), 1)
        self.assertEqual(solution.findLengthOfLCIS([1, 3, 2, 1, 7]), 2)
        self.assertEqual(solution.findLengthOfLCIS([1, 3, 5, 7]), 4)
        self.assertEqual(solution.findLengthOfLCIS([1, 3, 5, 4, 2, 3, 4, 5]), 4)

        self.assertEqual(solution.findLengthOfLCIS2([1, 3, 5, 4, 7]), 3)
        self.assertEqual(solution.findLengthOfLCIS2([2, 2, 2, 2, 2]), 1)
        self.assertEqual(solution.findLengthOfLCIS2([1, 3, 2, 1, 7]), 2)
        self.assertEqual(solution.findLengthOfLCIS2([1, 3, 5, 7]), 4)
        self.assertEqual(solution.findLengthOfLCIS2([1, 3, 5, 4, 2, 3, 4, 5]), 4)


if __name__ == '__main__':
    unittest.main()
