#!/usr/bin/env python3

"""Module for src.sparse_vector."""

from collections import defaultdict

class SparseVector(object):

    def __init__(self, N):
        self.vector = defaultdict(int)
        self.size = N

    def put(self, key, value):
        if key < 0 or key >= self.size:
            raise KeyError
        self.vector[key] = value

    def get(self, key):
        return self.vector.get(key, 0.0)

    def indices(self):
        return iter(self.vector.keys())

    def dot(self, that):
        if not isinstance(that, list) or len(that) != self.size:
            raise ValueError

        _sum = 0.0
        for index in range(self.size):
            _sum = _sum + self.get(index)*that[index]
        return _sum
