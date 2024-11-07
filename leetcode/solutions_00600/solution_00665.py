#!/usr/bin/env python

import unittest

class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        cnt = 0
        idx = None
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                cnt += 1
                idx = i

        if cnt == 0:
            return True
        elif cnt > 1:
            return False

        if idx == 0:
            return True
        elif idx == len(nums) - 2:
            return True

        return nums[idx - 1] <= nums[idx+1] or nums[idx + 1] <= nums[idx] <= nums[idx+2]

class TestSolution(unittest.TestCase):

    def test_checkPossibility(self):
        solution = Solution()
        self.assertTrue(solution.checkPossibility([4, 2, 3]))
        self.assertFalse(solution.checkPossibility([4, 2, 1]))
        self.assertFalse(solution.checkPossibility([3, 4, 2, 3]))
        self.assertTrue(solution.checkPossibility([2, 3, 3, 2, 4]))
        self.assertTrue(solution.checkPossibility([-1, 4, 2, 3]))

if __name__ == '__main__':
    unittest.main()
