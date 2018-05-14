#!/usr/bin/env python

import unittest

class MinStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self._min = None

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self._min = min(self._min, x) if self._min is not None else x
        self.stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        buf = self.stack.pop() if not self._is_empty() else None

        if buf == self._min:
            self._min = min(self.stack) if not self._is_empty() else None

    def top(self):
        """
        :rtype: int
        """

        return self.stack[-1] if not self._is_empty() else None

    def getMin(self):
        """
        :rtype: int
        """

        return self._min if not self._is_empty() else None

    def _is_empty(self):
        return len(self.stack) == 0

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
        stack.pop()
        self.assertIsNone(stack.getMin())
        self.assertIsNone(stack.top())

if __name__ == '__main__':
    unittest.main()
