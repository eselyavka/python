#!/usr/bin/env python

import unittest
from collections import defaultdict
import heapq


class Solution(object):
    def find(self, parent, x):
        if parent[x] == x:
            return x

        parent[x] = self.find(parent, parent[x])

        return parent[x]

    def union(self, parent, rank, x, y):
        xx = self.find(parent, x)
        yy = self.find(parent, y)

        if xx != yy:
            if rank[xx] > rank[yy]:
                parent[yy] = parent[xx]
            elif rank[yy] > rank[xx]:
                parent[xx] = parent[yy]
            else:
                parent[yy] = parent[xx]
                rank[xx] += 1

    def smallestStringWithSwaps(self, s, pairs):
        """
        :type s: str
        :type pairs: List[List[int]]
        :rtype: str
        """
        n = len(s)
        parent = [x for x in range(n)]
        rank = [0 for _ in range(n)]

        for x, y in pairs:
            self.union(parent, rank, x, y)

        d = defaultdict(list)
        for idx, c in enumerate(s):
            heapq.heappush(d[self.find(parent, idx)], c)

        res = ''
        for idx, c in enumerate(s):
            res += heapq.heappop(d[self.find(parent, idx)])

        return res


class TestSolution(unittest.TestCase):

    def test_smallestStringWithSwaps(self):
        solution = Solution()
        self.assertEqual(solution.smallestStringWithSwaps("dcab", [[0, 3], [1, 2]]), "bacd")
        self.assertEqual(solution.smallestStringWithSwaps("cba", [[0, 1], [1, 2]]), "abc")
        self.assertEqual(solution.smallestStringWithSwaps("dcab", [[0, 3], [1, 2], [0, 2]]), "abcd")


if __name__ == '__main__':
    unittest.main()
