#!/usr/bin/env python

import unittest


class Solution(object):
    def __init__(self):
        self.res = 0

    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        if len(tiles) == 1:
            return 1

        capital_letters = [0] * 26
        for letter in tiles:
            capital_letters[ord(letter) - ord('A')] += 1

        def rec(nums):
            for i in range(26):
                if nums[i] > 0:
                    self.res += 1
                    nums[i] -= 1
                    rec(nums)
                    nums[i] += 1

        rec(capital_letters)

        return self.res


class TestSolution(unittest.TestCase):
    def test_numTilePossibilities(self):
        solution = Solution()
        self.assertEqual(solution.numTilePossibilities('AAB'), 8)


if __name__ == '__main__':
    unittest.main()
