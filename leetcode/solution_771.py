#!/usr/bin/env python

import unittest
from collections import defaultdict

class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        d = defaultdict(int)
        for c in S:
            d[c] += 1

        res = 0

        for c in J:
            res += d[c]

        return res

class TestSolution(unittest.TestCase):

    def test_numJewelsInStones(self):
        solution = Solution()
        self.assertEqual(solution.numJewelsInStones('aA', 'aAAbbbb'), 3)
        self.assertEqual(solution.numJewelsInStones('z', 'ZZ'), 0)

if __name__ == '__main__':
    unittest.main()
