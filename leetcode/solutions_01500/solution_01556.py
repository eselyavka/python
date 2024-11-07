#!/usr/bin/env python

import unittest


class Solution(object):
    def thousandSeparator(self, n):
        """
        :type n: int
        :rtype: str
        """
        str_n = list(str(n))
        i = len(str_n) - 1
        c = 0
        while i >= 0:
            if c == 3:
                str_n.insert(i+1, '.')
                c = 0
            i -= 1
            c += 1
        return ''.join(str_n)


class TestSolution(unittest.TestCase):
    def test_thousandSeparator(self):
        solution = Solution()
        self.assertEqual(solution.thousandSeparator(1234), '1.234')


if __name__ == '__main__':
    unittest.main()
