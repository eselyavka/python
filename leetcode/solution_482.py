#!/usr/bin/env python

import unittest

class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        i, j = len(S) - 1, 0
        res = []

        while i >= 0:
            if S[i] == '-':
                i -= 1
                continue

            if j == K:
                res.append('-')
                j = 0
                continue
            else:
                res.append(S[i].upper())

            j += 1
            i -= 1

        return ''.join(res[::-1])

class TestSolution(unittest.TestCase):
    def test_licenseKeyFormatting(self):
        solution = Solution()
        self.assertEqual(solution.licenseKeyFormatting('5F3Z-2e-9-w', 4), '5F3Z-2E9W')
        self.assertEqual(solution.licenseKeyFormatting('2-5g-3-J', 2), '2-5G-3J')
        self.assertEqual(solution.licenseKeyFormatting('2-4A0r7-4k', 4), '24A0-R74K')

if __name__ == '__main__':
    unittest.main()
