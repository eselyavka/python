import unittest


class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        vowels = {"a", "e", "i", "o", "u"}

        cnt = 0
        for i in range(k):
            cnt += 1 if s[i] in vowels else 0

        ans = cnt
        n = len(s)
        for i in range(k, n):
            cnt += 1 if s[i] in vowels else 0
            cnt -= 1 if s[i - k] in vowels else 0
            ans = max(ans, cnt)

        return ans


class TestSolution(unittest.TestCase):
    def test_maxVowels(self):
        solution = Solution()
        self.assertEqual(solution.maxVowels("abciiidef", 3), 3)


if __name__ == '__main__':
    unittest.main()
