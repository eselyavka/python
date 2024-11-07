#!/usr/bin/env python

import unittest

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        local_cnt, i = 0, 0
        while i < len(nums) - 1:
            if nums[i] == nums[i+1]:
                local_cnt += 1
                if local_cnt >= 2:
                    del nums[i]
                    continue
            else:
                local_cnt = 0
            i += 1

        return len(nums)

class TestSolution(unittest.TestCase):
    def test_removeDuplicates(self):
        solution = Solution()
        nums = [1, 1, 1, 2, 2, 3]
        nums2 = [0, 0, 1, 1, 1, 1, 2, 3, 3]
        nums3 = [1, 1, 1]
        nums4 = [1, 1, 1, 0, 0, 0, 4, 5, 6, 3, 3, 3]
        self.assertEqual(solution.removeDuplicates(nums), 5)
        self.assertEqual(solution.removeDuplicates(nums2), 7)
        self.assertEqual(solution.removeDuplicates(nums3), 2)
        self.assertEqual(solution.removeDuplicates(nums4), 9)
        self.assertEqual(nums, [1, 1, 2, 2, 3])
        self.assertEqual(nums2, [0, 0, 1, 1, 2, 3, 3])
        self.assertEqual(nums3, [1, 1])
        self.assertEqual(nums4, [1, 1, 0, 0, 4, 5, 6, 3, 3])

if __name__ == '__main__':
    unittest.main()
