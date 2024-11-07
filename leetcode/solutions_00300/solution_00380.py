#!/usr/bin/env python

import unittest
import random

class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s = set()

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.s:
            return False

        self.s.add(val)
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.s:
            self.s.remove(val)
            return True

        return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        if self.s:
            return random.choice(list(self.s))

class TestSolution(unittest.TestCase):

    def test_RandomizedSet(self):
        solution = RandomizedSet()
        self.assertTrue(solution.insert(1))
        self.assertFalse(solution.remove(2))
        self.assertTrue(solution.insert(2))
        self.assertTrue(solution.getRandom() in [1, 2])
        self.assertTrue(solution.remove(1))
        self.assertFalse(solution.insert(2))
        self.assertEqual(solution.getRandom(), 2)

        solution = RandomizedSet()


if __name__ == '__main__':
    unittest.main()
