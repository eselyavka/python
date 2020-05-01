#!/usr/bin/env python

import unittest
import heapq


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return sorted(nums)[-k]


class Solution2(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        invert = [x*-1 for x in nums]
        heapq.heapify(invert)

        res = None
        while k:
            res = heapq.heappop(invert)
            k -= 1

        return res * -1


class TestSolution(unittest.TestCase):

    def test_findKthLargest(self):
        nums = [3, 2, 1, 5, 6, 4]
        solution = Solution()
        self.assertEqual(solution.findKthLargest(nums, 2), 5)

        solution2 = Solution2()
        self.assertEqual(solution2.findKthLargest(nums, 2), 5)


if __name__ == '__main__':
    unittest.main()
