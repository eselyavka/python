import unittest


class Solution(object):
    def minChanges(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        changes = 0

        for i in range(1, n, 2):
            if s[i] != s[i - 1]:
                changes += 1

        return changes


class TestSolution(unittest.TestCase):
    def test_minChanges(self):
        solution = Solution()
        self.assertEqual(solution.minChanges("1001"), 2)


if __name__ == '__main__':
    unittest.main()
