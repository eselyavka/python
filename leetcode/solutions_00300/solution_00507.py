#!/usr/bin/env python

import unittest


class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return False

        sum_ = 1
        for i in range(2, int(num ** 0.5)+1):
            if num % i == 0:
                sum_ += i + num / i

        return sum_ == num


class TestSolution(unittest.TestCase):
    def test_checkPerfectNumber(self):
        solution = Solution()
        self.assertTrue(solution.checkPerfectNumber(28))


if __name__ == '__main__':
    unittest.main()
