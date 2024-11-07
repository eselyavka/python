#!/usr/bin/env python

import unittest
from collections import Counter


class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        if not secret:
            return "0A0B"

        bulls = 0
        cnt_guess = Counter(guess)
        cnt_secret = Counter(secret)

        for i, c in enumerate(secret):
            if c == guess[i]:
                bulls += 1
                cnt_guess[c] -= 1
                cnt_secret[c] -= 1

        cows = sum((cnt_guess & cnt_secret).values())

        return "{}A{}B".format(bulls, cows)


class TestSolution(unittest.TestCase):
    def test_getHint(self):
        solution = Solution()
        self.assertEqual(solution.getHint('1123', '0111'), '1A1B')


if __name__ == '__main__':
    unittest.main()
