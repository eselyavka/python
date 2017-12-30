#!/usr/bin/env python

import unittest

class Solution(object):
    def dfs(self, graph, kill, visited=None):
        if visited is None:
            visited = set()

        visited.add(kill)
        for i in graph[kill] - visited:
            self.dfs(graph, i, visited)

        return visited

    def killProcess(self, pid, ppid, kill):
        proc_lst = {p:set() for p in set(pid + ppid)}

        for i, parent in enumerate(ppid):
            proc_lst[parent].add(pid[i])

        return list(self.dfs(proc_lst, kill))

class TestSolution(unittest.TestCase):

    def test_killProcess(self):
        pid = [1, 3, 10, 5]
        ppid = [3, 0, 5, 3]
        kill = 5

        pid1 = [1, 2, 3]
        ppid1 = [0, 1, 2]
        kill1 = 1

        pid2 = [1, 2, 3, 4, 5]
        ppid2 = [0, 1, 1, 1, 1]
        kill2 = 1

        solution = Solution()
        self.assertEqual(sorted(solution.killProcess(pid, ppid, kill)), [5, 10])
        self.assertEqual(sorted(solution.killProcess(pid1, ppid1, kill1)), [1, 2, 3])
        self.assertEqual(sorted(solution.killProcess(pid2, ppid2, kill2)), [1, 2, 3, 4, 5])

if __name__ == '__main__':
    unittest.main()
