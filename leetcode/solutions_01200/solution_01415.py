#!/usr/bin/env python

import unittest


class Solution(object):
    def getHappyString(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        res = []

        def generate_permutations(chars, n, current=""):
            if n == 0:
                res.append(current)
                return

            for char in chars:
                if not current or current[-1] != char:
                    generate_permutations(chars, n - 1, current + char)

        generate_permutations(['a', 'b', 'c'], n)

        res.sort()

        if k > len(res):
            return ""

        return res[k - 1]


class TestSolution(unittest.TestCase):
    def test_getHappyString(self):
        solution = Solution()
        self.assertEqual(solution.getHappyString(3, 9), 'cab')


if __name__ == '__main__':
    unittest.main()
