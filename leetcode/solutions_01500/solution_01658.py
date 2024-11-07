#!/usr/bin/env python

import unittest


class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        curr = sum(nums)
        ans = float('+inf')
        left = 0
        n = len(nums)

        for i in range(n):
            curr -= nums[i]

            while curr < x and left <= i:
                curr += nums[left]
                left += 1

            if curr == x:
                ans = min(ans, (n-1-i) + left)

        return ans if ans != float("+inf") else -1


class TestSolution(unittest.TestCase):

    def test_minOperations(self):
        solution = Solution()
        self.assertEqual(solution.minOperations([3, 2, 20, 1, 1, 3], 10), 5)


if __name__ == '__main__':
    unittest.main()
