#!/usr/bin/env python

import unittest


class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        self.min.append(val) if not self.min else self.min.append(min(val, self.min[-1]))

    def pop(self):
        """
        :rtype: None
        """
        _ = self.min.pop()
        return self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min[-1]


class TestMinStack(unittest.TestCase):

    def test_MinStack(self):
        stack = MinStack()
        stack.push(-2)
        stack.push(0)
        stack.push(-3)
        self.assertEqual(stack.getMin(), -3)
        stack.pop()
        self.assertEqual(len(stack.stack), 2)
        self.assertEqual(stack.top(), 0)
        self.assertEqual(stack.getMin(), -2)
        stack.pop()
        self.assertEqual(len(stack.stack), 1)
        self.assertEqual(stack.top(), -2)
        self.assertEqual(stack.getMin(), -2)


if __name__ == '__main__':
    unittest.main()
