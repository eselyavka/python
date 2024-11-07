#!/usr/bin/env python

import unittest


class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        i, k = 1, 0
        res = []
        while i <= n and k < len(target):
            if target[k] == i:
                res.append('Push')
                k += 1
            else:
                res.extend(['Push', 'Pop'])
            i += 1

        return res


class TestSolution(unittest.TestCase):

    def test_buildArray(self):
        solution = Solution()
        self.assertListEqual(solution.buildArray([1, 3], 3), ["Push", "Push", "Pop", "Push"])


if __name__ == '__main__':
    unittest.main()
