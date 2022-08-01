#!/usr/bin/env python

import unittest
from collections import defaultdict


class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        def get_hash(string, shift):
            s = ''
            for c in string:
                s += chr((ord(c) - shift) % 26 + ord("a"))

            return s

        res = defaultdict(list)

        for string in strings:
            res[get_hash(string, ord(string[0]))].append(string)

        return list(res.values())


class TestSolution(unittest.TestCase):
    def test_groupStrings(self):
        solution = Solution()

        self.assertListEqual(sorted(solution.groupStrings(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"])),
						   sorted([["a", "z"], ["abc", "bcd", "xyz"], ["az", "ba"], ["acef"]]))


if __name__ == '__main__':
    unittest.main()
