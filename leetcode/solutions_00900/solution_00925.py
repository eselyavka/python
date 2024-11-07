#!/usr/bin/env python

import unittest


class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        idx_name = 0
        idx_typed = 0
        prev = None
        while idx_typed < len(typed):
            if idx_name < len(name) and name[idx_name] == typed[idx_typed]:
                idx_name += 1
                idx_typed += 1
            else:
                if prev == typed[idx_typed]:
                    idx_typed += 1
                else:
                    return False
            prev = typed[idx_typed - 1]

        return name[-1] == typed[-1]


class TestSolution(unittest.TestCase):
    def test_isLongPressedName(self):
        solution = Solution()
        self.assertTrue(solution.isLongPressedName("alex", "aaleex"))
        self.assertFalse(solution.isLongPressedName("alex", "plleex"))
        self.assertFalse(solution.isLongPressedName("alex", "pplleex"))
        self.assertFalse(solution.isLongPressedName("alex", "alleey"))
        self.assertFalse(solution.isLongPressedName("alex", "alleeyy"))
        self.assertFalse(solution.isLongPressedName("saeed", "ssaaedd"))
        self.assertTrue(solution.isLongPressedName("leelee", "lleeelee"))
        self.assertTrue(solution.isLongPressedName("laiden", "laiden"))
        self.assertTrue(solution.isLongPressedName("vtkgn", "vttkgnn"))
        self.assertFalse(solution.isLongPressedName("vtkgn", "vttkgnny"))
        self.assertFalse(solution.isLongPressedName("pyplrz", "ppyypllr"))


if __name__ == '__main__':
    unittest.main()
