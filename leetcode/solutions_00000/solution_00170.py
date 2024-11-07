#!/usr/bin/env python

import unittest

class TwoSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.numbers = {}

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """
        if self.numbers.has_key(number):
            self.numbers[number] += 1
        else:
            self.numbers[number] = 1

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """

        for element in self.numbers:
            term = value - element
            if term in self.numbers and (term != element or self.numbers[element] > 1):
                return True

        return False

class TestSolution(unittest.TestCase):

    def test_TwoSums(self):
        solution = TwoSum()
        [solution.add(x) for x in [1, 3, 5]]
        solution2 = TwoSum()
        solution2.add(0)
        solution3 = TwoSum()
        [solution3.add(x) for x in [3, 2, 1]]

        self.assertTrue(solution.find(4))
        self.assertFalse(solution.find(7))
        self.assertFalse(solution2.find(0))
        self.assertFalse(solution3.find(2))
        self.assertTrue(solution3.find(3))
        self.assertTrue(solution3.find(4))
        self.assertTrue(solution3.find(5))
        self.assertFalse(solution3.find(6))

if __name__ == '__main__':
    unittest.main()
