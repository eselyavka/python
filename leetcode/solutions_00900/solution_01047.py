#!/usr/bin/env python

import unittest


class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        if len(S) == 1:
            return S

        s = list()

        for c in S:
            con = False

            if s and c == s[-1]:
                _ = s.pop()
                con = True

            if con:
                continue

            s.append(c)

        return ''.join(s)


class TestSolution(unittest.TestCase):
    def test_removeDuplicates(self):
        solution = Solution()
        self.assertEqual(solution.removeDuplicates("abbaca"), "ca")


if __name__ == '__main__':
    unittest.main()
