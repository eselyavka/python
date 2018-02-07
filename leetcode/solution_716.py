#!/usr/bin/env python

import unittest

class MaxStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self._max = None

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self._max = max(self._max, x) if self._max is not None else x
        self.stack.append(x)

    def pop(self):
        """
        :rtype: int
        """
        buf = self.stack.pop() if not self._is_empty() else None

        if buf == self._max:
            self._max = max(self.stack) if not self._is_empty() else None

        return buf

    def top(self):
        """
        :rtype: int
        """

        return self.stack[-1] if not self._is_empty() else None

    def peekMax(self):
        """
        :rtype: int
        """

        return self._max

    def popMax(self):
        """
        :rtype: int
        """
        i = 1
        buf = self._max

        while i <= len(self.stack):
            if self.stack[-i] == self._max:
                del self.stack[-i]
                break
            i += 1
        self._max = max(self.stack) if not self._is_empty() else None

        return buf

    def _is_empty(self):
        return len(self.stack) == 0

class TestMaxStack(unittest.TestCase):

    def test_MaxStack(self):
        stack = MaxStack()
        stack.push(5)
        stack.push(1)
        stack.push(5)
        self.assertEqual(stack.top(), 5)
        self.assertEqual(stack.popMax(), 5)
        self.assertEqual(stack.top(), 1)
        self.assertEqual(stack.peekMax(), 5)
        self.assertEqual(stack.pop(), 1)
        self.assertEqual(stack.top(), 5)
        self.assertEqual(stack.popMax(), 5)
        self.assertIsNone(stack.top())
        stack.push(1)
        self.assertEqual(stack.top(), 1)
        self.assertEqual(stack.peekMax(), 1)
        self.assertEqual(stack.popMax(), 1)

if __name__ == '__main__':
    unittest.main()
