import unittest


class Solution(object):
    def appendCharacters(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        if s == t:
            return 0

        i, j = 0, 0
        n = len(s)
        m = len(t)

        ans = m
        while i < n and j < m:
            if s[i] == t[j]:
                i += 1
                j += 1
                ans -= 1
            else:
                i += 1
        return ans


class TestSolution(unittest.TestCase):
    def test_appendCharacters(self):
        solution = Solution()
        self.assertEqual(solution.appendCharacters(s="coaching", t="coding"), 4)


if __name__ == '__main__':
    unittest.main()
