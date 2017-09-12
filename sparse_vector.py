#!/usr/bin/env python
from collections import defaultdict

class SparseVector(object):

    def __init__(self, N):
        self.vector = defaultdict(int)
        self.size = N

    def put(self, key, value):
        if key >= self.size:
            raise KeyError
        self.vector[key] = value

    def get(self, key):
        if self.vector.has_key(key):
            return self.vector[key]
        return 0.0

    def indices(self):
        return self.vector.iterkeys()

    def dot(self, that):
        if not isinstance(that, list) or len(that) != self.size:
            raise ValueError

        _sum = 0.0
        for index in range(self.size):
            _sum = _sum + self.get(index)*that[index]
        return _sum
