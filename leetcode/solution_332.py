#!/usr/bin/env python

import unittest


from collections import defaultdict


class Solution(object):
    def __init__(self):
        self.best_path = []

    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        graph = defaultdict(list)
        for src, dst in tickets:
            graph[src] += [dst]

        self.best_path = ['JFK']

        def dfs(src):
            if len(self.best_path) == len(tickets) + 1:
                return self.best_path

            dsts = sorted(graph[src])

            for dst in dsts:
                graph[src].remove(dst)
                self.best_path += [dst]
                path = dfs(dst)
                if path:
                    return path
                self.best_path.pop()
                graph[src] += [dst]

            return None

        return dfs('JFK')


class TestSolution(unittest.TestCase):
    def test_findItinerary(self):
        solution = Solution()
        self.assertListEqual(solution.findItinerary([["EZE", "AXA"],
                                                     ["TIA", "ANU"],
                                                     ["ANU", "JFK"],
                                                     ["JFK", "ANU"],
                                                     ["ANU", "EZE"],
                                                     ["TIA", "ANU"],
                                                     ["AXA", "TIA"],
                                                     ["TIA", "JFK"],
                                                     ["ANU", "TIA"],
                                                     ["JFK", "TIA"]]),
                             ["JFK", "ANU", "EZE", "AXA",
                              "TIA", "ANU", "JFK", "TIA",
                              "ANU", "TIA", "JFK"])
        self.assertListEqual(solution.findItinerary([["JFK", "AAA"],
                                                     ["AAA", "JFK"],
                                                     ["JFK", "BBB"],
                                                     ["JFK", "CCC"],
                                                     ["CCC", "JFK"]]),
                             ["JFK", "AAA", "JFK", "CCC", "JFK", "BBB"])
        self.assertListEqual(solution.findItinerary([["JFK", "KUL"],
                                                     ["JFK", "NRT"],
                                                     ["NRT", "JFK"]]),
                             ["JFK", "NRT", "JFK", "KUL"])
        self.assertListEqual(solution.findItinerary([["MUC", "LHR"],
                                                     ["JFK", "MUC"],
                                                     ["SFO", "SJC"],
                                                     ["LHR", "SFO"]]),
                             ["JFK", "MUC", "LHR", "SFO", "SJC"])
        self.assertListEqual(solution.findItinerary([["JFK", "ATL"],
                                                     ["ORD", "PHL"],
                                                     ["JFK", "ORD"],
                                                     ["PHX", "LAX"],
                                                     ["LAX", "JFK"],
                                                     ["PHL", "ATL"],
                                                     ["ATL", "PHX"]]),
                             ["JFK", "ATL", "PHX", "LAX",
                              "JFK", "ORD", "PHL", "ATL"])
        self.assertListEqual(solution.findItinerary([["JFK", "SFO"],
                                                     ["JFK", "ATL"],
                                                     ["SFO", "ATL"],
                                                     ["ATL", "JFK"],
                                                     ["ATL", "SFO"]]),
                             ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"])


if __name__ == '__main__':
    unittest.main()
