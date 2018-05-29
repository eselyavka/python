#!/usr/bin/env python

import unittest

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

        return d.values()

class TestSolution(unittest.TestCase):
    def test_groupAnagrams(self):
        solution = Solution()
        self.assertEqual(solution.groupAnagrams(["eat",
                                                 "tea",
                                                 "tan",
                                                 "ate",
                                                 "nat",
                                                 "bat"]),
                         [['tan', 'nat'],
                          ['bat'],
                          ['eat', 'tea', 'ate']])

if __name__ == '__main__':
    unittest.main()
