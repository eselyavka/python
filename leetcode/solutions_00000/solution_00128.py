#!/usr/bin/env python

import unittest


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set(nums)

        longest_len = 0

        i = 0
        while i < len(nums):
            if nums[i] - 1 not in s:
                curr_len = 1
                next_num = nums[i] + 1
                while next_num in s:
                    curr_len += 1
                    next_num += 1

                longest_len = max(longest_len, curr_len)
            i += 1

        return longest_len

class TestSolution(unittest.TestCase):

    def test_longestConsecutive(self):
        nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
        solution = Solution()
        self.assertEqual(solution.longestConsecutive(nums), 9)



if __name__ == '__main__':
    unittest.main()
