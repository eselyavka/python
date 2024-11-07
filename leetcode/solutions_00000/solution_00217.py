#!/usr/bin/env python

import unittest
from collections import defaultdict

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d = defaultdict(int)

        for num in nums:
            d[num] += 1
            if d[num] > 1:
                return True

        return False

class TestSolution(unittest.TestCase):
    def test_anagramMappings(self):
        solution = Solution()
        self.assertTrue(solution.containsDuplicate([1, 2, 3, 1]))
        self.assertFalse(solution.containsDuplicate([1, 2, 3, 4]))
        self.assertTrue(solution.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
        self.assertTrue(solution.containsDuplicate([3, 3]))

if __name__ == '__main__':
    unittest.main()
