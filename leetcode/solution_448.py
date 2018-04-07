#!/usr/bin/env python

import unittest

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s = set(nums)
        res = []
        for i in range(1, len(nums)+1):
            if i not in s:
                res.append(i)

        return res
class TestSolution(unittest.TestCase):

    def test_findDisappearedNumbers(self):
        solution = Solution()

        self.assertEqual(solution.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]), [5, 6])
        self.assertEqual(solution.findDisappearedNumbers([1, 3]), [2])

if __name__ == '__main__':
    unittest.main()
