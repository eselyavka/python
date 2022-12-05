import unittest


class Solution(object):
    def partitionString(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        if len(s) == 1:
            return 1

        n = len(s)

        seen = set()

        seen.add(s[0])
        ans = 1
        for i in range(1, n):
            if s[i] in seen:
                seen = set()
                ans += 1
            seen.add(s[i])
        return ans


class TestSolution(unittest.TestCase):
    def test_partitionString(self):
        solution = Solution()
        self.assertEqual(solution.partitionString("abacaba"), 4)


if __name__ == '__main__':
    unittest.main()
