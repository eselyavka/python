#!/usr/bin/env python

import unittest
import string

class Solution(object):
    def _cmp(self, arr1, arr2):
        for i in range(len(string.lowercase)):
            if arr1[i] != arr2[i]:
                return False
        return True

    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(s) < len(p):
            return []

        if len(s) == len(p) and sorted(s) == sorted(p):
            return [0]

        s_size = len(s)
        p_size = len(p)
        res = []

        p_arr, w_arr = [0 for _ in string.lowercase], [0 for _ in string.lowercase]

        for i in range(len(p)):
            p_arr[ord(p[i]) - ord('a')] += 1
            w_arr[ord(s[i]) - ord('a')] += 1

        for i in range(p_size, s_size):
            if self._cmp(p_arr, w_arr):
                res.append(i - p_size)

            w_arr[ord(s[i]) - ord('a')] += 1
            w_arr[ord(s[i-p_size]) - ord('a')] -= 1

        if self._cmp(p_arr, w_arr):
            res.append(s_size - p_size)

        return res

class TestSolution(unittest.TestCase):

    def test_findAnagrams(self):

        solution = Solution()

        self.assertEqual(solution.findAnagrams("one", "three"), [])
        self.assertEqual(solution.findAnagrams("abc", "cab"), [0])
        self.assertEqual(solution.findAnagrams("cbaebabacd", "abc"), [0, 6])

if __name__ == '__main__':
    unittest.main()
