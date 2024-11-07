#!/usr/bin/env python

import unittest
from collections import Counter


class Solution(object):
    def numSplits(self, s):
        """
        :type s: str
        :rtype: int
        """
        set_left = set()
        dict_cnt = Counter(s)
        res = 0
        for c in s:
            set_left.add(c)
            dict_cnt[c] -= 1

            if len(set_left) == len([x for x in dict_cnt.items() if x[1]]):
                res += 1

        return res


class TestSolution(unittest.TestCase):
    def test_numSplits(self):
        solution = Solution()
        self.assertEqual(solution.numSplits("aacaba"), 2)


if __name__ == '__main__':
    unittest.main()
