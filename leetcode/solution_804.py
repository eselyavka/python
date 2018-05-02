#!/usr/bin/env python

import unittest
from string import ascii_lowercase

class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse = [".-",
                 "-...",
                 "-.-.",
                 "-..",
                 ".",
                 "..-.",
                 "--.",
                 "....",
                 "..",
                 ".---",
                 "-.-",
                 ".-..",
                 "--",
                 "-.",
                 "---",
                 ".--.",
                 "--.-",
                 ".-.",
                 "...",
                 "-",
                 "..-",
                 "...-",
                 ".--",
                 "-..-",
                 "-.--",
                 "--.."]
        d = dict(map(None, [c for c in ascii_lowercase], morse))
        s = set()

        for word in words:
            word_in_morse = ''
            for c in word:
                word_in_morse += d[c]
            s.add(word_in_morse)
        return len(s)

class TestSolution(unittest.TestCase):

    def test_uniqueMorseRepresentations(self):
        solution = Solution()
        self.assertEqual(solution.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]), 2)

if __name__ == '__main__':
    unittest.main()
