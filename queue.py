#!/usr/bin/env python

import unittest

class Queue(object):

    def __init__(self):
        self._queue = list()

    def add(self, value):
        """
        Add element as the last item in the Queue.
        """
        self._queue = self._queue + [value]

    def remove(self):
        """
        Remove element from the front of the Queue and return it's value.
        """
        payload = self._queue[0]
        self._queue = self._queue[1:]
        return payload

    def is_empty(self):
        """
        Returns a boolean indicating if the Queue is empty.
        """
        return len(self._queue) == 0

    def size(self):
        """
        Return size of the Queue.
        """
        return len(self._queue)

class TestQueue(unittest.TestCase):

    def test_queue(self):
        solution = Queue()
        [solution.add(num) for num in range(6)]
        self.assertEqual(solution.remove(), 0)
        self.assertEqual(solution.remove(), 1)
        self.assertEqual(solution.size(), 4)
        self.assertFalse(solution.is_empty())
        self.assertEqual(solution.remove(), 2)
        self.assertEqual(solution.remove(), 3)
        self.assertEqual(solution.remove(), 4)
        self.assertEqual(solution.remove(), 5)
        self.assertTrue(solution.is_empty())

if __name__ == '__main__':
    unittest.main()
