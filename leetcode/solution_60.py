#!/usr/bin/env python

import unittest


class Solution(object):
    def factorial(self, n):
        if n <= 1:
            return 1

        return n * self.factorial(n-1)

    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        arr = range(1, n+1)
        k -= 1
        res = []
        for i in range(1, n+1):
            idx = k / self.factorial(n - i)
            res.append(str(arr[idx]))
            arr.pop(idx)
            k -= idx * self.factorial(n - i)

        return ''.join(res)


class TestSolution(unittest.TestCase):
    def test_getPermutation(self):
        solution = Solution()
        self.assertEqual(solution.getPermutation(3, 3), '213')


if __name__ == '__main__':
    unittest.main()
