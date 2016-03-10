#!/usr/bin/env python
""" Unit test for mymod.py """

import unittest
import os.path
import tempfile
import sys

sys.path.insert(0, '../')
import mymod

class TestCountFunctions(unittest.TestCase):
    """ Unit test for mymod.py """

    tmpfilepath = os.path.join(tempfile.gettempdir(), "testfile")

    def setUp(self):
        with(open(self.tmpfilepath, 'w')) as fh:
            fh.write("one\ntwo\nthree")

    def test_countChars(self):
        self.assertIsNotNone(mymod.count_chars(self.tmpfilepath))
        self.assertEqual(mymod.count_chars(self.tmpfilepath), 13)

    def test_countLines(self):
        self.assertIsNotNone(mymod.count_lines(self.tmpfilepath))
        self.assertEqual(mymod.count_lines(self.tmpfilepath), 3)

    def test_countBytes(self):
        self.assertIsNotNone(mymod.count_bytes(self.tmpfilepath))
        self.assertEqual(mymod.count_bytes(self.tmpfilepath), 13)

if __name__ == '__main__':
    unittest.main()
