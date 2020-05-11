#!/usr/bin/env python

import unittest
import math


class Solution(object):
    def numPrimeArrangements(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 1

        prime = [True] * (n + 1)
        prime[0] = prime[1] = False
        for i in range(2, n + 1):
            if prime[i]:
                j = 2
                while j * i <= n:
                    prime[j*i] = False
                    j += 1

        prime_ = prime[1:]
        sum_prime = sum(prime_)
        sum_composite = len(prime_) - sum_prime

        res = (math.factorial(sum_prime) * math.factorial(sum_composite)) % (10 ** 9 + 7)

        return res


class TestSolution(unittest.TestCase):

    def test_numPrimeArrangements(self):
        solution = Solution()
        self.assertEqual(solution.numPrimeArrangements(5), 12)
        self.assertEqual(solution.numPrimeArrangements(100), 682289015)


if __name__ == '__main__':
    unittest.main()
