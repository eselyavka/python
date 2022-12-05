import unittest


class Solution(object):
    def bestClosingTime(self, customers):
        """
        :type customers: str
        :rtype: int
        """
        n = len(customers)
        prefix_sum = [0 for _ in range(n + 1)]

        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + int(customers[i - 1] == "N")

        suffix_sum = [0 for _ in range(n + 1)]

        for j in range(n - 1, -1, -1):
            suffix_sum[j] = suffix_sum[j + 1] + int(customers[j] == "Y")

        ans = 0, prefix_sum[0] + suffix_sum[0]
        for i in range(n + 1):
            if prefix_sum[i] + suffix_sum[i] < ans[1]:
                ans = i, prefix_sum[i] + suffix_sum[i]

        return ans[0]


class TestSolution(unittest.TestCase):
    def test_bestClosingTime(self):
        solution = Solution()
        self.assertEqual(solution.bestClosingTime("YYNY"), 2)


if __name__ == '__main__':
    unittest.main()
