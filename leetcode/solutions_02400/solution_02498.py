import unittest


class Solution(object):
    def maxJump(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """

        n = len(stones)
        if n == 2:
            return stones[1]

        ans = float("-inf")
        i = 0
        while i < n:
            ans = max(ans, abs(stones[i - 2] - stones[i]) if i >= 2 else stones[i])
            i += 2

        i = 1
        while i < n:
            ans = max(ans, abs(stones[i - 2] - stones[i]) if i >= 3 else stones[i])
            i += 2

        return ans


class TestSolution(unittest.TestCase):
    def test_maxJump(self):
        solution = Solution()
        self.assertEqual(solution.maxJump([0, 2, 5, 6, 7]), 5)


if __name__ == '__main__':
    unittest.main()
