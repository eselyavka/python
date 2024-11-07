#!/usr/bin/env python

import unittest


class Solution(object):
    def canBeEqual(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: bool
        """
        if len(target) == 1:
            return target[0] == arr[0]

        if set(target) - set(arr):
            return False

        return sorted(target) == sorted(arr)


class TestSolution(unittest.TestCase):
    def test_canBeEqual(self):
        solution = Solution()
        self.assertTrue(solution.canBeEqual([1, 2, 3, 4], [2, 4, 1, 3]))


if __name__ == '__main__':
    unittest.main()
