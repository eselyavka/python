#!/usr/bin/env python

import unittest

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        vowels = {'a', 'e', 'i', 'o', 'u'}
        s = list(s)
        left, right = 0, len(s) - 1

        while left <= right:
            lower_left, lower_right = s[left].lower(), s[right].lower()
            if lower_left in vowels and lower_right in vowels:
                s[left], s[right] = s[right], s[left]
            elif lower_left in vowels:
                right -= 1
                continue
            elif lower_right in vowels:
                left += 1
                continue

            left += 1
            right -= 1

        return ''.join(s)

class TestSolution(unittest.TestCase):

    def test_reverseVowels(self):
        solution = Solution()

        self.assertEqual(solution.reverseVowels("hello"), "holle")
        self.assertEqual(solution.reverseVowels("leetcode"), "leotcede")

if __name__ == '__main__':
    unittest.main()
