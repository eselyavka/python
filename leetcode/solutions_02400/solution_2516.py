#!/usr/bin/env python

import unittest


class Solution(object):
    def takeCharacters(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        cnt = [0] * 3
        for c in s:
            cnt[ord(c) - ord("a")] += 1

        for v in cnt:
            if v < k:
                return -1

        left, max_window = 0, 0
        window = [0] * 3

        for right in range(n):
            window[ord(s[right]) - ord("a")] += 1

            while left <= right and (cnt[0] - window[0] < k or cnt[1] - window[1] < k or cnt[2] - window[2] < k):
                window[ord(s[left]) - ord("a")] -= 1
                left += 1

            max_window = max(max_window, right - left + 1)

        return n - max_window


class TestSolution(unittest.TestCase):
    def test_takeCharacters(self):
        solution = Solution()
        self.assertEqual(solution.takeCharacters("aabaaaacaabc", 2), 8)


if __name__ == '__main__':
    unittest.main()
