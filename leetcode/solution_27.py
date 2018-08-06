#!/usr/bin/env python

import unittest

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0

        while i < len(nums):
            if nums[i] == val:
                del nums[i]
                continue
            i += 1

        return len(nums)

class TestSolution(unittest.TestCase):
    def test_removeElement(self):
        solution = Solution()
        nums = [3, 2, 2, 3]
        nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
        self.assertEqual(solution.removeElement(nums, 3), 2)
        self.assertListEqual(nums, [2, 2])
        self.assertEqual(solution.removeElement(nums2, 2), 5)
        self.assertListEqual(nums2, [0, 1, 3, 0, 4])

if __name__ == '__main__':
    unittest.main()
