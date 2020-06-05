#!/usr/bin/env python

import unittest


def isBadVersion(mid):
    return mid == 4


class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n

        while left <= right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                if isBadVersion(mid-1):
                    right = mid - 1
                else:
                    return mid
            else:
                if isBadVersion(mid+1):
                    return mid + 1
                else:
                    left = mid + 1


class TestSolution(unittest.TestCase):

    def test_firstBadVersion(self):
        solution = Solution()
        self.assertEqual(solution.firstBadVersion(5), 4)


if __name__ == '__main__':
    unittest.main()
