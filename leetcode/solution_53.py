#!/usr/bin/env python

import unittest


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        ans = float("-inf")
        acc = 0
        for num in nums:
            acc += num
            ans = max(ans, acc)
            acc = max(acc, 0)

        return ans


class TestSolution(unittest.TestCase):

    def test_singleNumber(self):
        nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        nums2 = [-1]
        solution = Solution()
        self.assertEqual(solution.maxSubArray(nums), 6)
        self.assertEqual(solution.maxSubArray(nums2), -1)


if __name__ == '__main__':
    unittest.main()
