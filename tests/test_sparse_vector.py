#!/usr/bin/env python
""" Unit test for sparse_vector.py """

import unittest
import sys

sys.path.insert(0, '../')
from sparse_vector import SparseVector

class TestSparseVector(unittest.TestCase):
    """ Unit test for sparse_vector.py """

    def setUp(self):
        self.sparse_vector = SparseVector(10)
        self.values = [0.4, 0.89]
        self.that = [0.4, 0.6, 0.2, 0.1, 0.0, 0.056, 0.34, 0.8, 0.009, 0.21]

    def _put(self):
        self.sparse_vector.put(0, self.values[0])
        self.sparse_vector.put(5, self.values[1])

    def test_put(self):
        self._put()
        self.assertEqual(len(list(self.sparse_vector.indices())), 2)

    def test_put_exception(self):
        with self.assertRaises(KeyError):
            self.sparse_vector.put(43, 0.06)

    def test_get(self):
        self._put()
        self.assertTrue(all([self.values[0] == self.sparse_vector.get(0),
                             self.values[1] == self.sparse_vector.get(5)]))
        self.assertTrue(self.sparse_vector.get(43) == 0.0)

    def test_dot(self):
        self._put()
        self.assertEqual(float("{0:.5f}".format(self.sparse_vector.dot(self.that))),
                         0.20984)

if __name__ == '__main__':
    unittest.main()
