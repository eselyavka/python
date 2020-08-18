#!/usr/bin/env python

import unittest


class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        res = [None] * len(indices)

        sidx = 0
        for idx in indices:
            res[idx] = s[sidx]
            sidx += 1

        return ''.join(res)


class TestSolution(unittest.TestCase):
    def test_restoreString(self):
        solution = Solution()
        self.assertEqual(solution.restoreString('codeleet',
                                                [4, 5, 6, 7, 0, 2, 1, 3]),
                         'leetcode')


if __name__ == '__main__':
    unittest.main()
