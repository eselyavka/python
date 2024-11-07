#!/usr/bin/python

import unittest
from collections import defaultdict


class Solution(object):
    def shortestAlternatingPaths(self, n, red_edges, blue_edges):
        """
        :type n: int
        :type red_edges: List[List[int]]
        :type blue_edges: List[List[int]]
        :rtype: List[int]
        """
        graph = defaultdict(set)

        for i, j in red_edges:
            graph[i].add((j, 1))
        for i, j in blue_edges:
            graph[i].add((j, 0))

        q = [(0, 1, 0), (0, 0, 0)]
        seen = {(0, 1), (0, 0)}
        res = [float('inf')] * n
        res[0] = 0

        while q:
            node, color, distance = q.pop(0)
            for node_, color_ in graph[node]:
                if color == color_ and (node_, color_) not in seen:
                    seen.add((node_, color_))
                    q.append((node_, color_ ^ 1, distance + 1))
                    res[node_] = min(res[node_], distance + 1)
        return [-1 if x == float('inf') else x for x in res]


class TestSolution(unittest.TestCase):

    def test_shortestAlternatingPaths(self):
        solution = Solution()
        self.assertListEqual(solution.shortestAlternatingPaths(3, [[0, 1], [1, 2]], []), [0, 1, -1])


if __name__ == '__main__':
    unittest.main()
