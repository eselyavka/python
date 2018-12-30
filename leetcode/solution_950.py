#!/usr/bin/env python

import unittest

class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        size = len(deck)
        res = [None] * size
        idx = range(size)

        for card in sorted(deck):
            res[idx.pop(0)] = card
            if idx:
                idx.append(idx.pop(0))

        return res


class TestSolution(unittest.TestCase):
    def test_deckRevealedIncreasing(self):
        solution = Solution()
        self.assertEqual(solution.deckRevealedIncreasing([17, 13, 11, 2, 3, 5, 7]),
                         [2, 13, 3, 11, 5, 17, 7])


if __name__ == '__main__':
    unittest.main()
