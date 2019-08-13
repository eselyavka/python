#!/usr/bin/env python

import unittest
from collections import Counter, defaultdict

class FreqStack(object):

    def __init__(self):
        self.counter = Counter()
        self.freq = defaultdict(list)
        self.max_freq = 0

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.counter[x] += 1
        self.freq[self.counter[x]].append(x)
        self.max_freq = max(self.counter[x], self.max_freq)

    def pop(self):
        """
        :rtype: int
        """
        res = self.freq[self.max_freq].pop()
        if not self.freq[self.max_freq]:
            self.max_freq -= 1

        self.counter[res] -= 1

        return res


class TestSolution(unittest.TestCase):
    def test_FreqStack(self):
        solution = FreqStack()
        _ = [solution.push(x) for x in [5, 7, 5, 7, 4, 5]]
        self.assertEqual(solution.pop(), 5)
        self.assertEqual(solution.pop(), 7)
        self.assertEqual(solution.pop(), 5)
        self.assertEqual(solution.pop(), 4)

        solution = FreqStack()
        _ = [solution.push(x) for x in [4, 0, 9, 3, 4, 2]]
        self.assertEqual(solution.pop(), 4)
        solution.push(1)
        self.assertEqual(solution.pop(), 1)
        solution.push(1)
        self.assertEqual(solution.pop(), 1)
        solution.push(4)
        self.assertEqual(solution.pop(), 4)
        self.assertEqual(solution.pop(), 2)
        self.assertEqual(solution.pop(), 3)
        self.assertEqual(solution.pop(), 9)
        self.assertEqual(solution.pop(), 0)

        solution = FreqStack()
        _ = [solution.push(x) for x in [1, 0, 0, 1, 5, 4, 1, 5, 1, 6]]
        self.assertEqual(solution.pop(), 1)
        self.assertEqual(solution.pop(), 1)
        self.assertEqual(solution.pop(), 5)
        self.assertEqual(solution.pop(), 1)
        self.assertEqual(solution.pop(), 0)
        self.assertEqual(solution.pop(), 6)
        self.assertEqual(solution.pop(), 4)
        self.assertEqual(solution.pop(), 5)
        self.assertEqual(solution.pop(), 0)
        self.assertEqual(solution.pop(), 1)


if __name__ == '__main__':
    unittest.main()
