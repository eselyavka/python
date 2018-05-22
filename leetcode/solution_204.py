#!/usr/bin/env python

import unittest

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <=2:
            return 0

        prime = [True] * n
        prime[0] = prime[1] = False
        p = 2
        while (p * p <= n):
            if prime[p]:
                for i in xrange(2*p, n, p):
                    prime[i] = False
            p += 1

        return sum(prime)

class TestSolution(unittest.TestCase):
    def test_countPrimes(self):
        solution = Solution()
        self.assertEqual(solution.countPrimes(10), 4)
        self.assertEqual(solution.countPrimes(1), 0)
        self.assertEqual(solution.countPrimes(2), 0)
        self.assertEqual(solution.countPrimes(3), 1)
        self.assertEqual(solution.countPrimes(4), 2)
        self.assertEqual(solution.countPrimes(5), 2)
        self.assertEqual(solution.countPrimes(1500000), 114155)

if __name__ == '__main__':
    unittest.main()
