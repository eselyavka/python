#!/usr/bin/env python

import unittest


class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def binary_search(nums, l, r):
            if l > r:
                return -1

            if l == r:
                return nums[l]

            mid = (l + r) // 2

            if mid % 2 == 0:
                if nums[mid] == nums[mid + 1]:
                    return binary_search(nums, mid + 2, r)
                return binary_search(nums, l, mid)

            if nums[mid] == nums[mid - 1]:
                return binary_search(nums, mid + 1, r)

            return binary_search(nums, l, mid - 1)

        return binary_search(nums, 0, len(nums) - 1)


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
