#!/usr/bin/env python

import unittest


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if len(nums) == 1:
            return 0 if target in nums else -1

        def _binary_search(l, r, elem):
            if l > r:
                return -1

            mid = (l+r)//2

            if nums[mid] == elem:
                return mid

            if nums[l] <= nums[mid]:
                if nums[l] <= elem <= nums[mid]:
                    return  _binary_search(l, mid - 1, elem)

                return _binary_search(mid+1, r, elem)

            if  nums[mid] < elem <= nums[r]:
                return _binary_search(mid+1, r, elem)

            return _binary_search(l, mid-1, elem)

        return _binary_search(0, len(nums) - 1, target)


class Solution2(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)

        if n == 1:
            return 0 if target == nums[0] else -1

        pivotal = 0
        for i in range(1, n):
            if nums[i] < nums[i-1]:
                pivotal = i

        if nums[pivotal] == target:
            return pivotal

        def search(left, right):
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid

                if target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            return -1

        if pivotal == 0:
            return search(0, n-1)

        if target < nums[0]:
            return search(pivotal, n-1)

        return search(0, pivotal)


class TestSolution(unittest.TestCase):
    def test_search(self):
        solution = Solution()
        self.assertEqual(solution.search([0, 1, 2, 4, 5, 6, 7], 4), 3)
        self.assertEqual(solution.search([4, 5, 6, 7, 0, 1, 2], 0), 4)
        self.assertEqual(solution.search([4, 5, 6, 7, 0, 1, 2], 3), -1)
        self.assertEqual(solution.search([5, 6, 7, 0, 1, 2, 4], 5), 0)
        self.assertEqual(solution.search([3, 5, 1], 3), 0)
        self.assertEqual(solution.search([5], 3), -1)
        self.assertEqual(solution.search([5], 5), 0)
        self.assertEqual(solution.search([2, 1], 1), 1)

        solution = Solution2()
        self.assertEqual(solution.search([0, 1, 2, 4, 5, 6, 7], 4), 3)
        self.assertEqual(solution.search([4, 5, 6, 7, 0, 1, 2], 0), 4)
        self.assertEqual(solution.search([4, 5, 6, 7, 0, 1, 2], 3), -1)
        self.assertEqual(solution.search([5, 6, 7, 0, 1, 2, 4], 5), 0)
        self.assertEqual(solution.search([3, 5, 1], 3), 0)
        self.assertEqual(solution.search([5], 3), -1)
        self.assertEqual(solution.search([5], 5), 0)
        self.assertEqual(solution.search([2, 1], 1), 1)

if __name__ == '__main__':
    unittest.main()
