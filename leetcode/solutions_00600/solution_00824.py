#!/usr/bin/env python

import unittest

class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        res = []
        vowels = {'a', 'e', 'i', 'o', 'u'}

        for i, word in enumerate(S.split()):

            if word[0].lower() in vowels:
                payload = word + 'ma'
            else:
                payload = word[1:] + word[0] + 'ma'

            payload = payload + 'a' * (i+1)

            res.append(payload)

        return ' '.join(res)

class TestSolution(unittest.TestCase):

    def test_toGoatLatin(self):
        solution = Solution()

        self.assertEqual(solution.toGoatLatin("I speak Goat Latin"),
                         "Imaa peaksmaaa oatGmaaaa atinLmaaaaa")
        self.assertEqual(solution.toGoatLatin("The quick brown fox jumped over the lazy dog"),
                         "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa \
                         umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa")

if __name__ == '__main__':
    unittest.main()
