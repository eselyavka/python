#!/usr/bin/env python

import unittest

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = {}
        for i, num in enumerate(nums):
            if num in d:
                if any([abs(i - x) <= k for x in d[num]]):
                    return True
                else:
                    d[num].append(i)
            else:
                d[num] = [i]
        return False

class TestSolution(unittest.TestCase):

    def test_containsNearbyDuplicate(self):

        solution = Solution()

        self.assertTrue(solution.containsNearbyDuplicate([1, 2, 3, 1], 3))
        self.assertTrue(solution.containsNearbyDuplicate([1, 0, 1, 1], 1))
        self.assertFalse(solution.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))

if __name__ == '__main__':
    unittest.main()
