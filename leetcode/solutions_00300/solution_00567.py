#!/usr/bin/env python

import unittest
import string

class Solution(object):
    def _cmp(self, arr1, arr2):
        for i in range(len(string.lowercase)):
            if arr1[i] != arr2[i]:
                return False
        return True

    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False

        s1_arr, s2_arr, i = [0 for _ in string.lowercase], [0 for _ in string.lowercase], 0
        size_s1, size_s2 = len(s1), len(s2)

        while i < size_s1:
            s1_arr[ord(s1[i]) - ord('a')] += 1
            s2_arr[ord(s2[i]) - ord('a')] += 1
            i += 1

        i = 0

        while i < (size_s2 - size_s1):
            if self._cmp(s1_arr, s2_arr):
                return True

            s2_arr[ord(s2[i+size_s1]) - ord('a')] += 1
            s2_arr[ord(s2[i]) - ord('a')] -= 1
            i += 1

        return False if not self._cmp(s1_arr, s2_arr) else True

class TestSolution(unittest.TestCase):
    def test_checkInclusion(self):
        solution = Solution()
        self.assertTrue(solution.checkInclusion("ab", "eidbaooo"))
        self.assertFalse(solution.checkInclusion("ab", "eidboaoo"))
        self.assertTrue(solution.checkInclusion("adc", "dcda"))

if __name__ == '__main__':
    unittest.main()
