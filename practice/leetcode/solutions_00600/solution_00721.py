#!/usr/bin/env python3

"""LeetCode solution 00721."""

import unittest
from collections import defaultdict


class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """

        g = defaultdict(set)
        em_to_name = {}
        for account in accounts:
            name = account[0]
            for k in range(1, len(account)):
                g[account[1]].add(account[k])
                g[account[k]].add(account[1])
                em_to_name[account[k]] = name

        seen = set()
        res = []
        for email in g:
            if email not in seen:
                stack = [email]
                seen.add(email)
                buf = []
                while stack:
                    node = stack.pop()
                    buf.append(node)
                    for adj in g[node]:
                        if adj not in seen:
                            seen.add(adj)
                            stack.append(adj)
                res.append([em_to_name[email]] + sorted(buf))

        return res


class TestSolution(unittest.TestCase):
    def test_accountsMerge(self):
        solution = Solution()
        result = solution.accountsMerge([["John", "johnsmith@mail.com", "john00@mail.com"],
                                         ["John", "johnnybravo@mail.com"],
                                         ["John",
                                          "johnsmith@mail.com",
                                          "john_newyork@mail.com"],
                                         ["Mary", "mary@mail.com"]])
        expected = [["John", "johnnybravo@mail.com"],
                    ["John",
                     "john00@mail.com",
                     "john_newyork@mail.com",
                     "johnsmith@mail.com"],
                    ["Mary", "mary@mail.com"]]
        self.assertEqual(sorted(result), sorted(expected))


if __name__ == '__main__':
    unittest.main()
