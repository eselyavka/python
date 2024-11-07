#!/usr/bin/env python

import unittest


class Solution(object):
    def __init__(self):
        self.cnt = 0

    def countVowelStrings(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.cnt = 0

        vowels = ['a', 'e', 'i', 'o', 'u']
        mapping = {'a': 0,
                   'e': 1,
                   'i': 2,
                   'o': 3,
                   'u': 4}

        length = len(vowels)

        def rec(char, size):
            if size == n:
                self.cnt += 1
                return

            for i in xrange(mapping[char], length):
                rec(vowels[i], size+1)

        rec('a', 0)

        return self.cnt


class TestSolution(unittest.TestCase):

    def test_countVowelStrings(self):
        solution = Solution()
        self.assertEqual(solution.countVowelStrings(2), 15)


if __name__ == '__main__':
    unittest.main()
