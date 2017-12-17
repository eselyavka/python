#!/usr/bin/env python

import unittest

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0

        arr = [1 for _ in range(len(nums))]
        maxans = 1

        for i in range(1, len(nums)):
            maxval = 0
            for j in range(0, i):
                if nums[i] > nums[j]:
                    maxval = max(arr[j], maxval)

            arr[i] = maxval + 1
            maxans = max(maxans, arr[i])

        return maxans

class TestSolution(unittest.TestCase):

    def test_lengthOfLIS(self):
        nums = [10, 9, 2, 5, 3, 7, 101, 18]
        nums1 = [10, 9, 400, 5, 3, 7, 101, 18]
        nums2 = [0]
        nums3 = []
        nums4 = [2, 2]
        nums5 = [-2, -1]
        nums6 = [1, 3, 6, 7, 9, 4, 10, 5, 6]
        nums7 = [2, 15, 3, 7, 8, 6, 18]

        solution = Solution()
        self.assertEqual(solution.lengthOfLIS(nums), 4)
        self.assertEqual(solution.lengthOfLIS(nums1), 3)
        self.assertEqual(solution.lengthOfLIS(nums2), 1)
        self.assertEqual(solution.lengthOfLIS(nums3), 0)
        self.assertEqual(solution.lengthOfLIS(nums4), 1)
        self.assertEqual(solution.lengthOfLIS(nums5), 2)
        self.assertEqual(solution.lengthOfLIS(nums6), 6)
        self.assertEqual(solution.lengthOfLIS(nums7), 5)

if __name__ == '__main__':
    unittest.main()
