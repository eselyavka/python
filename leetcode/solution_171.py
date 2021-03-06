#!/usr/bin/env python

import unittest
from string import ascii_uppercase


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {ascii_uppercase[x]: x+1 for x in range(len(ascii_uppercase))}

        if s in d:
            return d[s]

        base = 26
        res = i = 0
        j = len(s) - 1
        while j >= 0:
            res += d[s[j]] * base ** i
            i += 1
            j -= 1

        return res


class Solution2(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        return reduce(lambda res, c: res * 26 + ord(c) - ord('A') + 1, s, 0)


class TestSolution(unittest.TestCase):

    def test_titleToNumber(self):
        solution = Solution()
        self.assertEqual(solution.titleToNumber('A'), 1)
        self.assertEqual(solution.titleToNumber('AB'), 28)
        self.assertEqual(solution.titleToNumber('ZY'), 701)

        solution2 = Solution2()
        self.assertEqual(solution2.titleToNumber('A'), 1)
        self.assertEqual(solution2.titleToNumber('AB'), 28)
        self.assertEqual(solution2.titleToNumber('ZY'), 701)


if __name__ == '__main__':
    unittest.main()
