#!/usr/bin/env python

import unittest

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        if not n:
            return []

        if n % 3 == 0 and n % 5 == 0:
            return self.fizzBuzz(n-1) + ['FizzBuzz']
        if n % 3 == 0:
            return self.fizzBuzz(n-1) + ['Fizz']
        if n % 5 == 0:
            return self.fizzBuzz(n-1) + ['Buzz']

        return self.fizzBuzz(n-1) + [str(n)]

class TestSolution(unittest.TestCase):

    def test_fizzBuzz(self):
        solution = Solution()
        self.assertEqual(solution.fizzBuzz(15), ['1',
                                                 '2',
                                                 'Fizz',
                                                 '4',
                                                 'Buzz',
                                                 'Fizz',
                                                 '7',
                                                 '8',
                                                 'Fizz',
                                                 'Buzz',
                                                 '11',
                                                 'Fizz',
                                                 '13',
                                                 '14',
                                                 'FizzBuzz'])

if __name__ == '__main__':
    unittest.main()
