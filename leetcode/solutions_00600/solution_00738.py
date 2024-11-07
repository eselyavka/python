#!/usr/bin/env python

import unittest


class Solution(object):
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N < 10:
            return N

        arr = []
        while N:
            arr.insert(0, N % 10)
            N = N // 10

        idx = 1
        while idx < len(arr) and arr[idx - 1] <= arr[idx]:
            idx += 1

        while 0 < idx < len(arr) and arr[idx - 1] > arr[idx]:
            arr[idx - 1] = arr[idx - 1] - 1
            idx -= 1

        for k in range(idx+1, len(arr)):
            arr[k] = 9

        res = 0
        pow_ = 0
        while arr:
            res += arr.pop() * pow(10, pow_)
            pow_ += 1

        return res


class TestSolution(unittest.TestCase):
    def test_monotoneIncreasingDigits(self):
        solution = Solution()
        self.assertEqual(solution.monotoneIncreasingDigits(10), 9)
        self.assertEqual(solution.monotoneIncreasingDigits(8), 8)
        self.assertEqual(solution.monotoneIncreasingDigits(1234), 1234)
        self.assertEqual(solution.monotoneIncreasingDigits(332), 299)
        self.assertEqual(solution.monotoneIncreasingDigits(120), 119)
        self.assertEqual(solution.monotoneIncreasingDigits(999998), 899999)


if __name__ == '__main__':
    unittest.main()
