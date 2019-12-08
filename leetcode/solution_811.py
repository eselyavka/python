#!/usr/bin/python

import unittest
from collections import defaultdict


class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        res = defaultdict(int)
        for d in cpdomains:
            cnt_, domain = d.split()
            cnt = int(cnt_)
            res[domain] += cnt
            two, three = [None] * 2

            try:
                _, two, three = domain.split('.')
            except ValueError:
                _, two = domain.split('.')

            if three:
                res[two + '.' + three] += cnt
                res[three] += cnt
            else:
                res[two] += cnt

        return [' '.join([str(t[1]), t[0]]) for t in res.items()]


class TestSolution(unittest.TestCase):

    def test_subdomainVisits(self):
        solution = Solution()

        self.assertListEqual(solution.subdomainVisits(["9001 discuss.leetcode.com"]),
                             ["9001 leetcode.com",
                              "9001 discuss.leetcode.com",
                              "9001 com"])


if __name__ == '__main__':
    unittest.main()
