#!/usr/bin/env python

import unittest

class LogSystem(object):

    def __init__(self):
        self.log = {}
        self.mapping = {'year': 5,
                        'month': 8,
                        'day': 11,
                        'hour': 14,
                        'minute': 17,
                        'second': 20}

    def put(self, id, timestamp):
        """
        :type id: int
        :type timestamp: str
        :rtype: void
        """
        assert id not in self.log

        self.log[id] = timestamp

    def _align_to_granularity(self, ts, granularity):
        return ts[:self.mapping[granularity]]

    def retrieve(self, s, e, gra):
        """
        :type s: str
        :type e: str
        :type gra: str
        :rtype: List[int]
        """
        _gra = gra.lower()
        assert _gra in self.mapping

        _start, _end = self._align_to_granularity(s, _gra), self._align_to_granularity(e, _gra)

        res = []
        for _id, ts in self.log.iteritems():
            _ts = self._align_to_granularity(ts, _gra)
            if _ts >= _start and _ts <= _end:
                res.append(_id)

        return res

class TestSolution(unittest.TestCase):
    def test_LogSystem(self):
        solution = LogSystem()
        solution.put(1, "2017:01:01:23:59:59")
        solution.put(2, "2017:01:01:22:59:59")
        solution.put(3, "2016:01:01:00:00:00")
        self.assertListEqual(solution.retrieve("2016:01:01:01:01:01",
                                               "2017:01:01:23:00:00",
                                               "Year"), [1, 2, 3])
        self.assertListEqual(solution.retrieve("2016:01:01:01:01:01",
                                               "2017:01:01:23:00:00",
                                               "Hour"), [1, 2])

if __name__ == '__main__':
    unittest.main()
