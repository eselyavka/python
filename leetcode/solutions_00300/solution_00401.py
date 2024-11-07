#!/usr/bin/env python

import unittest


class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        res = []
        for h in range(12):
            for m in range(60):
                if (bin(h) + bin(m)).count('1') == num:
                    res.append("%01d:%02d" % (h, m))

        return res


class TestSolution(unittest.TestCase):

    def test_readBinaryWatch(self):
        solution = Solution()
        self.assertListEqual(sorted(solution.readBinaryWatch(1)), sorted(["1:00",
                                                                          "2:00",
                                                                          "4:00",
                                                                          "8:00",
                                                                          "0:01",
                                                                          "0:02",
                                                                          "0:04",
                                                                          "0:08",
                                                                          "0:16",
                                                                          "0:32"]))


if __name__ == '__main__':
    unittest.main()
