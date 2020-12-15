#!/usr/bin/env python

import unittest


class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for num in nums:
            idx = abs(num)
            if nums[idx - 1] < 0:
                res.append(idx)
            else:
                nums[idx - 1] *= -1

        return res


class TestSolution(unittest.TestCase):

    def test_findDuplicates(self):
        solution = Solution()
        self.assertListEqual(solution.findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]), [2, 3])
        self.assertListEqual(solution.findDuplicates([1, 4, 5, 1, 3]), [1])


if __name__ == '__main__':
    unittest.main()
