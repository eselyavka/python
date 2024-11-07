#!/usr/bin/env python

import unittest

class Solution(object):

    @staticmethod
    def is_greater(i, nums_len, nums):
        if i == nums_len - 1:
            return -1

        num = -1
        for j in range(i, nums_len):
            if nums[j] > nums[i]:
                num = nums[j]
                break

        return num


    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """

        res = list()

        for element in findNums:
            for i in range(len(nums)):
                if nums[i] == element:
                    res.append(Solution.is_greater(i, len(nums), nums))
        return res

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.dataset1 = [4, 1, 2], [1, 3, 4, 2]
        self.dataset2 = [2, 4], [1, 2, 3, 4]
        self.dataset3 = [1, 3, 5, 2, 4], [6, 5, 4, 3, 2, 1, 7]

    def test_matrixReshape(self):
        solution = Solution()
        self.assertEqual(solution.nextGreaterElement(*self.dataset1), [-1, 3, -1])
        self.assertEqual(solution.nextGreaterElement(*self.dataset2), [3, -1])
        self.assertEqual(solution.nextGreaterElement(*self.dataset3), [7, 7, 7, 7, 7])

if __name__ == '__main__':
    unittest.main()
