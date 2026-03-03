#!/usr/bin/env python3

"""Unit tests for mymod.py."""

import os.path
import tempfile
import unittest

from src import mymod

class TestCountFunctions(unittest.TestCase):
    """Unit tests for mymod.py."""

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
