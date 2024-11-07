#!/usr/bin/env python

import unittest


class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt_r, cnt_l = 0, 0
        res = 0
        for c in s:
            if cnt_r and cnt_l and (cnt_r == cnt_l):
                res += 1
                cnt_r, cnt_l = 0, 0

            if c == 'R':
                cnt_r += 1
            else:
                cnt_l += 1

        if cnt_r and cnt_l and (cnt_r == cnt_l):
            res += 1

        return res


class TestSolution(unittest.TestCase):
    def test_balancedStringSplit(self):
        solution = Solution()
        self.assertEqual(solution.balancedStringSplit('RLRRLLRLRL'), 4)


if __name__ == '__main__':
    unittest.main()
