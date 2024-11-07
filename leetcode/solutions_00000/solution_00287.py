#!/usr/bin/env python

import unittest


class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) - 1
        nums.sort()
        i = 0

        while i < n:
            if nums[i] == nums[i+1]:
                return nums[i]

            i += 1


class Solution2(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = set()
        res = -1
        for num in nums:
            if num in seen:
                res = num
            seen.add(num)

        return res


class Solution3(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        fast = slow = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return fast


class TestSolution(unittest.TestCase):
    def test_findDuplicate(self):
        solution1 = Solution()
        solution2 = Solution2()
        solution3 = Solution3()
        dups1 = [1, 3, 4, 2, 2]
        dups2 = [3, 1, 3, 4, 2]
        for solution in [solution1, solution2, solution3]:
            self.assertEqual(solution.findDuplicate(dups1), 2)
            self.assertEqual(solution.findDuplicate(dups2), 3)


if __name__ == '__main__':
    unittest.main()
