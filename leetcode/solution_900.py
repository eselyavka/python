#!/usr/bin/env python

import unittest


class RLEIterator(object):

    def __init__(self, A):
        """
        :type A: List[int]
        """
        self.d = dict()
        self.nums = []
        for i in range(1, len(A), 2):
            if A[i-1]:
                self.d[(i, A[i])] = A[i-1]
                self.nums.append((i, A[i]))

    def next(self, n):
        """
        :type n: int
        :rtype: int
        """
        try:
            element = self.nums.pop(0)
        except IndexError:
            return -1

        diff = self.d[element] - n
        if diff >= 0:
            if diff > 0:
                self.nums.insert(0, element)
            self.d[element] = diff
            return element[1]
        else:
            while diff < 0:
                try:
                    element = self.nums.pop(0)
                except IndexError:
                    return -1
                diff += self.d[element]
            self.d[element] = diff
            self.nums.insert(0, element)
            return element[1]

        return -1


class TestSolution(unittest.TestCase):
    def test_RLEIterator(self):
        solution = RLEIterator([3, 8, 0, 9, 2, 5])
        actual = []
        for num in [2, 1, 1, 2]:
            actual.append(solution.next(num))

        self.assertListEqual(actual, [8, 8, 5, -1])


if __name__ == '__main__':
    unittest.main()
