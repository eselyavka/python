import unittest
from collections import defaultdict


class Solution(object):
    def countLargestGroup(self, n):
        """
        :type n: int
        :rtype: int
        """

        def sum_digit(num):
            total = 0
            while num:
                total += num % 10
                num //= 10
            return total

        digit_sums = defaultdict(int)
        curr_max = -1
        for i in range(1, n + 1):
            s_digit = sum_digit(i)
            digit_sums[s_digit] += 1
            curr_max = max(curr_max, digit_sums[s_digit])

        ans = 0
        for v in digit_sums.values():
            if v == curr_max:
                ans += 1

        return ans


class TestSolution(unittest.TestCase):
    def test_countLargestGroup(self):
        solution = Solution()
        self.assertEqual(solution.countLargestGroup(13), 4)


if __name__ == '__main__':
    unittest.main()
