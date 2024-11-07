#!/usr/bin/env python

import unittest


class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        if not arr:
            return []

        _arr = sorted(arr)
        seen = dict()
        i = 1
        for element in _arr:
            if element in seen:
                continue
            seen[element] = i
            i += 1
        rank = []

        for element in arr:
            rank.append(seen.get(element))
        return rank


class TestSolution(unittest.TestCase):

    def test_arrayRankTransform(self):
        solution = Solution()
        self.assertListEqual(solution.arrayRankTransform([40, 10, 20, 30]), [4, 1, 2, 3])
        self.assertListEqual(solution.arrayRankTransform([100, 100, 100]), [1, 1, 1])


if __name__ == '__main__':
    unittest.main()
