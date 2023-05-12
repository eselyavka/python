import unittest


class Solution(object):
    def mostPoints(self, questions):
        """
        :type questions: List[List[int]]
        :rtype: int
        """
        n = len(questions)

        memo = [0] * n

        def dfs(i):
            if i >= n:
                return 0

            if memo[i] != 0:
                return memo[i]

            points, bpower = questions[i]

            memo[i] = max(dfs(i + 1), points + dfs(i + 1 + bpower))

            return memo[i]

        return dfs(0)


class TestSolution(unittest.TestCase):
    def test_mostPoints(self):
        solution = Solution()
        self.assertEqual(solution.mostPoints([[3, 2], [4, 3], [4, 4], [2, 5]]), 5)


if __name__ == '__main__':
    unittest.main()
