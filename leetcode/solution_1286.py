#!/usr/bin/env python

import unittest


class CombinationIterator(object):

    def __init__(self, characters, combinationLength):
        """
        :type characters: str
        :type combinationLength: int
        """
        self.res = []
        self.i = 0

        def rec(s, prefix, l, r, k, visited):
            if not k:
                for p in range(1, len(prefix)):
                    if prefix[p-1] > prefix[p]:
                        return
                self.res.append(prefix)
                return
            for i in range(l, r):
                if visited[i]:
                    continue
                visited[i] = True
                prefix_ = prefix + s[i]
                rec(s, prefix_, l+1, r, k-1, visited)
                visited[i] = False

        v = [False] * len(characters)
        rec(characters, '', 0, len(characters), combinationLength, v)

    def next(self):
        """
        :rtype: str
        """
        res = self.res[self.i]
        self.i += 1
        return res

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.i < len(self.res)


class TestSolution(unittest.TestCase):
    def test_CombinationIterator(self):
        solution = CombinationIterator('abc', 2)
        self.assertEqual(solution.next(), 'ab')
        self.assertTrue(solution.hasNext())
        self.assertEqual(solution.next(), 'ac')
        self.assertTrue(solution.hasNext())
        self.assertEqual(solution.next(), 'bc')
        self.assertFalse(solution.hasNext())


if __name__ == '__main__':
    unittest.main()
