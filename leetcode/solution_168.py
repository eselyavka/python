#!/usr/bin/env python

import unittest
from string import ascii_uppercase

class Solution(object):
    def convertToTitle(self, n):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {x+1:ascii_uppercase[x] for x in range(len(ascii_uppercase))}

        if n <= 26:
            return d[n]

        return (self.convertToTitle((n//26-1) if n%26 == 0 else n//26) +
                self.convertToTitle(26 if n%26 == 0 else n%26))

class TestSolution(unittest.TestCase):

    def test_convertToTitle(self):
        solution = Solution()
        d = {x+1:ascii_uppercase[x] for x in range(len(ascii_uppercase))}

        for i in range(1, 27):
            self.assertEqual(solution.convertToTitle(i), d[i])

        self.assertEqual(solution.convertToTitle(27), 'AA')
        self.assertEqual(solution.convertToTitle(28), 'AB')
        self.assertEqual(solution.convertToTitle(1015), 'AMA')
        self.assertEqual(solution.convertToTitle(51), 'AY')
        self.assertEqual(solution.convertToTitle(52), 'AZ')

if __name__ == '__main__':
    unittest.main()
