#!/usr/bin/env python

import unittest


class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        if not num:
            return num

        res = 0
        while num:
            if num % 2 == 0:
                num = num >> 1
            else:
                num = num - 1
            res += 1

        return res


class TestSolution(unittest.TestCase):

    def test_numberOfSteps(self):
        solution = Solution()
        self.assertEqual(solution.numberOfSteps(14), 6)


if __name__ == '__main__':
    unittest.main()
