#!/usr/bin/env python

import unittest

class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(0, len(nums), 2):
            idx1 = i+1 if i < len(nums) - 1 else i - 1
            idx2 = i-1 if i > 0 else i + 1
            if nums[i] != nums[idx1] and nums[i] != nums[idx2]:
                return nums[i]

class TestSolution(unittest.TestCase):

    def test_singleNonDuplicate(self):
        arr = [1, 1, 3, 5, 5]
        arr2 = [3, 3, 7, 7, 10, 11, 11]
        arr3 = [1, 1, 2, 3, 3, 4, 4, 8, 8]
        arr4 = [1, 1, 2]
        arr5 = [2, 3, 3]
        solution = Solution()
        self.assertEqual(solution.singleNonDuplicate(arr), 3)
        self.assertEqual(solution.singleNonDuplicate(arr2), 10)
        self.assertEqual(solution.singleNonDuplicate(arr3), 2)
        self.assertEqual(solution.singleNonDuplicate(arr4), 2)
        self.assertEqual(solution.singleNonDuplicate(arr5), 2)

if __name__ == '__main__':
    unittest.main()
