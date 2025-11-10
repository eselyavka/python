import unittest


class Solution(object):
    def minCost(self, colors, neededTime):
        """
        :type colors: str
        :type neededTime: List[int]
        :rtype: int
        """
        ans = 0
        best = 0

        prev = None
        for idx, curr in enumerate(colors):
            if curr == prev:
                ans += min(best, neededTime[idx])
                best = max(best, neededTime[idx])
            else:
                prev = curr
                best = neededTime[idx]

        return ans


class TestSolution(unittest.TestCase):
    def test_minCost(self):
        solution = Solution()
        self.assertEqual(solution.minCost("aaabbbabbbb", [3, 5, 10, 7, 5, 3, 5, 5, 4, 8, 1]), 26)


if __name__ == '__main__':
    unittest.main()
