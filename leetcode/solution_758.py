#!/usr/bin/env python

import unittest
import itertools

class Solution(object):
    def boldWords(self, words, S):
        """
        :type words: List[str]
        :type S: str
        :rtype: str
        """
        if not S:
            return S

        bit_mask = [0 for _ in range(len(S))]
        i = 0
        for i in xrange(len(S)):
            prefix = S[i:]
            for word in words:
                if prefix.startswith(word):
                    for j in xrange(i, min(i + len(word), len(S))):
                        bit_mask[j] = 1
        res = []

        for incl, grp in itertools.groupby(zip(S, bit_mask), lambda z: z[1]):
            if incl: res.append("<b>")
            res.append("".join(z[0] for z in grp))
            if incl: res.append("</b>")

        return "".join(res)

class TestSolution(unittest.TestCase):

    def test_boldWords(self):
        solution = Solution()

        self.assertEqual(solution.boldWords(["ab", "bc"], "aabcd"), "a<b>abc</b>d")
        self.assertEqual(solution.boldWords(["ab", "bcd"], "aabcd"), "a<b>abcd</b>")
        self.assertEqual(solution.boldWords(["a", "bcd"], "a"), "<b>a</b>")
        self.assertEqual(solution.boldWords(["a", "bcd"], ""), "")
        self.assertEqual(solution.boldWords(["ac", "bcd"], "ac"), "<b>ac</b>")
        self.assertEqual(solution.boldWords([""], "ac"), "ac")

if __name__ == '__main__':
    unittest.main()
