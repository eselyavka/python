#!/usr/bin/env python

import unittest


class CustomStack(object):

    def __init__(self, maxSize):
        """
        :type maxSize: int
        """
        self.stack = []
        self.size = maxSize

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.stack) == self.size:
            return

        self.stack.append(x)

    def pop(self):
        """
        :rtype: int
        """
        try:
            return self.stack.pop()
        except IndexError:
            return -1

    def increment(self, k, val):
        """
        :type k: int
        :type val: int
        :rtype: None
        """
        for i in range(min(k, len(self.stack))):
            self.stack[i] += val


class TestSolution(unittest.TestCase):
    def test_CustomStack(self):
        solution = CustomStack(3)
        solution.push(1)
        solution.push(2)
        self.assertEqual(solution.pop(), 2)
        solution.push(2)
        solution.push(3)
        solution.push(4)
        solution.increment(5, 100)
        self.assertListEqual(solution.stack, [101, 102, 103])
        solution.increment(2, 100)
        self.assertListEqual(solution.stack, [201, 202, 103])


if __name__ == '__main__':
    unittest.main()
