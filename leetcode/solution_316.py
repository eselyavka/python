#!/usr/bin/env python

import unittest
from collections import Counter


class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []
        counter = Counter(s)

        for c in s:
            if c in res:
                counter[c] -= 1
                continue
            while res and res[-1] > c and counter[res[-1]] > 0:
                res.pop()

            res.append(c)
            counter[c] -= 1

        return ''.join(res)


class TestSolution(unittest.TestCase):
    def test_removeDuplicateLetters(self):
        solution = Solution()
        self.assertEqual(solution.removeDuplicateLetters('leetcode'), 'letcod')


if __name__ == '__main__':
    unittest.main()
