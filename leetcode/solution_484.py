#!/usr/bin/env python

import unittest

class Solution(object):
    def rev(self, start, end, arr):
        for i in range((end-start)/2):
            buf = arr[i + start]
            arr[i + start] = arr[end - i - 1]
            arr[end - i - 1] = buf

    def findPermutation(self, s):
        """
        :type s: str
        :rtype: List[int]
        """

        res = range(1, len(s) + 2)

        i = 1
        while i <= len(s):
            j = i
            while i <= len(s) and s[i-1] == 'D':
                i += 1
            self.rev(j - 1, i, res)
            i += 1
        return res

class TestSolution(unittest.TestCase):

    def test_findPermutation(self):
        solution = Solution()
        self.assertEqual(solution.findPermutation('I'), [1, 2])
        self.assertEqual(solution.findPermutation('III'), [1, 2, 3, 4])
        self.assertEqual(solution.findPermutation('DD'), [3, 2, 1])
        self.assertEqual(solution.findPermutation('DDD'), [4, 3, 2, 1])
        self.assertEqual(solution.findPermutation('D'), [2, 1])
        self.assertEqual(solution.findPermutation('DI'), [2, 1, 3])
        self.assertEqual(solution.findPermutation('DDIIDI'), [3, 2, 1, 4, 6, 5, 7])

if __name__ == '__main__':
    unittest.main()
