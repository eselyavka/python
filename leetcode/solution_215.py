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
        if not nums:
            return 0

        if k == 1:
            return max(nums)

        return heapq.nlargest(k, nums)[-1]


class Solution3(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        def quickSelect(l, r, k):
            pivot, p = nums[r], l

            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1

            nums[p], nums[r] = nums[r], nums[p]

            if k < p:
                return quickSelect(l, p - 1, k)

            if k > p:
                return quickSelect(p + 1, r, k)

            return nums[p]

        return quickSelect(0, len(nums) - 1, len(nums) - k)


class TestSolution(unittest.TestCase):

    def test_findKthLargest(self):
        nums = [3, 2, 1, 5, 6, 4]
        solution = Solution()
        self.assertEqual(solution.findKthLargest(nums, 2), 5)

        solution2 = Solution2()
        self.assertEqual(solution2.findKthLargest(nums, 2), 5)

        solution3 = Solution3()
        self.assertEqual(solution3.findKthLargest(nums, 2), 5)


if __name__ == '__main__':
    unittest.main()
