#!/usr/bin/env python

import unittest

class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        res = 0
        for x in range(1, N+1):
            strX = str(x)
            res += (all([c not in '347' for c in strX]) and any([c in '2569' for c in strX]))
        return res

class TestSolution(unittest.TestCase):
    def test_rotatedDigits(self):
        solution = Solution()
        self.assertEqual(solution.rotatedDigits(10), 4)
        self.assertEqual(solution.rotatedDigits(2), 1)
        self.assertEqual(solution.rotatedDigits(5), 2)

if __name__ == '__main__':
    unittest.main()
