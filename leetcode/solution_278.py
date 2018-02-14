#!/usr/bin/env python

import unittest

def isBadVersion(version):
    if version > 1702766718:
        return True
    return False

class Solution(object):
    def binary_search(self, l, r):
        while l <= r:
            mid = l + (r - l) / 2
            if not isBadVersion(mid):
                l = mid + 1
            elif isBadVersion(mid) and not isBadVersion(mid - 1):
                return mid
            else:
                r = mid - 1

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return n if isBadVersion(n) else None

        return self.binary_search(1, n)

class TestSolution(unittest.TestCase):

    def test_firstBadVersion(self):
        solution = Solution()
        self.assertEqual(solution.firstBadVersion(1), None)
        self.assertEqual(solution.firstBadVersion(2126753390), 1702766719)

if __name__ == '__main__':
    unittest.main()
