#!/usr/bin/env python

import unittest

class Solution(object):

    def _rec(self, num, digit):
        if not digit:
            return True

        if int(num) % int(digit[0]) == 0:
            return self._rec(num, digit[1:])

        return False

    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res = []
        for i in range(left, right + 1):
            s = str(i)
            if '0' in s:
                continue
            if self._rec(s, s):
                res.append(i)
        return res

class TestSolution(unittest.TestCase):

    def test_countSubstrings(self):
        left = 1
        right = 22
        solution = Solution()
        self.assertEqual(solution.selfDividingNumbers(left, right),
                         [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22])

if __name__ == '__main__':
    unittest.main()
