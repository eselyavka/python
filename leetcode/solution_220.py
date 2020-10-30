#!/usr/bin/env python

import unittest
from sortedcontainers import SortedList


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

        sorted_list = SortedList()
        for i in range(len(nums)):
            if i > k:
                sorted_list.remove(nums[i-k-1])

            pos1 = SortedList.bisect_left(sorted_list, nums[i] - t)
            pos2 = SortedList.bisect_right(sorted_list, nums[i] + t)

            if pos1 != pos2:
                return True

            sorted_list.add(nums[i])

        return False


class TestSolution(unittest.TestCase):
    def test_containsNearbyAlmostDuplicate(self):
        solution = Solution()
        self.assertTrue(solution.containsNearbyAlmostDuplicate([1, 2, 3, 1], 3, 0))


if __name__ == '__main__':
    unittest.main()
