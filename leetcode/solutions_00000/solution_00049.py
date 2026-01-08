#!/usr/bin/env python

import unittest
from collections import defaultdict


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for s in strs:
            ss = ''.join(sorted(s))
            try:
                d[ss].append(s)
            except KeyError:
                d[ss] = [s]

        return list(d.values())


class Solution2(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        ans = defaultdict(list)

        for s in strs:
            cnt = [0] * 26
            for c in s:
                cnt[ord(c) - ord("a")] += 1
            ans[tuple(cnt)].append(s)

        return list(ans.values())


class TestSolution(unittest.TestCase):
    def test_groupAnagrams(self):
        solution = Solution()
        self.assertEqual(solution.groupAnagrams(["eat",
                                                 "tea",
                                                 "tan",
                                                 "ate",
                                                 "nat",
                                                 "bat"]).sort(),
                         [['tan', 'nat'],
                          ['bat'],
                          ['eat', 'tea', 'ate']].sort())
        solution2 = Solution2()
        self.assertEqual(solution2.groupAnagrams(["eat",
                                                  "tea",
                                                  "tan",
                                                  "ate",
                                                  "nat",
                                                  "bat"]).sort(),
                         [['tan', 'nat'],
                          ['bat'],
                          ['eat', 'tea', 'ate']].sort())


if __name__ == '__main__':
    unittest.main()
