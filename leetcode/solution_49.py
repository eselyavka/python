#!/usr/bin/env python

import unittest

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        res = dict()

        for s in strs:
            sorted_str = ''.join(sorted(s))

            if res.has_key(sorted_str):
                res[sorted_str].append(s)
            else:
                res[sorted_str] = [s]

        return [sorted(mas) for mas in res.values()]

class TestSolution(unittest.TestCase):

    def test_groupAnagrams(self):
        anagrams = ["eat", "tea", "tan", "ate", "nat", "bat"]
        solution = Solution()
        self.assertEqual(solution.groupAnagrams(anagrams),
                         [["nat", "tan"],
                          ["bat"],
                          ["ate", "eat", "tea"]])

if __name__ == '__main__':
    unittest.main()
