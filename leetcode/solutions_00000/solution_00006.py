#!/usr/bin/env python

import unittest

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        d = {x:[] for x in range(numRows)}
        direction = 0
        row = 0
        for c in s:

            d[row].append(c)

            if row == numRows - 1:
                direction = 1

            if row == 0:
                direction = 0

            if direction == 0:
                row += 1
            else:
                row -= 1

        return ''.join([''.join(d[x]) for x in d])

class TestSolution(unittest.TestCase):

    def test_convert(self):
        solution = Solution()
        self.assertEqual(solution.convert('testtest', 2), 'tstsetet')
        self.assertEqual(solution.convert('PAYPALISHIRING', 3), 'PAHNAPLSIIGYIR')
        self.assertEqual(solution.convert('PAYPALISHIRING', 4), 'PINALSIGYAHRPI')
        self.assertEqual(solution.convert('AB', 1), 'AB')

if __name__ == '__main__':
    unittest.main()
