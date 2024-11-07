#!/usr/bin/env python

import unittest


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        size = 2 ** len(nums)
        res = []
        for i in range(size):
            tmp = []
            for j in range(len(nums)):
                if i & (1 << j):
                    tmp.append(nums[j])
            res.append(tmp)

        return res


class Solution2(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def rec(nums, idx, subset, acc):
            acc.append(subset[:])
            for i in range(idx, len(nums)):
                subset.append(nums[i])
                rec(nums, i + 1, subset, acc)
                subset.pop()

        ans = []
        subset = []
        rec(nums, 0, subset, ans)

        return ans


class TestSolution(unittest.TestCase):

    def test_subsets(self):
        solution = Solution()
        self.assertListEqual(sorted(solution.subsets([1, 2, 3])), sorted([[], [1], [2], [1, 2], [3],
                                                                          [1, 3], [2, 3], [1, 2, 3]]))
        self.assertListEqual(sorted(solution.subsets([1, 2])), sorted([[], [1], [2], [1, 2]]))
        self.assertListEqual(sorted(solution.subsets([0])), sorted([[], [0]]))
        solution2 = Solution2()
        self.assertListEqual(sorted(solution2.subsets([1, 2, 3])), sorted([[], [1], [2], [1, 2], [3],
                                                                           [1, 3], [2, 3], [1, 2, 3]]))
        self.assertListEqual(sorted(solution2.subsets([1, 2])), sorted([[], [1], [2], [1, 2]]))
        self.assertListEqual(sorted(solution2.subsets([0])), sorted([[], [0]]))


if __name__ == '__main__':
    unittest.main()
