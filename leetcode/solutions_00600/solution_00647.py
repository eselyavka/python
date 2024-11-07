#!/usr/bin/env python

import unittest


class Solution(object):

    def _rec(self, s, idx=1):
        if not s:
            return 0

        if idx > len(s):
            return self._rec(s[1:], 1)

        ss = s[:idx]

        if ss == ss[::-1]:
            return 1 + self._rec(s, idx + 1)

        return self._rec(s, idx + 1)

    def _itr(self, s):
        cnt = 0
        for i in range(len(s)):
            buf = s[i]
            cnt += 1
            for j in range(i+1, len(s)):
                buf += s[j]
                if buf == buf[::-1]:
                    cnt += 1
        return cnt

    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        #return self._rec(s)
        return self._itr(s)


class Solution2(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [None for _ in range(n)]
        ans = 0

        for j in range(n):
            for i in range(j+1):
                if j == i:
                    dp[i] = True
                elif j == i+1:
                    dp[i] = (s[i] == s[j])
                else:
                    dp[i] = (dp[i+1] and s[i] == s[j])
                if dp[i]:
                    ans += 1

        return ans


class TestSolution(unittest.TestCase):

    def test_countSubstrings(self):
        s1 = 'abc'
        s2 = 'aaa'
        s3 = 'abctstdef'
        s4 = 'a'

        solution = Solution()

        self.assertEqual(solution.countSubstrings(s1), 3)
        self.assertEqual(solution.countSubstrings(s2), 6)
        self.assertEqual(solution.countSubstrings(s3), 10)
        self.assertEqual(solution.countSubstrings(s4), 1)
        self.assertEqual(solution.countSubstrings(s4*999), 499500)

        solution2 = Solution2()
        self.assertEqual(solution2.countSubstrings(s1), 3)
        self.assertEqual(solution2.countSubstrings(s2), 6)
        self.assertEqual(solution2.countSubstrings(s3), 10)
        self.assertEqual(solution2.countSubstrings(s4), 1)
        self.assertEqual(solution2.countSubstrings(s4*999), 499500)


if __name__ == '__main__':
    unittest.main()
