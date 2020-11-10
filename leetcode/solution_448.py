#!/usr/bin/env python

import unittest


class Solution2(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)

        for i in range(n):
            idx = abs(nums[i]) - 1

            if nums[idx] > 0:
                nums[idx] = -nums[idx]

        res = []

        for i in range(n):
            if nums[i] > 0:
                res.append(i + 1)

        return res


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
        self.assertEqual(solution.findDisappearedNumbers([1, 3, 3]), [2])

        solution2 = Solution2()

        self.assertEqual(solution2.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]), [5, 6])
        self.assertEqual(solution2.findDisappearedNumbers([1, 3, 3]), [2])


if __name__ == '__main__':
    unittest.main()
