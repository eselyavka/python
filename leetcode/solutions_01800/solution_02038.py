import unittest


class Solution(object):
    def winnerOfGame(self, colors):
        """
        :type colors: str
        :rtype: bool
        """
        n = len(colors)

        if n < 3:
            return False

        alice = 0
        bob = 0

        for i in range(1, n - 1):
            if colors[i] == "A" and colors[i - 1] == "A" and colors[i + 1] == "A":
                alice += 1
            if colors[i] == "B" and colors[i - 1] == "B" and colors[i + 1] == "B":
                bob += 1

        return bob < alice


class TestSolution(unittest.TestCase):
    def test_winnerOfGame(self):
        solution = Solution()
        self.assertFalse(solution.winnerOfGame("ABBBBBBBAAA"))


if __name__ == '__main__':
    unittest.main()
