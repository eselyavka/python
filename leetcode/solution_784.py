#!/usr/bin/env python

import unittest


class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        res = []
        n = 1 << len([c for c in S if c.isalpha()])

        if n > 1:
            res.append(S.upper())
            res.append(S.lower())
        elif n == 1:
            res.append(S)
        else:
            return ['']

        for i in range(1, n-1):
            buf = []
            k = 0
            for c in S:
                if c.isdigit():
                    buf.append(c)
                else:
                    if (i >> k) & 1:
                        buf.append(c.lower())
                    else:
                        buf.append(c.upper())
                    k += 1
            res.append(''.join(buf))

        return res


class TestSolution(unittest.TestCase):

    def test_letterCasePermutation(self):
        solution = Solution()
        self.assertListEqual(sorted(solution.letterCasePermutation("a1b2")),
                             sorted(["a1b2", "a1B2", "A1b2", "A1B2"]))


if __name__ == '__main__':
    unittest.main()
