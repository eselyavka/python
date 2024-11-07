#!/usr/bin/env python

import unittest


class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = list()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.queue.insert(0, x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        element = self.queue[0]
        self.queue = self.queue[1:]
        return element

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.queue[0]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.queue) == 0


class TestSolution(unittest.TestCase):

    def test_MyStack(self):
        s = MyStack()
        s.push(1)
        s.push(2)
        self.assertEqual(s.top(), 2)
        self.assertEqual(s.top(), 2)
        self.assertFalse(s.empty())
        self.assertEqual(s.pop(), 2)
        self.assertFalse(s.empty())
        self.assertEqual(s.top(), 1)
        self.assertEqual(s.pop(), 1)
        self.assertTrue(s.empty())


if __name__ == '__main__':
    unittest.main()
