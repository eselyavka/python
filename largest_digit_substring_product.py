import unittest

class Solution:
    def largestDigitSubstringproduct(self, s, k):
        """
        Will determinate largest product of numbers in string
        """

        if not s:
            return 0

        n = len(s)

        if k == n:
            return s

        idx = 0

        max_product = float("-inf")
        ans = ""
        while idx < n:
            j = 0
            run_product = 1
            while j < k:
                if idx + j >= n:
                    break
                run_product *= int(s[idx + j])
                j += 1
            if run_product > max_product:
                max_product = run_product
                ans = s[idx:min(idx + j,n)]
            idx += 1

        return ans


class TestSolution(unittest.TestCase):
    def test_largestDigitSubstringproduct(self):
        solution = Solution()
        self.assertEqual(solution.largestDigitSubstringproduct("809723", 2), "97")
        self.assertEqual(solution.largestDigitSubstringproduct("123456", 3), "456")


if __name__ == '__main__':
    unittest.main()
