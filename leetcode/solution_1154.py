#!/usr/bin/env python

import unittest


class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        leap_years = [1904, 1908, 1912, 1916, 1920,
                      1924, 1928, 1932, 1936, 1940,
                      1944, 1948, 1952, 1956, 1960,
                      1964, 1968, 1972, 1976, 1980,
                      1984, 1988, 1992, 1996, 2000,
                      2004, 2008, 2012, 2016, 2020]
        days_in_month = {1: 31,
                         2: 28,
                         3: 31,
                         4: 30,
                         5: 31,
                         6: 30,
                         7: 31,
                         8: 31,
                         9: 30,
                         10: 31,
                         11: 30,
                         12: 31}
        year, month, day = map(int, date.split('-'))
        if year in leap_years:
            days_in_month[2] = 29

        res = 0
        for i in range(month):
            res += days_in_month.get(i, 0)

        return res + day


class TestSolution(unittest.TestCase):

    def test_dayOfYear(self):
        solution = Solution()
        self.assertEqual(solution.dayOfYear("1969-09-28"), 271)


if __name__ == '__main__':
    unittest.main()
