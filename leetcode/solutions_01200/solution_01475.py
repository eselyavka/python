import unittest


class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        ans = prices[:]

        stack = []

        n = len(prices)
        for i in range(n):
            while stack and prices[stack[-1]] >= prices[i]:
                idx = stack.pop()
                ans[idx] -= prices[i]
            stack.append(i)

        return ans


class TestSolution(unittest.TestCase):

    def test_finalPrices(self):
        solution = Solution()
        self.assertListEqual(solution.finalPrices([8, 4, 6, 2, 3]), [4, 2, 4, 2, 3])


if __name__ == '__main__':
    unittest.main()
