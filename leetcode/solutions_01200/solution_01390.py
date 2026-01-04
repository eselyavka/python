#!/usr/bin/env python
import math
import unittest


class Solution(object):
    def sumFourDivisors(self, nums):
        ans = 0

        for num in nums:
            cnt = 2
            s = 1 + num
            limit = int(math.sqrt(num))

            for d in range(2, limit + 1):
                if num % d == 0:
                    other = num // d
                    if other == d:
                        cnt += 1
                        s += d
                    else:
                        cnt += 2
                        s += d + other

                    if cnt > 4:
                        break

            if cnt == 4:
                ans += s

        return ans


class TestSolution(unittest.TestCase):

    def test_sumFourDivisors(self):
        solution = Solution()
        self.assertEqual(solution.sumFourDivisors([21, 4, 7]), 32)


if __name__ == '__main__':
    unittest.main()
