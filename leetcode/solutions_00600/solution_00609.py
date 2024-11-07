#!/usr/bin/env python

import unittest
from collections import defaultdict
import os
import hashlib

class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        d = defaultdict(list)
        s = set()
        for path in paths:
            entities = path.split()
            for i in range(1, len(entities)):
                name, data = entities[i].split('(')
                payload = hashlib.sha256(data.split(')')[0]).hexdigest()
                if payload in d:
                    s.add(payload)
                d[payload].append(os.path.join(entities[0], name))

        return [d[x] for x in s]

class TestSolution(unittest.TestCase):

    def test_findDuplicate(self):
        solution = Solution()

        self.assertListEqual(solution.findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)",
                                                     "root/c 3.txt(abcd)",
                                                     "root/c/d 4.txt(efgh)",
                                                     "root 4.txt(efgh)"]),
                             [["root/a/2.txt",
                               "root/c/d/4.txt",
                               "root/4.txt"],
                              ["root/a/1.txt",
                               "root/c/3.txt"]])

if __name__ == '__main__':
    unittest.main()
