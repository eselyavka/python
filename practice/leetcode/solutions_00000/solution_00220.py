#!/usr/bin/env python3

"""LeetCode solution 00220."""

import unittest
from bisect import bisect_left, bisect_right, insort


class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if not nums:
            return 0

        sorted_list = []
        for i, num in enumerate(nums):
            if i > k:
                sorted_list.pop(bisect_left(sorted_list, nums[i-k-1]))

            pos1 = bisect_left(sorted_list, num - t)
            pos2 = bisect_right(sorted_list, num + t)

            if pos1 != pos2:
                return True

            insort(sorted_list, num)

        return False


class TestSolution(unittest.TestCase):
    def test_containsNearbyAlmostDuplicate(self):
        solution = Solution()
        self.assertTrue(solution.containsNearbyAlmostDuplicate([1, 2, 3, 1], 3, 0))


if __name__ == '__main__':
    unittest.main()
