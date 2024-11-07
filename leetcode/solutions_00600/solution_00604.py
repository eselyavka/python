#!/usr/bin/env python

import unittest

class MyIt(object):
    def __init__(self, alpha, times):
        self.alpha = alpha
        self.times = times
        self.n = None
        self._alpha = None

    def __iter__(self):
        return self

    def next(self):
        if self.alpha and self.times or self.n:
            if not self.n:
                self._alpha = self.alpha.pop(0)
                self.n = self.times.pop(0)
            if self.n > 0:
                self.n -= 1
                return self._alpha
        raise StopIteration

class StringIterator(object):

    def __init__(self, compressedString):
        """
        :type compressedString: str
        """
        self._hasnext = None
        i, _num = 0, ''
        self.stack_alpha, self.stack_digit = [], []

        if compressedString:
            while i < len(compressedString):
                if compressedString[i].isalpha():
                    if self.stack_alpha:
                        self.stack_alpha.append(compressedString[i])
                        self.stack_digit.append(int(_num))
                        _num = ''
                    else:
                        self.stack_alpha.append(compressedString[i])
                else:
                    _num += compressedString[i]

                if i == len(compressedString) - 1:
                    self.stack_digit.append(int(_num))

                i += 1

        self.it = iter(MyIt(self.stack_alpha, self.stack_digit))

    def next(self):
        """
        :rtype: str
        """
        if self._hasnext:
            res = self._hasnext
            self._hasnext = None
            return res
        else:
            try:
                return self.it.next()
            except StopIteration:
                return ' '

    def hasNext(self):
        """
        :rtype: bool
        """
        if self._hasnext:
            return True
        else:
            try:
                self._hasnext = self.it.next()
            except StopIteration:
                return False

        return True

class TestSolution(unittest.TestCase):
    def test_StringIterator(self):
        solution = StringIterator('L1e2t1C1o1d1e1')
        self.assertListEqual([solution.next() for _ in range(6)],
                             ["L", "e", "e", "t", "C", "o"])
        self.assertTrue(solution.hasNext())
        self.assertEqual(solution.next(), "d")
        self.assertTrue(solution.hasNext())

        solution = StringIterator('L10e2t1C1o1d1e11')
        self.assertTrue(all([solution.next() == 'L' for _ in range(6)]))

        solution = StringIterator('L1')
        self.assertEqual(solution.next(), 'L')
        self.assertFalse(solution.hasNext())

        solution = StringIterator(None)
        self.assertEqual(solution.next(), ' ')
        self.assertFalse(solution.hasNext())

        solution = StringIterator('')
        self.assertFalse(solution.hasNext())
        self.assertEqual(solution.next(), ' ')

        solution = StringIterator('x6')
        [solution.next() for _ in range(3)]
        self.assertTrue(solution.hasNext())

if __name__ == '__main__':
    unittest.main()
