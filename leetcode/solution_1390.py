#!/usr/bin/env python

import unittest


class Solution(object):
    def sumFourDivisors(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def divisors(n):
            divisors = [1, n]
            i = 2
            while i ** 2 <= n:
                if len(divisors) > 4:
                    return []
                if n % i == 0:
                    if n / i != i:
                        divisors.extend([i, n / i])
                    else:
                        divisors.append(n/i)
                i += 1

            return divisors if len(divisors) == 4 else []

        res = 0
        for n in nums:
            divisors_ = divisors(n)
            res += sum(divisors_) if divisors_ else 0

        return res


class TestSolution(unittest.TestCase):

    def test_sumFourDivisors(self):
        solution = Solution()
        self.assertEqual(solution.sumFourDivisors([21, 4, 7]), 32)


if __name__ == '__main__':
    unittest.main()
