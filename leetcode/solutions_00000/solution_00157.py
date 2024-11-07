#!/usr/bin/env python

def read4(buf):
    buf = ''
    return buf

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        if not n:
            return n

        mas, res = [], 0
        while True:
            buf4 = [""]*4
            _read = read4(buf4)
            if not _read:
                break
            res += _read
            mas.extend(buf4)

        for i in xrange(min(n, len(mas))):
            buf[i] = mas[i]

        return min(res, n)
