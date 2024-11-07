#!/usr/bin/env python

import unittest

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()

        n = len(nums)
        res = set()
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = n - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == 0:
                    res.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif s < 0:
                    l += 1
                else:
                    r -= 1

        return [list(x) for x in res]


class Solution2(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 3:
            return [nums] if sum(nums) == 0 else []

        res = set()
        for i in range(len(nums)-1):
            s = set()
            for j in range(i+1, len(nums)):
                sum_ = -nums[i] - nums[j]
                if sum_ in s:
                    res.add(tuple(sorted((nums[i],nums[j],sum_))))
                s.add(nums[j])

        return [list(x) for x in res]


def nestedListEqual(nestedList1, nestedList2):
    sortedNestedList1 = [sorted(lst) for lst in nestedList1]
    sortedNestedList2 = [sorted(lst) for lst in nestedList2]

    for lst1 in sortedNestedList1:
        equal = False
        for lst2 in sortedNestedList2:
            if lst1 == lst2:
                equal = True

        if not equal:
            return False

    return True

class TestSolution(unittest.TestCase):

    def test_threeSum(self):
        solution = Solution()
        solution2 = Solution2()

        self.assertTrue(nestedListEqual(solution.threeSum([-1, 0, 1, 2, -1, -4]),
                         [[-1, -1, 2], [-1, 0, 1]]))
        self.assertEqual(solution.threeSum([1, 1, -2]), [[-2, 1, 1]])
        self.assertEqual(solution.threeSum([0, 0, 0, 0]), [[0, 0, 0]])
        self.assertEqual(solution.threeSum([-2, 0, 0, 2, 2]), [[-2, 0, 2]])

        self.assertTrue(nestedListEqual(solution2.threeSum([-1, 0, 1, 2, -1, -4]),
                         [[-1, -1, 2], [-1, 0, 1]]))
        self.assertTrue(nestedListEqual(solution2.threeSum([1, 1, -2]), [[-2, 1, 1]]))
        self.assertEqual(solution2.threeSum([0, 0, 0, 0]), [[0, 0, 0]])
        self.assertEqual(solution2.threeSum([-2, 0, 0, 2, 2]), [[-2, 0, 2]])

if __name__ == '__main__':
    unittest.main()
