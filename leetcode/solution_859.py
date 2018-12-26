#!/usr/bin/env python

import unittest
from collections import defaultdict

class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if not A or not B:
            return False

        if len(A) != len(B):
            return False

        if A == B:
            d = defaultdict(int)
            for c in A:
                d[c] += 1
                if d[c] >= 2:
                    return True

            return False

        arr_A = list(A)
        arr_B = list(B)
        size = len(arr_A) - 1
        swap = []

        while size >= 0:
            if arr_A[size] != arr_B[size]:
                swap.append(size)
            size -= 1

        if len(swap) != 2:
            return False

        arr_A[swap[0]], arr_A[swap[1]] = arr_A[swap[1]], arr_A[swap[0]]

        return ''.join(arr_A) == ''.join(arr_B)


class TestSolution(unittest.TestCase):
    def test_buddyStrings(self):
        solution = Solution()
        self.assertTrue(solution.buddyStrings("ab", "ba"))
        self.assertFalse(solution.buddyStrings("ab", "ab"))
        self.assertTrue(solution.buddyStrings("aa", "aa"))
        self.assertTrue(solution.buddyStrings("aac", "aac"))
        self.assertTrue(solution.buddyStrings("aaaaaaabc", "aaaaaaacb"))
        self.assertFalse(solution.buddyStrings("", "aa"))


if __name__ == '__main__':
    unittest.main()
