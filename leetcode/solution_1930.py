import unittest
from collections import defaultdict


class Solution(object):
    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 3:
            return 1 if s == s[::-1] else 0

        d = defaultdict(list)
        for i, c in enumerate(s):
            if d[c]:
                d[c][-1] = i
            else:
                d[c] = [i, -1]

        ans = 0
        for c in d:
            used = set()
            idx_s = set(d[c])
            for i in range(d[c][0], d[c][1]):
                if i not in idx_s and s[i] not in used:
                    ans += 1
                    used.add(s[i])

            if len(d[c]) >= 3:
                ans += 1

        return ans


class TestSolution(unittest.TestCase):
    def test_countPalindromicSubsequence(self):
        solution = Solution()
        self.assertEqual(solution.countPalindromicSubsequence("bbcbaba"), 4)


if __name__ == '__main__':
    unittest.main()
