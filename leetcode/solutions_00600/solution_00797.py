#!/usr/bin/env python

import unittest


class Solution(object):
    def dfs(self, graph, start, target):
        s = [(start, [start])]
        while s:
            vertex, path = s.pop()
            for v in graph[vertex]:
                if v == target:
                    yield path + [v]
                else:
                    s.append((v, path + [v]))

    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        return list(self.dfs(graph, 0, len(graph) - 1))


class TestSolution(unittest.TestCase):

    def test_allPathsSourceTarget(self):
        solution = Solution()

        self.assertTrue(all([p in solution.allPathsSourceTarget(
            [[1, 2], [3], [3], []]) for p in [[0, 1, 3], [0, 2, 3]]]))
        self.assertTrue(all(
            [p in solution.allPathsSourceTarget(
                [[4, 3, 1], [3, 2, 4], [3], [4], []]) for p in
             [[0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4], [0, 1, 4]]]))


if __name__ == '__main__':
    unittest.main()
