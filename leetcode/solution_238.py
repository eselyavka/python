#!/usr/bin/env python

import unittest


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        p = 1
        for n in nums:
            res.append(p)
            p = p*n

        p = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] = res[i] * p
            p = p*nums[i]

        return res

    def productExceptSelf2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left, right = [], []
        L, R = 1, 1

        for num in nums:
            left.append(L)
            L = L * num

        for i in range(len(nums) - 1, -1, -1):
            right.append(R)
            R = R * nums[i]

        res = []
        j = len(right) - 1
        for num in left:
            res.append(num * right[j])
            j -= 1

        return res


class TestSolution(unittest.TestCase):

    def test_productExceptSelf(self):
        nums = [1, 2, 3, 4]
        nums2 = [0, 0]
        nums3 = [0, 1, 20]
        solution = Solution()
        self.assertEqual(solution.productExceptSelf(nums), [24, 12, 8, 6])
        self.assertEqual(solution.productExceptSelf(nums2), [0, 0])
        self.assertEqual(solution.productExceptSelf(nums3), [20, 0, 0])

        self.assertEqual(solution.productExceptSelf2(nums), [24, 12, 8, 6])
        self.assertEqual(solution.productExceptSelf2(nums2), [0, 0])
        self.assertEqual(solution.productExceptSelf2(nums3), [20, 0, 0])


if __name__ == '__main__':
    unittest.main()
