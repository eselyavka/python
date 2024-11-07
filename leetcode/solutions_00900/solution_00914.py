#!/usr/bin/env python

import unittest
from collections import defaultdict

class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        if not deck or len(deck) < 2:
            return False

        d = defaultdict(int)

        for card in deck:
            d[card] += 1

        _min, _max = min(d.values()), max(d.values())
        if _min == 1:
            return False
        for val in d.values():
            if val % _min == 1:
                return False
        return True


class TestSolution(unittest.TestCase):
    def test_sortArrayByParityII(self):
        solution = Solution()
        self.assertTrue(solution.hasGroupsSizeX([1, 2, 3, 4, 4, 3, 2, 1]))
        self.assertFalse(solution.hasGroupsSizeX([1, 1, 1, 2, 2, 2, 3, 3]))
        self.assertFalse(solution.hasGroupsSizeX([1]))
        self.assertTrue(solution.hasGroupsSizeX([1, 1]))
        self.assertTrue(solution.hasGroupsSizeX([1, 1, 2, 2, 2, 2]))
        self.assertTrue(solution.hasGroupsSizeX([1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3]))
        self.assertFalse(solution.hasGroupsSizeX([0, 0, 0, 0, 0, 1, 1, 2, 3, 4]))


if __name__ == '__main__':
    unittest.main()
