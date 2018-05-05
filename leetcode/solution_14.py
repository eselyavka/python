#!/usr/bin/env python

import unittest

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''

        if len(strs) == 1:
            return strs[0]

        min_len = min([len(x) for x in strs])

        res = ''
        for i in range(min_len):
            c = strs[0][i]
            for j in range(1, len(strs)):
                if strs[j][i] != c:
                    return res
            res += c

        return res

class TestSolution(unittest.TestCase):

    def test_longestCommonPrefix(self):
        solution = Solution()
        self.assertEqual(solution.longestCommonPrefix(['flower', 'flow', 'flight']), 'fl')
        self.assertEqual(solution.longestCommonPrefix(['dog', 'racecar', 'car']), '')
        self.assertEqual(solution.longestCommonPrefix([]), '')
        self.assertEqual(solution.longestCommonPrefix(['dog']), 'dog')
        self.assertEqual(solution.longestCommonPrefix(['abab', 'aba', 'abc']), 'ab')
        self.assertEqual(solution.longestCommonPrefix(['aca', 'cba']), '')

if __name__ == '__main__':
    unittest.main()
