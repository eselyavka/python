#!/usr/bin/env python

import unittest

class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        if not A:
            return A

        if len(A) == 1:
            return A

        s = reduce(lambda x, y: set(x) & set(y), A)
        res = []
        for c in s:
            _min = float('+inf')
            for word in A:
                _min = min(_min, word.count(c))
            res.extend([c] * _min)

        return res


class TestSolution(unittest.TestCase):
    def test_commonChars(self):
        solution = Solution()
        self.assertListEqual(solution.commonChars(["bella", "label", "roller"]), ["e", "l", "l"])
        self.assertListEqual(solution.commonChars(["cool", "lock", "cook"]), ["c", "o"])
        self.assertListEqual(solution.commonChars(["cool"]), ["cool"])
        self.assertListEqual(solution.commonChars(["cool", "dry"]), [])


if __name__ == '__main__':
    unittest.main()
