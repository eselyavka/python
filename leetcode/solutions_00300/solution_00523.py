#!/usr/bin/env python

import unittest


class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        reminders = {0:-1}
        total = 0

        for i, n in enumerate(nums):
            total += n
            r = total % k

            if r not in reminders:
                reminders[r] = i
            elif i - reminders[r] > 1:
                return True

        return False


class Solution2(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        n = len(nums)

        for i in range(n):
            curr = nums[i]
            for j in range(i + 1, n):
                curr += nums[j]
                if k and curr % k == 0:
                    return True
                if k == 0 and curr == 0:
                    return True
        return False


class TestSolution(unittest.TestCase):
    def test_checkSubarraySum(self):
        solution = Solution()
        self.assertTrue(solution.checkSubarraySum([23, 2, 4, 6, 7], 6))

        solution2 = Solution2()
        self.assertTrue(solution2.checkSubarraySum([23, 2, 4, 6, 7], 6))


if __name__ == '__main__':
    unittest.main()
