#!/usr/bin/env python

import unittest


class Solution(object):
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        if len(start) != len(end):
            return False

        if len(start) == 1:
            return start == end

        n = len(start)
        i = 0
        res = []
        ss = list(start)
        ee = list(end)
        while i < n - 1:
            if ss[i] != ee[i]:
                if ss[i] == 'R' and ss[i+1] == 'X':
                    ss[i], ss[i+1] = ss[i+1], ss[i]
                elif ss[i] == 'X' and ss[i+1] == 'L':
                    ss[i], ss[i+1] = ss[i+1], ss[i]
                else:
                    if ss[i] == 'X':
                        j = i
                        while j < n - 1:
                            if ss[j] == 'L':
                                ss[i], ss[j] = ss[j], ss[i]
                                break
                            j += 1
                    elif ss[i] == 'R':
                        # R first
                        j = i
                        while j < n - 1:
                            if ss[j] == 'X':
                                ss[i], s[j] = ss[j], ss[i]
                                break
                            j += 1
                    else:
                        return False
            i += 1
        return ss == ee


class TestSolution(unittest.TestCase):
    def test_canTransform(self):
        solution = Solution()
        self.assertFalse(solution.canTransform('L', 'X'))
        self.assertTrue(solution.canTransform('RXXLRXRXL', 'XRLXXRRLX'))
        self.assertFalse(solution.canTransform('RL', 'LR'))
        self.assertFalse(solution.canTransform('XXRXXLXXXX', 'XXXXRXXLXX'))
        self.assertTrue(solution.canTransform('XXXXXLXXXX', 'LXXXXXXXXX'))
        self.assertTrue(solution.canTransform('XLXRRXXRXX', 'LXXXXXXRRR'))


if __name__ == '__main__':
    unittest.main()
