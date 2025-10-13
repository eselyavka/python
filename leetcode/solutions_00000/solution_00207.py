import unittest
from collections import defaultdict


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        edges = list(range(numCourses))
        adj = defaultdict(list)

        for item in prerequisites:
            a, b = item
            adj[a].append(b)

        visited = set()
        in_stack = set()

        def dfs(u):
            visited.add(u)
            in_stack.add(u)

            for v in adj[u]:
                if v not in visited:
                    if dfs(v):
                        return True
                elif v in in_stack:
                    return True

            in_stack.remove(u)
            return False

        is_cycle = False

        for e in edges:
            if e not in visited and dfs(e):
                is_cycle = True

        return not is_cycle


class TestSolution(unittest.TestCase):
    def test_canFinish(self):
        solution = Solution()
        self.assertTrue(solution.canFinish(2, [[1, 0]]))


if __name__ == '__main__':
    unittest.main()
