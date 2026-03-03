#!/usr/bin/env python3

"""LeetCode solution 00027."""

import unittest


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        k = 0
        for num in nums:
            if num != val:
                nums[k] = num
                k += 1

        return k


class TestSolution(unittest.TestCase):
    def test_removeElement(self):
        solution = Solution()
        nums = [3, 2, 2, 3]
        nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
        self.assertEqual(solution.removeElement(nums, 3), 2)
        self.assertEqual(solution.removeElement(nums2, 2), 5)


if __name__ == '__main__':
    unittest.main()
