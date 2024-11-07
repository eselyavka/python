#!/usr/bin/env python

import unittest


class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {0: 0}
        count = 0
        max_ = 0

        for idx, num in enumerate(nums, start=1):
            if num:
                count += 1
            else:
                count -= 1

            if count in d:
                max_ = max(max_, idx - d[count])
            else:
                d[count] = idx

        return max_


class TestSolution(unittest.TestCase):
    def test_findMaxLength(self):
        solution = Solution()
        self.assertEqual(solution.findMaxLength([0, 1, 1, 0, 1, 1, 1, 0]), 4)
        self.assertEqual(solution.findMaxLength([0, 1]), 2)
        self.assertEqual(solution.findMaxLength([0, 1, 0]), 2)


if __name__ == '__main__':
    unittest.main()
