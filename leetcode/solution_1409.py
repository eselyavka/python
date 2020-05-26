#!/usr/bin/env python

import unittest


class Solution(object):
    def processQueries(self, queries, m):
        """
        :type queries: List[int]
        :type m: int
        :rtype: List[int]
        """
        p = list(range(1, m+1))
        res = []

        for q in queries:
            p_idx = p.index(q)
            p.insert(0, p.pop(p_idx))
            res.append(p_idx)
        return res


class TestSolution(unittest.TestCase):
    def test_processQueries(self):
        solution = Solution()
        self.assertListEqual(solution.processQueries([3, 1, 2, 1], 5), [2, 1, 2, 1])


if __name__ == '__main__':
    unittest.main()
