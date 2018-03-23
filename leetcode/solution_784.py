#!/usr/bin/env python

import unittest

class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        res = []
        for i in range(1 << len([c for c in S if not c.isdigit()])):
            s1 = []
            k = 0
            for c in S:
                if c.isdigit():
                    s1.append(c)
                    continue
                else:
                    if (i >> k) & 1:
                        s1.append(c.lower())
                    else:
                        s1.append(c.upper())
                    k += 1
            res.append(''.join(s1))
        return res if res else ['']

class TestSolution(unittest.TestCase):

    def test_letterCasePermutation(self):
        solution = Solution()
        self.assertEqual(solution.letterCasePermutation('12345'), ['12345'])
        self.assertEqual(solution.letterCasePermutation('ab'), ['AB', 'aB', 'Ab', 'ab'])
        self.assertEqual(solution.letterCasePermutation('a1b2'), ['A1B2',
                                                                  'a1B2',
                                                                  'A1b2',
                                                                  'a1b2'])
        self.assertEqual(solution.letterCasePermutation(''), [''])
        self.assertEqual(solution.letterCasePermutation('C'), ['C', 'c'])

if __name__ == '__main__':
    unittest.main()
