#!/usr/bin/env python

import unittest


class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s or len(s) == 1:
            return s

        arr, i = list(s), 1

        while i < len(arr):
            if arr[i].lower() == arr[i-1].lower():
                if ((arr[i].isupper() and arr[i-1].islower()) or
                        (arr[i].islower() and arr[i-1].isupper())):
                    del arr[i-1]
                    del arr[i-1]
                    i = i - 2 if i >= 2 else 0
            i += 1
        return ''.join(arr)


class TestSolution(unittest.TestCase):
    def test_makeGood(self):
        solution = Solution()
        self.assertEqual(solution.makeGood('leEeetcode'), 'leetcode')


if __name__ == '__main__':
    unittest.main()
