#!/usr/bin/env python

import unittest


class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        ans, curr_sum = 0, 0
        left, right = 0, 0
        idx_map = {}

        for idx in range(n):
            curr_num = nums[idx]
            seen = idx_map.get(curr_num, -1)
            while left <= seen or right - left + 1 > k:
                curr_sum -= nums[left]
                left += 1
            idx_map[curr_num] = idx
            curr_sum += nums[right]
            if right - left + 1 == k:
                ans = max(ans, curr_sum)
            right += 1

        return ans


class TestSolution(unittest.TestCase):
    def test_maximumSubarraySum(self):
        solution = Solution()
        self.assertEqual(solution.maximumSubarraySum([1, 5, 4, 2, 9, 9, 9], 3), 15)


if __name__ == '__main__':
    unittest.main()
