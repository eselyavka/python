#!/usr/bin/env python3

"""LeetCode solution 00648."""

import unittest

class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """

        res = sentence.split()
        i = 0

        while i < len(res):
            for dw in dictionary:
                if res[i].startswith(dw):
                    res[i] = dw
                    break
            i += 1

        return ' '.join(res)

class TestSolution(unittest.TestCase):
    def test_replaceWords(self):
        solution = Solution()
        self.assertEqual(solution.replaceWords(['cat', 'bat', 'rat'],
                                               'the cattle was rattled by the battery'),
                         'the cat was rat by the bat')

if __name__ == '__main__':
    unittest.main()
