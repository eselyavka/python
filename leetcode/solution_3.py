#!/usr/bin/env python

import unittest

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest_dup_free_subarray_idx = result = 0
        most_recent_occurrence = dict()
        for i, char in enumerate(s):
            if most_recent_occurrence.has_key(char):
                dup_idx = most_recent_occurrence[char]
                if dup_idx >= longest_dup_free_subarray_idx:
                    result = max(result, i - longest_dup_free_subarray_idx)
                    longest_dup_free_subarray_idx = dup_idx + 1
            most_recent_occurrence[char] = i

        return max(result, len(s) - longest_dup_free_subarray_idx)

class TestSolution(unittest.TestCase):

    def test_lengthOfLongestSubstring(self):
        solution = Solution()

        self.assertEqual(solution.lengthOfLongestSubstring("abcabcbb"), 3)
        self.assertEqual(solution.lengthOfLongestSubstring("bbbbb"), 1)
        self.assertEqual(solution.lengthOfLongestSubstring("pwwkew"), 3)
        self.assertEqual(solution.lengthOfLongestSubstring("dvdf"), 3)

if __name__ == '__main__':
    unittest.main()
