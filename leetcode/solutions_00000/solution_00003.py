#!/usr/bin/env python

import unittest


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest_dup_free_subarray_idx = result = 0
        most_recent_occurrence = {}
        for i, char in enumerate(s):
            dup_idx = most_recent_occurrence.get(char)
            if dup_idx is not None and dup_idx >= longest_dup_free_subarray_idx:
                result = max(result, i - longest_dup_free_subarray_idx)
                longest_dup_free_subarray_idx = dup_idx + 1
            most_recent_occurrence[char] = i

        return max(result, len(s) - longest_dup_free_subarray_idx)


class Solution2(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        i = 0
        j = 1
        seen = set()

        res = 0
        buf = 0
        while i < len(s):
            if s[i] not in seen:
                buf += 1
                seen.add(s[i])
                i += 1
            else:
                res = max(buf, res)
                i = j
                j += 1
                buf = 0
                seen = set()

        return max(res, buf)


class Solution3(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        last = {}
        l = 0
        ans = 0

        for r, ch in enumerate(s):
            if ch in last:
                l = max(l, last[ch] + 1)

            last[ch] = r

            ans = max(ans, r - l + 1)

        return ans


class TestSolution(unittest.TestCase):

    def test_lengthOfLongestSubstring(self):
        solution = Solution()
        solution2 = Solution2()
        solution3 = Solution3()

        self.assertEqual(solution.lengthOfLongestSubstring("abcabcbb"), 3)
        self.assertEqual(solution.lengthOfLongestSubstring("bbbbb"), 1)
        self.assertEqual(solution.lengthOfLongestSubstring("pwwkew"), 3)
        self.assertEqual(solution.lengthOfLongestSubstring("dvdf"), 3)

        self.assertEqual(solution2.lengthOfLongestSubstring("abcabcbb"), 3)
        self.assertEqual(solution2.lengthOfLongestSubstring("bbbbb"), 1)
        self.assertEqual(solution2.lengthOfLongestSubstring("pwwkew"), 3)
        self.assertEqual(solution2.lengthOfLongestSubstring("dvdf"), 3)

        self.assertEqual(solution3.lengthOfLongestSubstring("abcabcbb"), 3)
        self.assertEqual(solution3.lengthOfLongestSubstring("bbbbb"), 1)
        self.assertEqual(solution3.lengthOfLongestSubstring("pwwkew"), 3)
        self.assertEqual(solution3.lengthOfLongestSubstring("dvdf"), 3)


if __name__ == '__main__':
    unittest.main()
