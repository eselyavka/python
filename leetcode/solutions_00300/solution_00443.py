#!/usr/bin/env python

import unittest


class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """

        i = 0

        while i < len(chars):
            j = i + 1
            cnt = 1

            while j < len(chars):
                if chars[i] == chars[j]:
                    del chars[j]
                    cnt += 1
                    continue
                break

            if cnt > 1:
                tokens = list(str(cnt))
                i += len(tokens)
                while tokens:
                    chars.insert(j, tokens.pop())

            i += 1

        return len(chars)


class TestSolution(unittest.TestCase):
    def test_compress(self):
        solution = Solution()
        chars = ["a", "a", "a", "b", "b", "a", "a"]
        self.assertEqual(solution.compress(chars), 6)
        self.assertListEqual(chars, ["a", "3", "b", "2", "a", "2"])

        chars = ["a", "b", "c"]
        self.assertEqual(solution.compress(chars), 3)
        self.assertListEqual(chars, ["a", "b", "c"])

        chars = ["a", "a", "b", "b", "c", "c", "c"]
        self.assertEqual(solution.compress(chars), 6)
        self.assertListEqual(chars, ["a", "2", "b", "2", "c", "3"])

        chars = ["a"]
        self.assertEqual(solution.compress(chars), 1)
        self.assertListEqual(chars, ["a"])

        chars = ["a", "a", "b"]
        self.assertEqual(solution.compress(chars), 3)
        self.assertListEqual(chars, ["a", "2", "b"])

        chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
        self.assertEqual(solution.compress(chars), 4)
        self.assertListEqual(chars, ["a", "b", "1", "2"])

        chars = ["p", "p", "p", "p", "m", "m", "b", "b", "b", "b", "b", "u", "u", "r", "r", "u", "n", "n", "n", "n",
                 "n", "n", "n", "n", "n", "n", "n", "u", "u", "u", "u", "a", "a", "u", "u", "r", "r", "r", "s", "s",
                 "a", "a", "y", "y", "y", "g", "g", "g", "g", "g"]
        self.assertEqual(solution.compress(chars), 30)
        self.assertListEqual(chars,
                             ["p", "4", "m", "2", "b", "5", "u", "2", "r", "2", "u", "n", "1", "1", "u", "4", "a", "2",
                              "u", "2", "r", "3", "s", "2", "a", "2", "y", "3", "g", "5"])

        chars = ["b", "l", "l", "l", "l", "l", "l", "4", "4", "W", "W", "&", "d", "d", "d", "@", "D", "D", ".", ".",
                 ".", "8", "8", "8", "U", "V", ">", "J", "J", "k", "H", "H", "=", "l", "[", "[", "[", "[", "[", "[",
                 "[", "a", "a", "'", "<", "[", "[", "y", "V", "l", "l", "'", "$", "E", "`", "v", "k", "E", "E", "t",
                 "t", "t", "t", "t", "=", "=", "0", "C", "a", "l", "l", "l", "r", "R", "M", "M", "c", "c", "c", "A",
                 "A", "S", "9", "9", "9", "9", ")", ")", "\\", "s", "\\", "\\", "y", "W", "W", "W", "J", "J", "J", "J",
                 "6", "6", "<", "<", "E", "u", "e", "e", "e", "e", "e", "e", "e", "e", "e", "9", "9", "9", "9", "R",
                 "8", "?", "F", "3", "&", "&", "&", "&", "f", "%", "%", "2", "2", "2", ")", ")", ")", "J", "p", "|",
                 "D", "D", "D", "s", "t", "V", "V", "?", "^", "^", "S", "3", "3", "3", "3", "h", "*", "|", "|", "b",
                 "b", "a", "a", "a", "r", "r", "r", "r", "J", ".", "^", "^", "~", "g", ":", ":", ":", "(", "4", "4",
                 "4", "4", "w", "w", "w", "w", "w", "w", "w", "C", "?", "=", "d", "L", ":", "0", "0", "c", "w", "w",
                 "w", "w", "w", "w", "{", "{", "t", "k", "k", "k", "&", "&", "&", "h", "j", "j", "j", "0", "3", "l",
                 ";", ";", ";", ";", ";", ".", ".", ".", "%", "1", "1", "1", "l", "9", "?", "?", "?", "t", ">", "E",
                 "N", "N", "@", ">", ".", ".", "I", "a", "a", "a", "a", "B", "7", "7", "{", "o", "o", "-", "+", "+",
                 "+", "+", "o", "o", "}", "B", "B", "r", "r", "r", "q", "4", "4", "4", "9", "W", "W", "W", "W", "W",
                 "'", "'", "'", "g", "J", "(", "(", "(", "(", "t", "t", "?", ";", "g", "g", "g", "0", "]", "]", "]"]
        self.assertEqual(solution.compress(chars), 224)
        self.assertListEqual(chars,
                             ["b", "l", "6", "4", "2", "W", "2", "&", "d", "3", "@", "D", "2", ".", "3", "8", "3", "U",
                              "V", ">", "J", "2", "k", "H", "2", "=", "l", "[", "7", "a", "2", "'", "<", "[", "2", "y",
                              "V", "l", "2", "'", "$", "E", "`", "v", "k", "E", "2", "t", "5", "=", "2", "0", "C", "a",
                              "l", "3", "r", "R", "M", "2", "c", "3", "A", "2", "S", "9", "4", ")", "2", "\\", "s",
                              "\\", "2", "y", "W", "3", "J", "4", "6", "2", "<", "2", "E", "u", "e", "9", "9", "4", "R",
                              "8", "?", "F", "3", "&", "4", "f", "%", "2", "2", "3", ")", "3", "J", "p", "|", "D", "3",
                              "s", "t", "V", "2", "?", "^", "2", "S", "3", "4", "h", "*", "|", "2", "b", "2", "a", "3",
                              "r", "4", "J", ".", "^", "2", "~", "g", ":", "3", "(", "4", "4", "w", "7", "C", "?", "=",
                              "d", "L", ":", "0", "2", "c", "w", "6", "{", "2", "t", "k", "3", "&", "3", "h", "j", "3",
                              "0", "3", "l", ";", "5", ".", "3", "%", "1", "3", "l", "9", "?", "3", "t", ">", "E", "N",
                              "2", "@", ">", ".", "2", "I", "a", "4", "B", "7", "2", "{", "o", "2", "-", "+", "4", "o",
                              "2", "}", "B", "2", "r", "3", "q", "4", "3", "9", "W", "5", "'", "3", "g", "J", "(", "4",
                              "t", "2", "?", ";", "g", "3", "0", "]", "3"])


if __name__ == '__main__':
    unittest.main()
