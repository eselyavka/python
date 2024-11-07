#!/usr/bin/env python

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """

        first_line = set(['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'])
        second_line = set(['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'])
        third_line = set(['z', 'x', 'c', 'v', 'b', 'n', 'm'])
        letter_lines = [first_line, second_line, third_line]

        res = list()

        for word in words:
            for line in letter_lines:
                if (set(word.lower()) & line) == set(word.lower()):
                    res.append(word)
                    break

        return res
