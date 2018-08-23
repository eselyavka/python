#!/usr/bin/env python

import unittest

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        size = len(s)
        i = 0
        ds, stack = [], []
        times = ''
        while i < size:
            if s[i].isdigit():
                times += s[i]
            elif s[i] == ']':
                buf = ''
                k = len(stack) - 1
                while stack[k] != '[':
                    buf = stack.pop() + buf
                    k -= 1

                stack.pop()
                stack.append(buf * ds.pop())
            else:
                stack.append(s[i])
                if times:
                    ds.append(int(times))

                times = ''

            i += 2

        return ''.join(stack)

class TestSolution(unittest.TestCase):

    def test_decodeString(self):

        solution = Solution()

        self.assertEqual(solution.decodeString("3[a]2[bc]"), "aaabcbc")
        self.assertEqual(solution.decodeString("3[a2[c]]"), "accaccacc")
        self.assertEqual(solution.decodeString("2[abc]3[cd]ef"), "abcabccdcdcdef")
        self.assertEqual(solution.decodeString("ef3[cd]"), "efcdcdcd")

if __name__ == '__main__':
    unittest.main()
