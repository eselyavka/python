#!/usr/bin/env python3

"""LeetCode solution 00451."""

import unittest
import collections

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        d = collections.defaultdict(int)

        for c in s:
            d[c] += 1

        res = ''
        for key, value in sorted(iter(d.items()), key=lambda k_v: (k_v[1], k_v[0]), reverse=True):
            res += key * value

        return res


class TestSolution(unittest.TestCase):

    def test_frequencySort(self):
        solution = Solution()
        s = 'tree'
        s2 = 'cccaaa'
        s3 = 'Aabb'
        self.assertEqual(solution.frequencySort(s), "eetr")
        self.assertEqual(solution.frequencySort(s2), 'cccaaa')
        self.assertEqual(solution.frequencySort(s3), 'bbaA')

if __name__ == '__main__':
    unittest.main()
