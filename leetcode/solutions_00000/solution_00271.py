#!/usr/bin/env python

import unittest

class Codec(object):

    def encode(self, strs):
        """
        Encodes a list of strings to a single string.
        :type strs: List[str]
        :rtype: str
        """
        return chr(0).join(strs) if strs else None

    def decode(self, s):
        """
        Decodes a single string to a list of strings.
        :type s: str
        :rtype: List[str]
        """
        return s.split(chr(0)) if s is not None else []

class TestSolution(unittest.TestCase):
    def test_codec(self):
        solution = Codec()

        payload = ['abc', 'aka', 'ena']
        self.assertEqual(solution.decode(solution.encode(payload)), payload)

        payload = ['abc', 'aka', 'ena', '']
        self.assertEqual(solution.decode(solution.encode(payload)), payload)

        payload = ['']
        self.assertEqual(solution.decode(solution.encode(payload)), payload)

        payload = [' ', '']
        self.assertEqual(solution.decode(solution.encode(payload)), payload)

        payload = []
        self.assertEqual(solution.decode(solution.encode(payload)), payload)

if __name__ == '__main__':
    unittest.main()
