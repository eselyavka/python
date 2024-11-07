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

        if start.replace('X', '') != end.replace('X', ''):
            return False

        used = [False] * len(end)
        for i, c in enumerate(end):
            if c == 'L':
                found = False
                for j in range(i, len(start)):
                    if start[j] == 'R':
                        return False
                    if start[j] == 'L' and not used[j]:
                        used[j] = True
                        found = True
                        break

                if not found:
                    return False

            if c == 'R':
                found = False
                for j in range(i, -1, -1):
                    if start[j] == 'L':
                        return False
                    if start[j] == 'R' and not used[j]:
                        used[j] = True
                        found = True
                        break

                if not found:
                    return False

        return True


class TestSolution(unittest.TestCase):
    def test_canTransform(self):
        solution = Solution()
        self.assertTrue(solution.canTransform('RXXLRXRXL', 'XRLXXRRLX'))


if __name__ == '__main__':
    unittest.main()
