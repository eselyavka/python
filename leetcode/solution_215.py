#!/usr/bin/env python

import unittest

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return sorted(nums)[-k]

class TestSolution(unittest.TestCase):

    def test_findKthLargest(self):
        nums = [3, 2, 1, 5, 6, 4]
        solution = Solution()
        self.assertEqual(solution.findKthLargest(nums, 2), 5)

if __name__ == '__main__':
    unittest.main()
