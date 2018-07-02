#!/usr/bin/env python

import unittest

class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """

        res = sentence.split()
        i = 0

        while i < len(res):
            for dw in dict:
                if res[i].startswith(dw):
                    res[i] = dw
                    break
            i += 1

        return ' '.join(res)

class TestSolution(unittest.TestCase):
    def test_replaceWords(self):
        solution = Solution()
        self.assertEquals(solution.replaceWords(['cat', 'bat', 'rat'],
                                                'the cattle was rattled by the battery'),
                          'the cat was rat by the bat')

if __name__ == '__main__':
    unittest.main()
