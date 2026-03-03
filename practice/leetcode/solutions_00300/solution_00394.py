#!/usr/bin/env python3

"""LeetCode solution 00394."""

import unittest

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        count_stack = []
        string_stack = []
        current = ''
        times = 0

        for char in s:
            if char.isdigit():
                times = times * 10 + int(char)
            elif char == '[':
                count_stack.append(times)
                string_stack.append(current)
                current = ''
                times = 0
            elif char == ']':
                current = string_stack.pop() + current * count_stack.pop()
            else:
                current += char

        return current

class TestSolution(unittest.TestCase):

    def test_decodeString(self):

        solution = Solution()

        self.assertEqual(solution.decodeString("3[a]2[bc]"), "aaabcbc")
        self.assertEqual(solution.decodeString("3[a2[c]]"), "accaccacc")
        self.assertEqual(solution.decodeString("2[abc]3[cd]ef"), "abcabccdcdcdef")
        self.assertEqual(solution.decodeString("ef3[cd]"), "efcdcdcd")

if __name__ == '__main__':
    unittest.main()
