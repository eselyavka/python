#!/usr/bin/env python

import unittest


class Solution(object):
    def letterCasePermutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n = len(s)

        def rec(i, s, local_res, res):
            if i == len(s):
                res.append("".join(local_res))
                return

            if s[i].isalpha():
                local_res[i] = s[i].lower()
                rec(i + 1, s, local_res, res)
                local_res[i] = s[i].upper()
                rec(i + 1, s, local_res, res)
            else:
                local_res[i] = s[i]
                rec(i + 1, s, local_res, res)

        local_res = [None] * n
        res = []

        rec(0, s, local_res, res)

        return res


class Solution2(object):
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
            return [""]

        for i in range(1, n - 1):
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
        self.assertListEqual(solution.letterCasePermutation("a1b2"),
                             ["a1b2", "a1B2", "A1b2", "A1B2"])
        solution2 = Solution2()
        self.assertListEqual(sorted(solution2.letterCasePermutation("a1b2")),
                             sorted(["a1b2", "a1B2", "A1b2", "A1B2"]))


if __name__ == '__main__':
    unittest.main()
